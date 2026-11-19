"""预设风格模板定义与管理（主图风格 + SKU 视觉风格 + 文案风格）。

扩展说明：后续可在 BUILTIN_STYLE_PRESETS 或 studio_config.json 中新增风格，
也可在 studio/pipeline.py 中读取 style_preset 控制图片与文案生成行为。
"""
from __future__ import annotations

import copy
from typing import Any

BUILTIN_STYLE_PRESETS: dict[str, dict[str, Any]] = {
    "shopee_clean": {
        "id": "shopee_clean",
        "name": "Shopee 爆款白底框",
        "description": "800x800 纯白底 + 虾皮橙细边框 + 左上角 HOT PICK 角标 + SKU 底部规格胶囊标签",
        "main_image": {
            "canvas_size": 800,
            "bg_color": "#FFFFFF",
            "padding_pct": 0.05,
            "border_color": "#EE4D2D",
            "border_width": 5,
            "badge_text": "HOT PICK",
            "badge_color": "#EE4D2D",
            "badge_text_color": "#FFFFFF",
            "badge_position": "top-left",
            "bottom_banner_text": "",
            "bottom_banner_color": "#EE4D2D",
            "ai_prompt": (
                "Clean high-converting Shopee e-commerce main image, pure white studio background, "
                "crisp soft shadow, centered product, sharp detail, no Chinese text."
            ),
        },
        "sku_image": {
            "canvas_size": 800,
            "bg_color": "#FFFFFF",
            "padding_pct": 0.06,
            "border_color": "#E5E7EB",
            "border_width": 3,
            "label_enabled": True,
            "label_bg": "#111827",
            "label_fg": "#FFFFFF",
            "ai_prompt": (
                "Clean e-commerce SKU variant photo on pure white background, centered single variant, "
                "natural lighting, no Chinese characters."
            ),
        },
        "copy_style": {
            "tone": "高转化跨境卖点风，简洁有力，突出材质/功能/适用场景，去除国内电商废话",
        },
    },
    "jp_kr_fresh": {
        "id": "jp_kr_fresh",
        "name": "日韩清新奶油风",
        "description": "暖杏奶油背景 + 柔和焦糖细框 + NEW 轻角标 + SKU 暖棕胶囊标签",
        "main_image": {
            "canvas_size": 800,
            "bg_color": "#FAF6F0",
            "padding_pct": 0.07,
            "border_color": "#D6B89C",
            "border_width": 4,
            "badge_text": "NEW",
            "badge_color": "#8C6239",
            "badge_text_color": "#FFFFFF",
            "badge_position": "top-left",
            "bottom_banner_text": "SOFT & COMFORTABLE",
            "bottom_banner_color": "#8C6239",
            "ai_prompt": (
                "Japanese and Korean minimalist warm cream aesthetic product photo, soft natural sunlight, "
                "warm beige clean background, cozy lifestyle studio mood, no Chinese text."
            ),
        },
        "sku_image": {
            "canvas_size": 800,
            "bg_color": "#FAF6F0",
            "padding_pct": 0.07,
            "border_color": "#E5D6C5",
            "border_width": 3,
            "label_enabled": True,
            "label_bg": "#8C6239",
            "label_fg": "#FFFFFF",
            "ai_prompt": (
                "Minimalist warm cream background SKU variant shot, soft studio lighting, no Chinese text."
            ),
        },
        "copy_style": {
            "tone": "日韩温柔质感风，强调穿搭氛围感、亲肤细节与日常实用性",
        },
    },
    "promo_burst": {
        "id": "promo_burst",
        "name": "大促强视觉促销风",
        "description": "纯白底 + 醒目双色促销框 + FLASH DEAL 角标 + 底部现货速发条",
        "main_image": {
            "canvas_size": 800,
            "bg_color": "#FFFFFF",
            "padding_pct": 0.06,
            "border_color": "#DC2626",
            "border_width": 8,
            "badge_text": "FLASH DEAL",
            "badge_color": "#DC2626",
            "badge_text_color": "#FFFFFF",
            "badge_position": "top-left",
            "bottom_banner_text": "READY STOCK • FAST SHIPPING",
            "bottom_banner_color": "#111827",
            "ai_prompt": (
                "Vibrant high-impact e-commerce hero product image, bright clean white studio backdrop, "
                "high contrast commercial product lighting, crisp edges, no Chinese characters."
            ),
        },
        "sku_image": {
            "canvas_size": 800,
            "bg_color": "#FFFFFF",
            "padding_pct": 0.06,
            "border_color": "#FCA5A5",
            "border_width": 4,
            "label_enabled": True,
            "label_bg": "#DC2626",
            "label_fg": "#FFFFFF",
            "ai_prompt": (
                "Bright commercial SKU variant photo on clean white backdrop, crisp colors, no Chinese text."
            ),
        },
        "copy_style": {
            "tone": "强促销高点击风，突出性价比、核心功能卖点与下单理由",
        },
    },
    "minimal_clean": {
        "id": "minimal_clean",
        "name": "纯白合规无字风",
        "description": "标准 800x800 纯白无边框无水印，最稳妥过审；SKU 仅白底居中规范化",
        "main_image": {
            "canvas_size": 800,
            "bg_color": "#FFFFFF",
            "padding_pct": 0.06,
            "border_color": "#FFFFFF",
            "border_width": 0,
            "badge_text": "",
            "badge_color": "#111827",
            "badge_text_color": "#FFFFFF",
            "badge_position": "top-left",
            "bottom_banner_text": "",
            "bottom_banner_color": "#111827",
            "ai_prompt": (
                "Pure white background e-commerce catalog product image, no text, no badges, no borders, "
                "natural shadow, accurate product appearance."
            ),
        },
        "sku_image": {
            "canvas_size": 800,
            "bg_color": "#FFFFFF",
            "padding_pct": 0.06,
            "border_color": "#FFFFFF",
            "border_width": 0,
            "label_enabled": False,
            "label_bg": "#111827",
            "label_fg": "#FFFFFF",
            "ai_prompt": (
                "Pure white background product variant photo, no text or labels, centered."
            ),
        },
        "copy_style": {
            "tone": "客观规范类目描述，清晰准确说明规格、材质、尺寸与用途",
        },
    },
}


def list_style_presets(custom_presets: dict[str, dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    """合并内置与用户自定义风格模板。"""
    out = copy.deepcopy(BUILTIN_STYLE_PRESETS)
    for pid, pdata in (custom_presets or {}).items():
        if isinstance(pdata, dict):
            base = out.get(pid, copy.deepcopy(BUILTIN_STYLE_PRESETS["shopee_clean"]))
            merged = _merge_dict(base, pdata)
            merged["id"] = pid
            out[pid] = merged
    return out


def get_style_preset(style_id: str | None, custom_presets: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    all_presets = list_style_presets(custom_presets)
    if style_id and style_id in all_presets:
        return all_presets[style_id]
    return all_presets["shopee_clean"]


def _merge_dict(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _merge_dict(out[k], v)
        else:
            out[k] = v
    return out
