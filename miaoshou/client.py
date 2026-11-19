"""妙手ERP开放平台 Python 客户端。

签名规则（来自官方《快速接入》文档）:
    sign = HmacSHA256(key=appSecret, msg=appSecret + path + timestamp + appKey + bodyJson + appSecret)
    -> 小写 hex；timestamp 为秒级；path 不含域名和 query；仅支持 POST + application/json。
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
from pathlib import Path
from typing import Any, Iterator

import requests

BASE_URL = "https://openapi-erp.91miaoshou.com"
ROOT = Path(__file__).resolve().parent.parent
RATE_LIMIT_CODES = {
    "accountQpsRateLimit", "appQpsRateLimit", "apiQpsRateLimit", "platformQpsRateLimit",
    "accountApiQpsRateLimit", "accountQpmRateLimit", "appQpmRateLimit", "apiQpmRateLimit",
    "platformQpmRateLimit", "accountApiQpmRateLimit",
}
RETRY_CODES = RATE_LIMIT_CODES | {
    "upstreamError", "upstreamConnectTimeout", "upstreamReadTimeout", "upstreamReset",
    "redisConnectionError", "redisTimeout", "systemError",
}


class MiaoshouError(Exception):
    def __init__(self, code: str, message: str, resp: dict | None = None):
        super().__init__(f"[{code}] {message}")
        self.code, self.message, self.resp = code, message, resp


def load_env(path: Path | None = None) -> None:
    """读取项目根目录 .env（KEY=VALUE），不覆盖已有环境变量。"""
    path = path or ROOT / ".env"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def make_sign(app_secret: str, path: str, timestamp: int | str, app_key: str, body_json: str = "") -> str:
    content = f"{app_secret}{path}{timestamp}{app_key}{body_json or ''}{app_secret}"
    return hmac.new(app_secret.encode("utf-8"), content.encode("utf-8"), hashlib.sha256).hexdigest()


def dump_body(body: Any) -> str:
    """固定序列化方式：签名用的字符串和实际发送的字节完全一致。"""
    if body is None:
        return ""
    if isinstance(body, str):
        return body
    return json.dumps(body, ensure_ascii=False, separators=(",", ":"))


class MiaoshouClient:
    def __init__(self, app_key: str | None = None, app_secret: str | None = None,
                 base_url: str | None = None, sub_account_id: str | None = None,
                 timeout: float = 60, max_retries: int = 4, verbose: bool = False):
        load_env()
        self.app_key = app_key or os.getenv("MIAOSHOU_APP_KEY", "")
        self.app_secret = app_secret or os.getenv("MIAOSHOU_APP_SECRET", "")
        self.base_url = (base_url or os.getenv("MIAOSHOU_BASE_URL") or BASE_URL).rstrip("/")
        self.sub_account_id = sub_account_id or os.getenv("MIAOSHOU_SUB_ACCOUNT_ID") or None
        if not self.app_key or not self.app_secret:
            raise MiaoshouError("configMissing",
                                "未配置 MIAOSHOU_APP_KEY / MIAOSHOU_APP_SECRET（写入项目根目录 .env 或环境变量）")
        self.timeout, self.max_retries, self.verbose = timeout, max_retries, verbose
        self.session = requests.Session()

    # ------------------------------------------------------------------ core
    def call_raw(self, path: str, body: Any = None) -> dict:
        """发送请求，返回完整响应 JSON（不检查 result）。"""
        if not path.startswith("/"):
            path = "/" + path
        if not path.startswith("/open/"):
            path = "/open/v1/" + path.lstrip("/")
        body_json = dump_body({} if body is None else body)
        attempt = 0
        while True:
            ts = int(time.time())
            headers = {
                "Content-Type": "application/json",
                "x-app-key": self.app_key,
                "x-timestamp": str(ts),
                "x-sign": make_sign(self.app_secret, path, ts, self.app_key, body_json),
            }
            if self.sub_account_id:
                headers["x-sub-account-id"] = str(self.sub_account_id)
            if self.verbose:
                print(f">>> POST {self.base_url}{path}\n>>> {body_json[:2000]}")
            try:
                r = self.session.post(self.base_url + path, data=body_json.encode("utf-8"),
                                      headers=headers, timeout=self.timeout)
                try:
                    data = r.json()
                except ValueError:
                    data = {"result": "fail", "code": f"http{r.status_code}", "message": r.text[:500]}
            except requests.RequestException as e:
                data = {"result": "fail", "code": "networkError", "message": str(e)}
            code = str(data.get("code", ""))
            if data.get("result") != "success" and (code in RETRY_CODES or code == "networkError") \
                    and attempt < self.max_retries:
                attempt += 1
                wait = (2 if code in RATE_LIMIT_CODES else 1) * attempt
                if "Qpm" in code:
                    wait = 15 * attempt
                if self.verbose:
                    print(f"!!! {code}，{wait}s 后重试 ({attempt}/{self.max_retries})")
                time.sleep(wait)
                continue
            if self.verbose:
                print("<<<", json.dumps(data, ensure_ascii=False)[:2000])
            return data

    def call(self, path: str, body: Any = None) -> Any:
        """发送请求，成功返回 data，失败抛 MiaoshouError。"""
        data = self.call_raw(path, body)
        if data.get("result") != "success":
            raise MiaoshouError(str(data.get("code")), str(data.get("message") or data.get("reason") or ""), data)
        return data.get("data")

    # ------------------------------------------------------------ pagination
    def iter_pages(self, path: str, body: dict | None = None, page_size: int = 50,
                   page_key: str | None = None, max_pages: int = 10_000) -> Iterator[list]:
        """自动翻页，逐页产出 data 中的列表。page_key 默认根据接口文档自动识别 page / pageNo。"""
        from .catalog import find_endpoint
        body = dict(body or {})
        if page_key is None:
            ep = find_endpoint(path)
            fields = {r[0] for r in ep["request"]} if ep else set()
            page_key = "pageNo" if "pageNo" in fields else "page"
        body.setdefault("pageSize", page_size)
        page_size = body["pageSize"]
        page = body.get(page_key, 1)
        seen = 0
        for _ in range(max_pages):
            body[page_key] = page
            data = self.call(path, body)
            items, total = extract_list(data)
            yield items
            seen += len(items)
            if not items or len(items) < page_size or (total is not None and seen >= total):
                return
            page += 1

    def fetch_all(self, path: str, body: dict | None = None, **kw) -> list:
        out: list = []
        for items in self.iter_pages(path, body, **kw):
            out.extend(items)
        return out


def extract_list(data: Any) -> tuple[list, int | None]:
    """从 data 中找出列表字段和 total。"""
    if isinstance(data, list):
        return data, None
    if not isinstance(data, dict):
        return [], None
    total = None
    for k in ("total", "totalCount", "totalNum", "count"):
        if isinstance(data.get(k), (int, str)) and str(data.get(k)).isdigit():
            total = int(data[k])
            break
    lists = [(k, v) for k, v in data.items() if isinstance(v, list)]
    if lists:
        return max(lists, key=lambda kv: len(kv[1]))[1], total
    for v in data.values():  # 嵌套一层，如 data.page.list
        if isinstance(v, dict):
            items, t = extract_list(v)
            if items:
                return items, total if total is not None else t
    return [], total
