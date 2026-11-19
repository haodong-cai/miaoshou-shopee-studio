"""模块化草稿处理流水线（Draft Template Pipeline）。

每个功能模块拆分为独立步骤并注册在 STEP_REGISTRY 中：
  1. translate   : 标题、描述与 SKU 规格属性/选项翻译
  2. main_images : 按预设风格处理产品主图
  3. sku_images  : 按预设风格处理 SKU 规格图
  4. pricing     : 按定价公式模板计算 SKU 售价与利润拆解

后续扩展新功能（如：AI 匹配类目属性、违禁词检测、尺码表生成、自动打水印等），
只需新增 step 函数并注册到 STEP_REGISTRY 即可，无需重写主流程。
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Any, Callable

from . import config, models, presets, pricing, storage

DEFAULT_STEPS = ["translate", "main_images", "sku_images", "pricing"]


@dataclass
class PipelineContext:
    cfg: dict[str, Any]
    style_preset: dict[str, Any]
    pricing_preset: dict[str, Any]
    image_options: dict[str, Any] | None = None


def build_context(
    cfg: dict[str, Any] | None = None,
    style_id: str | None = None,
    pricing_id: str | None = None,
    image_options: dict[str, Any] | None = None,
) -> PipelineContext:
    full_cfg = cfg or config.load_config()
    tpl = full_cfg.get("template") or {}
    eff_style_id = style_id or tpl.get("style_id") or "shopee_clean"
    eff_pricing_id = pricing_id or tpl.get("pricing_id") or "shopee_ph"
    style = presets.get_style_preset(eff_style_id, full_cfg.get("custom_style_presets"))
    price_cfg = pricing.get_pricing_preset(eff_pricing_id, full_cfg.get("custom_pricing_presets"))
    return PipelineContext(
        cfg=full_cfg,
        style_preset=style,
        pricing_preset=price_cfg,
        image_options=image_options,
    )


def step_translate(item: dict[str, Any], ctx: PipelineContext) -> dict[str, Any]:
    """步骤 1：翻译商品标题、描述以及 SKU 规格名/选项值。"""
    text_cfg = ctx.cfg["text_model"]
    if not text_cfg.get("enabled", True):
        return item

    sku_draft = item.setdefault("sku_draft", {})
    colors = sku_draft.get("colors") or []
    sizes = sku_draft.get("sizes") or []
    color_names = [c["orig_name"] for c in colors]
    size_names = [s["orig_name"] for s in sizes]
    style_tone = (ctx.style_preset.get("copy_style") or {}).get("tone") or ""

    res = models.generate_draft_copy(
        item.get("orig_title") or "",
        item.get("orig_notes") or "",
        text_cfg,
        color_prop_name=sku_draft.get("orig_color_prop") or "",
        size_prop_name=sku_draft.get("orig_size_prop") or "",
        color_names=color_names,
        size_names=size_names,
        style_tone=style_tone,
    )
    item["draft_title"] = res["title"]
    item["draft_notes"] = res["notes"]

    if res.get("color_prop_name"):
        sku_draft["draft_color_prop"] = res["color_prop_name"]
    if res.get("size_prop_name"):
        sku_draft["draft_size_prop"] = res["size_prop_name"]

    c_map = res.get("colors") or {}
    for c in colors:
        c["draft_name"] = c_map.get(c["orig_name"]) or c.get("draft_name") or c["orig_name"]

    s_map = res.get("sizes") or {}
    for s in sizes:
        s["draft_name"] = s_map.get(s["orig_name"]) or s.get("draft_name") or s["orig_name"]

    for sku in sku_draft.get("skus") or []:
        if sku.get("color_orig"):
            sku["color_draft"] = c_map.get(sku["color_orig"]) or sku.get("color_draft") or sku["color_orig"]
        if sku.get("size_orig"):
            sku["size_draft"] = s_map.get(sku["size_orig"]) or sku.get("size_draft") or sku["size_orig"]

    return item


def step_main_images(item: dict[str, Any], ctx: PipelineContext) -> dict[str, Any]:
    """步骤 2：按预设风格与选图/编辑选项生成产品主图。"""
    img_cfg = ctx.cfg["image_model"]
    orig_imgs: list[str] = item.get("orig_images") or []
    did = item["detail_id"]
    target_lang = (ctx.cfg.get("text_model") or {}).get("target_language") or "English"

    if ctx.image_options is None:
        pcount = int(img_cfg.get("process_count") or 0)
        target_n = len(orig_imgs) if pcount <= 0 else min(pcount, len(orig_imgs))
        draft_imgs: list[dict[str, Any]] = []
        for idx, url in enumerate(orig_imgs):
            if idx < target_n:
                res = models.process_single_image(
                    url, did, idx, img_cfg, style_preset=ctx.style_preset, target_language=target_lang
                )
                res["source_index"] = idx
                draft_imgs.append(res)
            else:
                draft_imgs.append({
                    "source_url": url,
                    "source_index": idx,
                    "preview_url": url,
                    "public_url": url,
                    "mode": "original",
                })
        item["draft_images"] = draft_imgs
        item["style_id"] = ctx.style_preset["id"]
        return item

    img_opts = ctx.image_options
    eff_opts = {**(img_cfg.get("edit_options") or {}), **(img_opts.get("options") or {})}

    pool: list[tuple[int, str]] = []
    if img_opts.get("source_urls"):
        pool = [(i, u) for i, u in enumerate(img_opts["source_urls"]) if u]
    elif isinstance(img_opts.get("selected_indices"), list) and img_opts["selected_indices"]:
        for raw_i in img_opts["selected_indices"]:
            try:
                i = int(raw_i)
            except (TypeError, ValueError):
                continue
            if 0 <= i < len(orig_imgs) and orig_imgs[i]:
                pool.append((i, orig_imgs[i]))
    if not pool:
        pool = [(i, u) for i, u in enumerate(orig_imgs) if u]

    if not pool:
        item["draft_images"] = []
        item["style_id"] = ctx.style_preset["id"]
        return item

    req_count = img_opts.get("count")
    if req_count is not None and int(req_count) > 0:
        target_n = int(req_count)
    else:
        target_n = len(pool)

    tasks = [(slot_i, pool[slot_i % len(pool)][0], pool[slot_i % len(pool)][1]) for slot_i in range(target_n)]
    force_variation = target_n > len(pool)

    cached_bytes: dict[str, bytes] = {}
    if (img_cfg.get("mode") or "skip") != "skip":
        for _, _, u in tasks:
            if u not in cached_bytes:
                cached_bytes[u] = models._download_bytes(u)

    def _run_slot(t: tuple[int, int, str]) -> dict[str, Any]:
        slot_i, orig_idx, url = t
        res = models.process_single_image(
            url,
            did,
            slot_i,
            img_cfg,
            style_preset=ctx.style_preset,
            options=eff_opts,
            target_language=target_lang,
            variant_total=target_n,
            force_variation=force_variation,
            orig_bytes_override=cached_bytes.get(url),
        )
        res["source_index"] = orig_idx
        return res

    if target_n <= 1:
        generated = [_run_slot(tasks[0])]
    else:
        with ThreadPoolExecutor(max_workers=min(4, target_n)) as ex:
            generated = list(ex.map(_run_slot, tasks))

    if img_opts.get("keep_originals"):
        used_indices = {t[1] for t in tasks}
        for idx, url in enumerate(orig_imgs):
            if idx not in used_indices:
                generated.append({
                    "source_url": url,
                    "source_index": idx,
                    "preview_url": url,
                    "public_url": url,
                    "mode": "original",
                })

    item["draft_images"] = generated
    item["style_id"] = ctx.style_preset["id"]
    item["image_edit_plan"] = {
        "count": target_n,
        "selected_indices": list(dict.fromkeys(t[1] for t in tasks)),
        "options": eff_opts,
    }
    return item


def generate_main_images_for_item(
    detail_id: int | str,
    *,
    style_id: str | None = None,
    image_options: dict[str, Any] | None = None,
    slot_index: int | None = None,
) -> dict[str, Any]:
    """按选图与编辑选项生成整组主图，或单独重做其中某一张。"""
    item = storage.get_item(detail_id)
    if not item:
        raise ValueError(f"本地草稿不存在: {detail_id}")

    ctx = build_context(
        style_id=style_id or item.get("style_id") or None,
        pricing_id=item.get("pricing_id") or None,
        image_options=image_options or {},
    )
    img_cfg = ctx.cfg["image_model"]
    target_lang = (ctx.cfg.get("text_model") or {}).get("target_language") or "English"

    try:
        if slot_index is not None:
            draft_imgs = list(item.get("draft_images") or [])
            if slot_index < 0 or slot_index >= len(draft_imgs):
                raise ValueError(f"主图槽位不存在: {slot_index}")
            cur_slot = draft_imgs[slot_index]
            orig_imgs = item.get("orig_images") or []
            src_url = cur_slot.get("source_url") or (orig_imgs[0] if orig_imgs else "")
            if not src_url:
                raise ValueError("缺少可用于重做的原图 URL")
            eff_opts = {**(img_cfg.get("edit_options") or {}), **((image_options or {}).get("options") or {})}
            new_slot = models.process_single_image(
                src_url,
                item["detail_id"],
                slot_index,
                img_cfg,
                style_preset=ctx.style_preset,
                options=eff_opts,
                target_language=target_lang,
                variant_total=len(draft_imgs),
                force_variation=bool(eff_opts.get("multi_angle")),
            )
            new_slot["source_index"] = cur_slot.get("source_index", 0)
            draft_imgs[slot_index] = new_slot
            item["draft_images"] = draft_imgs
            item["style_id"] = ctx.style_preset["id"]
        else:
            item = step_main_images(item, ctx)

        if item.get("status") in ("pending", "error", ""):
            item["status"] = "drafted"
        item["error"] = ""
    except Exception as e:
        item["status"] = "error"
        item["error"] = str(e)
        storage.save_item(item)
        raise

    return storage.save_item(item)


def step_sku_images(item: dict[str, Any], ctx: PipelineContext) -> dict[str, Any]:
    """步骤 3：按预设风格处理 SKU 规格图片。"""
    img_cfg = ctx.cfg["image_model"]
    if not img_cfg.get("sku_enabled", True):
        return item

    sku_draft = item.setdefault("sku_draft", {})
    colors = sku_draft.get("colors") or []
    did = item["detail_id"]
    for idx, c in enumerate(colors):
        orig_url = c.get("orig_img") or ""
        if not orig_url:
            continue
        label = (c.get("draft_name") or c.get("orig_name") or "").strip()
        c["draft_img"] = models.process_sku_image(
            orig_url, did, idx, label, img_cfg, style_preset=ctx.style_preset
        )
    item["style_id"] = ctx.style_preset["id"]
    return item


def step_pricing(item: dict[str, Any], ctx: PipelineContext) -> dict[str, Any]:
    """步骤 4：按定价公式计算所有 SKU 售价及利润明细。"""
    pcfg = ctx.pricing_preset
    sku_draft = item.setdefault("sku_draft", {})
    skus = sku_draft.get("skus") or []

    min_price: float | None = None
    max_price: float | None = None
    profits: list[float] = []
    margins: list[float] = []

    for sku in skus:
        cost = float(sku.get("cost_rmb") or 0.0)
        weight = float(sku.get("weight_kg") or 0.0)
        orig_p = float(sku.get("orig_price") or 0.0)
        calc = pricing.calculate_price(cost, weight, pcfg, orig_sell_price=orig_p)
        sku["draft_price"] = calc["final_price"]
        sku["shipping_rmb"] = calc["shipping_rmb"]
        sku["profit_rmb"] = calc["profit_rmb"]
        sku["margin_pct"] = calc["margin_pct"]
        sku["currency"] = calc["currency"]

        fp = float(calc["final_price"])
        min_price = fp if min_price is None else min(min_price, fp)
        max_price = fp if max_price is None else max(max_price, fp)
        profits.append(float(calc["profit_rmb"]))
        margins.append(float(calc["margin_pct"]))

    item["pricing_id"] = pcfg["id"]
    item["pricing_summary"] = {
        "pricing_id": pcfg["id"],
        "pricing_name": pcfg.get("name") or pcfg["id"],
        "currency": pcfg.get("currency") or "PHP",
        "min_price": min_price,
        "max_price": max_price,
        "avg_profit_rmb": round(sum(profits) / len(profits), 2) if profits else 0.0,
        "avg_margin_pct": round(sum(margins) / len(margins), 1) if margins else 0.0,
    }
    return item


STEP_REGISTRY: dict[str, Callable[[dict[str, Any], PipelineContext], dict[str, Any]]] = {
    "translate": step_translate,
    "main_images": step_main_images,
    "sku_images": step_sku_images,
    "pricing": step_pricing,
}


def run_draft_pipeline(
    detail_id: int | str,
    *,
    steps: list[str] | None = None,
    style_id: str | None = None,
    pricing_id: str | None = None,
    image_options: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """执行指定草稿处理步骤并持久化结果。"""
    item = storage.get_item(detail_id)
    if not item:
        raise ValueError(f"本地草稿不存在: {detail_id}")

    chosen = [s for s in (steps or DEFAULT_STEPS) if s in STEP_REGISTRY]
    if not chosen:
        chosen = list(DEFAULT_STEPS)

    ctx = build_context(
        style_id=style_id or item.get("style_id") or None,
        pricing_id=pricing_id or item.get("pricing_id") or None,
        image_options=image_options,
    )

    try:
        for step_name in chosen:
            item = STEP_REGISTRY[step_name](item, ctx)
        item["status"] = "drafted"
        item["error"] = ""
    except Exception as e:
        item["status"] = "error"
        item["error"] = str(e)
        storage.save_item(item)
        raise

    return storage.save_item(item)
