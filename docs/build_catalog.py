"""把 md/ 下各接口的 OpenAPI 片段合并成 openapi.json，并生成 API目录.md / endpoints.json。"""
import json, os, re, glob
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "md")
llms = open(os.path.join(HERE, "llms.txt"), encoding="utf-8").read()

# llms.txt 中的顺序 = 文档左侧目录顺序
order = []
for m in re.finditer(r"- (.+?) \[(.+?)\]\(https://s\.apifox\.cn/[^)]+/(api-\d+)\.md\)", llms):
    order.append((m.group(1).strip(), m.group(2).strip(), m.group(3)))

merged = {"openapi": "3.0.1",
          "info": {"title": "妙手ERP开放平台", "version": "1.0.0"},
          "servers": [{"url": "https://openapi-erp.91miaoshou.com"}],
          "paths": {}, "components": {"schemas": {}}}
endpoints = []
HEADER_SKIP = {"x-app-key", "x-timestamp", "x-sign", "cookie"}


def resolve(schema, comps, depth=0):
    if not isinstance(schema, dict) or depth > 12:
        return schema
    if "$ref" in schema:
        name = schema["$ref"].split("/")[-1]
        return resolve(comps.get(name, {}), comps, depth + 1)
    out = {}
    for k, v in schema.items():
        if k == "properties":
            out[k] = {pk: resolve(pv, comps, depth + 1) for pk, pv in v.items()}
        elif k == "items":
            out[k] = resolve(v, comps, depth + 1)
        elif k in ("allOf", "anyOf", "oneOf"):
            out[k] = [resolve(x, comps, depth + 1) for x in v]
        else:
            out[k] = v
    return out


def flatten(schema, prefix="", required=(), rows=None, depth=0):
    """把 schema 展开成 (字段路径, 类型, 必填, 说明) 行。"""
    rows = [] if rows is None else rows
    if not isinstance(schema, dict) or depth > 8:
        return rows
    props = schema.get("properties") or {}
    req = set(schema.get("required") or [])
    for name, p in props.items():
        if name.startswith("x-apifox"):
            continue
        p = p or {}
        t = p.get("type", "object" if "properties" in p else "")
        if isinstance(t, list):
            t = "|".join(map(str, t))
        desc = (p.get("description") or p.get("title") or "").replace("\n", " ").replace("|", "/")
        extra = []
        if "enum" in p:
            extra.append("枚举:" + ",".join(map(str, p["enum"])))
        if "maximum" in p:
            extra.append(f"max:{p['maximum']}")
        if extra:
            desc = (desc + " " + " ".join(extra)).strip()
        path = f"{prefix}{name}"
        if t == "array":
            it = p.get("items") or {}
            it_t = it.get("type", "object" if "properties" in it else "")
            rows.append((path, f"array<{it_t}>", name in req, desc))
            if it.get("properties"):
                flatten(it, path + "[].", rows=rows, depth=depth + 1)
        else:
            rows.append((path, t, name in req, desc))
            if p.get("properties"):
                flatten(p, path + ".", rows=rows, depth=depth + 1)
    return rows


for cat, title, aid in order:
    f = os.path.join(MD, aid + ".md")
    txt = open(f, encoding="utf-8").read()
    m = re.search(r"```yaml\n(.*?)\n```", txt.replace("\r\n", "\n"), re.S)
    spec = yaml.safe_load(m.group(1))
    comps = (spec.get("components") or {}).get("schemas") or {}
    merged["components"]["schemas"].update(comps)
    for path, ops in spec["paths"].items():
        for method, op in ops.items():
            merged["paths"].setdefault(path, {})[method] = op
            body = (((op.get("requestBody") or {}).get("content") or {}).get("application/json") or {}).get("schema") or {}
            body = resolve(body, comps)
            resp = ((op.get("responses") or {}).get("200") or {}).get("content", {}).get("application/json", {}).get("schema") or {}
            resp = resolve(resp, comps)
            data = (resp.get("properties") or {}).get("data") or {}
            endpoints.append({
                "id": aid,
                "category": cat.replace("开放平台 > ", ""),
                "title": title,
                "method": method.upper(),
                "path": path,
                "description": op.get("description") or "",
                "request": flatten(body),
                "response": flatten(data),
                "requestSchema": body,
            })

json.dump(merged, open(os.path.join(HERE, "openapi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(endpoints, open(os.path.join(HERE, "endpoints.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- Markdown 目录 ----------
lines = ["# 妙手ERP开放平台 接口目录", "",
         f"共 {len(endpoints)} 个接口。基础域名 `https://openapi-erp.91miaoshou.com`，全部为 `POST` + `application/json`。",
         "签名：`x-sign = HmacSHA256(appSecret, appSecret + path + timestamp + appKey + bodyJson + appSecret)`（小写 hex）。",
         "", "## 总览", "", "| 分类 | 接口 | 路径 |", "|---|---|---|"]
for e in endpoints:
    lines.append(f"| {e['category']} | {e['title']} | `{e['path']}` |")
lines += ["", "## 接口详情", ""]
cur = None
for e in endpoints:
    if e["category"] != cur:
        cur = e["category"]
        lines += [f"### {cur}", ""]
    lines += [f"#### {e['title']}", "", f"`POST {e['path']}`  (文档: {e['id']})", ""]
    if e["description"]:
        lines += [e["description"].strip(), ""]
    if e["request"]:
        lines += ["请求参数：", "", "| 字段 | 类型 | 必填 | 说明 |", "|---|---|---|---|"]
        lines += [f"| `{r[0]}` | {r[1]} | {'是' if r[2] else ''} | {r[3]} |" for r in e["request"]]
        lines.append("")
    else:
        lines += ["请求参数：无（body 传 `{}`）", ""]
    if e["response"]:
        top = [r for r in e["response"]][:40]
        lines += ["返回 data 字段：", "", "| 字段 | 类型 | 说明 |", "|---|---|---|"]
        lines += [f"| `{r[0]}` | {r[1]} | {r[3]} |" for r in top]
        if len(e["response"]) > 40:
            lines.append(f"| … | | 共 {len(e['response'])} 个字段，详见 openapi.json |")
        lines.append("")
open(os.path.join(HERE, "API目录.md"), "w", encoding="utf-8").write("\n".join(lines))
print("endpoints:", len(endpoints), "paths:", len(merged["paths"]))
