# 妙手ERP开放平台 对接工具

官方文档：https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68 （密码 d8DUQdqH）

## 快速开始

> 📘 **新手完整图文配置教程（含妙手密钥申请、中转站生图/翻译配置、AI 索引助手与排错指南）请先看**：[使用说明.md](使用说明.md)

```powershell
pip install -r requirements.txt
python -m miaoshou studio   # 启动 Web 工作台（默认 http://127.0.0.1:18765）
```

> 妙手 ERP 密钥可在启动工作台后直接在页面右上角 **「⚙ 全局配置 → 🔑 妙手 ERP 密钥」** 可视化填写保存，也可以手动编辑 `.env` 后运行 `python -m miaoshou test` 验证。

## 铺货草稿工作台（Web 界面：自有模型/中转站批量处理 + 批量预览）

```powershell
python -m miaoshou studio
```

启动后浏览器打开 `http://127.0.0.1:18765`（也可用 `--port` 指定其他端口），顶部内置 **「🤖 AI 助手」**（全系统知识库索引问答）、**「📖 使用教程」** 与 **「⚙ 全局配置」** 弹窗，完整支持：
1. **内置 AI 智能索引助手（右下角 / 顶部入口 + 配置弹窗 Tab 5）**：知识库完整索引工作台全流程、密钥申请、中转站配置、定价公式与全部 196 个妙手开放平台接口，支持复用翻译模型、独立配置中转站/OpenAI 兼容语言模型或零费用本地知识库检索，并附带一键跳转操作按钮。
2. **妙手 ERP 密钥可视化配置（Tab 0）**：直接在页面填写并保存 `AppKey` / `AppSecret` 到 `.env`（无需重启立即生效），支持一键测试连通性与常见错误诊断。
2. **模型与中转站配置（Tab 1 / Tab 2）**：
   - **翻译模型**：内置零费用本地词典演示，也支持 DeepSeek / 豆包 / 通义 / OpenAI 及任意 OpenAI 兼容中转站（Base URL 填到 `/v1` 为止）。
   - **生图/改图模型（支持中转站）**：
     - **对话改图 `/chat/completions`（中转站首选）**：绝大多数 OneAPI / NewAPI / 聚合中转站直接支持 `https://你的中转站域名/v1` + `gemini-2.5-flash-image` / `gpt-4o-image`，支持按原图换纯白底、翻译图内中文、去水印与多角度出图；
     - **图片编辑 `/images/edits`**：适用于官方 OpenAI 或支持 `/images/edits` 的中转站（如 `gpt-image-1`）；
     - **本地 Pillow 模板渲染**：零费用白底框/角标/SKU 标签预览；
     - **自定义 HTTP 图片接口**：对接自建 ComfyUI/脚本；
     - **图片回传妙手**：中转站返回公网 URL 可直接转存妙手图片空间；若返回 Base64 或使用本地图，可配置自定义图床上传接口或 `public_base_url`（如 Cloudflare Tunnel / ngrok）。
3. **双分区工作流 + 离线可用能力**：
   - 第 1 页「采集与选品中心」支持货源链接采集、公共采集箱认领、Shopee 采集箱拉取、**手动新建本地商品**（无采集也能离线测试翻译/做图/定价）与 **CSV 导出**；
   - 第 2 页「批量编辑与发布台」支持批量生成、单品选图重做 3/4/5 张主图、SKU 逐行/批量调价与实时利润重算、一键保存草稿回妙手采集箱或提交发布到目标店铺。

### 妙手 ERP 应用密钥申请步骤

1. 登录妙手 ERP 后台，进入 **「开放平台」→「创建应用」**。
2. 填写应用名称、用途描述并勾选商品/采集箱/店铺/图片空间权限，提交审核。
3. 审核通过后复制 **AppKey（`ak_...`）** 和 **AppSecret（`as_...`）**，在工作台右上角「⚙ 全局配置 → 🔑 妙手 ERP 密钥」粘贴保存（或写入根目录 `.env`）。
4. **梯子/代理提醒**：妙手开放平台域名 `openapi-erp.91miaoshou.com` 为国内服务，若开启系统代理/梯子导致采集或同步超时（或触发 `ipNotInWhitelist`），请将 `91miaoshou.com` 加入代理直连规则（`DOMAIN-SUFFIX,91miaoshou.com,DIRECT`）。本地编辑、AI 翻译、中转站生图、跨境算价与 CSV 导出不受妙手网络影响。

## 命令

| 命令 | 作用 |
|---|---|
| `python -m miaoshou list 采购单` | 搜索接口（关键词匹配分类/名称/路径） |
| `python -m miaoshou info 获取订单包裹列表` | 查看参数、返回字段、请求体骨架 |
| `python -m miaoshou call ewm/warehouse/fetch/search_warehouse_page "{\"page\":1,\"pageSize\":20}"` | 调用任意接口（body 可写 `@body.json`） |
| `python -m miaoshou export order/package/fetch/search_package_list -o out/包裹.csv` | 自动翻页导出 CSV（Excel 可直接打开）/ JSON |
| `python -m miaoshou -v call ...` | 打印请求响应细节 |
| `python -m miaoshou --sub 1000013 call ...` | 以子账号身份调用 |

Python 中使用：

```python
from miaoshou import MiaoshouClient
c = MiaoshouClient()                       # 自动读取 .env
shops = c.call("product/shop/shop/get_shop_list",
               {"platform": "pddkj", "site": "PDDKJ", "pageNo": 1, "pageSize": 100})
packages = c.fetch_all("order/package/fetch/search_package_list", {"platform": "shopee"}, page_size=200)
```

客户端已处理：HmacSHA256 签名、秒级时间戳、body 序列化与签名一致、限流/下游错误自动退避重试、自动翻页（自动识别 `page`/`pageNo`）。

## 文件

- [功能分析.md](功能分析.md) — 能做什么、可落地的场景
- [docs/API目录.md](docs/API目录.md) — 196 个接口完整参数表
- `docs/openapi.json` — 合并后的 OpenAPI 3 规范（可导入 Apifox/Postman）
- `docs/endpoints.json` — 机器可读接口目录（CLI 使用）
- `docs/fetch_docs.py` / `docs/build_catalog.py` — 文档更新后重新拉取/生成（约 20 秒）
- `miaoshou/` — 客户端 + CLI；`tests/test_offline.py` — 离线自检
