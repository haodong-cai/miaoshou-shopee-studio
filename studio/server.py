"""铺货草稿工作台 Web 服务（FastAPI）。"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import uvicorn
from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, Response

from . import assistant, config, models, pipeline, presets, pricing, service, storage

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="妙手铺货草稿工作台", version="2.0.0")


def _slim_item(item: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in item.items() if k != "raw_site_data"}


@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(
        content=(STATIC_DIR / "index.html").read_text(encoding="utf-8"),
        headers={"Cache-Control": "no-store"},
    )


@app.get("/draft-images/{filename}")
def get_draft_image(filename: str):
    if "/" in filename or "\\" in filename or ".." in filename:
        raise HTTPException(400, "非法文件名")
    p = storage.IMAGES_DIR / filename
    if not p.exists() or not p.is_file():
        raise HTTPException(404, "图片不存在")
    return FileResponse(p)


@app.get("/api/config")
def api_get_config():
    return config.load_public_config()


@app.post("/api/config")
def api_save_config(patch: dict[str, Any] = Body(...)):
    return config.save_config(patch)


@app.get("/api/miaoshou/credentials")
def api_get_miaoshou_credentials():
    return config.load_miaoshou_env_public()


@app.post("/api/miaoshou/credentials")
def api_save_miaoshou_credentials(payload: dict[str, Any] = Body(...)):
    try:
        return config.save_miaoshou_env(payload)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/test/miaoshou")
def api_test_miaoshou(payload: dict[str, Any] = Body(default={})):
    try:
        return service.test_miaoshou_connection(payload if payload else None)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/test/assistant")
def api_test_assistant(payload: dict[str, Any] = Body(default={})):
    try:
        return assistant.test_assistant_model(payload if payload else None)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/assistant/ask")
def api_assistant_ask(payload: dict[str, Any] = Body(...)):
    try:
        return assistant.ask_assistant(
            question=str(payload.get("question") or ""),
            history=payload.get("history") if isinstance(payload.get("history"), list) else None,
            assistant_override=payload.get("assistant_override") if isinstance(payload.get("assistant_override"), dict) else None,
        )
    except Exception as e:
        raise HTTPException(400, str(e))


@app.get("/api/assistant/knowledge")
def api_assistant_knowledge(q: str = ""):
    return assistant.list_knowledge_index(q)


@app.get("/api/presets")
def api_get_presets():
    cfg = config.load_config()
    tpl = cfg.get("template") or {}
    return {
        "style_presets": presets.list_style_presets(cfg.get("custom_style_presets")),
        "pricing_presets": pricing.list_pricing_presets(cfg.get("custom_pricing_presets")),
        "active_style_id": tpl.get("style_id") or "shopee_clean",
        "active_pricing_id": tpl.get("pricing_id") or "shopee_ph",
        "available_steps": list(pipeline.STEP_REGISTRY.keys()),
    }


@app.post("/api/presets/style")
def api_save_style_preset(payload: dict[str, Any] = Body(...)):
    pid = str(payload.get("id") or "").strip()
    if not pid:
        raise HTTPException(400, "风格模板 ID 不能为空")
    config.save_config({"custom_style_presets": {pid: payload}})
    return api_get_presets()


@app.post("/api/presets/pricing")
def api_save_pricing_preset(payload: dict[str, Any] = Body(...)):
    pid = str(payload.get("id") or "").strip()
    if not pid:
        raise HTTPException(400, "定价模板 ID 不能为空")
    config.save_config({"custom_pricing_presets": {pid: payload}})
    return api_get_presets()


@app.get("/api/pricing/fx")
def api_pricing_fx(base: str = "CNY"):
    try:
        return pricing.fetch_live_fx_rates(base=base)
    except Exception as e:
        raise HTTPException(400, f"获取实时汇率失败: {e}")


@app.post("/api/pricing/preview")
def api_pricing_preview(payload: dict[str, Any] = Body(...)):
    raw_cost = payload.get("cost_rmb")
    raw_weight = payload.get("weight_kg")
    cost = 18.0 if (raw_cost is None or raw_cost == "") else float(raw_cost)
    weight = 0.1 if (raw_weight is None or raw_weight == "") else float(raw_weight)
    pcfg = payload.get("pricing_cfg")
    if not pcfg:
        cfg = config.load_config()
        pid = payload.get("pricing_id") or (cfg.get("template") or {}).get("pricing_id")
        pcfg = pricing.get_pricing_preset(pid, cfg.get("custom_pricing_presets"))
    try:
        return pricing.calculate_price(cost, weight, pcfg)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/test/text")
def api_test_text(payload: dict[str, Any] = Body(default={})):
    cfg = config.resolve_runtime_config({"text_model": payload} if payload else None)
    try:
        return models.test_text_model(cfg["text_model"])
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/test/image")
def api_test_image(payload: dict[str, Any] = Body(default={})):
    raw_payload = dict(payload) if isinstance(payload, dict) else {}
    style_id = raw_payload.pop("style_id", None)
    cfg = config.resolve_runtime_config({"image_model": raw_payload} if raw_payload else None)
    eff_style_id = style_id or (cfg.get("template") or {}).get("style_id")
    style = presets.get_style_preset(eff_style_id, cfg.get("custom_style_presets"))
    if not style_id and ("pillow_size" in raw_payload or "pillow_badge" in raw_payload):
        import copy
        style = copy.deepcopy(style)
        if "pillow_size" in raw_payload:
            style.setdefault("main_image", {})["canvas_size"] = raw_payload["pillow_size"]
        if "pillow_badge" in raw_payload:
            style.setdefault("main_image", {})["badge_text"] = raw_payload["pillow_badge"]
    try:
        return models.test_image_model(cfg["image_model"], style_preset=style)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.get("/api/shops")
def api_shops(refresh: bool = False):
    try:
        return {"shops": service.list_shopee_shops(refresh=refresh)}
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/collect/pull")
def api_pull(payload: dict[str, Any] = Body(default={})):
    try:
        return service.pull_collect_box(
            site=str(payload.get("site") or "PH"),
            status=str(payload.get("status") or "notPublished"),
            limit=int(payload.get("limit") or 20),
        )
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/collect/url")
def api_collect_url(payload: dict[str, Any] = Body(...)):
    try:
        return service.collect_from_url(
            source_url=str(payload.get("url") or ""),
            site=str(payload.get("site") or "PH"),
            auto_claim=bool(payload.get("auto_claim", True)),
            auto_process=bool(payload.get("auto_process", False)),
            style_id=payload.get("style_id") or None,
            pricing_id=payload.get("pricing_id") or None,
        )
    except Exception as e:
        raise HTTPException(400, str(e))


@app.get("/api/collect/common")
def api_list_common(page_no: int = 1, page_size: int = 20, tab: str = "all"):
    try:
        return service.list_common_collect_box(page_no=page_no, page_size=page_size, tab=tab)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/collect/common/claim")
def api_claim_common(payload: dict[str, Any] = Body(...)):
    cids = payload.get("common_detail_ids") or []
    site = str(payload.get("site") or "PH")
    try:
        return service.claim_common_items(cids, site=site)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.get("/api/drafts")
def api_list_drafts():
    items = [_slim_item(x) for x in storage.list_items()]
    return {"items": items}


@app.post("/api/drafts/manual")
def api_create_manual_draft(payload: dict[str, Any] = Body(...)):
    try:
        item = service.create_manual_draft(payload)
        return _slim_item(item)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.get("/api/drafts/export.csv")
def api_export_drafts_csv(ids: str = ""):
    dids = [int(x) for x in ids.split(",") if x.strip().isdigit()] if ids else None
    csv_bytes = service.export_drafts_csv(dids)
    return Response(
        content=csv_bytes,
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="miaoshou_drafts.csv"'},
    )


@app.patch("/api/drafts/{detail_id}")
def api_update_draft(detail_id: int, payload: dict[str, Any] = Body(...)):
    item = storage.get_item(detail_id)
    if not item:
        raise HTTPException(404, "草稿不存在")
    if "draft_title" in payload:
        item["draft_title"] = str(payload["draft_title"])
    if "draft_notes" in payload:
        item["draft_notes"] = str(payload["draft_notes"])
    if "draft_images" in payload and isinstance(payload["draft_images"], list):
        item["draft_images"] = payload["draft_images"]
    if "style_id" in payload:
        item["style_id"] = str(payload["style_id"])
    if "pricing_id" in payload:
        item["pricing_id"] = str(payload["pricing_id"])

    # 支持在线微调 SKU 属性名、颜色/尺码译文、单条 SKU 成本/重量/售价
    if "sku_patch" in payload and isinstance(payload["sku_patch"], dict):
        sp = payload["sku_patch"]
        sd = item.setdefault("sku_draft", {})
        if "draft_color_prop" in sp:
            sd["draft_color_prop"] = str(sp["draft_color_prop"])
        if "draft_size_prop" in sp:
            sd["draft_size_prop"] = str(sp["draft_size_prop"])
        if isinstance(sp.get("color_rename"), dict):
            orig_n = sp["color_rename"].get("orig_name")
            new_n = str(sp["color_rename"].get("draft_name") or "")
            for c in sd.get("colors") or []:
                if c.get("orig_name") == orig_n:
                    c["draft_name"] = new_n
            for sk in sd.get("skus") or []:
                if sk.get("color_orig") == orig_n:
                    sk["color_draft"] = new_n
        if isinstance(sp.get("size_rename"), dict):
            orig_n = sp["size_rename"].get("orig_name")
            new_n = str(sp["size_rename"].get("draft_name") or "")
            for s in sd.get("sizes") or []:
                if s.get("orig_name") == orig_n:
                    s["draft_name"] = new_n
            for sk in sd.get("skus") or []:
                if sk.get("size_orig") == orig_n:
                    sk["size_draft"] = new_n
        sku_price_dirty = False
        if isinstance(sp.get("sku_row"), dict):
            row = sp["sku_row"]
            okey = row.get("orig_key")
            for sk in sd.get("skus") or []:
                if sk.get("orig_key") == okey:
                    for num_f in ("draft_price", "cost_rmb", "weight_kg"):
                        if num_f in row and row[num_f] is not None and row[num_f] != "":
                            sk[num_f] = float(row[num_f])
                            sku_price_dirty = True
                    if "stock" in row and row["stock"] is not None and row["stock"] != "":
                        sk["stock"] = int(float(row["stock"]))
            if "stock" in row:
                item["stock"] = str(sum(int(s.get("stock") or 0) for s in (sd.get("skus") or [])))
            if sku_price_dirty and not payload.get("auto_reprice"):
                service.refresh_manual_pricing_summary(
                    item, pricing_id=payload.get("pricing_id") or item.get("pricing_id") or None
                )

    if item.get("status") == "pending" and (item.get("draft_title") or item.get("draft_notes")):
        item["status"] = "drafted"
    saved = storage.save_item(item)
    if payload.get("auto_reprice"):
        saved = service.recalculate_item_pricing(detail_id, pricing_id=payload.get("pricing_id") or None)
    return _slim_item(saved)


@app.post("/api/drafts/batch-edit")
def api_batch_edit_drafts(payload: dict[str, Any] = Body(...)):
    dids = payload.get("detail_ids") or []
    ops = payload.get("ops") or {}
    if not dids:
        raise HTTPException(400, "请先选择商品")
    try:
        res = service.batch_edit_drafts(
            dids,
            ops,
            auto_reprice=bool(payload.get("auto_reprice", True)),
            pricing_id=payload.get("pricing_id") or None,
        )
        return {"updated": res["updated"], "items": [_slim_item(x) for x in res["items"]]}
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/drafts/{detail_id}/reprice")
def api_reprice_draft(detail_id: int, payload: dict[str, Any] = Body(default={})):
    try:
        updated = service.recalculate_item_pricing(
            detail_id, pricing_id=payload.get("pricing_id") or None
        )
        return _slim_item(updated)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/drafts/{detail_id}/generate-images")
def api_generate_item_images(detail_id: int, payload: dict[str, Any] = Body(default={})):
    try:
        slot_raw = payload.get("slot_index")
        slot_idx = int(slot_raw) if slot_raw is not None else None
        img_opts = {
            "count": payload.get("count"),
            "selected_indices": payload.get("selected_indices"),
            "source_urls": payload.get("source_urls"),
            "options": payload.get("options") or {},
            "keep_originals": bool(payload.get("keep_originals", False)),
        }
        updated = service.generate_item_main_images(
            detail_id,
            style_id=payload.get("style_id") or None,
            image_options=img_opts,
            slot_index=slot_idx,
        )
        return _slim_item(updated)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.delete("/api/drafts/{detail_id}")
def api_delete_draft(detail_id: int):
    return {"deleted": storage.delete_item(detail_id)}


@app.post("/api/jobs/generate")
def api_start_generate(payload: dict[str, Any] = Body(...)):
    dids = payload.get("detail_ids") or []
    if not dids:
        raise HTTPException(400, "请先选择商品")
    steps = payload.get("steps")
    job_id = service.start_batch_job(
        dids,
        do_text=bool(payload.get("do_text", True)),
        do_image=bool(payload.get("do_image", True)),
        steps=steps if isinstance(steps, list) else None,
        style_id=payload.get("style_id") or None,
        pricing_id=payload.get("pricing_id") or None,
        image_options=payload.get("image_options"),
        per_item_image_options=payload.get("per_item_image_options"),
    )
    return {"job_id": job_id}


@app.get("/api/jobs/{job_id}")
def api_job_status(job_id: str):
    j = service.get_job(job_id)
    if not j:
        raise HTTPException(404, "任务不存在")
    return j


@app.post("/api/miaoshou/sync")
def api_sync(payload: dict[str, Any] = Body(...)):
    dids = payload.get("detail_ids") or []
    if not dids:
        raise HTTPException(400, "请先选择商品")
    try:
        return service.sync_to_miaoshou(dids)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.post("/api/miaoshou/publish")
def api_publish(payload: dict[str, Any] = Body(...)):
    dids = payload.get("detail_ids") or []
    sids = payload.get("shop_ids") or []
    if not dids or not sids:
        raise HTTPException(400, "请选择商品和目标店铺")
    try:
        return service.publish_items(dids, sids)
    except Exception as e:
        raise HTTPException(400, str(e))


@app.get("/api/miaoshou/publish-records")
def api_publish_records(page_no: int = 1, page_size: int = 20):
    try:
        return service.list_publish_records(page_no, page_size)
    except Exception as e:
        raise HTTPException(400, str(e))


def run(host: str = "127.0.0.1", port: int = 18765):
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    run()
