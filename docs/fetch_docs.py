"""直接通过 HTTP 下载妙手开放平台 Apifox 文档 (llms.txt + 全部 .md)。"""
import re, sys, os, http.cookiejar, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor

DOC_ID = "fd54e57e-9b98-4c34-bada-306221c39e68"
PASSWORD = "d8DUQdqH"
BASE = f"https://s.apifox.cn/{DOC_ID}"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "md")
os.makedirs(OUT, exist_ok=True)

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [("User-Agent", "Mozilla/5.0")]


def get(url):
    with opener.open(url, timeout=30) as r:
        return r.read().decode("utf-8")


def auth():
    data = urllib.parse.urlencode({"id": DOC_ID, "password": PASSWORD}).encode()
    for host in ("https://s.apifox.cn", "https://api.apifox.com"):
        try:
            req = urllib.request.Request(host + "/api/v1/shared-doc-auth", data=data,
                                         headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
            with opener.open(req, timeout=30) as r:
                body = r.read().decode("utf-8", "ignore")
            print("auth", host, body[:300])
            print("cookies", [c.name + "@" + c.domain for c in cj])
            txt = get(BASE + "/llms.txt")
            if not txt.lstrip().startswith("<!DOCTYPE"):
                return txt
        except Exception as e:
            print("auth fail", host, e)
    sys.exit("could not authenticate")


llms = auth()
open(os.path.join(OUT, "..", "llms.txt"), "w", encoding="utf-8").write(llms)
urls = sorted(set(re.findall(r"\((https://s\.apifox\.cn/[^)]+?\.md)\)", llms)))
print("md urls:", len(urls))


def dl(u):
    name = u.rsplit("/", 1)[-1]
    p = os.path.join(OUT, name)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return name, "cached"
    for _ in range(3):
        try:
            t = get(u)
            open(p, "w", encoding="utf-8").write(t)
            return name, len(t)
        except Exception as e:
            err = e
    return name, f"ERR {err}"


with ThreadPoolExecutor(12) as ex:
    for name, r in ex.map(dl, urls):
        if isinstance(r, str) and r.startswith("ERR"):
            print(name, r)
print("done")
