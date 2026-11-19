"""命令行工具。

用法:
  python -m miaoshou list [关键词...]          列出/搜索接口
  python -m miaoshou info <路径或关键词>        查看接口参数与请求体骨架
  python -m miaoshou call <路径> [JSON|@文件]   调用任意接口
  python -m miaoshou export <路径> [JSON] -o out.csv   自动翻页导出到 CSV/JSON
  python -m miaoshou test                        只读冒烟测试（验证密钥/签名）
  python -m miaoshou sign <路径> <timestamp> [JSON]   仅计算签名（排查用）
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from . import catalog
from .client import MiaoshouClient, MiaoshouError, dump_body, make_sign, load_env

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def parse_body(s: str | None):
    if not s:
        return {}
    if s.startswith("@"):
        s = Path(s[1:]).read_text(encoding="utf-8-sig")
    return json.loads(s)


def resolve_path(arg: str) -> str:
    if "/" in arg:
        return catalog.normalize(arg)
    hits = catalog.search(arg)
    if len(hits) == 1:
        return hits[0]["path"]
    if not hits:
        sys.exit(f"找不到接口: {arg}")
    for e in hits:
        print(f"  {e['category']} | {e['title']} | {e['path']}")
    sys.exit(f"关键词匹配到 {len(hits)} 个接口，请写得更具体或直接给路径")


def cmd_list(a):
    hits = catalog.search(" ".join(a.keyword))
    for e in hits:
        print(f"{e['category']:<36} {e['title']:<28} {e['path']}")
    print(f"\n共 {len(hits)} 个")


def cmd_info(a):
    p = resolve_path(" ".join(a.target))
    e = catalog.find_endpoint(p)
    print(f"{e['category']} > {e['title']}\nPOST {e['path']}\n")
    if e["description"]:
        print(e["description"].strip(), "\n")
    print("请求参数:")
    for r in e["request"] or []:
        print(f"  {'*' if r[2] else ' '} {r[0]:<45} {r[1]:<16} {r[3]}")
    if not e["request"]:
        print("  (无)")
    print("\n返回 data 字段:")
    for r in e["response"][:60]:
        print(f"    {r[0]:<45} {r[1]:<16} {r[3]}")
    if len(e["response"]) > 60:
        print(f"    ... 共 {len(e['response'])} 个")
    print("\n请求体骨架(仅必填):")
    print(json.dumps(catalog.example_body(p), ensure_ascii=False, indent=2))


def client(a) -> MiaoshouClient:
    return MiaoshouClient(verbose=getattr(a, "verbose", False), sub_account_id=getattr(a, "sub", None))


def cmd_call(a):
    p = resolve_path(a.path)
    body = parse_body(a.body)
    miss = catalog.missing_required(p, body)
    if miss:
        print(f"[警告] 缺少必填字段: {', '.join(miss)}", file=sys.stderr)
    resp = client(a).call_raw(p, body)
    out = json.dumps(resp, ensure_ascii=False, indent=2)
    if a.output:
        Path(a.output).write_text(out, encoding="utf-8")
        print(f"已保存 {a.output}  result={resp.get('result')} code={resp.get('code')}")
    else:
        print(out)
    sys.exit(0 if resp.get("result") == "success" else 1)


def flatten_row(obj, prefix="", out=None):
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            flatten_row(v, f"{prefix}{k}.", out)
    elif isinstance(obj, list) and obj and all(not isinstance(x, (dict, list)) for x in obj):
        out[prefix[:-1]] = ",".join(map(str, obj))
    elif isinstance(obj, list):
        out[prefix[:-1]] = json.dumps(obj, ensure_ascii=False)
    else:
        out[prefix[:-1]] = obj
    return out


def write_rows(rows: list, output: str):
    path = Path(output)
    if path.suffix.lower() == ".json":
        path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
        return
    flat = [flatten_row(r) for r in rows]
    cols: list[str] = []
    for r in flat:
        for k in r:
            if k not in cols:
                cols.append(k)
    with path.open("w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig: Excel 直接打开不乱码
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(flat)


def cmd_export(a):
    p = resolve_path(a.path)
    body = parse_body(a.body)
    c = client(a)
    rows = []
    for i, items in enumerate(c.iter_pages(p, body, page_size=a.page_size), 1):
        rows.extend(items)
        print(f"  第 {i} 页: {len(items)} 条，累计 {len(rows)}", file=sys.stderr)
    write_rows(rows, a.output)
    print(f"导出 {len(rows)} 条 -> {a.output}")


SMOKE = [
    ("货源账号列表", "/open/v1/resell_account/fetch/search_reseller_account_page", {"page": 1, "pageSize": 10}),
    ("自营仓仓库列表", "/open/v1/ewm/warehouse/fetch/search_warehouse_page", {"page": 1, "pageSize": 10}),
    ("仓储商品列表", "/open/v1/ewm/goods/goods/fetch/search_goods_page", {"page": 1, "pageSize": 10}),
    ("供应商列表", "/open/v1/ewm/supplier/fetch/search_supplier_page", {"page": 1, "pageSize": 10}),
    ("订单包裹列表", "/open/v1/order/package/fetch/search_package_list", {"page": 1, "pageSize": 10}),
    ("TEMU全托店铺", "/open/v1/product/shop/shop/get_shop_list",
     {"platform": "pddkj", "site": "PDDKJ", "pageNo": 1, "pageSize": 20}),
    ("Shopee全球店铺", "/open/v1/product/shop/shop/get_shop_list",
     {"platform": "shopeeGlobal", "site": "SHOPEEGLOBAL", "pageNo": 1, "pageSize": 20}),
]


def cmd_test(a):
    c = client(a)
    print(f"域名: {c.base_url}\nAppKey: {c.app_key[:6]}***\n")
    ok = 0
    for name, path, body in SMOKE:
        r = c.call_raw(path, body)
        if r.get("result") == "success":
            ok += 1
            items, total = __import__("miaoshou.client", fromlist=["x"]).extract_list(r.get("data"))
            print(f"[OK ] {name:<14} 返回 {len(items)} 条" + (f" / 共 {total}" if total is not None else ""))
        else:
            print(f"[ERR] {name:<14} {r.get('code')}: {r.get('message') or r.get('reason')}")
    print(f"\n{ok}/{len(SMOKE)} 成功")
    sys.exit(0 if ok else 1)


def cmd_sign(a):
    load_env()
    import os
    key, sec = os.getenv("MIAOSHOU_APP_KEY", ""), os.getenv("MIAOSHOU_APP_SECRET", "")
    body = dump_body(parse_body(a.body)) if a.body else ""
    print(make_sign(sec, catalog.normalize(a.path), a.timestamp, key, body))


def cmd_studio(a):
    from studio.server import run
    url = f"http://{a.host}:{a.port}"
    print(f"启动妙手铺货草稿工作台: {url}")
    if not a.no_browser:
        import threading, webbrowser
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    run(host=a.host, port=a.port)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m miaoshou", description="妙手ERP开放平台 CLI")
    ap.add_argument("-v", "--verbose", action="store_true", help="打印请求/响应")
    ap.add_argument("--sub", help="x-sub-account-id 子账号ID")
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("list"); s.add_argument("keyword", nargs="*"); s.set_defaults(f=cmd_list)
    s = sp.add_parser("info"); s.add_argument("target", nargs="+"); s.set_defaults(f=cmd_info)
    s = sp.add_parser("call"); s.add_argument("path"); s.add_argument("body", nargs="?")
    s.add_argument("-o", "--output"); s.set_defaults(f=cmd_call)
    s = sp.add_parser("export"); s.add_argument("path"); s.add_argument("body", nargs="?")
    s.add_argument("-o", "--output", required=True); s.add_argument("--page-size", type=int, default=50)
    s.set_defaults(f=cmd_export)
    s = sp.add_parser("test"); s.set_defaults(f=cmd_test)
    s = sp.add_parser("sign"); s.add_argument("path"); s.add_argument("timestamp"); s.add_argument("body", nargs="?")
    s.set_defaults(f=cmd_sign)
    s = sp.add_parser("studio"); s.add_argument("--host", default="127.0.0.1"); s.add_argument("--port", type=int, default=18765)
    s.add_argument("--no-browser", action="store_true"); s.set_defaults(f=cmd_studio)
    a = ap.parse_args(argv)
    try:
        a.f(a)
    except MiaoshouError as e:
        sys.exit(f"错误 {e}")


if __name__ == "__main__":
    main()
