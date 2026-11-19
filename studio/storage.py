"""草稿本地持久化（out/drafts/items/*.json 与 out/drafts/images/）。"""
from __future__ import annotations

import json
import threading
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = ROOT / "out" / "drafts"
ITEMS_DIR = DRAFTS_DIR / "items"
IMAGES_DIR = DRAFTS_DIR / "images"

_LOCK = threading.Lock()


def ensure_dirs() -> None:
    ITEMS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)


def item_path(detail_id: int | str) -> Path:
    ensure_dirs()
    return ITEMS_DIR / f"{detail_id}.json"


def _to_float(val: Any, default: float = 0.0) -> float:
    try:
        if val is None or val == "":
            return default
        return float(val)
    except (TypeError, ValueError):
        return default


def _to_int(val: Any, default: int = 0) -> int:
    try:
        if val is None or val == "":
            return default
        return int(float(val))
    except (TypeError, ValueError):
        return default


def _parse_sku_key(key: str, color_keys: set[str], size_keys: set[str]) -> tuple[str, str]:
    """解析妙手 skuMap key（通常形如 ';颜色;尺码;' 或 ';颜色;;'）。"""
    parts = [p for p in str(key).split(";") if p != ""]
    color = ""
    size = ""
    for p in parts:
        if not color and p in color_keys:
            color = p
        elif not size and p in size_keys:
            size = p
    if not color and not size and len(parts) == 1:
        if color_keys:
            color = parts[0]
        elif size_keys:
            size = parts[0]
    elif not color and not size and len(parts) >= 2:
        color, size = parts[0], parts[1]
    return color, size


def extract_sku_draft(raw_site_data: dict[str, Any] | None, fallback_price: Any = "", fallback_stock: Any = "") -> dict[str, Any]:
    """从妙手 siteDetailSimpleData 中提取规范化 SKU 结构。"""
    sd = raw_site_data or {}
    color_map = sd.get("colorMap") if isinstance(sd.get("colorMap"), dict) else {}
    size_map = sd.get("sizeMap") if isinstance(sd.get("sizeMap"), dict) else {}
    sku_map = sd.get("skuMap") if isinstance(sd.get("skuMap"), dict) else {}

    colors: list[dict[str, Any]] = []
    for cname, cobj in color_map.items():
        cobj = cobj if isinstance(cobj, dict) else {}
        img_url = cobj.get("imgUrl") or (cobj.get("imgUrls") or [""])[0]
        colors.append({
            "orig_name": str(cname),
            "draft_name": "",
            "orig_img": img_url or "",
            "draft_img": None,
        })

    sizes: list[dict[str, Any]] = []
    for sname in size_map.keys():
        sizes.append({
            "orig_name": str(sname),
            "draft_name": "",
        })

    color_keys = set(color_map.keys())
    size_keys = set(size_map.keys())
    default_cost = _to_float(sd.get("originPrice"), 0.0)
    default_weight = _to_float(sd.get("weight"), 0.1)

    skus: list[dict[str, Any]] = []
    if sku_map:
        for skey, sobj in sku_map.items():
            sobj = sobj if isinstance(sobj, dict) else {}
            c_orig, s_orig = _parse_sku_key(skey, color_keys, size_keys)
            cost = _to_float(sobj.get("originPrice"), default_cost)
            weight = _to_float(sobj.get("weight"), default_weight)
            skus.append({
                "orig_key": str(skey),
                "color_orig": c_orig,
                "size_orig": s_orig,
                "color_draft": "",
                "size_draft": "",
                "item_num": str(sobj.get("itemNum") or ""),
                "cost_rmb": cost,
                "weight_kg": weight,
                "stock": _to_int(sobj.get("stock"), 0),
                "orig_price": _to_float(sobj.get("price"), _to_float(fallback_price, 0.0)),
                "draft_price": None,
                "shipping_rmb": None,
                "profit_rmb": None,
                "margin_pct": None,
                "currency": "",
            })
    else:
        skus.append({
            "orig_key": "__single__",
            "color_orig": "",
            "size_orig": "",
            "color_draft": "",
            "size_draft": "",
            "item_num": str(sd.get("itemNum") or ""),
            "cost_rmb": default_cost,
            "weight_kg": default_weight,
            "stock": _to_int(sd.get("stock") or fallback_stock, 0),
            "orig_price": _to_float(sd.get("price") or fallback_price, 0.0),
            "draft_price": None,
            "shipping_rmb": None,
            "profit_rmb": None,
            "margin_pct": None,
            "currency": "",
        })

    return {
        "orig_color_prop": str(sd.get("colorPropName") or ("颜色" if colors else "")),
        "draft_color_prop": "",
        "orig_size_prop": str(sd.get("sizePropName") or ("尺寸" if sizes else "")),
        "draft_size_prop": "",
        "colors": colors,
        "sizes": sizes,
        "skus": skus,
    }


def normalize_item(item: dict[str, Any]) -> dict[str, Any]:
    """确保草稿结构完整（兼容早期保存的草稿 JSON）。"""
    item.setdefault("style_id", "")
    item.setdefault("pricing_id", "")
    item.setdefault("pricing_summary", {})
    if not item.get("sku_draft") or not isinstance(item.get("sku_draft"), dict):
        item["sku_draft"] = extract_sku_draft(
            item.get("raw_site_data"),
            fallback_price=item.get("price"),
            fallback_stock=item.get("stock"),
        )
    return item


def save_item(item: dict[str, Any]) -> dict[str, Any]:
    normalize_item(item)
    item["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    p = item_path(item["detail_id"])
    with _LOCK:
        p.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
    return item


def get_item(detail_id: int | str) -> dict[str, Any] | None:
    p = item_path(detail_id)
    if not p.exists():
        return None
    with _LOCK:
        data = json.loads(p.read_text(encoding="utf-8"))
    return normalize_item(data)


def list_items() -> list[dict[str, Any]]:
    ensure_dirs()
    out = []
    with _LOCK:
        for p in sorted(ITEMS_DIR.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
            try:
                out.append(normalize_item(json.loads(p.read_text(encoding="utf-8"))))
            except Exception:
                continue
    return out


def delete_item(detail_id: int | str) -> bool:
    p = item_path(detail_id)
    if p.exists():
        p.unlink()
        return True
    return False
