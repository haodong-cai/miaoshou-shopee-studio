"""基于 docs/endpoints.json 的接口目录查询。"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"


@lru_cache
def endpoints() -> list[dict]:
    return json.loads((DOCS / "endpoints.json").read_text(encoding="utf-8"))


def normalize(path: str) -> str:
    path = "/" + path.lstrip("/")
    if not path.startswith("/open/"):
        path = "/open/v1" + path
    return path


def find_endpoint(path: str) -> dict | None:
    p = normalize(path)
    for e in endpoints():
        if e["path"] == p:
            return e
    return None


def search(keyword: str = "") -> list[dict]:
    kws = keyword.lower().split()
    out = []
    for e in endpoints():
        hay = f"{e['category']} {e['title']} {e['path']}".lower()
        if all(k in hay for k in kws):
            out.append(e)
    return out


def missing_required(path: str, body: dict) -> list[str]:
    """检查顶层必填字段是否缺失。"""
    ep = find_endpoint(path)
    if not ep or not isinstance(body, dict):
        return []
    return [r[0] for r in ep["request"] if r[2] and "." not in r[0] and "[" not in r[0] and r[0] not in body]


def example_body(path: str) -> dict:
    """根据 schema 生成一个请求体骨架（仅必填字段 + 分页默认值）。"""
    ep = find_endpoint(path)
    if not ep:
        return {}

    def build(schema, only_required=True):
        props = schema.get("properties") or {}
        req = set(schema.get("required") or [])
        out = {}
        for k, p in props.items():
            if k.startswith("x-apifox") or (only_required and k not in req):
                continue
            out[k] = sample(k, p or {})
        return out

    def sample(name, p):
        t = p.get("type")
        if name in ("page", "pageNo"):
            return 1
        if name == "pageSize":
            return 20
        if "enum" in p:
            return p["enum"][0]
        if t == "integer" or t == "number":
            return 0
        if t == "boolean":
            return False
        if t == "array":
            it = p.get("items") or {}
            return [build(it)] if it.get("properties") else []
        if t == "object" or p.get("properties"):
            return build(p)
        return ""

    return build(ep.get("requestSchema") or {})
