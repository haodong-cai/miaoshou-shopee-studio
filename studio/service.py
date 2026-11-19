"""业务编排层：货源采集/公共采集箱认领 -> 拉取妙手采集箱 -> 草稿流水线 -> 同步回妙手/发布。"""
from __future__ import annotations

import copy
import csv
import io
import json
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any
from urllib.parse import urlparse

from miaoshou import MiaoshouClient

from . import config, pipeline, storage

SHOPEE_SITES = "PH TW ID MY SG TH VN BR MX CL CO PL ES FR AR SHOPEEGLOBAL".split()
SHOPS_CACHE_PATH = storage.ROOT / "out" / "shops.json"

_JOBS: dict[str, dict[str, Any]] = {}
_JOBS_LOCK = threading.Lock()
_SHOPS_CACHE: list[dict[str, Any]] = []


def _client() -> MiaoshouClient:
    return MiaoshouClient()


def _read_shops_cache() -> list[dict[str, Any]]:
    if _SHOPS_CACHE:
        return copy.deepcopy(_SHOPS_CACHE)
    if SHOPS_CACHE_PATH.exists():
        try:
            data = json.loads(SHOPS_CACHE_PATH.read_text(encoding="utf-8"))
            if isinstance(data, list) and data:
                _SHOPS_CACHE[:] = data
                return copy.deepcopy(data)
        except Exception:
            pass
    return []


def list_shopee_shops(refresh: bool = False) -> list[dict[str, Any]]:
    """查询账号下所有有店铺的 Shopee 站点/全球店铺（优先走本地缓存，避免接口限流/超时卡住页面）。"""
    cached = _read_shops_cache()
    if not refresh and cached:
        return cached

    c = MiaoshouClient(timeout=8, max_retries=0)
    shops: list[dict[str, Any]] = []
    queries = [("shopeeGlobal", "SHOPEEGLOBAL")] + [("shopee", s) for s in SHOPEE_SITES if s != "SHOPEEGLOBAL"]

    def _fetch(q):
        plat, site = q
        r = c.call_raw("product/shop/shop/get_shop_list",
                       {"platform": plat, "site": site, "pageNo": 1, "pageSize": 100})
        if r.get("result") != "success":
            return []
        d = r.get("data") or {}
        lst = next((v for v in d.values() if isinstance(v, list)), []) if isinstance(d, dict) else []
        for s in lst:
            s["platform"] = plat
            s["site"] = site
        return lst

    try:
        with ThreadPoolExecutor(6) as ex:
            for res in ex.map(_fetch, queries):
                shops.extend(res)
    except Exception:
        shops = []

    if shops:
        _SHOPS_CACHE[:] = shops
        try:
            SHOPS_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            SHOPS_CACHE_PATH.write_text(json.dumps(shops, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass
        return copy.deepcopy(shops)

    return cached


def _build_item_from_site_detail(
    did: int,
    site: str,
    status: str,
    detail: dict[str, Any],
    row: dict[str, Any] | None = None,
) -> dict[str, Any]:
    row = row or {}
    sd = detail.get("siteDetailSimpleData") or {}
    existing = storage.get_item(did) or {}
    orig_imgs = sd.get("imgUrls") or ([row["thumbnail"]] if row.get("thumbnail") else [])

    fresh_sku = storage.extract_sku_draft(
        sd,
        fallback_price=sd.get("price") or row.get("price") or "",
        fallback_stock=sd.get("stock") or row.get("stock") or "",
    )
    # 如果本地已有草稿翻译/改图/定价，保留与现有规格匹配的草稿字段
    if existing.get("sku_draft"):
        old_sku = existing["sku_draft"]
        fresh_sku["draft_color_prop"] = old_sku.get("draft_color_prop") or ""
        fresh_sku["draft_size_prop"] = old_sku.get("draft_size_prop") or ""
        old_c_by_name: dict[str, dict[str, Any]] = {}
        for c in (old_sku.get("colors") or []):
            old_c_by_name[c["orig_name"]] = c
            if c.get("synced_name"):
                old_c_by_name[c["synced_name"]] = c
        for c in fresh_sku["colors"]:
            oc = old_c_by_name.get(c["orig_name"])
            if oc:
                c["draft_name"] = oc.get("draft_name") or ""
                c["draft_img"] = oc.get("draft_img")
                if oc.get("synced_name"):
                    c["synced_name"] = oc["synced_name"]
        old_s_by_name: dict[str, dict[str, Any]] = {}
        for s in (old_sku.get("sizes") or []):
            old_s_by_name[s["orig_name"]] = s
            if s.get("synced_name"):
                old_s_by_name[s["synced_name"]] = s
        for s in fresh_sku["sizes"]:
            os_ = old_s_by_name.get(s["orig_name"])
            if os_:
                s["draft_name"] = os_.get("draft_name") or ""
                if os_.get("synced_name"):
                    s["synced_name"] = os_["synced_name"]
        old_skus_by_key: dict[str, dict[str, Any]] = {}
        for k in (old_sku.get("skus") or []):
            old_skus_by_key[k["orig_key"]] = k
            if k.get("synced_key"):
                old_skus_by_key[k["synced_key"]] = k
        for sk in fresh_sku["skus"]:
            osk = old_skus_by_key.get(sk["orig_key"])
            if osk:
                for fld in ("color_draft", "size_draft", "draft_price", "shipping_rmb", "profit_rmb", "margin_pct", "currency", "synced_key"):
                    if osk.get(fld) is not None:
                        sk[fld] = osk.get(fld)

    item = {
        "detail_id": did,
        "site": site,
        "list_status": status,
        "price": sd.get("price") or row.get("price") or "",
        "stock": sd.get("stock") or row.get("stock") or "",
        "cid": sd.get("cid"),
        "gmt_create": row.get("gmtCreate") or existing.get("gmt_create") or "",
        "oss_md5": detail.get("ossMd5") or "",
        "orig_title": sd.get("title") or row.get("title") or "",
        "orig_notes": sd.get("notes") or "",
        "orig_images": orig_imgs,
        "raw_site_data": sd,
        "sku_draft": fresh_sku,
        "style_id": existing.get("style_id") or "",
        "pricing_id": existing.get("pricing_id") or "",
        "pricing_summary": existing.get("pricing_summary") or {},
        "draft_title": existing.get("draft_title") or "",
        "draft_notes": existing.get("draft_notes") or "",
        "draft_images": existing.get("draft_images") or [],
        "status": existing.get("status") or "pending",
        "error": existing.get("error") or "",
        "last_sync_warn": existing.get("last_sync_warn") or "",
    }
    if existing.get("image_edit_plan"):
        item["image_edit_plan"] = existing["image_edit_plan"]
    return storage.save_item(item)


def pull_single_detail(detail_id: int | str, site: str = "PH", status: str = "notPublished") -> dict[str, Any]:
    """拉取单个 Shopee 采集箱产品详情到本地草稿工作台。"""
    c = _client()
    did = int(detail_id)
    detail = c.call(
        "product/collect_box/shopee/collect_box/get_site_detail_simple_data",
        {"detailId": did, "site": site},
    )
    return _build_item_from_site_detail(did, site, status, detail)


def pull_collect_box(site: str = "PH", status: str = "notPublished", limit: int = 20) -> dict[str, Any]:
    """从妙手 Shopee 采集箱拉取商品及站点编辑详情，写入本地草稿库。"""
    c = _client()
    body: dict[str, Any] = {"pageNo": 1, "pageSize": max(1, min(200, int(limit)))}
    if status and status != "all":
        body["filter"] = {"status": status}
    lst_data = c.call("product/collect_box/shopee/collect_box/search_collect_box_detail_list", body) or {}
    rows = lst_data.get("detailList") or []

    def _load_detail(row: dict[str, Any]) -> dict[str, Any]:
        did = int(row["collectBoxDetailId"])
        detail = c.call("product/collect_box/shopee/collect_box/get_site_detail_simple_data",
                        {"detailId": did, "site": site})
        return _build_item_from_site_detail(did, site, status, detail, row=row)

    pulled: list[dict[str, Any]] = []
    errors: list[str] = []
    with ThreadPoolExecutor(4) as ex:
        futs = {ex.submit(_load_detail, r): r.get("collectBoxDetailId") for r in rows}
        for fut in as_completed(futs):
            did = futs[fut]
            try:
                pulled.append(fut.result())
            except Exception as e:
                errors.append(f"{did}: {e}")
    return {"pulled": len(pulled), "errors": errors}


# ------------------------------------------------------------------ Common Collect Box & URL Collection


def validate_collect_url(url: str) -> str:
    """校验货源链接基本合法性（防止 fetch_item 高危接口因无效链接误采无关商品）。"""
    cleaned = (url or "").strip()
    if not cleaned:
        raise ValueError("请输入货源链接")
    parsed = urlparse(cleaned)
    if parsed.scheme not in ("http", "https") or not parsed.netloc or "." not in parsed.netloc:
        raise ValueError("货源链接格式无效，必须为完整的 http(s):// 商品详情 URL")
    if parsed.hostname in ("localhost", "127.0.0.1", "0.0.0.0"):
        raise ValueError("不支持采集本地地址")
    if (not parsed.path or parsed.path == "/") and not parsed.query:
        raise ValueError("请提供具体商品详情页链接，而非站点首页")
    return cleaned


def list_common_collect_box(page_no: int = 1, page_size: int = 20, tab: str = "all") -> dict[str, Any]:
    """查询妙手公共采集箱列表。"""
    c = _client()
    body: dict[str, Any] = {
        "pageNo": max(1, int(page_no)),
        "pageSize": max(1, min(100, int(page_size))),
    }
    if tab and tab != "all":
        body["filter"] = {"tabPaneName": tab}
    return c.call("product/common_collect_box/common_collect_box/get_common_collect_box_list", body) or {}


def claim_common_items(common_detail_ids: list[int | str], site: str = "PH") -> dict[str, Any]:
    """将公共采集箱商品认领到 Shopee 采集箱，并自动拉取进本地工作台。"""
    if not common_detail_ids:
        raise ValueError("请先选择要认领的公共采集箱商品")
    c = _client()
    payload_list = [
        {"detailId": int(cid), "platform": "shopee", "serialNumber": idx + 1}
        for idx, cid in enumerate(common_detail_ids)
    ]
    res = c.call(
        "product/common_collect_box/common_collect_box/claimed",
        {"detailSerialNumberPlatformList": payload_list},
    ) or {}
    id_map = (res.get("platformCollectBoxDetailIdMap") or {}).get("shopee") or {}
    imported: list[int] = []
    errors: list[str] = []
    for k, shopee_did in id_map.items():
        try:
            item = pull_single_detail(int(shopee_did), site=site)
            imported.append(int(item["detail_id"]))
        except Exception as e:
            errors.append(f"{k}->{shopee_did}: {e}")
    return {"claimed_map": id_map, "imported_detail_ids": imported, "errors": errors}


def collect_from_url(
    source_url: str,
    site: str = "PH",
    *,
    auto_claim: bool = True,
    auto_process: bool = False,
    style_id: str | None = None,
    pricing_id: str | None = None,
) -> dict[str, Any]:
    """通过货源链接采集进妙手公共采集箱，并自动认领到 Shopee 导入工作台。"""
    url = validate_collect_url(source_url)
    c = _client()
    before = list_common_collect_box(page_no=1, page_size=20, tab="all")
    before_ids = {int(x["commonCollectBoxDetailId"]) for x in (before.get("detailList") or [])}

    c.call("product/common_collect_box/common_collect_box/fetch_item", {"collectLinks": [url]})

    new_common_id: int | None = None
    for _ in range(5):
        time.sleep(1.0)
        after = list_common_collect_box(page_no=1, page_size=20, tab="all")
        rows = after.get("detailList") or []
        for r in rows:
            cid = int(r["commonCollectBoxDetailId"])
            src_urls = [s.get("sourceItemUrl") or "" for s in (r.get("sourceList") or [])]
            if cid not in before_ids or any(url in u or u in url for u in src_urls if u):
                new_common_id = cid
                break
        if new_common_id is not None:
            break

    if new_common_id is None:
        return {
            "collected": True,
            "common_detail_id": None,
            "imported_detail_ids": [],
            "message": "已提交采集任务，请在「公共采集箱」弹窗刷新查看并在列表中认领导入。",
        }

    if not auto_claim:
        return {
            "collected": True,
            "common_detail_id": new_common_id,
            "imported_detail_ids": [],
            "message": f"已采集到公共采集箱 #{new_common_id}",
        }

    claim_res = claim_common_items([new_common_id], site=site)
    imported_ids = claim_res.get("imported_detail_ids") or []
    if auto_process and imported_ids:
        for did in imported_ids:
            pipeline.run_draft_pipeline(did, style_id=style_id, pricing_id=pricing_id)

    return {
        "collected": True,
        "common_detail_id": new_common_id,
        "imported_detail_ids": imported_ids,
        "errors": claim_res.get("errors") or [],
        "message": f"采集并认领成功，已导入工作台：{imported_ids}" if imported_ids else "采集完成，请确认认领状态",
    }


# ------------------------------------------------------------------ Draft Pipeline & Batch Jobs


def process_one_item(
    detail_id: int | str,
    do_text: bool = True,
    do_image: bool = True,
    *,
    steps: list[str] | None = None,
    style_id: str | None = None,
    pricing_id: str | None = None,
    image_options: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """使用配置好的草稿流水线处理单条商品。"""
    if steps is None:
        steps = []
        if do_text:
            steps.append("translate")
        if do_image:
            steps.extend(["main_images", "sku_images"])
        steps.append("pricing")
    return pipeline.run_draft_pipeline(
        detail_id, steps=steps, style_id=style_id, pricing_id=pricing_id, image_options=image_options
    )


def generate_item_main_images(
    detail_id: int | str,
    *,
    style_id: str | None = None,
    image_options: dict[str, Any] | None = None,
    slot_index: int | None = None,
) -> dict[str, Any]:
    """针对单条商品按选图与编辑选项生成主图或重做单张槽位。"""
    return pipeline.generate_main_images_for_item(
        detail_id,
        style_id=style_id,
        image_options=image_options,
        slot_index=slot_index,
    )


def _apply_num_op(cur: float, op: str, val: float, *, min_val: float = 0.0) -> float:
    if op == "set":
        out = val
    elif op == "add":
        out = cur + val
    elif op == "mul":
        out = cur * val
    else:
        raise ValueError(f"不支持的批量操作: {op}")
    return max(min_val, out)


def batch_edit_drafts(
    detail_ids: list[int | str],
    ops: dict[str, Any],
    *,
    auto_reprice: bool = True,
    pricing_id: str | None = None,
) -> dict[str, Any]:
    """批量修改多个（或单个）草稿的进货价、重量、库存、售价与标题。"""
    if not detail_ids:
        raise ValueError("请先选择要修改的商品")

    cfg = config.load_config()
    color_filter = (ops.get("color_filter") or "").strip()
    sku_keys = set(ops.get("sku_keys") or [])

    cost_op = ops.get("cost_rmb")
    weight_op = ops.get("weight_kg")
    stock_op = ops.get("stock")
    price_op = ops.get("draft_price")

    title_prefix = ops.get("title_prefix") or ""
    title_suffix = ops.get("title_suffix") or ""
    title_find = ops.get("title_find") or ""
    title_replace = ops.get("title_replace") or ""

    updated_items: list[dict[str, Any]] = []
    for did in detail_ids:
        item = storage.get_item(did)
        if not item:
            continue

        # 1) 标题批量前后缀 / 查找替换
        if title_prefix or title_suffix or title_find:
            base_t = item.get("draft_title") or item.get("orig_title") or ""
            if title_find:
                base_t = base_t.replace(title_find, title_replace)
            item["draft_title"] = f"{title_prefix}{base_t}{title_suffix}".strip()

        # 2) SKU 批量修改（进货价 / 重量 / 库存 / 售价）
        sd = item.setdefault("sku_draft", {})
        skus = sd.get("skus") or []
        total_stock = 0
        for sk in skus:
            matched = True
            if color_filter and sk.get("color_orig") != color_filter and sk.get("color_draft") != color_filter:
                matched = False
            if sku_keys and sk.get("orig_key") not in sku_keys:
                matched = False

            if matched:
                if cost_op and cost_op.get("op") in ("set", "add", "mul"):
                    sk["cost_rmb"] = round(_apply_num_op(float(sk.get("cost_rmb") or 0), cost_op["op"], float(cost_op["value"])), 2)
                if weight_op and weight_op.get("op") in ("set", "add", "mul"):
                    sk["weight_kg"] = round(_apply_num_op(float(sk.get("weight_kg") or 0), weight_op["op"], float(weight_op["value"])), 3)
                if stock_op and stock_op.get("op") in ("set", "add"):
                    sk["stock"] = int(round(_apply_num_op(float(sk.get("stock") or 0), stock_op["op"], float(stock_op["value"]))))
                if price_op and price_op.get("op") in ("set", "add", "mul"):
                    base_p = float(sk.get("draft_price") if sk.get("draft_price") is not None else (sk.get("orig_price") or 0))
                    sk["draft_price"] = round(_apply_num_op(base_p, price_op["op"], float(price_op["value"]), min_val=0.01), 2)

            total_stock += int(sk.get("stock") or 0)

        if stock_op and skus:
            item["stock"] = str(total_stock)

        # 若改动了进货价/重量且未显式覆盖售价，按当前公式重算价格与利润
        should_reprice = auto_reprice and (cost_op or weight_op) and not price_op
        if should_reprice:
            ctx = pipeline.build_context(cfg=cfg, pricing_id=pricing_id or item.get("pricing_id") or None)
            pipeline.step_pricing(item, ctx)
        elif price_op or cost_op or weight_op:
            # 手动改售价或关闭自动重算时，仍按完整站点费率与当前重量同步更新藏价、利润与区间汇总
            refresh_manual_pricing_summary(item, pricing_id=pricing_id or item.get("pricing_id") or None, cfg=cfg)

        if item.get("status") == "pending":
            item["status"] = "drafted"
        updated_items.append(storage.save_item(item))

    return {"updated": len(updated_items), "items": updated_items}


def refresh_manual_pricing_summary(
    item: dict[str, Any],
    *,
    pricing_id: str | None = None,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """根据各 SKU 当前手动售价(draft_price)、进货价与重量，精确重算运费、净利润与 pricing_summary。"""
    ctx = pipeline.build_context(cfg=cfg, pricing_id=pricing_id or item.get("pricing_id") or None)
    pcfg = ctx.pricing_preset
    skus = (item.get("sku_draft") or {}).get("skus") or []
    prices: list[float] = []
    profits: list[float] = []
    margins: list[float] = []
    for sk in skus:
        if sk.get("draft_price") is not None:
            ev = pipeline.pricing.evaluate_manual_price(
                final_price=float(sk["draft_price"]),
                cost_rmb=float(sk.get("cost_rmb") or 0.0),
                weight_kg=float(sk.get("weight_kg") or 0.0),
                cfg=pcfg,
            )
            sk["shipping_rmb"] = ev["shipping_rmb"]
            sk["currency"] = ev["currency"]
            sk["profit_rmb"] = ev["profit_rmb"]
            sk["margin_pct"] = ev["margin_pct"]
            prices.append(ev["final_price"])
            profits.append(ev["profit_rmb"])
            margins.append(ev["margin_pct"])
    if prices:
        item["pricing_id"] = pcfg["id"]
        item["pricing_summary"] = {
            "pricing_id": pcfg["id"],
            "pricing_name": pcfg.get("name") or pcfg["id"],
            "currency": pcfg.get("currency") or "PHP",
            "min_price": min(prices),
            "max_price": max(prices),
            "avg_profit_rmb": round(sum(profits) / len(profits), 2),
            "avg_margin_pct": round(sum(margins) / len(margins), 1),
        }
    return item


def recalculate_item_pricing(detail_id: int | str, pricing_id: str | None = None) -> dict[str, Any]:
    """仅重新计算单条草稿的公式定价。"""
    return pipeline.run_draft_pipeline(detail_id, steps=["pricing"], pricing_id=pricing_id)


def start_batch_job(
    detail_ids: list[int | str],
    do_text: bool = True,
    do_image: bool = True,
    *,
    steps: list[str] | None = None,
    style_id: str | None = None,
    pricing_id: str | None = None,
    image_options: dict[str, Any] | None = None,
    per_item_image_options: dict[str, dict[str, Any]] | None = None,
) -> str:
    """后台并发执行批量生成草稿，返回 job_id 供前端轮询进度。"""
    cfg = config.load_config()
    workers = max(1, min(8, int((cfg.get("batch") or {}).get("concurrency") or 3)))
    job_id = uuid.uuid4().hex[:12]
    job = {
        "job_id": job_id,
        "total": len(detail_ids),
        "done": 0,
        "ok": 0,
        "failed": 0,
        "running": True,
        "errors": [],
        "started_at": time.strftime("%H:%M:%S"),
    }
    with _JOBS_LOCK:
        _JOBS[job_id] = job

    per_item_map = per_item_image_options or {}

    def _run():
        with ThreadPoolExecutor(workers) as ex:
            futs = {
                ex.submit(
                    process_one_item,
                    did,
                    do_text,
                    do_image,
                    steps=steps,
                    style_id=style_id,
                    pricing_id=pricing_id,
                    image_options=per_item_map.get(str(did)) or image_options,
                ): did
                for did in detail_ids
            }
            for fut in as_completed(futs):
                did = futs[fut]
                with _JOBS_LOCK:
                    job["done"] += 1
                    try:
                        fut.result()
                        job["ok"] += 1
                    except Exception as e:
                        job["failed"] += 1
                        job["errors"].append(f"{did}: {e}")
        with _JOBS_LOCK:
            job["running"] = False

    threading.Thread(target=_run, daemon=True).start()
    return job_id


def get_job(job_id: str) -> dict[str, Any] | None:
    with _JOBS_LOCK:
        return copy.deepcopy(_JOBS.get(job_id))


# ------------------------------------------------------------------ Sync Back & Publish


def _resolve_upload_url(c: MiaoshouClient, img_obj: dict[str, Any], upload_space: bool) -> tuple[str | None, bool]:
    """返回 (最终可用URL, 是否因仅本地图而跳过)。"""
    pub = img_obj.get("public_url")
    src = img_obj.get("source_url")
    if pub:
        if pub != src and upload_space and pub.startswith("http"):
            up = c.call("product/picture/picture_space/upload_picture_link", {"imgUrl": pub, "scene": "product"})
            return up.get("picturePath") or pub, False
        return pub, False
    return src, True


def _rebuild_sku_key(orig_key: str, color_orig: str, size_orig: str, color_new: str, size_new: str) -> str:
    if not color_orig and not size_orig:
        return orig_key
    new_key = orig_key
    if color_orig and color_new and color_orig != color_new:
        new_key = new_key.replace(f";{color_orig};", f";{color_new};", 1)
    if size_orig and size_new and size_orig != size_new:
        new_key = new_key.replace(f";{size_orig};", f";{size_new};", 1)
    return new_key


def sync_to_miaoshou(detail_ids: list[int | str]) -> dict[str, Any]:
    """将审核后的草稿（标题/描述/主图/SKU名称/SKU图/SKU定价）保存回妙手 Shopee 采集箱。"""
    c = _client()
    cfg = config.load_config()
    upload_space = bool(cfg["image_model"].get("upload_to_miaoshou", True))
    results: list[dict[str, Any]] = []

    for did in detail_ids:
        item = storage.get_item(did)
        if not item:
            results.append({"detail_id": did, "ok": False, "error": "本地草稿不存在"})
            continue
        if item.get("is_local_only"):
            err_msg = "本地手动创建的演示草稿无法直接同步回妙手采集箱（仅支持导出 CSV 或测试翻译/做图/定价）"
            item["error"] = err_msg
            storage.save_item(item)
            results.append({"detail_id": did, "ok": False, "error": err_msg})
            continue
        site = item.get("site") or "PH"
        try:
            fresh = c.call("product/collect_box/shopee/collect_box/get_site_detail_simple_data",
                           {"detailId": int(did), "site": site})
            sd = copy.deepcopy(fresh["siteDetailSimpleData"])
            oss_md5 = fresh["ossMd5"]

            if (item.get("draft_title") or "").strip():
                sd["title"] = item["draft_title"].strip()
            if (item.get("draft_notes") or "").strip():
                sd["notes"] = item["draft_notes"].strip()

            warns: list[str] = []
            local_only_cnt = 0

            # 1) 主图同步
            draft_imgs = item.get("draft_images") or []
            if draft_imgs:
                final_urls: list[str] = []
                for img in draft_imgs:
                    resolved, is_local_only = _resolve_upload_url(c, img, upload_space)
                    if is_local_only:
                        local_only_cnt += 1
                    if resolved:
                        final_urls.append(resolved)
                if final_urls:
                    sd["imgUrls"] = final_urls

            # 2) SKU 规格翻译 + SKU 图片 + SKU 定价同步
            sku_draft = item.get("sku_draft") or {}
            if (sku_draft.get("draft_color_prop") or "").strip():
                sd["colorPropName"] = sku_draft["draft_color_prop"].strip()
            if (sku_draft.get("draft_size_prop") or "").strip():
                sd["sizePropName"] = sku_draft["draft_size_prop"].strip()

            color_rename: dict[str, str] = {}
            synced_color_names: list[tuple[dict[str, Any], str]] = []
            old_cmap = sd.get("colorMap") if isinstance(sd.get("colorMap"), dict) else {}
            if old_cmap and sku_draft.get("colors"):
                new_cmap: dict[str, Any] = {}
                for c_item in sku_draft["colors"]:
                    orig_n = c_item["orig_name"]
                    synced_n = (c_item.get("synced_name") or "").strip()
                    new_n = (c_item.get("draft_name") or orig_n).strip() or orig_n
                    color_rename[orig_n] = new_n
                    remote_c = old_cmap.get(orig_n)
                    if remote_c is None and synced_n:
                        remote_c = old_cmap.get(synced_n)
                    if remote_c is None:
                        remote_c = old_cmap.get(new_n)
                    c_obj = copy.deepcopy(remote_c or {"name": orig_n})
                    c_obj["name"] = new_n
                    d_img = c_item.get("draft_img")
                    if isinstance(d_img, dict) and d_img.get("source_url"):
                        resolved, is_local_only = _resolve_upload_url(c, d_img, upload_space)
                        if is_local_only:
                            local_only_cnt += 1
                        if resolved:
                            c_obj["imgUrl"] = resolved
                            c_obj["imgUrls"] = [resolved]
                    new_cmap[new_n] = c_obj
                    synced_color_names.append((c_item, new_n))
                sd["colorMap"] = new_cmap

            size_rename: dict[str, str] = {}
            synced_size_names: list[tuple[dict[str, Any], str]] = []
            old_smap = sd.get("sizeMap") if isinstance(sd.get("sizeMap"), dict) else {}
            if old_smap and sku_draft.get("sizes"):
                new_smap: dict[str, Any] = {}
                for s_item in sku_draft["sizes"]:
                    orig_n = s_item["orig_name"]
                    synced_n = (s_item.get("synced_name") or "").strip()
                    new_n = (s_item.get("draft_name") or orig_n).strip() or orig_n
                    size_rename[orig_n] = new_n
                    remote_s = old_smap.get(orig_n)
                    if remote_s is None and synced_n:
                        remote_s = old_smap.get(synced_n)
                    if remote_s is None:
                        remote_s = old_smap.get(new_n)
                    s_obj = copy.deepcopy(remote_s or {"name": orig_n})
                    s_obj["name"] = new_n
                    new_smap[new_n] = s_obj
                    synced_size_names.append((s_item, new_n))
                sd["sizeMap"] = new_smap

            old_skumap = sd.get("skuMap") if isinstance(sd.get("skuMap"), dict) else {}
            draft_skus = sku_draft.get("skus") or []
            synced_sku_keys: list[tuple[dict[str, Any], str]] = []
            if old_skumap and draft_skus:
                new_skumap: dict[str, Any] = {}
                sku_lookup: dict[str, dict[str, Any]] = {}
                for s in draft_skus:
                    c_o = s.get("color_orig") or ""
                    s_o = s.get("size_orig") or ""
                    c_n = color_rename.get(c_o, s.get("color_draft") or c_o)
                    s_n = size_rename.get(s_o, s.get("size_draft") or s_o)
                    rebuilt_k = _rebuild_sku_key(s["orig_key"], c_o, s_o, c_n, s_n)
                    sku_lookup[s["orig_key"]] = s
                    if s.get("synced_key"):
                        sku_lookup[s["synced_key"]] = s
                    sku_lookup.setdefault(rebuilt_k, s)
                min_p: float | None = None
                for orig_k, orig_v in old_skumap.items():
                    sk_entry = sku_lookup.get(orig_k)
                    v_copy = copy.deepcopy(orig_v)
                    if sk_entry:
                        c_orig = sk_entry.get("color_orig") or ""
                        s_orig = sk_entry.get("size_orig") or ""
                        c_new = color_rename.get(c_orig, sk_entry.get("color_draft") or c_orig)
                        s_new = size_rename.get(s_orig, sk_entry.get("size_draft") or s_orig)
                        new_k = _rebuild_sku_key(sk_entry["orig_key"], c_orig, s_orig, c_new, s_new)
                        if sk_entry.get("draft_price") is not None:
                            p_val = float(sk_entry["draft_price"])
                            v_copy["price"] = p_val
                            min_p = p_val if min_p is None else min(min_p, p_val)
                        if sk_entry.get("cost_rmb") is not None:
                            v_copy["originPrice"] = float(sk_entry["cost_rmb"])
                        if sk_entry.get("weight_kg") is not None:
                            v_copy["weight"] = float(sk_entry["weight_kg"])
                        if sk_entry.get("stock") is not None:
                            v_copy["stock"] = int(sk_entry["stock"])
                        synced_sku_keys.append((sk_entry, new_k))
                    else:
                        new_k = orig_k
                    new_skumap[new_k] = v_copy
                sd["skuMap"] = new_skumap
                if min_p is not None:
                    sd["price"] = str(min_p)
                if draft_skus[0].get("weight_kg") is not None:
                    sd["weight"] = float(draft_skus[0]["weight_kg"])
                sd["stock"] = str(sum(int(s.get("stock") or 0) for s in draft_skus))
            elif draft_skus:
                if draft_skus[0].get("draft_price") is not None:
                    sd["price"] = str(draft_skus[0]["draft_price"])
                if draft_skus[0].get("cost_rmb") is not None:
                    sd["originPrice"] = str(draft_skus[0]["cost_rmb"])
                if draft_skus[0].get("weight_kg") is not None:
                    sd["weight"] = float(draft_skus[0]["weight_kg"])
                if draft_skus[0].get("stock") is not None:
                    sd["stock"] = str(int(draft_skus[0]["stock"]))

            if local_only_cnt:
                warns.append(f"{local_only_cnt} 张本地做图未配置公网图床URL，已保留原图")

            saved = c.call("product/collect_box/shopee/collect_box/save_site_detail_data", {
                "detailId": int(did),
                "site": site,
                "ossMd5": oss_md5,
                "siteDetailSimpleData": sd,
            })
            for c_item, new_n in synced_color_names:
                c_item["synced_name"] = new_n
            for s_item, new_n in synced_size_names:
                s_item["synced_name"] = new_n
            for sk_entry, new_k in synced_sku_keys:
                sk_entry["synced_key"] = new_k
            item["oss_md5"] = (saved or {}).get("ossMd5") or oss_md5
            item["raw_site_data"] = sd
            item["price"] = sd.get("price") or item.get("price") or ""
            item["status"] = "synced"
            item["error"] = ""
            item["last_sync_warn"] = "；".join(warns)
            storage.save_item(item)
            results.append({"detail_id": did, "ok": True, "warn": item["last_sync_warn"]})
        except Exception as e:
            item["error"] = str(e)
            storage.save_item(item)
            results.append({"detail_id": did, "ok": False, "error": str(e)})
    return {"results": results}


def publish_items(detail_ids: list[int | str], shop_ids: list[int | str]) -> dict[str, Any]:
    """提交妙手发布任务（save_move_collect_task）。"""
    if not shop_ids:
        raise ValueError("请先勾选要发布的目标店铺")
    c = _client()
    dids = [int(x) for x in detail_ids]
    sids = [int(x) for x in shop_ids]
    res = c.call("product/collect_box/shopee/move_collect/save_move_collect_task", {
        "detailIds": dids,
        "shopIds": sids,
    })
    for did in dids:
        item = storage.get_item(did)
        if item:
            item["status"] = "published"
            storage.save_item(item)
    return {"detailIds": dids, "shopIds": sids, "response": res}


def list_publish_records(page_no: int = 1, page_size: int = 20) -> dict[str, Any]:
    c = _client()
    return c.call("product/collect_box/shopee/move_collect/search_move_collect_list",
                  {"pageNo": page_no, "pageSize": page_size}) or {}


# ------------------------------------------------------------------ Diagnostics, Manual Draft & CSV Export


_MIAOSHOU_ERROR_HINTS: dict[str, str] = {
    "appNotFound": "应用不存在或未审核通过，请核对 AppKey 并在妙手开放平台确认应用状态。",
    "signInvalid": "签名校验不通过，请核对 AppSecret（注意区分大小写、不要多带空格）。",
    "signExpired": "时间戳已过期（偏差超过 5 分钟），请同步本机系统时间。",
    "appNoPermission": "应用暂无该接口权限，请在妙手开放平台为该应用勾选对应接口权限。",
    "ipNotInWhitelist": "当前出口 IP 不在妙手账户白名单中；若开启了梯子会导致出口 IP 变化，请关闭白名单或把妙手域名加入直连。",
    "networkError": "连接妙手服务器超时或网络异常；若本机开启了代理/梯子，请将 91miaoshou.com 加入代理直连规则（Bypass/Direct）后重试。",
}


def test_miaoshou_connection(patch: dict[str, Any] | None = None) -> dict[str, Any]:
    """只读测试妙手 ERP 开放平台密钥与网络连通性（支持直接测试表单中尚未保存的值）。"""
    creds = config.resolve_miaoshou_credentials(patch)
    if not creds["app_key"] or not creds["app_secret"]:
        raise ValueError("请先填写妙手 AppKey 和 AppSecret")

    c = MiaoshouClient(
        app_key=creds["app_key"],
        app_secret=creds["app_secret"],
        base_url=creds["base_url"],
        sub_account_id=creds["sub_account_id"] or None,
        timeout=8,
        max_retries=0,
    )
    t0 = time.time()
    resp = c.call_raw(
        "resell_account/fetch/search_reseller_account_page",
        {"page": 1, "pageSize": 5},
    )
    dt_ms = int((time.time() - t0) * 1000)
    if resp.get("result") == "success":
        return {
            "ok": True,
            "elapsed_ms": dt_ms,
            "base_url": creds["base_url"],
            "message": f"妙手 ERP 接口连接成功（{dt_ms}ms），密钥与签名有效！",
        }
    code = str(resp.get("code") or "unknown")
    raw_msg = str(resp.get("message") or resp.get("reason") or "")
    hint = _MIAOSHOU_ERROR_HINTS.get(code, "")
    return {
        "ok": False,
        "elapsed_ms": dt_ms,
        "code": code,
        "message": f"[{code}] {raw_msg}",
        "hint": hint,
    }


def create_manual_draft(payload: dict[str, Any]) -> dict[str, Any]:
    """在本地新建一条商品草稿（不依赖妙手采集接口，离线/梯子环境下可直接测试翻译、做图与定价）。"""
    title = str(payload.get("title") or "").strip()
    if not title:
        raise ValueError("请输入商品标题")
    site = str(payload.get("site") or "PH").strip().upper() or "PH"
    notes = str(payload.get("notes") or "").strip()
    cost_rmb = max(0.0, float(payload.get("cost_rmb") if payload.get("cost_rmb") not in (None, "") else 18.0))
    weight_kg = max(0.0, float(payload.get("weight_kg") if payload.get("weight_kg") not in (None, "") else 0.15))
    stock = max(0, int(float(payload.get("stock") if payload.get("stock") not in (None, "") else 100)))
    orig_price = max(0.0, float(payload.get("price") if payload.get("price") not in (None, "") else 0.0))

    raw_imgs = payload.get("images") or []
    if isinstance(raw_imgs, str):
        img_urls = [ln.strip() for ln in raw_imgs.splitlines() if ln.strip().startswith(("http://", "https://"))]
    elif isinstance(raw_imgs, list):
        img_urls = [str(u).strip() for u in raw_imgs if str(u).strip().startswith(("http://", "https://"))]
    else:
        img_urls = []

    raw_colors = payload.get("colors") or []
    if isinstance(raw_colors, str):
        colors = [x.strip() for x in raw_colors.replace("，", ",").split(",") if x.strip()]
    elif isinstance(raw_colors, list):
        colors = [str(x).strip() for x in raw_colors if str(x).strip()]
    else:
        colors = []

    raw_sizes = payload.get("sizes") or []
    if isinstance(raw_sizes, str):
        sizes = [x.strip() for x in raw_sizes.replace("，", ",").split(",") if x.strip()]
    elif isinstance(raw_sizes, list):
        sizes = [str(x).strip() for x in raw_sizes if str(x).strip()]
    else:
        sizes = []

    # 构造标准 siteDetailSimpleData 结构，确保与采集拉取的商品数据结构完全一致
    color_map = {
        c: {"name": c, "imgUrl": img_urls[i % len(img_urls)] if img_urls else "", "imgUrls": [img_urls[i % len(img_urls)]] if img_urls else []}
        for i, c in enumerate(colors)
    }
    size_map = {s: {"name": s} for s in sizes}
    sku_map: dict[str, Any] = {}
    if colors and sizes:
        for ci, c in enumerate(colors):
            for si, s in enumerate(sizes):
                sku_map[f";{c};{s};"] = {
                    "itemNum": f"LOCAL-C{ci + 1}S{si + 1}",
                    "price": orig_price,
                    "originPrice": cost_rmb,
                    "stock": stock,
                    "weight": weight_kg,
                }
    elif colors:
        for ci, c in enumerate(colors):
            sku_map[f";{c};;"] = {
                "itemNum": f"LOCAL-C{ci + 1}",
                "price": orig_price,
                "originPrice": cost_rmb,
                "stock": stock,
                "weight": weight_kg,
            }
    elif sizes:
        for si, s in enumerate(sizes):
            sku_map[f";;{s};"] = {
                "itemNum": f"LOCAL-S{si + 1}",
                "price": orig_price,
                "originPrice": cost_rmb,
                "stock": stock,
                "weight": weight_kg,
            }

    raw_sd: dict[str, Any] = {
        "title": title,
        "notes": notes,
        "price": str(orig_price or ""),
        "originPrice": cost_rmb,
        "weight": weight_kg,
        "stock": str(stock * max(1, len(sku_map))),
        "imgUrls": img_urls,
        "colorPropName": "颜色" if colors else "",
        "sizePropName": "尺寸" if sizes else "",
        "colorMap": color_map,
        "sizeMap": size_map,
        "skuMap": sku_map,
    }

    did = 9000000000 + int(time.time() * 1000) % 900000000
    while storage.get_item(did) is not None:
        did += 1

    sku_draft = storage.extract_sku_draft(raw_sd, fallback_price=raw_sd["price"], fallback_stock=raw_sd["stock"])
    item = {
        "detail_id": did,
        "site": site,
        "list_status": "localManual",
        "is_local_only": True,
        "price": raw_sd["price"] or "-",
        "stock": raw_sd["stock"],
        "cid": None,
        "gmt_create": time.strftime("%Y-%m-%d %H:%M:%S"),
        "oss_md5": "",
        "orig_title": title,
        "orig_notes": notes,
        "orig_images": img_urls,
        "raw_site_data": raw_sd,
        "sku_draft": sku_draft,
        "style_id": "",
        "pricing_id": "",
        "pricing_summary": {},
        "draft_title": "",
        "draft_notes": "",
        "draft_images": [],
        "status": "pending",
        "error": "",
        "last_sync_warn": "",
    }
    return storage.save_item(item)


def export_drafts_csv(detail_ids: list[int] | None = None) -> bytes:
    """将本地草稿（指定 ID 或全部）导出为 Excel 可直接打开的 UTF-8-SIG CSV。"""
    all_items = storage.list_items()
    if detail_ids:
        wanted = {int(x) for x in detail_ids}
        items = [x for x in all_items if int(x["detail_id"]) in wanted]
    else:
        items = all_items

    buf = io.StringIO()
    cols = [
        "商品ID", "站点", "状态", "采集原标题", "上架草稿标题", "草稿描述",
        "SKU数量", "参考进货价(RMB)", "参考重量(kg)", "总库存",
        "建议售价币种", "最低建议售价", "最高建议售价", "平均预估利润(RMB)", "平均利润率(%)",
        "原图数量", "草稿主图数量", "草稿主图链接", "更新时间",
    ]
    writer = csv.DictWriter(buf, fieldnames=cols)
    writer.writeheader()
    for it in items:
        skus = (it.get("sku_draft") or {}).get("skus") or []
        first_sku = skus[0] if skus else {}
        ps = it.get("pricing_summary") or {}
        d_imgs = it.get("draft_images") or []
        img_links = " | ".join(
            (im.get("public_url") or im.get("preview_url") or "")
            for im in d_imgs
            if isinstance(im, dict)
        )
        writer.writerow({
            "商品ID": it.get("detail_id", ""),
            "站点": it.get("site", ""),
            "状态": it.get("status", ""),
            "采集原标题": it.get("orig_title", ""),
            "上架草稿标题": it.get("draft_title", ""),
            "草稿描述": it.get("draft_notes", ""),
            "SKU数量": len(skus),
            "参考进货价(RMB)": first_sku.get("cost_rmb", ""),
            "参考重量(kg)": first_sku.get("weight_kg", ""),
            "总库存": it.get("stock", ""),
            "建议售价币种": ps.get("currency", ""),
            "最低建议售价": ps.get("min_price", ""),
            "最高建议售价": ps.get("max_price", ""),
            "平均预估利润(RMB)": ps.get("avg_profit_rmb", ""),
            "平均利润率(%)": ps.get("avg_margin_pct", ""),
            "原图数量": len(it.get("orig_images") or []),
            "草稿主图数量": len(d_imgs),
            "草稿主图链接": img_links,
            "更新时间": it.get("updated_at", ""),
        })
    return buf.getvalue().encode("utf-8-sig")
