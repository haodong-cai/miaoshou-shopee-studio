"""外部模型对接层（文本大模型 / 本地词典演示 + 风格化图片处理 + 图床上传）。"""
from __future__ import annotations

import base64
import io
import json
import re
import time
import uuid
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageColor, ImageDraw, ImageEnhance, ImageFont

from .storage import IMAGES_DIR, ensure_dirs


class ModelError(Exception):
    pass


# ------------------------------------------------------------------ Text & SKU Translation

_LOCAL_COLOR_DICT = {
    "黑白色": "Black & White",
    "黑白": "Black & White",
    "蓝白色": "Blue & White",
    "蓝白": "Blue & White",
    "黑红色": "Black & Red",
    "黑红": "Black & Red",
    "蓝黄色": "Blue & Yellow",
    "蓝黄": "Blue & Yellow",
    "黑色": "Black",
    "白色": "White",
    "粉色": "Pink",
    "浅粉色": "Light Pink",
    "红色": "Red",
    "酒红色": "Wine Red",
    "蓝色": "Blue",
    "天蓝色": "Sky Blue",
    "藏青色": "Navy Blue",
    "深蓝色": "Dark Blue",
    "黄色": "Yellow",
    "绿色": "Green",
    "军绿色": "Army Green",
    "紫色": "Purple",
    "灰色": "Gray",
    "浅灰色": "Light Gray",
    "深灰色": "Dark Gray",
    "米白色": "Beige White",
    "米色": "Beige",
    "卡其色": "Khaki",
    "杏色": "Apricot",
    "棕色": "Brown",
    "咖啡色": "Coffee Brown",
    "橙色": "Orange",
    "橘色": "Orange",
    "银色": "Silver",
    "金色": "Gold",
    "彩色": "Multicolor",
}

_LOCAL_TERM_MAP = [
    ("韩系", "Korean Style "),
    ("活力", "Sporty "),
    ("男童", "Boys "),
    ("女童", "Girls "),
    ("儿童", "Kids "),
    ("宝宝", "Toddler "),
    ("露趾", "Open-Toe "),
    ("包头", "Closed-Toe "),
    ("防滑", "Non-Slip "),
    ("软底", "Soft Sole "),
    ("平底", "Flat "),
    ("厚底", "Thick Sole "),
    ("魔术贴", "Velcro "),
    ("洞洞鞋", "Clogs "),
    ("沙滩凉鞋", "Beach Sandals "),
    ("沙滩凉拖", "Beach Sandals "),
    ("凉鞋", "Sandals "),
    ("拖鞋", "Slippers "),
    ("运动鞋", "Sneakers "),
    ("EVA", "EVA "),
    ("透气", "Breathable "),
    ("轻量", "Lightweight "),
    ("轻便", "Lightweight "),
    ("防水", "Waterproof "),
    ("居家", "Home "),
    ("户外", "Outdoor "),
    ("沙滩", "Beach "),
    ("新款", "New "),
    ("夏季", "Summer "),
    ("多色可选", "Multi-Color"),
    ("脚长", "Foot "),
    ("建议选择尺码", "Size "),
    ("尺码", "Size "),
    ("颜色", "Color"),
    ("尺寸", "Size"),
    ("规格", "Option"),
]


def _openai_endpoint(base_url: str, suffix: str) -> str:
    base = (base_url or "").strip().rstrip("/")
    if not base:
        raise ModelError("未配置模型 API Base URL")
    if base.endswith(suffix):
        return base
    return f"{base}{suffix}"


def _extract_json_payload(text: str) -> dict[str, Any]:
    """从模型输出中容错提取 JSON 对象。"""
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", cleaned, re.S)
    if fence:
        cleaned = fence.group(1)
    else:
        brace = re.search(r"\{.*\}", cleaned, re.S)
        if brace:
            cleaned = brace.group(0)
    try:
        obj = json.loads(cleaned)
        if isinstance(obj, dict) and ("title" in obj or "notes" in obj or "colors" in obj or "sizes" in obj):
            return {
                "title": str(obj.get("title") or "").strip(),
                "notes": str(obj.get("notes") or "").strip(),
                "color_prop_name": str(obj.get("color_prop_name") or "").strip(),
                "size_prop_name": str(obj.get("size_prop_name") or "").strip(),
                "colors": obj.get("colors") if isinstance(obj.get("colors"), dict) else {},
                "sizes": obj.get("sizes") if isinstance(obj.get("sizes"), dict) else {},
            }
    except Exception:
        pass
    title_m = re.search(r"(?:title|标题)\s*[:：]\s*(.+)", text, re.I)
    notes_m = re.search(r"(?:notes|description|描述)\s*[:：]\s*(.+)", text, re.I | re.S)
    if title_m:
        return {
            "title": title_m.group(1).strip().strip('"'),
            "notes": notes_m.group(1).strip() if notes_m else "",
            "color_prop_name": "",
            "size_prop_name": "",
            "colors": {},
            "sizes": {},
        }
    raise ModelError(f"模型返回内容无法解析为 JSON：{text[:200]}")


def _clip_title(title: str, max_len: int) -> str:
    if max_len <= 0 or len(title) <= max_len:
        return title
    cut = title[:max_len]
    if " " in cut and not re.search(r"[\u4e00-\u9fff]", cut):
        cut = cut.rsplit(" ", 1)[0] or cut
    return cut.strip()


def _dedup_mapping(orig_keys: list[str], raw_map: dict[str, Any], fallback_fn) -> dict[str, str]:
    """确保翻译后的规格值互不重复，避免妙手 skuMap key 冲突。"""
    used: set[str] = set()
    out: dict[str, str] = {}
    for k in orig_keys:
        val = str((raw_map or {}).get(k) or "").strip()
        if not val:
            val = fallback_fn(k)
        base = val or k
        cand = base
        idx = 2
        while cand in used:
            cand = f"{base} ({idx})"
            idx += 1
        used.add(cand)
        out[k] = cand
    return out


def _local_translate_spec(text: str, is_color: bool = False) -> str:
    s = (text or "").strip()
    if not s:
        return s
    if is_color and s in _LOCAL_COLOR_DICT:
        return _LOCAL_COLOR_DICT[s]
    out = s
    if is_color:
        for zh, en in _LOCAL_COLOR_DICT.items():
            if zh in out:
                out = out.replace(zh, en + " ")
    for zh, en in _LOCAL_TERM_MAP:
        out = out.replace(zh, en)
    out = out.replace("（", " (").replace("）", ") ").replace("，", ", ")
    out = re.sub(r"[\u4e00-\u9fff]+", " ", out)
    out = re.sub(r"\s+", " ", out).strip(" ,.-")
    return out or s


def _local_dict_translate(
    orig_title: str,
    orig_notes: str,
    color_prop_name: str,
    size_prop_name: str,
    color_names: list[str],
    size_names: list[str],
    max_len: int,
) -> dict[str, Any]:
    """零费用本地词典翻译演示（无需 API Key 即可跑通完整草稿模板流程）。"""
    t = orig_title or ""
    tokens: list[str] = []
    for zh, en in _LOCAL_TERM_MAP:
        if zh in t:
            w = en.strip()
            if w and w not in tokens:
                tokens.append(w)
    title = " ".join(tokens) if tokens else _local_translate_spec(t)
    title = _clip_title(title, max_len)

    lines = [ln.strip() for ln in (orig_notes or "").splitlines() if ln.strip()]
    kept: list[str] = []
    for ln in lines[:12]:
        tr = _local_translate_spec(ln)
        if tr and len(tr) > 2:
            kept.append(f"• {tr}")
    notes = "\n".join(kept) if kept else (f"• {title}\n• Ready stock & quality checked." if title else "")

    return {
        "title": title or orig_title,
        "notes": notes or orig_notes,
        "color_prop_name": "Color" if color_prop_name else "",
        "size_prop_name": "Size" if size_prop_name else "",
        "colors": _dedup_mapping(color_names, {}, lambda k: _local_translate_spec(k, is_color=True)),
        "sizes": _dedup_mapping(size_names, {}, lambda k: _local_translate_spec(k, is_color=False)),
    }


def generate_draft_copy(
    orig_title: str,
    orig_notes: str,
    text_cfg: dict[str, Any],
    *,
    color_prop_name: str = "",
    size_prop_name: str = "",
    color_names: list[str] | None = None,
    size_names: list[str] | None = None,
    style_tone: str = "",
    extra_info: str = "",
) -> dict[str, Any]:
    """翻译/生成商品标题、描述以及 SKU 规格属性和选项名称。"""
    c_names = list(color_names or [])
    s_names = list(size_names or [])
    max_len = int(text_cfg.get("title_max_len") or 120)
    provider = text_cfg.get("provider") or "llm"

    if provider == "local_dict":
        return _local_dict_translate(
            orig_title, orig_notes, color_prop_name, size_prop_name, c_names, s_names, max_len
        )

    if not text_cfg.get("api_key"):
        raise ModelError("未配置文本模型 API Key（如需先零费用演示，可在配置中切换为「内置本地词典演示」）")

    url = _openai_endpoint(text_cfg.get("base_url", ""), "/chat/completions")
    tpl = text_cfg.get("prompt_template") or ""
    try:
        sys_prompt = tpl.format(
            target_language=text_cfg.get("target_language") or "English",
            title_max_len=max_len,
            style_tone=style_tone or "自然地道、高转化跨境电商风格",
        )
    except KeyError:
        sys_prompt = tpl

    sku_block = {
        "color_prop_name": color_prop_name,
        "size_prop_name": size_prop_name,
        "colors": c_names,
        "sizes": s_names,
    }
    user_msg = (
        f"原标题：\n{orig_title}\n\n"
        f"原描述：\n{orig_notes or '(无)'}\n\n"
        f"SKU规格（需同步翻译并保持JSON映射）：\n{json.dumps(sku_block, ensure_ascii=False)}"
    )
    if extra_info:
        user_msg += f"\n\n补充信息：\n{extra_info}"

    payload = {
        "model": text_cfg.get("model") or "deepseek-chat",
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_msg},
        ],
        "temperature": float(text_cfg.get("temperature") or 0.4),
    }
    headers = {
        "Authorization": f"Bearer {text_cfg['api_key'].strip()}",
        "Content-Type": "application/json",
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=90)
    if resp.status_code >= 400:
        raise ModelError(f"文本模型 HTTP {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise ModelError(f"文本模型响应格式异常: {json.dumps(data, ensure_ascii=False)[:300]}") from e

    parsed = _extract_json_payload(content)
    parsed["title"] = _clip_title(parsed.get("title") or orig_title, max_len)
    if not parsed.get("notes"):
        parsed["notes"] = orig_notes
    if color_prop_name and not parsed.get("color_prop_name"):
        parsed["color_prop_name"] = "Color"
    if size_prop_name and not parsed.get("size_prop_name"):
        parsed["size_prop_name"] = "Size"
    parsed["colors"] = _dedup_mapping(c_names, parsed.get("colors") or {}, lambda k: _local_translate_spec(k, True))
    parsed["sizes"] = _dedup_mapping(s_names, parsed.get("sizes") or {}, lambda k: _local_translate_spec(k, False))
    return parsed


def generate_text_draft(
    orig_title: str,
    orig_notes: str,
    text_cfg: dict[str, Any],
    extra_info: str = "",
) -> dict[str, str]:
    """兼容旧调用签名：仅返回 {"title", "notes"}。"""
    res = generate_draft_copy(orig_title, orig_notes, text_cfg, extra_info=extra_info)
    return {"title": res["title"], "notes": res["notes"]}


def test_text_model(text_cfg: dict[str, Any]) -> dict[str, Any]:
    t0 = time.time()
    out = generate_draft_copy(
        "夏季新款儿童防滑软底洞洞鞋沙滩凉拖",
        "轻便EVA材质，防滑耐磨，多色可选，适合沙滩居家。",
        text_cfg,
        color_prop_name="颜色",
        size_prop_name="尺寸",
        color_names=["黑白色", "蓝黄色"],
        size_names=["C6（脚长13.5cm）"],
    )
    return {"elapsed_ms": int((time.time() - t0) * 1000), "sample": out}


# ------------------------------------------------------------------ Image & Style Rendering


def _download_bytes(url: str) -> bytes:
    r = requests.get(url, timeout=45, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return r.content


def _to_png_bytes(img_bytes: bytes) -> bytes:
    """将任意常见图片格式统一规范化为 PNG 字节流，确保图片编辑 API 校验通过。"""
    img = Image.open(io.BytesIO(img_bytes))
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def _save_png(img_bytes: bytes, detail_id: int | str, prefix: str) -> Path:
    ensure_dirs()
    img = Image.open(io.BytesIO(img_bytes)).convert("RGBA")
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    ts = int(time.time() * 1000) % 10_000_000
    uid = uuid.uuid4().hex[:4]
    name = f"{detail_id}_{prefix}_{ts}_{uid}.png"
    out_path = IMAGES_DIR / name
    bg.save(out_path, format="PNG", optimize=True)
    return out_path


def _load_font(size: int) -> ImageFont.ImageFont:
    for p in (
        "C:/Windows/Fonts/msyhbd.ttc",
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ):
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def _parse_color(val: str | None, default: tuple[int, int, int]) -> tuple[int, int, int]:
    if not val:
        return default
    try:
        rgb = ImageColor.getrgb(val.strip())
        return rgb[:3]
    except Exception:
        return default


def _render_styled_pillow(
    orig_bytes: bytes,
    img_cfg: dict[str, Any],
    *,
    style_cfg: dict[str, Any] | None = None,
    is_sku: bool = False,
    sku_label: str = "",
    options: dict[str, Any] | None = None,
) -> bytes:
    """按照预设风格模板与编辑选项渲染主图或 SKU 图。"""
    sc = style_cfg or {}
    opts = options or {}
    size = max(400, min(1600, int(sc.get("canvas_size") or img_cfg.get("pillow_size") or 800)))
    bg_rgb = (255, 255, 255) if (not is_sku and opts.get("white_bg")) else _parse_color(sc.get("bg_color"), (255, 255, 255))
    pad_pct = max(0.01, min(0.25, float(sc.get("padding_pct") or 0.05)))
    pad = int(size * pad_pct)

    im = Image.open(io.BytesIO(orig_bytes)).convert("RGBA")
    if opts.get("enhance"):
        rgb_part = ImageEnhance.Sharpness(im.convert("RGB")).enhance(1.12)
        rgb_part = ImageEnhance.Contrast(rgb_part).enhance(1.06)
        r, g, b = rgb_part.split()
        im = Image.merge("RGBA", (r, g, b, im.split()[3]))
    max_inner_h = size - pad * 2 - (44 if (is_sku and sc.get("label_enabled") and sku_label) else 0)
    im.thumbnail((size - pad * 2, max(120, max_inner_h)), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (size, size), bg_rgb)
    x = (size - im.width) // 2
    y = (size - im.height) // 2 - (14 if (is_sku and sc.get("label_enabled") and sku_label) else 0)
    canvas.paste(im, (x, max(pad // 2, y)), mask=im.split()[3])

    draw = ImageDraw.Draw(canvas)
    bw = max(0, int(sc.get("border_width") if sc.get("border_width") is not None else (0 if is_sku else 4)))
    if bw > 0:
        b_rgb = _parse_color(sc.get("border_color"), (238, 77, 45))
        draw.rectangle([bw // 2, bw // 2, size - 1 - bw // 2, size - 1 - bw // 2], outline=b_rgb, width=bw)

    if not is_sku:
        badge = (
            sc.get("badge_text")
            if "badge_text" in sc
            else (img_cfg.get("pillow_badge") or "")
        )
        badge = (badge or "").strip()
        if badge:
            font = _load_font(max(18, size // 28))
            bbox = draw.textbbox((0, 0), badge, font=font)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            margin = max(16, bw + 12)
            pos = sc.get("badge_position") or "top-left"
            bx1 = (size - tw - 28 - margin) if pos == "top-right" else margin
            by1 = margin
            bx2, by2 = bx1 + tw + 28, by1 + th + 18
            badge_bg = _parse_color(sc.get("badge_color"), (238, 77, 45))
            badge_fg = _parse_color(sc.get("badge_text_color"), (255, 255, 255))
            draw.rounded_rectangle([bx1, by1, bx2, by2], radius=10, fill=badge_bg)
            draw.text((bx1 + 14, by1 + 7), badge, fill=badge_fg, font=font)

        banner = (sc.get("bottom_banner_text") or "").strip()
        if banner:
            b_font = _load_font(max(16, size // 32))
            bar_h = max(44, size // 14)
            bar_bg = _parse_color(sc.get("bottom_banner_color"), (17, 24, 39))
            draw.rectangle([bw, size - bar_h - bw, size - bw - 1, size - bw - 1], fill=bar_bg)
            tb = draw.textbbox((0, 0), banner, font=b_font)
            tw, th = tb[2] - tb[0], tb[3] - tb[1]
            draw.text(((size - tw) // 2, size - bar_h - bw + (bar_h - th) // 2 - 2), banner, fill=(255, 255, 255), font=b_font)
    else:
        if sc.get("label_enabled", True) and (sku_label or "").strip():
            lbl = sku_label.strip()[:30]
            s_font = _load_font(max(18, size // 26))
            tb = draw.textbbox((0, 0), lbl, font=s_font)
            tw, th = tb[2] - tb[0], tb[3] - tb[1]
            pw, ph = tw + 34, th + 20
            px1 = (size - pw) // 2
            py1 = size - ph - max(18, bw + 12)
            l_bg = _parse_color(sc.get("label_bg"), (17, 24, 39))
            l_fg = _parse_color(sc.get("label_fg"), (255, 255, 255))
            draw.rounded_rectangle([px1, py1, px1 + pw, py1 + ph], radius=ph // 2, fill=l_bg)
            draw.text((px1 + 17, py1 + 8), lbl, fill=l_fg, font=s_font)

    buf = io.BytesIO()
    canvas.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def _process_local_pillow(orig_bytes: bytes, img_cfg: dict[str, Any]) -> bytes:
    """兼容旧签名：默认主图本地白底居中渲染。"""
    return _render_styled_pillow(orig_bytes, img_cfg, style_cfg=None, is_sku=False)


_IMAGE_VARIATION_HINTS = [
    "Front-facing centered commercial hero shot showcasing overall shape cleanly.",
    "Slightly angled 45-degree three-quarter studio perspective highlighting depth and form.",
    "Detailed close-up view emphasizing material texture, stitching, and build quality.",
    "Clean alternative angle displaying key functional design highlights.",
    "Well-balanced commercial showcase view from an appealing elevated angle.",
]


def _extract_image_from_b64_or_url(val: str) -> tuple[bytes, str | None]:
    s = (val or "").strip()
    if s.startswith("http://") or s.startswith("https://"):
        return _download_bytes(s), s
    b64 = s.split(",", 1)[-1] if s.startswith("data:") else s
    return base64.b64decode(b64), None


def _parse_image_api_response(resp: requests.Response) -> tuple[bytes, str | None]:
    """解析常见生图 API 返回格式（原始图片流 / url / b64_json / image_base64 / chat completions）。"""
    ctype = (resp.headers.get("Content-Type") or "").lower()
    if ctype.startswith("image/"):
        return resp.content, None
    data = resp.json()
    if isinstance(data, dict):
        items = data.get("data")
        if isinstance(items, list) and items:
            first = items[0]
            if first.get("b64_json"):
                return _extract_image_from_b64_or_url(first["b64_json"])
            if first.get("url"):
                return _download_bytes(first["url"]), first["url"]
        choices = data.get("choices")
        if isinstance(choices, list) and choices:
            msg = (choices[0] or {}).get("message") or {}
            imgs = msg.get("images")
            if isinstance(imgs, list) and imgs:
                u = ((imgs[0] or {}).get("image_url") or {}).get("url") or (imgs[0] or {}).get("url") or ""
                if u:
                    return _extract_image_from_b64_or_url(u)
            content = msg.get("content")
            if isinstance(content, list):
                for blk in content:
                    if not isinstance(blk, dict):
                        continue
                    if blk.get("type") == "image_url":
                        u = (blk.get("image_url") or {}).get("url") or ""
                        if u:
                            return _extract_image_from_b64_or_url(u)
                    if blk.get("type") in ("image", "output_image"):
                        u = blk.get("url") or blk.get("image_url") or blk.get("b64_json") or blk.get("data") or ""
                        if isinstance(u, dict):
                            u = u.get("url") or u.get("data") or ""
                        if u:
                            return _extract_image_from_b64_or_url(str(u))
                    if isinstance(blk.get("inline_data"), dict) and blk["inline_data"].get("data"):
                        return _extract_image_from_b64_or_url(str(blk["inline_data"]["data"]))
            elif isinstance(content, str):
                m_b64 = re.search(r"data:image/[a-zA-Z0-9+.-]+;base64,[A-Za-z0-9+/=]+", content)
                if m_b64:
                    return _extract_image_from_b64_or_url(m_b64.group(0))
                m_md_url = re.search(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", content)
                if m_md_url:
                    u = m_md_url.group(1)
                    return _download_bytes(u), u
                m_url = re.search(r"https?://[^\s)\"'>]+", content)
                if m_url:
                    u = m_url.group(0)
                    return _download_bytes(u), u
        for k in ("image_base64", "b64_json", "image"):
            if isinstance(data.get(k), str) and len(data[k]) > 100:
                return _extract_image_from_b64_or_url(data[k])
        for k in ("image_url", "url"):
            if isinstance(data.get(k), str) and data[k].startswith("http"):
                return _download_bytes(data[k]), data[k]
    raise ModelError(f"无法解析生图 API 返回: {resp.text[:300]}")


def _merge_prompt(base_prompt: str, style_prompt: str, extra: str = "") -> str:
    parts = [p.strip() for p in (style_prompt, base_prompt, extra) if p and p.strip()]
    return " ".join(parts) or "Clean e-commerce product photo"


def build_image_edit_prompt(
    base_prompt: str,
    style_prompt: str = "",
    *,
    options: dict[str, Any] | None = None,
    target_language: str = "",
    variant_index: int = 0,
    variant_total: int = 1,
    force_variation: bool = False,
) -> str:
    """根据所选风格与图片编辑选项（翻译、白底、去中文、精修、场景、多角度等）拼接生图指令。"""
    opts = options or {}
    parts: list[str] = []
    if style_prompt and style_prompt.strip():
        parts.append(style_prompt.strip())
    if base_prompt and base_prompt.strip():
        parts.append(base_prompt.strip())

    if opts.get("white_bg"):
        parts.append(
            "Pure solid white background (#FFFFFF), clean studio lighting, soft natural contact shadow under the product, centered product, no distracting props."
        )
    if opts.get("scene") and not opts.get("white_bg"):
        parts.append(
            "Realistic appealing commercial lifestyle usage scene fitting the product, natural depth of field, warm studio light."
        )
    elif opts.get("scene") and opts.get("white_bg"):
        parts.append("Minimalist clean bright studio surface with subtle lifestyle atmosphere.")
    if opts.get("clean_text"):
        parts.append(
            "Remove all Chinese characters, promotional stickers, messy callouts, price tags, watermarks, and QR codes while cleanly reconstructing the product and background."
        )
    if opts.get("translate"):
        lang = (target_language or "English").strip()
        parts.append(
            f"Translate any visible text, labels, specs, or selling-point badges in the image into natural {lang}; ensure zero leftover Chinese characters and keep typography neat."
        )
    if opts.get("enhance"):
        parts.append(
            "High-resolution studio photography retouching: sharpen product details, enhance material texture, balance exposure and color vibrancy while keeping the product 100% authentic."
        )
    if variant_total > 1 and (opts.get("multi_angle") or force_variation):
        hint = _IMAGE_VARIATION_HINTS[variant_index % len(_IMAGE_VARIATION_HINTS)]
        parts.append(f"[Variation {variant_index + 1}/{variant_total}] {hint}")

    extra = (opts.get("extra_prompt") or "").strip()
    if extra:
        parts.append(extra)
    return " ".join(parts) or "Clean e-commerce product photo"


def _process_openai_edit(orig_bytes: bytes, img_cfg: dict[str, Any], prompt_override: str = "") -> tuple[bytes, str | None]:
    if not img_cfg.get("api_key"):
        raise ModelError("未配置图片模型 API Key")
    url = _openai_endpoint(img_cfg.get("base_url", ""), "/images/edits")
    headers = {"Authorization": f"Bearer {img_cfg['api_key'].strip()}"}
    png_bytes = _to_png_bytes(orig_bytes)
    files = {"image": ("source.png", png_bytes, "image/png")}
    data = {
        "model": img_cfg.get("model") or "gpt-image-1",
        "prompt": prompt_override or img_cfg.get("prompt") or "Clean e-commerce product main image",
        "n": "1",
        "size": "1024x1024",
    }
    resp = requests.post(url, headers=headers, data=data, files=files, timeout=120)
    if resp.status_code >= 400:
        raise ModelError(f"图片模型 HTTP {resp.status_code}: {resp.text[:300]}")
    out_bytes, ext_url = _parse_image_api_response(resp)
    return out_bytes, ext_url


def _process_openai_chat_img(orig_bytes: bytes, img_cfg: dict[str, Any], prompt_override: str = "") -> tuple[bytes, str | None]:
    """通过 OpenAI 兼容 /chat/completions 多模态接口生图/改图（适配 Gemini / GPT-4o-image 等中转）。"""
    if not img_cfg.get("api_key"):
        raise ModelError("未配置图片模型 API Key")
    url = _openai_endpoint(img_cfg.get("base_url", ""), "/chat/completions")
    headers = {
        "Authorization": f"Bearer {img_cfg['api_key'].strip()}",
        "Content-Type": "application/json",
    }
    png_b64 = base64.b64encode(_to_png_bytes(orig_bytes)).decode("ascii")
    prompt = prompt_override or img_cfg.get("prompt") or "Clean e-commerce product main image"
    payload = {
        "model": img_cfg.get("model") or "gemini-2.5-flash-image",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{png_b64}"}},
                ],
            }
        ],
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    if resp.status_code >= 400:
        raise ModelError(f"图片模型 HTTP {resp.status_code}: {resp.text[:300]}")
    return _parse_image_api_response(resp)


def _process_custom_http(
    image_url: str,
    orig_bytes: bytes,
    detail_id: int | str,
    idx: int,
    img_cfg: dict[str, Any],
    prompt_override: str = "",
    is_sku: bool = False,
    sku_label: str = "",
    options: dict[str, Any] | None = None,
    target_language: str = "",
    variant_total: int = 1,
) -> tuple[bytes, str | None]:
    endpoint = (img_cfg.get("base_url") or "").strip()
    if not endpoint:
        raise ModelError("未配置自定义图片 API 地址")
    try:
        extra_headers = json.loads(img_cfg.get("custom_headers_json") or "{}")
    except Exception:
        extra_headers = {}
    headers = {"Content-Type": "application/json", **extra_headers}
    if img_cfg.get("api_key"):
        headers.setdefault("Authorization", f"Bearer {img_cfg['api_key'].strip()}")
    payload = {
        "model": img_cfg.get("model") or "",
        "prompt": prompt_override or img_cfg.get("prompt") or "",
        "image_url": image_url,
        "image_base64": base64.b64encode(orig_bytes).decode("ascii"),
        "detail_id": str(detail_id),
        "index": idx,
        "total_count": variant_total,
        "is_main": (not is_sku) and (idx == 0),
        "is_sku": is_sku,
        "sku_label": sku_label,
        "options": options or {},
        "target_language": target_language,
    }
    resp = requests.post(endpoint, json=payload, headers=headers, timeout=120)
    if resp.status_code >= 400:
        raise ModelError(f"自定义图片 API HTTP {resp.status_code}: {resp.text[:300]}")
    out_bytes, ext_url = _parse_image_api_response(resp)
    return out_bytes, ext_url


def upload_to_image_host(local_path: Path, img_cfg: dict[str, Any]) -> str | None:
    """如果配置了自定义图床或公网穿透前缀，返回可被妙手拉取的公网 URL。"""
    upload_url = (img_cfg.get("image_host_upload_url") or "").strip()
    if upload_url:
        with local_path.open("rb") as f:
            r = requests.post(upload_url, files={"file": (local_path.name, f, "image/png")}, timeout=60)
        r.raise_for_status()
        d = r.json()
        for k in ("url", "image_url"):
            if isinstance(d.get(k), str):
                return d[k]
        if isinstance(d.get("data"), dict) and d["data"].get("url"):
            return d["data"]["url"]
    pub_base = (img_cfg.get("public_base_url") or "").strip().rstrip("/")
    if pub_base:
        return f"{pub_base}/draft-images/{local_path.name}"
    return None


def process_single_image(
    image_url: str,
    detail_id: int | str,
    idx: int,
    img_cfg: dict[str, Any],
    *,
    style_preset: dict[str, Any] | None = None,
    options: dict[str, Any] | None = None,
    target_language: str = "",
    variant_total: int = 1,
    force_variation: bool = False,
    orig_bytes_override: bytes | None = None,
) -> dict[str, Any]:
    mode = img_cfg.get("mode") or "skip"
    if mode == "skip":
        return {"source_url": image_url, "preview_url": image_url, "public_url": image_url, "mode": "skip"}

    orig_bytes = orig_bytes_override if orig_bytes_override is not None else _download_bytes(image_url)
    ext_url: str | None = None
    main_style = (style_preset or {}).get("main_image") or {}
    eff_opts = options if options is not None else (img_cfg.get("edit_options") or {})
    ai_prompt = build_image_edit_prompt(
        img_cfg.get("prompt") or "",
        main_style.get("ai_prompt") or "",
        options=eff_opts,
        target_language=target_language,
        variant_index=idx,
        variant_total=variant_total,
        force_variation=force_variation,
    )

    if mode == "local_pillow":
        out_bytes = _render_styled_pillow(orig_bytes, img_cfg, style_cfg=main_style, is_sku=False, options=eff_opts)
    elif mode == "openai_edit":
        out_bytes, ext_url = _process_openai_edit(orig_bytes, img_cfg, prompt_override=ai_prompt)
    elif mode == "openai_chat_img":
        out_bytes, ext_url = _process_openai_chat_img(orig_bytes, img_cfg, prompt_override=ai_prompt)
    elif mode == "custom_http":
        out_bytes, ext_url = _process_custom_http(
            image_url, orig_bytes, detail_id, idx, img_cfg,
            prompt_override=ai_prompt, options=eff_opts,
            target_language=target_language, variant_total=variant_total,
        )
    else:
        raise ModelError(f"未知做图模式: {mode}")

    local_path = _save_png(out_bytes, detail_id, str(idx))
    public_url = ext_url or upload_to_image_host(local_path, img_cfg)
    return {
        "source_url": image_url,
        "local_file": local_path.name,
        "preview_url": f"/draft-images/{local_path.name}",
        "public_url": public_url,
        "mode": mode,
        "style_id": (style_preset or {}).get("id") or "",
        "options": eff_opts,
        "prompt_used": ai_prompt,
    }


def process_sku_image(
    image_url: str,
    detail_id: int | str,
    idx: int,
    sku_label: str,
    img_cfg: dict[str, Any],
    *,
    style_preset: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """按预设风格处理单条 SKU 颜色图（加规格标签/白底框或调用 AI 改图）。"""
    if not image_url:
        return {"source_url": "", "preview_url": "", "public_url": "", "mode": "empty"}
    mode = img_cfg.get("mode") or "skip"
    if mode == "skip":
        return {"source_url": image_url, "preview_url": image_url, "public_url": image_url, "mode": "skip"}

    orig_bytes = _download_bytes(image_url)
    ext_url: str | None = None
    sku_style = (style_preset or {}).get("sku_image") or {}
    ai_prompt = _merge_prompt(
        img_cfg.get("prompt") or "",
        sku_style.get("ai_prompt") or "",
        f"Variant label: {sku_label}." if sku_label else "",
    )

    if mode == "local_pillow":
        out_bytes = _render_styled_pillow(
            orig_bytes, img_cfg, style_cfg=sku_style, is_sku=True, sku_label=sku_label
        )
    elif mode == "openai_edit":
        out_bytes, ext_url = _process_openai_edit(orig_bytes, img_cfg, prompt_override=ai_prompt)
    elif mode == "openai_chat_img":
        out_bytes, ext_url = _process_openai_chat_img(orig_bytes, img_cfg, prompt_override=ai_prompt)
    elif mode == "custom_http":
        out_bytes, ext_url = _process_custom_http(
            image_url, orig_bytes, detail_id, idx, img_cfg,
            prompt_override=ai_prompt, is_sku=True, sku_label=sku_label,
        )
    else:
        raise ModelError(f"未知做图模式: {mode}")

    local_path = _save_png(out_bytes, detail_id, f"sku{idx}")
    public_url = ext_url or upload_to_image_host(local_path, img_cfg)
    return {
        "source_url": image_url,
        "local_file": local_path.name,
        "preview_url": f"/draft-images/{local_path.name}",
        "public_url": public_url,
        "mode": mode,
        "label": sku_label,
        "style_id": (style_preset or {}).get("id") or "",
    }


def test_image_model(img_cfg: dict[str, Any], style_preset: dict[str, Any] | None = None) -> dict[str, Any]:
    if img_cfg.get("mode") == "skip":
        return {"mode": "skip", "ok": True, "message": "当前为跳过做图模式"}
    buf = io.BytesIO()
    Image.new("RGB", (256, 256), (220, 235, 250)).save(buf, format="PNG")
    raw = buf.getvalue()
    t0 = time.time()
    mode = img_cfg.get("mode")
    main_style = (style_preset or {}).get("main_image") or {}
    eff_opts = img_cfg.get("edit_options") or {}
    ai_prompt = build_image_edit_prompt(
        img_cfg.get("prompt") or "", main_style.get("ai_prompt") or "", options=eff_opts
    )
    if mode == "local_pillow":
        out = _render_styled_pillow(raw, img_cfg, style_cfg=main_style, is_sku=False, options=eff_opts)
    elif mode == "openai_edit":
        out, _ = _process_openai_edit(raw, img_cfg, prompt_override=ai_prompt)
    elif mode == "openai_chat_img":
        out, _ = _process_openai_chat_img(raw, img_cfg, prompt_override=ai_prompt)
    elif mode == "custom_http":
        out, _ = _process_custom_http("https://example.com/test.png", raw, "test", 0, img_cfg, prompt_override=ai_prompt, options=eff_opts)
    else:
        raise ModelError(f"未知做图模式: {mode}")
    p = _save_png(out, "selftest", "0")
    return {
        "elapsed_ms": int((time.time() - t0) * 1000),
        "mode": mode,
        "preview_url": f"/draft-images/{p.name}",
    }
