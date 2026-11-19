"""工作台配置读写（保存在 studio_config.json，已加入 .gitignore）。"""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "studio_config.json"
ENV_PATH = ROOT / ".env"

DEFAULT_PROMPT = (
    "你是资深跨境电商运营专家。请根据原商品标题、描述与 SKU 规格，生成适合 {target_language} 买家的高转化商品草稿。\n"
    "要求：\n"
    "1. 标题控制在 {title_max_len} 字符以内，包含核心卖点、适用人群/场景、材质特点，不要堆砌无关词或违禁词。\n"
    "2. 描述分点清晰、自然地道，保留核心尺码/材质/卖点信息，去除国内电商废话（如“包邮”“拍下联系客服”等）。\n"
    "3. 文案风格要求：{style_tone}\n"
    "4. 如果提供了 SKU 属性与选项，请同步翻译为简洁地道的跨境买家表达，并保持选项之间互不重复。\n"
    "5. 严格以 JSON 格式输出：{\"title\": \"...\", \"notes\": \"...\", "
    "\"color_prop_name\": \"...\", \"size_prop_name\": \"...\", "
    "\"colors\": {\"原颜色名\": \"译文\"}, \"sizes\": {\"原尺码名\": \"译文\"}}"
)

DEFAULT_CONFIG: dict[str, Any] = {
    "miaoshou": {
        "default_site": "PH",
        "default_shop_ids": [],
    },
    "template": {
        "style_id": "shopee_clean",
        "pricing_id": "shopee_ph",
    },
    "text_model": {
        "enabled": True,
        "provider": "llm",  # llm | local_dict
        "base_url": "https://api.deepseek.com/v1",
        "api_key": "",
        "model": "deepseek-chat",
        "target_language": "English (Shopee Philippines)",
        "title_max_len": 120,
        "temperature": 0.4,
        "prompt_template": DEFAULT_PROMPT,
    },
    "image_model": {
        "mode": "local_pillow",  # skip | local_pillow | openai_edit | openai_chat_img | custom_http
        "base_url": "https://api.openai.com/v1",
        "api_key": "",
        "model": "gpt-image-1",
        "prompt": "Clean e-commerce product hero image on bright studio background, sharp lighting, keep product authentic.",
        "process_count": 1,  # 1=仅处理第1张主图，3/4/5=生成3/4/5张，0=全部
        "sku_enabled": True,
        "edit_options": {
            "translate": False,
            "white_bg": False,
            "clean_text": False,
            "enhance": False,
            "scene": False,
            "multi_angle": False,
            "extra_prompt": "",
        },
        "pillow_badge": "HOT PICK",
        "pillow_size": 800,
        "custom_headers_json": "{}",
        "upload_to_miaoshou": True,
        "image_host_upload_url": "",  # 可选：自定义图床上传接口（POST multipart file -> {"url": "..."}）
        "public_base_url": "",        # 可选：本机公网穿透地址（如 https://xxx.trycloudflare.com）
    },
    "assistant_model": {
        "mode": "reuse_text",  # reuse_text | custom_llm | local_index
        "base_url": "https://api.openai.com/v1",
        "api_key": "",
        "model": "gpt-4o-mini",
        "temperature": 0.3,
    },
    "custom_style_presets": {},
    "custom_pricing_presets": {},
    "batch": {
        "concurrency": 3,
    },
}


def _deep_merge(base: dict, override: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def mask_secret(val: str) -> str:
    if not val:
        return ""
    if len(val) <= 8:
        return "****"
    return f"{val[:4]}****{val[-4:]}"


def is_masked(val: str) -> bool:
    return "****" in (val or "")


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return copy.deepcopy(DEFAULT_CONFIG)
    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        return _deep_merge(DEFAULT_CONFIG, raw)
    except Exception:
        return copy.deepcopy(DEFAULT_CONFIG)


def load_public_config() -> dict[str, Any]:
    """返回脱敏后的配置给前端展示。"""
    cfg = load_config()
    cfg["text_model"]["api_key"] = mask_secret(cfg["text_model"].get("api_key", ""))
    cfg["image_model"]["api_key"] = mask_secret(cfg["image_model"].get("api_key", ""))
    cfg["assistant_model"]["api_key"] = mask_secret(cfg["assistant_model"].get("api_key", ""))
    return cfg


def resolve_runtime_config(patch: dict[str, Any] | None = None) -> dict[str, Any]:
    """合并未脱敏的运行时配置（用于在不落盘时直接测试表单里的值）。"""
    cur = load_config()
    if not patch:
        return cur
    merged = _deep_merge(cur, patch)
    for sec in ("text_model", "image_model", "assistant_model"):
        new_key = (patch.get(sec) or {}).get("api_key")
        if new_key is not None and is_masked(new_key):
            merged[sec]["api_key"] = cur[sec].get("api_key", "")
    return merged


def save_config(patch: dict[str, Any]) -> dict[str, Any]:
    """合并保存配置，保留前端未改动（带 ****）的密钥。"""
    merged = resolve_runtime_config(patch)
    CONFIG_PATH.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    return load_public_config()


# ------------------------------------------------------------------ Miaoshou .env Credentials

_ENV_KEYS = (
    "MIAOSHOU_APP_KEY",
    "MIAOSHOU_APP_SECRET",
    "MIAOSHOU_SUB_ACCOUNT_ID",
    "MIAOSHOU_BASE_URL",
)


def _parse_env_file(path: Path | None = None) -> dict[str, str]:
    p = path or ENV_PATH
    out: dict[str, str] = {}
    if not p.exists():
        return out
    for raw_line in p.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def resolve_miaoshou_credentials(patch: dict[str, Any] | None = None) -> dict[str, str]:
    """读取真实妙手密钥（优先 .env，回退环境变量，再叠加未落盘表单值；自动保留脱敏密钥）。"""
    file_env = _parse_env_file()
    cur = {
        "app_key": file_env.get("MIAOSHOU_APP_KEY") or os.getenv("MIAOSHOU_APP_KEY", ""),
        "app_secret": file_env.get("MIAOSHOU_APP_SECRET") or os.getenv("MIAOSHOU_APP_SECRET", ""),
        "sub_account_id": file_env.get("MIAOSHOU_SUB_ACCOUNT_ID") or os.getenv("MIAOSHOU_SUB_ACCOUNT_ID", ""),
        "base_url": file_env.get("MIAOSHOU_BASE_URL") or os.getenv("MIAOSHOU_BASE_URL", "") or "https://openapi-erp.91miaoshou.com",
    }
    if not patch:
        return cur
    out = dict(cur)
    if "app_key" in patch and patch["app_key"] is not None:
        out["app_key"] = str(patch["app_key"]).strip()
    if "app_secret" in patch and patch["app_secret"] is not None:
        sec = str(patch["app_secret"]).strip()
        if sec and not is_masked(sec):
            out["app_secret"] = sec
        elif sec == "":
            out["app_secret"] = ""
    if "sub_account_id" in patch and patch["sub_account_id"] is not None:
        out["sub_account_id"] = str(patch["sub_account_id"]).strip()
    if "base_url" in patch and patch["base_url"] is not None:
        out["base_url"] = str(patch["base_url"]).strip() or "https://openapi-erp.91miaoshou.com"
    return out


def load_miaoshou_env_public() -> dict[str, Any]:
    """返回脱敏后的妙手配置供前端展示。"""
    creds = resolve_miaoshou_credentials()
    return {
        "configured": bool(creds["app_key"] and creds["app_secret"]),
        "app_key": creds["app_key"],
        "app_secret": mask_secret(creds["app_secret"]),
        "sub_account_id": creds["sub_account_id"],
        "base_url": creds["base_url"],
        "env_file_exists": ENV_PATH.exists(),
    }


def save_miaoshou_env(patch: dict[str, Any]) -> dict[str, Any]:
    """将妙手 AppKey / AppSecret 写入根目录 .env 并同步刷新当前进程环境变量（无需重启生效）。"""
    creds = resolve_miaoshou_credentials(patch)
    existing_lines = ENV_PATH.read_text(encoding="utf-8").splitlines() if ENV_PATH.exists() else []
    new_vals = {
        "MIAOSHOU_APP_KEY": creds["app_key"],
        "MIAOSHOU_APP_SECRET": creds["app_secret"],
        "MIAOSHOU_SUB_ACCOUNT_ID": creds["sub_account_id"],
        "MIAOSHOU_BASE_URL": creds["base_url"],
    }
    written: set[str] = set()
    out_lines: list[str] = []
    for raw_line in existing_lines:
        stripped = raw_line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            k = stripped.split("=", 1)[0].strip()
            if k in new_vals:
                if new_vals[k]:
                    out_lines.append(f"{k}={new_vals[k]}")
                written.add(k)
                continue
        out_lines.append(raw_line)
    for k in _ENV_KEYS:
        if k not in written and new_vals[k]:
            out_lines.append(f"{k}={new_vals[k]}")

    ENV_PATH.write_text("\n".join(out_lines).rstrip() + "\n", encoding="utf-8")
    for k, v in new_vals.items():
        if v:
            os.environ[k] = v
        else:
            os.environ.pop(k, None)
    return load_miaoshou_env_public()
