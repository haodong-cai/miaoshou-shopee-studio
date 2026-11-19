"""铺货草稿工作台测试：python tests/test_studio.py"""
import base64
import io
import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from studio import config, models, pipeline, presets, pricing, service, storage
from studio.server import app


def _make_png_bytes(color=(100, 150, 200)) -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", (300, 200), color).save(buf, format="PNG")
    return buf.getvalue()


def test_config_mask_and_preserve():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "studio_config.json"
        with patch.object(config, "CONFIG_PATH", p):
            config.save_config({"text_model": {"api_key": "sk-secret-12345678", "model": "deepseek-chat"}})
            pub = config.load_public_config()
            assert pub["text_model"]["api_key"] == "sk-s****5678"
            config.save_config({"text_model": {"api_key": "sk-s****5678", "model": "gpt-4o-mini"}})
            real = config.load_config()
            assert real["text_model"]["api_key"] == "sk-secret-12345678"
            assert real["text_model"]["model"] == "gpt-4o-mini"


def test_text_model_extract_and_mock_call():
    raw = '```json\n{"title": "Kids EVA Clogs Beach Sandals Lightweight Non-Slip", "notes": "- Soft EVA\\n- Non-slip sole"}\n```'
    parsed = models._extract_json_payload(raw)
    assert parsed["title"].startswith("Kids EVA")
    assert "Non-slip" in parsed["notes"]

    class FakeResp:
        status_code = 200

        def json(self):
            return {"choices": [{"message": {"content": '{"title": "A B C D E", "notes": "Detail"}'}}]}

    with patch("studio.models.requests.post", return_value=FakeResp()):
        out = models.generate_text_draft("原标题", "原描述", {
            "base_url": "https://api.example.com/v1",
            "api_key": "sk-test",
            "model": "demo",
            "target_language": "English",
            "title_max_len": 7,
            "prompt_template": "to {target_language} <= {title_max_len}",
        })
        assert len(out["title"]) <= 7
        assert out["notes"] == "Detail"


def test_pricing_engine_and_safe_ast():
    ph = pricing.get_pricing_preset("shopee_ph")
    res = pricing.calculate_price(cost_rmb=18.0, weight_kg=0.1, cfg=ph)
    # 菲律宾 SLS 官方默认表: <=50g 23 PHP, >50g 每10g +4.5 PHP => 100g=45.5 PHP
    assert res["shipping_local"] == 45.5
    assert res["shipping_rmb"] == round(45.5 / ph["exchange_rate"], 2)
    assert res["fixed_order_rmb"] > 0
    assert res["final_price"] >= 340
    assert res["profit_rmb"] > 0

    # 验证打包补重 weight_buffer_g (100g 采集重 + 50g 包材缓冲 = 150g => 23 + 10*4.5 = 68.0 PHP)
    ph_buf = {**ph, "weight_buffer_g": 50}
    res_buf = pricing.calculate_price(cost_rmb=18.0, weight_kg=0.1, cfg=ph_buf)
    assert res_buf["effective_weight_kg"] == 0.15
    assert res_buf["shipping_local"] == 68.0

    # 验证官方表 200g T恤示例：SG=3.66, MY=3.0, TH=20, PH=90.5, VN=18000, TW=25, BR=23.8
    expected_200g = {
        "shopee_sg": 3.66,
        "shopee_my": 3.0,
        "shopee_th": 20.0,
        "shopee_ph": 90.5,
        "shopee_vn": 18000.0,
        "shopee_tw": 25.0,
        "shopee_br": 23.8,
    }
    for pid, exp_local in expected_200g.items():
        s = pricing.calc_shipping_detail(0.2, pricing.get_pricing_preset(pid))
        assert s["shipping_local"] == exp_local, (pid, s, exp_local)

    # 验证台湾分段阶梯：500g=25, 1000g=55, 1500g=95, 2500g=185, 2600g=245
    tw = pricing.get_pricing_preset("shopee_tw")
    assert pricing.calc_shipping_detail(0.5, tw)["shipping_local"] == 25.0
    assert pricing.calc_shipping_detail(1.0, tw)["shipping_local"] == 55.0
    assert pricing.calc_shipping_detail(1.5, tw)["shipping_local"] == 95.0
    assert pricing.calc_shipping_detail(2.5, tw)["shipping_local"] == 185.0
    assert pricing.calc_shipping_detail(2.6, tw)["shipping_local"] == 245.0

    # 验证人民币线性模式向后兼容
    rmb_cfg = {"exchange_rate": 9.57, "shipping_currency": "rmb", "first_weight_g": 50, "first_shipping_rmb": 4.5, "step_weight_g": 50, "step_shipping_rmb": 2.2}
    assert pricing.calc_shipping_rmb(0.1, rmb_cfg) == 6.7

    my = pricing.get_pricing_preset("shopee_my")
    res_my = pricing.calculate_price(cost_rmb=18.0, weight_kg=0.1, cfg=my)
    assert my["commission_rate"] == 0.1836
    assert my["tech_fee_rate"] == 0.05
    assert res_my["fixed_order_rmb"] > 0
    assert res_my["profit_rmb"] > 0

    custom_cfg = {
        **ph,
        "mode": "custom",
        "custom_formula": "(cost + shipping) * 1.5 * rate",
        "rounding": "dot99",
    }
    res_c = pricing.calculate_price(cost_rmb=10.0, weight_kg=0.05, cfg=custom_cfg)
    assert str(res_c["final_price"]).endswith(".99")

    # 拒绝恶意表达式
    try:
        pricing.eval_formula("__import__('os').system('echo 1')", {"cost": 10})
        assert False, "should reject unsafe AST"
    except ValueError:
        pass

    class FakeFxResp:
        def raise_for_status(self): pass
        def json(self):
            return {"result": "success", "base_code": "CNY", "time_last_update_utc": "now", "rates": {"PHP": 9.65}}

    with patch("studio.pricing.requests.get", return_value=FakeFxResp()):
        fx = pricing.fetch_live_fx_rates("CNY")
        assert fx["rates"]["PHP"] == 9.65


def test_url_validation():
    assert service.validate_collect_url("https://detail.1688.com/offer/123456.html").startswith("https://")
    for bad in ("", "not-a-url", "http://localhost:8000/a", "https://detail.1688.com/"):
        try:
            service.validate_collect_url(bad)
            assert False, f"should reject {bad}"
        except ValueError:
            pass


def test_full_pipeline_and_sync_mapping():
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        cfg_p = td_path / "cfg.json"
        items_d = td_path / "items"
        imgs_d = td_path / "images"
        with patch.object(config, "CONFIG_PATH", cfg_p), \
             patch.object(storage, "ITEMS_DIR", items_d), \
             patch.object(storage, "IMAGES_DIR", imgs_d), \
             patch.object(models, "IMAGES_DIR", imgs_d):

            config.save_config({
                "text_model": {"provider": "local_dict", "enabled": True},
                "image_model": {"mode": "local_pillow", "process_count": 1, "sku_enabled": True},
            })

            raw_sd = {
                "cid": 101060,
                "title": "韩系儿童露趾防滑凉鞋",
                "price": "171.48",
                "stock": "100",
                "weight": 0.1,
                "notes": "轻便EVA防滑软底",
                "imgUrls": ["https://example.com/main1.png", "https://example.com/main2.png"],
                "colorPropName": "颜色",
                "sizePropName": "尺寸",
                "colorMap": {
                    "黑白色": {"name": "黑白色", "imgUrl": "https://example.com/bw.png", "imgUrls": ["https://example.com/bw.png"]},
                    "蓝白色": {"name": "蓝白色", "imgUrl": "https://example.com/blw.png", "imgUrls": ["https://example.com/blw.png"]},
                },
                "sizeMap": {
                    "C6（脚长13.5cm）": {"name": "C6（脚长13.5cm）"},
                },
                "skuMap": {
                    ";黑白色;C6（脚长13.5cm）;": {"itemNum": "SKU1", "price": 171.48, "originPrice": 18, "stock": 50, "weight": 0.1},
                    ";蓝白色;C6（脚长13.5cm）;": {"itemNum": "SKU2", "price": 171.48, "originPrice": 20, "stock": 50, "weight": 0.15},
                },
            }

            storage.save_item({
                "detail_id": 8888,
                "site": "PH",
                "price": "171.48",
                "stock": "100",
                "orig_title": raw_sd["title"],
                "orig_notes": raw_sd["notes"],
                "orig_images": raw_sd["imgUrls"],
                "raw_site_data": raw_sd,
                "draft_title": "",
                "draft_notes": "",
                "draft_images": [],
                "status": "pending",
            })

            png_b = _make_png_bytes((120, 180, 240))
            with patch("studio.models._download_bytes", return_value=png_b):
                out = pipeline.run_draft_pipeline(8888, style_id="jp_kr_fresh", pricing_id="shopee_ph")

            assert out["status"] == "drafted"
            assert out["style_id"] == "jp_kr_fresh"
            assert out["pricing_id"] == "shopee_ph"
            assert "Kids" in out["draft_title"] or "Sandals" in out["draft_title"]
            assert len(out["draft_images"]) == 2
            assert out["draft_images"][0]["preview_url"].startswith("/draft-images/")
            assert out["sku_draft"]["draft_color_prop"] == "Color"
            assert out["sku_draft"]["colors"][0]["draft_name"] == "Black & White"
            assert out["sku_draft"]["colors"][0]["draft_img"]["preview_url"].startswith("/draft-images/")
            assert out["sku_draft"]["skus"][0]["draft_price"] > 300
            assert out["sku_draft"]["skus"][1]["draft_price"] > out["sku_draft"]["skus"][0]["draft_price"]

            # 验证同步回妙手时 colorMap / sizeMap / skuMap key 和价格正确重建
            captured = {}

            class FakeClient:
                def call(self, path, body=None):
                    if "get_site_detail_simple_data" in path:
                        return {"ossMd5": "md5_1", "siteDetailSimpleData": raw_sd}
                    if "save_site_detail_data" in path:
                        captured["saved"] = body
                        return {"ossMd5": "md5_2"}
                    return {}

            with patch("studio.service._client", return_value=FakeClient()):
                sync_res = service.sync_to_miaoshou([8888])
            assert sync_res["results"][0]["ok"] is True
            saved_sd = captured["saved"]["siteDetailSimpleData"]
            assert saved_sd["colorPropName"] == "Color"
            assert "Black & White" in saved_sd["colorMap"]
            assert any(k.startswith(";Black & White;") for k in saved_sd["skuMap"])
            assert float(saved_sd["price"]) == out["pricing_summary"]["min_price"]


def test_image_pillow_and_fastapi_endpoints():
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        cfg_p = td_path / "cfg.json"
        items_d = td_path / "items"
        imgs_d = td_path / "images"
        with patch.object(config, "CONFIG_PATH", cfg_p), \
             patch.object(storage, "ITEMS_DIR", items_d), \
             patch.object(storage, "IMAGES_DIR", imgs_d), \
             patch.object(models, "IMAGES_DIR", imgs_d):

            client = TestClient(app)
            r = client.get("/")
            assert r.status_code == 200
            assert "妙手铺货上架工作台" in r.text

            pr_resp = client.get("/api/presets")
            assert pr_resp.status_code == 200
            assert "shopee_clean" in pr_resp.json()["style_presets"]
            assert "shopee_ph" in pr_resp.json()["pricing_presets"]

            pv_resp = client.post("/api/pricing/preview", json={"cost_rmb": 18, "weight_kg": 0.1, "pricing_id": "shopee_ph"})
            assert pv_resp.status_code == 200
            assert pv_resp.json()["currency"] == "PHP"

            r = client.post("/api/test/image", json={"mode": "local_pillow", "pillow_badge": "NEW", "pillow_size": 500})
            assert r.status_code == 200
            prev = r.json()["preview_url"]
            assert prev.startswith("/draft-images/")
            img_resp = client.get(prev)
            assert img_resp.status_code == 200
            im = Image.open(io.BytesIO(img_resp.content))
            assert im.size == (500, 500)

            storage.save_item({
                "detail_id": 999,
                "site": "PH",
                "orig_title": "测试标题",
                "orig_notes": "测试描述",
                "orig_images": ["https://example.com/a.png"],
                "draft_title": "",
                "draft_notes": "",
                "draft_images": [],
                "status": "pending",
            })
            lst = client.get("/api/drafts").json()["items"]
            assert len(lst) == 1 and lst[0]["detail_id"] == 999

            upd = client.patch("/api/drafts/999", json={"draft_title": "Test Title EN"}).json()
            assert upd["draft_title"] == "Test Title EN"
            assert upd["status"] == "drafted"

            # 测试批量修改进货价、重量、库存、标题与自动重算公式定价
            storage.save_item({
                "detail_id": 1001,
                "site": "PH",
                "orig_title": "测试鞋",
                "orig_notes": "",
                "orig_images": [],
                "raw_site_data": {
                    "colorMap": {"黑": {"name": "黑"}, "白": {"name": "白"}},
                    "sizeMap": {"38": {"name": "38"}, "39": {"name": "39"}},
                    "skuMap": {
                        ";黑;38;": {"price": 100, "originPrice": 18, "weight": 0.1, "stock": 10},
                        ";黑;39;": {"price": 100, "originPrice": 18, "weight": 0.1, "stock": 10},
                        ";白;38;": {"price": 100, "originPrice": 18, "weight": 0.1, "stock": 10},
                    },
                },
                "status": "pending",
            })
            # 1) 仅改黑色进货价为 25、重量为 0.2，应自动重算价格
            be1 = client.post("/api/drafts/batch-edit", json={
                "detail_ids": [1001],
                "ops": {
                    "color_filter": "黑",
                    "cost_rmb": {"op": "set", "value": 25},
                    "weight_kg": {"op": "set", "value": 0.2},
                    "stock": {"op": "set", "value": 88},
                },
                "auto_reprice": True,
                "pricing_id": "shopee_ph",
            })
            assert be1.status_code == 200
            skus_after = be1.json()["items"][0]["sku_draft"]["skus"]
            black_skus = [s for s in skus_after if s["color_orig"] == "黑"]
            white_skus = [s for s in skus_after if s["color_orig"] == "白"]
            assert all(s["cost_rmb"] == 25 and s["weight_kg"] == 0.2 and s["stock"] == 88 for s in black_skus)
            assert white_skus[0]["cost_rmb"] == 18 and white_skus[0]["stock"] == 10
            assert black_skus[0]["draft_price"] > white_skus[0]["draft_price"]

            # 2) 跨商品批量加标题前后缀 + 统一加价
            be2 = client.post("/api/drafts/batch-edit", json={
                "detail_ids": [999, 1001],
                "ops": {
                    "title_prefix": "[NEW] ",
                    "draft_price": {"op": "add", "value": 10},
                },
                "auto_reprice": False,
                "pricing_id": "shopee_ph",
            })
            assert be2.status_code == 200
            assert be2.json()["updated"] == 2
            by_id = {x["detail_id"]: x for x in be2.json()["items"]}
            assert by_id[999]["draft_title"].startswith("[NEW] ")
            assert by_id[1001]["sku_draft"]["skus"][0]["draft_price"] > black_skus[0]["draft_price"] - 0.1

            png_b = _make_png_bytes((10, 20, 30))

            class FakeImgResp:
                status_code = 200
                headers = {"Content-Type": "application/json"}

                def json(self):
                    return {"image_base64": base64.b64encode(png_b).decode()}

            with patch("studio.models._download_bytes", return_value=png_b), \
                 patch("studio.models.requests.post", return_value=FakeImgResp()):
                res_im = models.process_single_image("https://example.com/1.png", 999, 0, {
                    "mode": "custom_http",
                    "base_url": "https://img.example.com/edit",
                    "api_key": "k",
                    "prompt": "white bg",
                })
                assert res_im["mode"] == "custom_http"
                assert res_im["preview_url"].startswith("/draft-images/")


def test_selective_multi_image_generation_and_options():
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        cfg_p = td_path / "cfg.json"
        items_d = td_path / "items"
        imgs_d = td_path / "images"
        with patch.object(config, "CONFIG_PATH", cfg_p), \
             patch.object(storage, "ITEMS_DIR", items_d), \
             patch.object(storage, "IMAGES_DIR", imgs_d), \
             patch.object(models, "IMAGES_DIR", imgs_d):

            # 1) 验证提示词拼接包含翻译、白底、去中文、精修、场景与变体提示
            prompt_txt = models.build_image_edit_prompt(
                "Base prompt",
                "Style prompt",
                options={
                    "translate": True,
                    "white_bg": True,
                    "clean_text": True,
                    "enhance": True,
                    "scene": False,
                    "multi_angle": True,
                    "extra_prompt": "Keep logo sharp",
                },
                target_language="English (Shopee Philippines)",
                variant_index=1,
                variant_total=4,
            )
            assert "Pure solid white background" in prompt_txt
            assert "Translate any visible text" in prompt_txt
            assert "English (Shopee Philippines)" in prompt_txt
            assert "Remove all Chinese characters" in prompt_txt
            assert "Variation 2/4" in prompt_txt
            assert "Keep logo sharp" in prompt_txt

            # 2) 准备含 5 张原图的商品
            storage.save_item({
                "detail_id": 2026,
                "site": "PH",
                "orig_title": "测试多图商品",
                "orig_notes": "",
                "orig_images": [
                    "https://example.com/img0.jpg",
                    "https://example.com/img1.jpg",
                    "https://example.com/img2.jpg",
                    "https://example.com/img3.jpg",
                    "https://example.com/img4.jpg",
                ],
                "draft_title": "",
                "draft_notes": "",
                "draft_images": [],
                "status": "pending",
            })

            # 生成 JPEG 字节流测试自动转 PNG 上传 & custom_http / openai_edit / openai_chat_img
            jpg_buf = io.BytesIO()
            Image.new("RGB", (120, 120), (180, 90, 50)).save(jpg_buf, format="JPEG")
            jpg_bytes = jpg_buf.getvalue()
            out_png = _make_png_bytes((255, 255, 255))

            # 2a) custom_http：只勾选第2张和第4张原图 ([1, 3])，要求生成 4 张主图
            captured_payloads = []

            class FakeCustomResp:
                status_code = 200
                headers = {"Content-Type": "application/json"}

                def json(self):
                    return {"image_base64": base64.b64encode(out_png).decode()}

            def fake_post(url, **kwargs):
                if "json" in kwargs and isinstance(kwargs["json"], dict):
                    captured_payloads.append(kwargs["json"])
                return FakeCustomResp()

            config.save_config({
                "image_model": {
                    "mode": "custom_http",
                    "base_url": "https://img.example.com/edit",
                    "api_key": "k-img",
                }
            })

            client = TestClient(app)
            with patch("studio.models._download_bytes", return_value=jpg_bytes), \
                 patch("studio.models.requests.post", side_effect=fake_post):
                r4 = client.post("/api/drafts/2026/generate-images", json={
                    "style_id": "shopee_clean",
                    "count": 4,
                    "selected_indices": [1, 3],
                    "options": {"translate": True, "white_bg": True},
                })
            assert r4.status_code == 200, r4.text
            d4 = r4.json()
            assert len(d4["draft_images"]) == 4
            assert [im["source_url"] for im in d4["draft_images"]] == [
                "https://example.com/img1.jpg",
                "https://example.com/img3.jpg",
                "https://example.com/img1.jpg",
                "https://example.com/img3.jpg",
            ]
            assert d4["image_edit_plan"]["count"] == 4
            assert d4["image_edit_plan"]["selected_indices"] == [1, 3]
            assert len(captured_payloads) == 4
            assert captured_payloads[0]["options"]["translate"] is True
            assert captured_payloads[0]["options"]["white_bg"] is True
            assert "Variation 1/4" in captured_payloads[0]["prompt"]

            # 2b) 单独重做第 2 槽位 (slot_index=1)，其余 3 张保留不变
            old_files = [im["local_file"] for im in d4["draft_images"]]
            with patch("studio.models._download_bytes", return_value=jpg_bytes), \
                 patch("studio.models.requests.post", side_effect=fake_post):
                r_slot = client.post("/api/drafts/2026/generate-images", json={
                    "style_id": "shopee_clean",
                    "slot_index": 1,
                    "options": {"white_bg": True, "enhance": True},
                })
            assert r_slot.status_code == 200
            d_slot = r_slot.json()
            assert len(d_slot["draft_images"]) == 4
            assert d_slot["draft_images"][0]["local_file"] == old_files[0]
            assert d_slot["draft_images"][1]["local_file"] != old_files[1]
            assert d_slot["draft_images"][2]["local_file"] == old_files[2]

            # 2c) 生成 3 张与 5 张，以及 local_pillow 强制白底
            config.save_config({"image_model": {"mode": "local_pillow"}})
            with patch("studio.models._download_bytes", return_value=jpg_bytes):
                r5 = client.post("/api/drafts/2026/generate-images", json={
                    "style_id": "jp_kr_fresh",  # 本身是暖杏奶油背景，选白底后角落应为纯白
                    "count": 5,
                    "selected_indices": [0, 2, 4],
                    "options": {"white_bg": True, "enhance": True},
                })
            assert r5.status_code == 200
            d5 = r5.json()
            assert len(d5["draft_images"]) == 5
            first_img_path = imgs_d / d5["draft_images"][0]["local_file"]
            im_check = Image.open(first_img_path)
            # 边框内侧背景像素应为纯白 (255,255,255)（避开左上角角标区域）
            assert im_check.getpixel((10, 400)) == (255, 255, 255)

            # 2d) 测试 openai_edit 发送有效 PNG 且 openai_chat_img 可解析 chat 图片响应
            seen_files = []

            class FakeOpenAIEditResp:
                status_code = 200
                headers = {"Content-Type": "application/json"}

                def json(self):
                    return {"data": [{"b64_json": base64.b64encode(out_png).decode()}]}

            def fake_oa_edit(url, **kwargs):
                seen_files.append(kwargs.get("files"))
                return FakeOpenAIEditResp()

            with patch("studio.models._download_bytes", return_value=jpg_bytes), \
                 patch("studio.models.requests.post", side_effect=fake_oa_edit):
                res_oa = models.process_single_image(
                    "https://example.com/x.jpg", 2026, 0,
                    {"mode": "openai_edit", "base_url": "https://api.openai.com/v1", "api_key": "sk-test"},
                    options={"white_bg": True},
                )
            assert res_oa["mode"] == "openai_edit"
            uploaded_bytes = seen_files[0]["image"][1]
            assert uploaded_bytes[:8] == b"\x89PNG\r\n\x1a\n"

            class FakeChatImgResp:
                status_code = 200
                headers = {"Content-Type": "application/json"}

                def json(self):
                    b64 = base64.b64encode(out_png).decode()
                    return {
                        "choices": [{
                            "message": {
                                "images": [{"image_url": {"url": f"data:image/png;base64,{b64}"}}]
                            }
                        }]
                    }

            with patch("studio.models._download_bytes", return_value=jpg_bytes), \
                 patch("studio.models.requests.post", return_value=FakeChatImgResp()):
                res_chat = models.process_single_image(
                    "https://example.com/x.jpg", 2026, 0,
                    {"mode": "openai_chat_img", "base_url": "https://api.example.com/v1", "api_key": "sk-test"},
                    options={"translate": True},
                )
            assert res_chat["mode"] == "openai_chat_img"
            assert res_chat["preview_url"].startswith("/draft-images/")


def test_bugfix_regressions():
    """回归测试：二次同步、手动改价利润重算、批量改价完整费率、0 成本试算、500 捕获、选图计划保留、自定义公式税率与前端协议字段。"""
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        cfg_p = td_path / "cfg.json"
        items_d = td_path / "items"
        imgs_d = td_path / "images"
        with patch.object(config, "CONFIG_PATH", cfg_p), \
             patch.object(storage, "ITEMS_DIR", items_d), \
             patch.object(storage, "IMAGES_DIR", imgs_d), \
             patch.object(models, "IMAGES_DIR", imgs_d):

            client = TestClient(app, raise_server_exceptions=False)

            # 1) 所有站点默认 custom_formula 均包含 tax_rate
            for pid, pcfg in pricing.list_pricing_presets().items():
                assert "tax_rate" in (pcfg.get("custom_formula") or ""), pid

            # 2) /api/pricing/preview 传入 cost_rmb=0 不回退为 18.0
            r_zero = client.post("/api/pricing/preview", json={"cost_rmb": 0, "weight_kg": 0.1, "pricing_id": "shopee_ph"})
            assert r_zero.status_code == 200
            assert r_zero.json()["cost_rmb"] == 0.0

            # 3) 单条 SKU 手动改 draft_price 时自动重算 profit_rmb / margin_pct 与 pricing_summary
            raw_sd = {
                "cid": 101060,
                "title": "测试儿童防滑凉鞋",
                "price": "180",
                "stock": "100",
                "weight": 0.15,
                "notes": "轻便软底",
                "imgUrls": ["https://example.com/1.png", "https://example.com/2.png"],
                "colorPropName": "颜色",
                "sizePropName": "尺寸",
                "colorMap": {
                    "黑色": {"name": "黑色", "imgUrl": "https://example.com/black.png", "imgUrls": ["https://example.com/black.png"]},
                    "白色": {"name": "白色", "imgUrl": "https://example.com/white.png", "imgUrls": ["https://example.com/white.png"]},
                },
                "sizeMap": {"38": {"name": "38"}},
                "skuMap": {
                    ";黑色;38;": {"itemNum": "B38", "price": 180, "originPrice": 20, "stock": 50, "weight": 0.15},
                    ";白色;38;": {"itemNum": "W38", "price": 180, "originPrice": 22, "stock": 50, "weight": 0.18},
                },
            }
            storage.save_item({
                "detail_id": 6001,
                "site": "MY",
                "price": "180",
                "stock": "100",
                "orig_title": raw_sd["title"],
                "orig_notes": raw_sd["notes"],
                "orig_images": raw_sd["imgUrls"],
                "raw_site_data": raw_sd,
                "draft_title": "",
                "draft_notes": "",
                "draft_images": [],
                "status": "pending",
            })
            before = client.post("/api/drafts/6001/reprice", json={"pricing_id": "shopee_my"}).json()
            old_prof = before["sku_draft"]["skus"][0]["profit_rmb"]
            patched = client.patch("/api/drafts/6001", json={
                "sku_patch": {"sku_row": {"orig_key": ";黑色;38;", "draft_price": 120.0}},
                "auto_reprice": False,
                "pricing_id": "shopee_my",
            }).json()
            assert patched["sku_draft"]["skus"][0]["profit_rmb"] > old_prof
            assert patched["pricing_summary"]["max_price"] == 120.0

            # 4) batch_edit_drafts 同时改重量与售价时按完整站点费率(含 tech_fee / fixed_order_fee)和新重量重算
            be = client.post("/api/drafts/batch-edit", json={
                "detail_ids": [6001],
                "ops": {
                    "weight_kg": {"op": "set", "value": 0.5},
                    "draft_price": {"op": "set", "value": 100.0},
                },
                "auto_reprice": False,
                "pricing_id": "shopee_my",
            }).json()
            my_cfg = pricing.get_pricing_preset("shopee_my")
            ev_ref = pricing.evaluate_manual_price(100.0, 20.0, 0.5, my_cfg)
            be_sku0 = be["items"][0]["sku_draft"]["skus"][0]
            assert be_sku0["shipping_rmb"] == ev_ref["shipping_rmb"]
            assert be_sku0["profit_rmb"] == ev_ref["profit_rmb"]

            # 5) 连续多次同步到妙手（含首次中->英改名、二次改价/库存、三次再次改名）均保留图片并正确写入
            config.save_config({
                "text_model": {"provider": "local_dict", "enabled": True},
                "image_model": {"mode": "local_pillow", "process_count": 1, "sku_enabled": True},
            })
            png_b = _make_png_bytes((90, 120, 150))
            with patch("studio.models._download_bytes", return_value=png_b):
                pipeline.run_draft_pipeline(6001, style_id="shopee_clean", pricing_id="shopee_my")

            import copy
            remote_state = {"sd": copy.deepcopy(raw_sd), "md5": "m1"}

            class StatefulFakeClient:
                def call(self, path, body=None):
                    if "get_site_detail_simple_data" in path:
                        return {"ossMd5": remote_state["md5"], "siteDetailSimpleData": copy.deepcopy(remote_state["sd"])}
                    if "save_site_detail_data" in path:
                        remote_state["sd"] = copy.deepcopy(body["siteDetailSimpleData"])
                        remote_state["md5"] = "m2"
                        return {"ossMd5": "m2"}
                    return {}

            with patch("studio.service._client", return_value=StatefulFakeClient()):
                assert service.sync_to_miaoshou([6001])["results"][0]["ok"] is True
                assert remote_state["sd"]["colorMap"]["Black"]["imgUrl"] == "https://example.com/black.png"

                # 二次同步：改售价和库存
                client.post("/api/drafts/batch-edit", json={
                    "detail_ids": [6001],
                    "ops": {"draft_price": {"op": "set", "value": 99.9}, "stock": {"op": "set", "value": 77}},
                    "auto_reprice": False,
                    "pricing_id": "shopee_my",
                })
                assert service.sync_to_miaoshou([6001])["results"][0]["ok"] is True
                assert remote_state["sd"]["colorMap"]["Black"]["imgUrl"] == "https://example.com/black.png"
                assert remote_state["sd"]["skuMap"][";Black;38;"]["price"] == 99.9
                assert remote_state["sd"]["skuMap"][";Black;38;"]["stock"] == 77

                # 三次同步：再次修改颜色译文 Black -> Matte Black
                client.patch("/api/drafts/6001", json={
                    "sku_patch": {"color_rename": {"orig_name": "黑色", "draft_name": "Matte Black"}},
                })
                assert service.sync_to_miaoshou([6001])["results"][0]["ok"] is True
                assert remote_state["sd"]["colorMap"]["Matte Black"]["imgUrl"] == "https://example.com/black.png"
                assert remote_state["sd"]["skuMap"][";Matte Black;38;"]["price"] == 99.9

            # 6) 重新拉取采集箱商品保留本地 image_edit_plan
            it = storage.get_item(6001)
            it["image_edit_plan"] = {"count": 4, "selected_indices": [0, 1], "options": {"white_bg": True}}
            storage.save_item(it)
            rebuilt = service._build_item_from_site_detail(6001, "MY", "notPublished", {"ossMd5": "m3", "siteDetailSimpleData": raw_sd})
            assert rebuilt.get("image_edit_plan", {}).get("count") == 4

            # 7) /api/miaoshou/sync 异常返回 400 而非 500
            with patch("studio.service._client", side_effect=RuntimeError("未配置密钥")):
                r_err = client.post("/api/miaoshou/sync", json={"detail_ids": [6001]})
                assert r_err.status_code == 400

            # 8) 前端发布记录字段名 & 站点筛选包含 ID
            html = (Path(__file__).resolve().parent.parent / "studio" / "static" / "index.html").read_text(encoding="utf-8")
            assert "moveCollectDetailList" in html
            assert 'id="collectTableSelectAll"' in html
            assert '<option value="ID">ID 印尼</option>' in html


def test_credentials_manual_draft_csv_and_relay_parsing():
    """测试妙手密钥 .env 读写脱敏、连通性诊断、手动新建本地商品、CSV 导出与中转站图片响应解析。"""
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        cfg_p = td_path / "cfg.json"
        env_p = td_path / ".env"
        items_d = td_path / "items"
        imgs_d = td_path / "images"
        import os
        with patch.object(config, "CONFIG_PATH", cfg_p), \
             patch.object(config, "ENV_PATH", env_p), \
             patch.dict(os.environ, {}, clear=False), \
             patch.object(storage, "ITEMS_DIR", items_d), \
             patch.object(storage, "IMAGES_DIR", imgs_d), \
             patch.object(models, "IMAGES_DIR", imgs_d):

            client = TestClient(app)

            # 1) 保存并脱敏读取妙手 .env 密钥，且二次提交脱敏值不覆盖原密钥
            r_save = client.post("/api/miaoshou/credentials", json={
                "app_key": "ak_demo123456",
                "app_secret": "as_supersecret9876",
                "sub_account_id": "10086",
            })
            assert r_save.status_code == 200
            pub = r_save.json()
            assert pub["configured"] is True
            assert pub["app_key"] == "ak_demo123456"
            assert pub["app_secret"] == "as_s****9876"
            assert env_p.exists()

            r_save2 = client.post("/api/miaoshou/credentials", json={
                "app_key": "ak_demo123456",
                "app_secret": "as_s****9876",
                "sub_account_id": "",
            })
            assert r_save2.status_code == 200
            assert config.resolve_miaoshou_credentials()["app_secret"] == "as_supersecret9876"

            # 2) 妙手连通性测试（mock 成功与超时诊断）
            class FakeMSOk:
                def __init__(self, **kw): pass
                def call_raw(self, path, body=None):
                    return {"result": "success", "data": {"list": []}}

            with patch("studio.service.MiaoshouClient", FakeMSOk):
                r_ok = client.post("/api/test/miaoshou", json={})
                assert r_ok.status_code == 200
                assert r_ok.json()["ok"] is True

            class FakeMSTimeout:
                def __init__(self, **kw): pass
                def call_raw(self, path, body=None):
                    return {"result": "fail", "code": "networkError", "message": "Read timed out"}

            with patch("studio.service.MiaoshouClient", FakeMSTimeout):
                r_to = client.post("/api/test/miaoshou", json={})
                assert r_to.status_code == 200
                assert r_to.json()["ok"] is False
                assert "91miaoshou.com" in r_to.json()["hint"]

            # 3) 手动新建本地商品草稿 + 算价 + 导出 CSV + 同步回妙手友好拦截
            r_m = client.post("/api/drafts/manual", json={
                "title": "手动测试儿童防滑凉鞋",
                "site": "PH",
                "cost_rmb": 20,
                "weight_kg": 0.2,
                "stock": 50,
                "colors": "黑色, 米白色",
                "sizes": "24-25, 26-27",
                "notes": "防滑耐磨",
                "images": "https://example.com/a.jpg\nhttps://example.com/b.jpg",
            })
            assert r_m.status_code == 200, r_m.text
            created = r_m.json()
            did = created["detail_id"]
            assert created["is_local_only"] is True
            assert len(created["sku_draft"]["skus"]) == 4

            r_rp = client.post(f"/api/drafts/{did}/reprice", json={"pricing_id": "shopee_ph"})
            assert r_rp.status_code == 200
            assert r_rp.json()["pricing_summary"]["min_price"] > 0

            r_csv = client.get(f"/api/drafts/export.csv?ids={did}")
            assert r_csv.status_code == 200
            csv_txt = r_csv.content.decode("utf-8-sig")
            assert "手动测试儿童防滑凉鞋" in csv_txt
            assert "PHP" in csv_txt

            with patch("studio.service._client", return_value=FakeMSOk()):
                r_sync = client.post("/api/miaoshou/sync", json={"detail_ids": [did]})
                assert r_sync.status_code == 200
                assert r_sync.json()["results"][0]["ok"] is False
                assert "本地手动创建" in r_sync.json()["results"][0]["error"]

            # 4) 中转站 Markdown 图片链接 & inline_data 响应解析
            png_b = _make_png_bytes((40, 120, 200))

            class FakeMdResp:
                headers = {"Content-Type": "application/json"}
                text = ""
                def json(self):
                    return {
                        "choices": [{
                            "message": {
                                "content": "参考链接 https://docs.example.com/info\n![result](https://cdn.example.com/out.png)"
                            }
                        }]
                    }

            with patch("studio.models._download_bytes", return_value=png_b) as dl_mock:
                out_b, ext_u = models._parse_image_api_response(FakeMdResp())
                assert out_b == png_b
                assert ext_u == "https://cdn.example.com/out.png"
                dl_mock.assert_called_once_with("https://cdn.example.com/out.png")

            class FakeInlineResp:
                headers = {"Content-Type": "application/json"}
                text = ""
                def json(self):
                    return {
                        "choices": [{
                            "message": {
                                "content": [{"inline_data": {"mime_type": "image/png", "data": base64.b64encode(png_b).decode()}}]
                            }
                        }]
                    }

            out_b2, ext_u2 = models._parse_image_api_response(FakeInlineResp())
            assert out_b2 == png_b and ext_u2 is None


def test_ai_knowledge_index_assistant():
    """测试内置 AI 知识库索引检索、196 接口动态检索、本地模式/复用模式/独立中转站模型问答与密钥脱敏。"""
    import os
    from studio import assistant

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        cfg_p = td_path / "cfg.json"
        env_p = td_path / ".env"
        items_d = td_path / "items"
        imgs_d = td_path / "images"
        with patch.object(config, "CONFIG_PATH", cfg_p), \
             patch.object(config, "ENV_PATH", env_p), \
             patch.dict(os.environ, {}, clear=False), \
             patch.object(storage, "ITEMS_DIR", items_d), \
             patch.object(storage, "IMAGES_DIR", imgs_d), \
             patch.object(models, "IMAGES_DIR", imgs_d):

            client = TestClient(app)

            # 1) 知识库全量与搜索接口（覆盖系统文档 + 196 个妙手开放平台接口）
            r_all = client.get("/api/assistant/knowledge")
            assert r_all.status_code == 200
            d_all = r_all.json()
            assert d_all["total_docs"] >= 10
            assert d_all["total_apis"] == 196

            r_q = client.get("/api/assistant/knowledge?q=采购单")
            assert r_q.status_code == 200
            assert len(r_q.json()["apis"]) >= 1

            # 2) 未配置 API Key 时自动平滑降级为本地知识库检索
            r_local = client.post("/api/assistant/ask", json={"question": "如何配置中转站生图 API？"})
            assert r_local.status_code == 200
            dl = r_local.json()
            assert dl["mode_used"] == "local_index"
            assert "openai_chat_img" in dl["answer"] or "中转站" in dl["answer"]
            assert any(s["action"] == "config:image" for s in dl["sources"])

            # 3) 配置独立中转站语言模型（密钥自动脱敏且保留）并测试多轮问答
            config.save_config({
                "assistant_model": {
                    "mode": "custom_llm",
                    "base_url": "https://relay.example.com/v1",
                    "api_key": "sk-asst-secret-9988",
                    "model": "gpt-4o-mini",
                    "temperature": 0.2,
                }
            })
            pub = config.load_public_config()
            assert pub["assistant_model"]["api_key"] == "sk-a****9988"

            captured_msgs = []

            class FakeChatResp:
                status_code = 200
                text = ""
                def json(self):
                    return {"choices": [{"message": {"content": "请打开「⚙ 全局配置 → 🔑 妙手 ERP 密钥」填入 AppKey 与 AppSecret。"}}]}

            def fake_post(url, **kwargs):
                assert url == "https://relay.example.com/v1/chat/completions"
                captured_msgs.append(kwargs["json"]["messages"])
                return FakeChatResp()

            with patch("studio.assistant.requests.post", side_effect=fake_post):
                r_llm = client.post("/api/assistant/ask", json={
                    "question": "妙手密钥怎么申请和配置？",
                    "history": [{"role": "user", "content": "你好"}, {"role": "assistant", "content": "你好"}],
                })
                assert r_llm.status_code == 200
                res_llm = r_llm.json()
                assert res_llm["mode_used"] == "custom_llm"
                assert res_llm["model_used"] == "gpt-4o-mini"
                assert "妙手 ERP 密钥" in res_llm["answer"]
                assert "系统知识库检索结果" in captured_msgs[0][0]["content"]
                assert len(captured_msgs[0]) == 4  # system + 2 history + current user

                # 测试 /api/test/assistant 直接用脱敏密钥也能正确解析原密钥通过
                r_test = client.post("/api/test/assistant", json={
                    "mode": "custom_llm",
                    "base_url": "https://relay.example.com/v1",
                    "api_key": "sk-a****9988",
                    "model": "gpt-4o-mini",
                })
                assert r_test.status_code == 200
                assert r_test.json()["ok"] is True

            # 4) 测试 local_index 模式自检
            r_test_local = client.post("/api/test/assistant", json={"mode": "local_index"})
            assert r_test_local.status_code == 200
            assert r_test_local.json()["mode_used"] == "local_index"
            assert "196" in r_test_local.json()["sample"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
