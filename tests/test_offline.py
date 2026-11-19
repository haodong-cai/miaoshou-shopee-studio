"""离线自检：python tests/test_offline.py"""
import hashlib, hmac, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from miaoshou.client import make_sign, dump_body, extract_list
from miaoshou import catalog


def test_sign_matches_official_python_example():
    s, k, p, t = "as_xxxxxxxxxxxxxxxx", "ak_1234567890abcdef", "/open/v1/order/create", 1700000000
    b = '{"orderNo":"ORD2024001","amount":100.00}'
    ref = hmac.new(s.encode(), (s + p + str(t) + k + b + s).encode(), hashlib.sha256).hexdigest()
    assert make_sign(s, p, t, k, b) == ref
    assert make_sign(s, p, t, k, "") == hmac.new(s.encode(), (s + p + str(t) + k + s).encode(), hashlib.sha256).hexdigest()


def test_dump_body_compact_utf8():
    assert dump_body({"a": "中文", "b": [1, 2]}) == '{"a":"中文","b":[1,2]}'


def test_extract_list():
    assert extract_list({"orderPackageList": [1, 2], "total": 5}) == ([1, 2], 5)
    assert extract_list({"page": {"list": [1], "total": 1}}) == ([1], 1)


def test_catalog():
    eps = catalog.endpoints()
    assert len(eps) == 196
    assert len({e["path"] for e in eps}) == 196
    assert catalog.missing_required("ewm/warehouse/fetch/search_warehouse_page", {}) == ["page", "pageSize"]
    assert catalog.example_body("/open/v1/product/shop/shop/get_shop_list")["pageNo"] == 1


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("PASS", name)
