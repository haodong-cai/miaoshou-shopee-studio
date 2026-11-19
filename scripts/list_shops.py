"""列出账号下所有平台/站点的店铺（只读）。"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding="utf-8")
from miaoshou import MiaoshouClient

SITES = {
    "tiktok": "ID VN TH MY PH BR MX ES FR GB US DE IT JP".split(),
    "tiktokGlobal": ["TIKTOKGLOBAL", "TIKTOKGLOBALUS", "TIKTOKGLOBALEU"],
    "shopee": "ID TW VN TH MY SG PH BR MX CL CO PL ES FR AR".split(),
    "shopeeGlobal": ["SHOPEEGLOBAL"],
    "pddkj": ["PDDKJ"], "pddkjChoice": ["PDDKJCHOICE"],
    "mercadolibre": ["CBT", "UP"], "ozon": ["OZON"],
}
c = MiaoshouClient()
allshops = []
for plat, sites in SITES.items():
    for site in sites:
        r = c.call_raw("/open/v1/product/shop/shop/get_shop_list",
                       {"platform": plat, "site": site, "pageNo": 1, "pageSize": 100})
        if r.get("result") != "success":
            print(f"[ERR] {plat}/{site}: {r.get('code')} {r.get('message')}")
            continue
        d = r.get("data") or {}
        lst = next((v for v in d.values() if isinstance(v, list)), []) if isinstance(d, dict) else d
        for s in lst:
            s["_query"] = f"{plat}/{site}"
            allshops.append(s)
            print(f"{plat:<13}{site:<15} shopId={s.get('shopId')} 名称={s.get('platformShopName') or s.get('shopName')} "
                  f"别名={s.get('shopNick')} 站点={s.get('siteName')} isCb={s.get('isCb')} isCnsc={s.get('isCnsc')} "
                  f"parent={s.get('parentShopId')} 状态={s.get('status')}")
Path("out").mkdir(exist_ok=True)
Path("out/shops.json").write_text(json.dumps(allshops, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\n共 {len(allshops)} 个店铺 -> out/shops.json")
