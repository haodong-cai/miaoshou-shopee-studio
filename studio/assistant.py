"""内置系统 AI 智能索引与问答引擎（全系统知识库检索 + 中转站 / OpenAI 兼容语言模型问答）。

特性：
1. 完整整理工作台全套功能、流程、妙手密钥申请、中转站生图/翻译配置、7 站点定价公式、
   CLI 命令、196 个妙手开放平台接口目录与常见报错排查。
2. 零额外依赖的中文/英文混合检索（关键词 + 汉字二元/三元组 + 标签加权），同时动态检索
   `docs/endpoints.json` 的 196 个妙手接口与当前工作台实时配置状态（不含任何密钥明文）。
3. 支持三种回答模式：
   - reuse_text : 复用「翻译与文本模型」的 OpenAI 兼容 / 中转站配置（若未填 Key 自动平滑降级到本地索引）
   - custom_llm : 独立配置 AI 助手专属的中转站或 OpenAI 兼容语言模型
   - local_index: 纯本地知识库精准检索（零费用、离线可用）
"""
from __future__ import annotations

import json
import re
import time
from typing import Any

import requests

from miaoshou import catalog

from . import config, models, presets, pricing, storage


SYSTEM_KNOWLEDGE_CHUNKS: list[dict[str, Any]] = [
    {
        "id": "workflow_overview",
        "category": "使用流程",
        "title": "工作台双分区架构与标准 5 步操作流程",
        "tags": ["流程", "怎么用", "上手", "入门", "步骤", "分区", "选品中心", "编辑台", "发布台", "工作流"],
        "action": "guide:quickstart",
        "action_label": "📖 打开快速上手教程",
        "content": (
            "本工作台采用【双分区工作流】：\n"
            "• 第 1 页「采集与选品中心」：负责把商品汇入本地选品池，支持 4 种来源——(A) 货源链接一键采集（1688/淘宝/拼多多）、"
            "(B) 打开妙手公共采集箱挑选认领、(C) 按站点/状态从妙手 Shopee 采集箱拉取、以及 (D) 点击顶部「➕ 手动新建商品」离线创建本地草稿。\n"
            "  筛选区支持按状态（全部/待处理/已做好草稿/已存回妙手/已发布/异常）、站点（含 PH/MY/SG/TH/TW/VN/ID/BR/SHOPEEGLOBAL）、"
            "队列状态与关键词搜索，并可在「选品卡片」与「紧凑表格」间切换。\n"
            "• 第 2 页「批量编辑与发布台」：在第 1 页勾选商品并点「➡️ 选中传入【第 2 页】」（也可点「📥 载入全部选品池商品」）后进入精修。\n"
            "• 标准 5 步操作：\n"
            "  1) 在第 1 页拉取/新建并勾选商品传入第 2 页；\n"
            "  2) 在第 2 页模块 1 选择主图视觉风格、定价公式模板、默认主图张数（1/3/4/5/全部）与快捷修图选项；\n"
            "  3) 在模块 2 点「⚡ 一键生成选中商品（翻译+做图+算价）」，或分别点「仅翻译 / 仅主图 / 仅SKU图 / 仅算定价」；\n"
            "  4) 在商品卡片中精修标题/描述、勾选指定原图重做 3/4/5 张主图、展开 SKU 表调成本/重量/售价/库存，或点「✏ 批量修改参数」跨商品批改；\n"
            "  5) 离线留档可点「📊 导出 CSV」；联网妙手后在模块 3 先点「☁ 保存选中回妙手」核对，再勾选店铺点「🚀 直接发布选中」，并在右上角「📋 发布记录」查看结果。"
        ),
    },
    {
        "id": "miaoshou_credentials",
        "category": "妙手接入",
        "title": "妙手 ERP 开放平台应用密钥（AppKey / AppSecret）申请与配置",
        "tags": ["妙手", "密钥", "AppKey", "AppSecret", "申请", "开放平台", ".env", "子账号", "白名单", "签名", "连通性"],
        "action": "config:miaoshou",
        "action_label": "🔑 去配置妙手密钥",
        "content": (
            "妙手 ERP 开放平台正式环境域名为 https://openapi-erp.91miaoshou.com，所有接口统一使用 POST + application/json + HmacSHA256 签名（客户端已自动处理签名与重试）。\n"
            "【申请 4 步流程】\n"
            "1) 使用主账号登录妙手 ERP 网页端，进入「开放平台」→「创建应用」（无入口请联系妙手客服开通开放平台权限）；\n"
            "2) 填写应用名称与用途描述，勾选所需业务权限（商品/采集箱、店铺列表、图片空间、订单包裹/采购/仓储等），提交审核；\n"
            "3) 审核通过后在应用详情页获取 AppKey（通常以 ak_ 开头）和 AppSecret（通常以 as_ 开头，请严格保密）；\n"
            "4) 在本工作台右上角点「⚙ 全局配置 → 🔑 妙手 ERP 密钥」粘贴 AppKey 和 AppSecret（子账号操作可填子账号 ID，对应请求头 x-sub-account-id），点「💾 保存妙手密钥到 .env」即可免重启生效，再点「🧪 测试妙手接口连通性」验证。\n"
            "【IP 白名单说明】妙手后台 IP 白名单是账户级配置：不配置则允许任意 IP 访问；若已配置，所有应用只能从白名单 IP 调用（开启梯子会改变出口 IP，容易报 ipNotInWhitelist）。"
        ),
    },
    {
        "id": "proxy_offline",
        "category": "网络与离线",
        "title": "开启梯子/代理导致妙手超时解决办法 & 离线可用功能清单",
        "tags": ["梯子", "代理", "超时", "timeout", "91miaoshou", "直连", "Clash", "v2ray", "离线", "手动新建", "CSV", "导出"],
        "action": "manual_draft",
        "action_label": "➕ 手动新建本地商品",
        "content": (
            "【为什么开梯子会采集/拉取超时？】\n"
            "妙手接口 openapi-erp.91miaoshou.com 是国内服务器，如果本机开启系统代理/全局梯子或 Fake-IP 接管了国内域名，请求容易出现 Read timed out（networkError）或触发 ipNotInWhitelist。\n"
            "【推荐分流设置】在 Clash / Mihomo / v2rayN 的分流规则或 Bypass（绕过代理）列表中加入：\n"
            "  DOMAIN-SUFFIX,91miaoshou.com,DIRECT（或 *.91miaoshou.com）\n"
            "这样妙手国内接口走直连，同时海外 AI / 中转站 API 仍可正常走代理。\n"
            "【完全不受梯子影响、现在就能离线/直接使用的功能】\n"
            "• 选品池已有商品的筛选、分组与入队；\n"
            "• 第 1 页顶部「➕ 手动新建商品」：手工填入标题、站点、进货价、重量、库存、颜色/尺码与图片链接生成本地草稿；\n"
            "• AI 翻译 / 零费用本地词典翻译；\n"
            "• 中转站 AI 生图/改图与零费用本地 Pillow 风格主图/SKU图；\n"
            "• Shopee 7 站点跨境定价公式、实时汇率同步（open.er-api.com）、SKU 逐行/批量改价与实时利润重算；\n"
            "• 第 1 页与第 2 页顶部「📊 导出 CSV」：一键导出 Excel 可直接打开的 UTF-8-SIG 表格（含标题、描述、成本、重量、建议售价区间、预估利润、主图链接）。"
        ),
    },
    {
        "id": "image_api_relay",
        "category": "生图与中转站",
        "title": "生图 / 改图 API 与中转站配置指南（4 种模式 + 图床回传妙手）",
        "tags": ["生图", "做图", "改图", "图片", "中转站", "OneAPI", "NewAPI", "Gemini", "gpt-4o-image", "gpt-image-1", "Pillow", "图床", "公网穿透", "Cloudflare", "ngrok", "base_url"],
        "action": "config:image",
        "action_label": "🖼 去配置生图 API / 中转站",
        "content": (
            "打开右上角「⚙ 全局配置 → 🖼 图片引擎与中转站」，支持 4 种做图引擎：\n"
            "1) OpenAI 兼容对话改图（openai_chat_img，走 /chat/completions）——【中转站最推荐】：绝大多数 OneAPI / NewAPI / 聚合中转站直接支持。按原图改纯白底、翻译图内中文、去水印、换场景、多角度出图效果最好。\n"
            "   • Base URL：填中转站地址，填到 /v1 为止（如 https://api.你的中转站.com/v1），不要手拼 /chat/completions；\n"
            "   • 常用模型名：gemini-2.5-flash-image、gemini-2.5-flash-image-preview、gpt-4o-image（以中转站实际模型列表为准）；\n"
            "   • API Key：填写中转站令牌 sk-...；填完直接点「🧪 用当前风格测试做图」验证出图。\n"
            "2) OpenAI 图片编辑接口（openai_edit，走 /images/edits）：程序自动将原图转 PNG 并 multipart 上传，适合官方 OpenAI 或支持 /images/edits 的中转站（如 gpt-image-1）。\n"
            "3) 本地 Pillow 模板渲染（local_pillow）：零费用无需 API Key，支持 800×800 纯白底居中、边框、角标、底部卖点条、SKU 底部规格胶囊标签与锐化增强。\n"
            "4) 自定义 HTTP 图片接口（custom_http）：POST JSON（含 prompt/image_url/image_base64/options/target_language），支持自定义请求头 JSON，适合对接自建 ComfyUI 或私有生图网关。\n"
            "【AI 新图 / 本地图如何回传妙手？】\n"
            "• 若中转站直接返回公网图片 URL，同步回妙手时会自动上传到妙手图片空间并替换主图；\n"
            "• 若返回 Base64 或使用本地 Pillow 图，可在 Tab 2 填写「自定义图床上传接口」（POST multipart file 返回 {\"url\":\"...\"}）或填写「本机公网穿透地址」（如 Cloudflare Tunnel / ngrok 的 https://xxx.trycloudflare.com），妙手即可自动拉取。"
        ),
    },
    {
        "id": "image_studio_card",
        "category": "主图精修",
        "title": "商品卡片内「主图精修工作区」使用方法（选图、3/4/5 张、单槽重做）",
        "tags": ["主图", "选图", "3张", "4张", "5张", "白底", "去中文", "翻译图片", "精修", "场景", "多角度", "重做", "置顶", "放大对比"],
        "action": "page:editor",
        "action_label": "🛠 去第 2 页编辑台",
        "content": (
            "在第 2 页每张商品卡片左侧的「主图精修区」中：\n"
            "• 点选原图：点击左侧「原主图」缩略图即可勾选/取消要参与生成的底图，也支持「全选 / 前3 / 前4 / 前5 / 清空」快捷按钮；点击缩略图右上角 🔍 可放大双栏对比原图与草稿图。\n"
            "• 指定生成张数：选择「按所选 / 3 张 / 4 张 / 5 张」；当目标张数大于所选原图张数时，系统会自动循环底图并注入多角度构图变化提示词，避免生成重复图。\n"
            "• 6 项修图开关：🌐 翻译图内文字、☀ 纯白底、🧹 去中文/水印、✨ 高清精修、🏡 场景氛围图、🔄 多角度变化，还可输入「补充修图指令」。\n"
            "• 单张操作：生成完成后，鼠标悬停在右侧「新做主图」上可点 ↻ 单独重做该槽位、★ 设为第 1 张主图、✕ 从草稿移除该图。"
        ),
    },
    {
        "id": "text_model_translate",
        "category": "翻译与文案",
        "title": "翻译与文本大模型配置（零费用词典 vs DeepSeek / OpenAI / 中转站）",
        "tags": ["翻译", "文本模型", "文案", "标题", "描述", "SKU翻译", "本地词典", "local_dict", "DeepSeek", "OpenAI", "通义", "豆包", "SiliconFlow", "中转站", "Prompt"],
        "action": "config:text",
        "action_label": "📝 去配置翻译模型",
        "content": (
            "打开「⚙ 全局配置 → 📝 翻译与文本模型」，支持两种模式：\n"
            "1) 零费用本地词典演示（local_dict）：无需 API Key，点击预设即可免费跑通标题、描述与 SKU 颜色/尺码翻译，适合先验证完整流程。\n"
            "2) OpenAI 兼容大模型（llm，正式上架推荐）：内置 DeepSeek、OpenAI、通义千问、火山豆包、SiliconFlow 以及「🌐 通用中转站」一键预设。\n"
            "   • Base URL 填到 /v1（豆包为 /api/v3），填入 Model 名称与 API Key（sk-...），点「🧪 测试翻译」验证。\n"
            "   • Prompt 模板支持变量 {target_language}、{title_max_len}、{style_tone}，会自动同步翻译商品标题、分点描述、颜色/尺寸属性名与全部规格值，并自动做去重处理防止妙手 skuMap key 冲突。\n"
            "   • 并发线程数可在 1～8 之间调整（默认 3）。"
        ),
    },
    {
        "id": "pricing_formula",
        "category": "定价公式",
        "title": "Shopee 7 站点跨境定价公式、SLS 藏价运费、实时汇率与自定义公式",
        "tags": ["定价", "公式", "价格", "利润", "利润率", "SLS", "藏价", "运费", "汇率", "补重", "打包重量", "佣金", "技术支持费", "基础设施费", "税率", "取整", "自定义公式", "PH", "MY", "SG", "TH", "TW", "VN", "BR"],
        "action": "config:pricing",
        "action_label": "💲 去配置定价公式",
        "content": (
            "打开「⚙ 全局配置 → 💲 定价公式模板」，已内置 Shopee 7 大站点 2026 官方默认 SLS 藏价表与公开费率：PH(PHP)、MY(MYR)、SG(SGD)、TH(THB)、TW(TWD 分段阶梯)、VN(VND)、BR(BRL 分段阶梯)。\n"
            "• 3 种公式模式：销售利润率模式（margin，总成本 ÷ (1 - 平台费率 - 目标利润率)）、成本加成模式（markup）、自定义公式（custom，使用 Python AST 白名单安全求值）。\n"
            "• 左栏=官方基准（首重/续重藏价、佣金率、交易手续费、技术支持费、每单基础设施费）；右栏标红=卖家自调项（打包补重 weight_buffer_g、结算汇率+「🌐 实时汇率」一键拉取 open.er-api.com 中间价、目标利润率、保底固定利润、国内寄仓费、折前抬价比例 promo_discount、额外防亏扣点 tax_rate）。\n"
            "• 尾数取整支持：四舍五入整数(int)、向上取整(ceil)、.99(dot99)、.90(dot90)、千位取整(k1000)、保留两位小数(none)。\n"
            "• 自定义公式可用变量：cost, weight, weight_g, rate, shipping, extra_fee, fixed_order_fee, commission, tx_fee, tech_fee, tax_rate, profit_rate, fixed_profit, orig_price；可用函数：max, min, round, ceil, floor, abs。\n"
            "• 底部「公式实时试算」支持输入任意进货价（含 0）与重量即时预览售价、藏价、平台费与净利润；点「+ 新建公式」保存后会自动持久化为当前默认定价模板。"
        ),
    },
    {
        "id": "batch_edit_sku",
        "category": "批量编辑与SKU",
        "title": "批量修改参数、SKU 明细逐行调价与利润实时重算",
        "tags": ["批量修改", "SKU", "进货价", "成本", "重量", "库存", "改价", "标题前缀", "查找替换", "移出编辑台", "删除"],
        "action": "page:editor",
        "action_label": "🛠 去第 2 页编辑台",
        "content": (
            "在第 2 页「批量编辑与发布台」支持三层编辑粒度：\n"
            "1) 跨商品「✏ 批量修改参数」弹窗：对所有已勾选商品批量修改进货价/重量/库存/售价（支持统一设为、加减、按倍数），勾选自动重算后可立即按公式刷新售价与利润；同时支持给标题批量加前缀/后缀或查找替换。\n"
            "2) 单品卡片「本品批量改」：展开 SKU 抽屉后，可按颜色筛选（如仅改「黑色」SKU）或针对全部 SKU 一键设进货价、重量、库存或直接售价。\n"
            "3) SKU 明细表逐行微调：修改某行的「进货价 / 重(kg)」会自动按当前公式重算新售价与利润；直接修改「公式新价」也会按当前站点完整费率即时重算该行预估利润并同步刷新卡片顶部 KPI 条；修改颜色译文会自动同步保存。\n"
            "• 注意区分：「📤 移出编辑台」只把商品从第 2 页编辑队列移出（草稿保留在第 1 页）；「🗑 删除」才会删除本地草稿文件（均不会删除妙手后台商品）。"
        ),
    },
    {
        "id": "style_presets",
        "category": "视觉风格",
        "title": "预设视觉风格模板（内置 4 套风格 + 自定义新建保存）",
        "tags": ["风格", "模板", "角标", "边框", "奶油风", "促销风", "纯白无字", "爆款白底", "新建风格"],
        "action": "config:style",
        "action_label": "🎨 去配置风格模板",
        "content": (
            "工作台内置 4 套视觉与文案风格（在「⚙ 全局配置 → 🎨 预设风格模板」可查看和编辑）：\n"
            "1) shopee_clean（Shopee 爆款白底框）：800×800 纯白底 + 虾皮橙细边框 + HOT PICK 角标 + SKU 底部黑色胶囊标签；\n"
            "2) jp_kr_fresh（日韩清新奶油风）：暖杏奶油背景 + 焦糖细框 + NEW 轻角标 + 底部柔感卖点条；\n"
            "3) promo_burst（大促强视觉促销风）：醒目红色促销框 + FLASH DEAL 角标 + READY STOCK 底部条；\n"
            "4) minimal_clean（纯白合规无字风）：无边框、无角标、无文字，最稳妥过审。\n"
            "点击「+ 新建风格」可自定义背景色、边框、角标、底部卖点条、SKU 标签、文案风格指令与 AI 生图风格 Prompt，保存后会自动刷新下拉框并持久化为默认风格。"
        ),
    },
    {
        "id": "sync_publish_records",
        "category": "同步与发布",
        "title": "保存草稿回妙手采集箱、发布到多店铺与查看发布记录",
        "tags": ["同步", "保存到妙手", "发布", "上架", "店铺", "发布记录", "二次同步", "本地草稿"],
        "action": "page:editor",
        "action_label": "🚀 去编辑与发布台",
        "content": (
            "• 先保存再发布：在第 2 页模块 3 先点「☁ 保存选中回妙手」（调用 get_site_detail_simple_data + save_site_detail_data），把标题、描述、主图、SKU 规格译文、SKU 图片及新售价/进货价/重量/库存写回妙手 Shopee 采集箱。\n"
            "• 支持多次重复同步：系统会记录已同步的规格名与 SKU key，二次/三次修改价格、库存或再次改名后重新保存回妙手，均会保留远端规格图并正确写入新值。\n"
            "• 提交发布：在模块 3 勾选目标 Shopee 店铺后点「🚀 直接发布选中」（调用 save_move_collect_task），提交后可在右上角「📋 发布记录」查看发布状态与失败原因（读取官方 moveCollectDetailList 字段）。\n"
            "• 本地手动新建的演示商品标记为 is_local_only，无法直接回传妙手采集箱，但可用于离线测试翻译/生图/算价与导出 CSV。"
        ),
    },
    {
        "id": "ai_assistant_config",
        "category": "AI 助手配置",
        "title": "内置 AI 智能索引助手的模型选择与中转站配置",
        "tags": ["AI助手", "索引", "知识库", "助手模型", "问答", "中转站", "OpenAI", "reuse_text", "custom_llm", "local_index"],
        "action": "config:assistant",
        "action_label": "🤖 去配置 AI 助手模型",
        "content": (
            "本内置 AI 索引助手知识库覆盖整个工作台的操作流程、配置说明、定价公式、CLI 工具与全部 196 个妙手开放平台接口，并在提问时自动附带工作台实时状态诊断。\n"
            "在「⚙ 全局配置 → 🤖 AI 助手模型」中支持 3 种驱动模式：\n"
            "1) 复用「翻译与文本模型」配置（reuse_text，默认）：无需重复填写密钥；若翻译模型尚未填 Key，会自动平滑降级为本地知识库检索；\n"
            "2) 独立配置中转站 / OpenAI 兼容语言模型（custom_llm）：可单独为 AI 助手指定任意中转站 Base URL（到 /v1）、Model（如 gpt-4o-mini / deepseek-chat / gemini-2.5-flash）与 API Key，并可点「🧪 测试 AI 助手」验证；\n"
            "3) 纯本地知识库索引（local_index）：零费用、无需 Key，离线直接检索系统知识库与 196 个妙手接口。"
        ),
    },
    {
        "id": "cli_and_196_apis",
        "category": "CLI 与开放接口",
        "title": "命令行 CLI 工具与妙手 196 个开放平台接口 5 大板块总览",
        "tags": ["CLI", "命令行", "接口", "196", "采购", "1688", "包裹", "面单", "发货", "仓储", "库存", "TikTok", "TEMU", "OZON", "美客多", "export", "call", "list", "info"],
        "action": "guide:miaoshou",
        "action_label": "🔑 查看妙手接入说明",
        "content": (
            "除 Web 工作台外，项目还内置命令行 CLI 工具（python -m miaoshou）：\n"
            "• python -m miaoshou studio [--port 18765] ：启动 Web 铺货草稿工作台\n"
            "• python -m miaoshou test ：只读冒烟测试，验证密钥与签名\n"
            "• python -m miaoshou list <关键词> ：在 196 个妙手接口中搜索路径\n"
            "• python -m miaoshou info <路径或关键词> ：查看接口必填参数、返回字段与请求体骨架\n"
            "• python -m miaoshou call <路径> <JSON|@文件> ：调用任意接口（支持 --sub 子账号、-v 打印详情）\n"
            "• python -m miaoshou export <路径> [JSON] -o out/结果.csv ：自动翻页导出 Excel CSV / JSON\n"
            "【196 个妙手开放平台接口 5 大板块】\n"
            "1) 商品/刊登（141）：店铺列表、公共采集箱（注意 fetch_item 高危需先校验链接）、图片空间、AI 公共服务（白底/消除/图译/润色）及 TikTok/TEMU全半托/Shopee/OZON/美客多采集箱与发布；\n"
            "2) 包裹/订单履约（17）：包裹列表/详情、设置物流、申请运单号、获取面单、发货、物流轨迹、退货/取消售后；\n"
            "3) 采购（18）：采购单增改查、一键向 1688 下单、缺货/备货建议、供应商管理；\n"
            "4) 仓储（18）：多规格商品主数据、自营仓/三方仓库存、安全库存、出入库申请单、销售与周转统计；\n"
            "5) 货源账号（2）：1688 货源账号与收货地址。\n"
            "【官方接口能力边界】不包含：直接查平台订单（只有包裹维度）、财务/利润报表、直接改库存数（需走出入库申请单）、Webhook 推送（仅支持轮询）。"
        ),
    },
    {
        "id": "troubleshooting",
        "category": "故障排查",
        "title": "常见报错与问题排查速查表",
        "tags": ["报错", "错误", "失败", "故障", "排查", "为什么", "API Key", "signExpired", "signInvalid", "appNotFound", "appNoPermission", "ipNotInWhitelist", "未配置"],
        "action": "guide:miaoshou",
        "action_label": "📖 打开排错速查表",
        "content": (
            "常见报错快速定位：\n"
            "• 「未配置文本模型 API Key」：打开「⚙ 全局配置 → 📝 翻译与文本模型」，填入 DeepSeek/OpenAI/中转站 Key，或先切换为「内置本地词典演示（免 Key）」。\n"
            "• 「networkError / Read timed out」：检查是否开了梯子/代理，把 91miaoshou.com 加入代理直连规则，或关代理后点「测试妙手接口连通性」。\n"
            "• 「appNotFound / signInvalid」：检查 AppKey(ak_...) 与 AppSecret(as_...) 是否有空格或大小写错误，确认应用已在妙手开放平台审核通过。\n"
            "• 「signExpired」：本机时间与服务器偏差超过 5 分钟，校准 Windows 系统时间即可。\n"
            "• 「ipNotInWhitelist」：出口 IP 不在妙手账户白名单内，清空妙手 IP 白名单或将当前直连 IP 加入白名单。\n"
            "• 「本地做图未配置公网图床URL，已保留原图」：本地 Pillow 或返回 base64 的生图需要配置图床上传接口或公网穿透地址（public_base_url）后才能上传替换妙手主图；使用返回公网 URL 的中转站则可自动上传。"
        ),
    },
]


def _tokenize(text: str) -> set[str]:
    """混合切词：英文单词/数字 + 中文 2-gram / 3-gram + 单字（零外部依赖）。"""
    s = (text or "").lower()
    tokens: set[str] = set()
    for w in re.findall(r"[a-z0-9_./-]{2,}", s):
        tokens.add(w)
    for seg in re.findall(r"[\u4e00-\u9fff]+", s):
        if len(seg) <= 1:
            tokens.add(seg)
            continue
        for n in (2, 3):
            if len(seg) >= n:
                for i in range(len(seg) - n + 1):
                    tokens.add(seg[i : i + n])
        if len(seg) <= 6:
            tokens.add(seg)
    return tokens


def _score_chunk(query: str, q_tokens: set[str], chunk: dict[str, Any]) -> float:
    q_low = (query or "").strip().lower()
    if not q_low:
        return 1.0
    title = (chunk.get("title") or "").lower()
    category = (chunk.get("category") or "").lower()
    tags = [str(t).lower() for t in (chunk.get("tags") or [])]
    content = (chunk.get("content") or "").lower()

    score = 0.0
    if q_low in title:
        score += 12.0
    if q_low in content:
        score += 6.0
    for t in tags:
        if t and (t in q_low or q_low in t):
            score += 5.5

    title_toks = _tokenize(title + " " + category + " " + " ".join(tags))
    body_toks = _tokenize(content)
    score += len(q_tokens & title_toks) * 2.5
    score += len(q_tokens & body_toks) * 0.7
    return score


def _search_miaoshou_endpoints(query: str, limit: int = 5) -> list[dict[str, Any]]:
    """当用户询问接口/能力/API 路径时，从 196 个妙手开放平台接口中检索最相关项。"""
    q_low = (query or "").strip().lower()
    if not q_low:
        return []
    q_tokens = _tokenize(q_low)
    try:
        eps = catalog.endpoints()
    except Exception:
        return []

    scored: list[tuple[float, dict[str, Any]]] = []
    for ep in eps:
        hay = f"{ep.get('category', '')} {ep.get('title', '')} {ep.get('path', '')}".lower()
        sc = 0.0
        if q_low in hay:
            sc += 10.0
        ep_toks = _tokenize(hay)
        overlap = q_tokens & ep_toks
        sc += len(overlap) * 2.0
        if sc >= 3.5:
            scored.append((sc, ep))
    scored.sort(key=lambda kv: kv[0], reverse=True)
    return [ep for _, ep in scored[:limit]]


def retrieve_knowledge(query: str, top_k: int = 4) -> list[dict[str, Any]]:
    """检索最相关的系统知识块（并按需动态附加命中的妙手开放平台 API 清单）。"""
    q = (query or "").strip()
    q_tokens = _tokenize(q)

    scored = [(_score_chunk(q, q_tokens, ch), ch) for ch in SYSTEM_KNOWLEDGE_CHUNKS]
    scored.sort(key=lambda kv: kv[0], reverse=True)

    hits: list[dict[str, Any]] = []
    for sc, ch in scored[:top_k]:
        if sc > 0 or not hits:
            hits.append({**ch, "score": round(sc, 2)})

    # 若问题涉及接口/API/具体业务板块，动态补充命中的妙手开放平台接口
    api_eps = _search_miaoshou_endpoints(q, limit=6)
    api_hint_words = ("接口", "api", "路径", "采购", "1688", "包裹", "面单", "运单", "发货", "物流", "库存", "仓库", "售后", "退货", "tiktok", "temu", "ozon", "美客多", "类目", "品牌", "运费模板")
    if api_eps and (any(w in q.lower() for w in api_hint_words) or (hits and hits[0]["score"] < 6.0)):
        lines = [f"• {e['category']} > {e['title']}：`POST {e['path']}`" for e in api_eps]
        hits.append({
            "id": "live_miaoshou_api_matches",
            "category": "妙手 196 接口实时索引",
            "title": f"匹配的妙手开放平台接口（共命中 {len(api_eps)} 个）",
            "tags": ["API", "接口目录"],
            "action": "guide:miaoshou",
            "action_label": "🔑 查看妙手接入说明",
            "content": "以下接口来自本地 docs/endpoints.json（可用 `python -m miaoshou info <路径>` 查看完整参数）：\n" + "\n".join(lines),
            "score": 8.0,
        })
    return hits


def _build_live_status_context(cfg: dict[str, Any]) -> str:
    """采集当前工作台的非敏感实时运行状态，供 AI 助手做针对性诊断。"""
    ms = config.load_miaoshou_env_public()
    tm = cfg.get("text_model") or {}
    im = cfg.get("image_model") or {}
    tpl = cfg.get("template") or {}
    items = storage.list_items()
    by_st: dict[str, int] = {}
    for it in items:
        st = it.get("status") or "pending"
        by_st[st] = by_st.get(st, 0) + 1

    style = presets.get_style_preset(tpl.get("style_id"), cfg.get("custom_style_presets"))
    pr = pricing.get_pricing_preset(tpl.get("pricing_id"), cfg.get("custom_pricing_presets"))
    return (
        "【当前工作台实时状态（非敏感摘要）】\n"
        f"- 妙手 .env 密钥：{'已配置' if ms.get('configured') else '未配置'}\n"
        f"- 翻译模型：provider={tm.get('provider')}, model={tm.get('model')}, api_key={'已填' if tm.get('api_key') else '未填'}\n"
        f"- 生图引擎：mode={im.get('mode')}, model={im.get('model')}, process_count={im.get('process_count')}, api_key={'已填' if im.get('api_key') else '未填'}\n"
        f"- 当前默认模板：风格={style.get('name')}({style.get('id')})，定价={pr.get('name')}({pr.get('id')})\n"
        f"- 本地草稿统计：共 {len(items)} 条（{json.dumps(by_st, ensure_ascii=False)}）"
    )


def resolve_effective_assistant_llm(cfg: dict[str, Any]) -> tuple[str, dict[str, Any] | None]:
    """解析当前 AI 助手实际生效的运行模式与 LLM 参数。

    返回 (mode_used, llm_cfg_or_None)：
      - ("custom_llm", {...})
      - ("reuse_text", {...})
      - ("local_index", None)
    """
    acfg = cfg.get("assistant_model") or {}
    mode = acfg.get("mode") or "reuse_text"

    if mode == "local_index":
        return "local_index", None

    if mode == "custom_llm":
        if (acfg.get("api_key") or "").strip() and (acfg.get("base_url") or "").strip():
            return "custom_llm", {
                "base_url": acfg["base_url"],
                "api_key": acfg["api_key"],
                "model": acfg.get("model") or "gpt-4o-mini",
                "temperature": float(acfg.get("temperature") if acfg.get("temperature") is not None else 0.3),
            }
        return "local_index", None

    # 默认 reuse_text：若文本模型是 llm 且已配置 Key 则复用，否则平滑降级到本地索引
    tcfg = cfg.get("text_model") or {}
    if tcfg.get("provider") == "llm" and (tcfg.get("api_key") or "").strip() and (tcfg.get("base_url") or "").strip():
        return "reuse_text", {
            "base_url": tcfg["base_url"],
            "api_key": tcfg["api_key"],
            "model": tcfg.get("model") or "deepseek-chat",
            "temperature": 0.3,
        }
    return "local_index", None


def _call_openai_chat(llm_cfg: dict[str, Any], messages: list[dict[str, str]], timeout: int = 60) -> str:
    url = models._openai_endpoint(llm_cfg.get("base_url", ""), "/chat/completions")
    payload = {
        "model": llm_cfg.get("model") or "gpt-4o-mini",
        "messages": messages,
        "temperature": float(llm_cfg.get("temperature") if llm_cfg.get("temperature") is not None else 0.3),
    }
    headers = {
        "Authorization": f"Bearer {llm_cfg['api_key'].strip()}",
        "Content-Type": "application/json",
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=timeout)
    if resp.status_code >= 400:
        raise models.ModelError(f"AI 助手模型 HTTP {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise models.ModelError(f"AI 助手响应格式异常: {json.dumps(data, ensure_ascii=False)[:300]}") from e
    if isinstance(content, list):
        content = "\n".join(str(b.get("text") or "") for b in content if isinstance(b, dict))
    return str(content or "").strip()


def _format_local_index_answer(question: str, hits: list[dict[str, Any]], configured_mode: str) -> str:
    """当未配置大模型 API Key 或主动选「仅本地知识库检索」时，输出结构化知识索引答复。"""
    parts: list[str] = []
    if not hits or (len(hits) == 1 and hits[0].get("score", 0) <= 0):
        parts.append("在系统知识库中暂未精准匹配到该词条，以下是工作台核心指引：")
    else:
        parts.append(f"根据系统知识库为你精准索引到以下 {min(3, len(hits))} 条说明：")

    for idx, ch in enumerate(hits[:3], 1):
        parts.append(f"\n**{idx}. {ch['title']}**（{ch['category']}）\n{ch['content']}")

    if configured_mode != "local_index":
        parts.append(
            "\n> 💡 当前为「本地知识库检索模式」（因为尚未填写大模型 API Key）。"
            "如需由大模型/中转站结合上下文为你智能总结回答，点上方「⚙ 切换/配置模型」填入中转站或 OpenAI 兼容语言模型即可。"
        )
    return "\n".join(parts)


def ask_assistant(
    question: str,
    *,
    history: list[dict[str, str]] | None = None,
    assistant_override: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """回答用户关于整个工作台的任何流程、配置、接口或排错问题。"""
    q = (question or "").strip()
    if not q:
        raise ValueError("请输入你想咨询的问题")

    t0 = time.time()
    cfg = config.resolve_runtime_config({"assistant_model": assistant_override} if assistant_override else None)
    configured_mode = (cfg.get("assistant_model") or {}).get("mode") or "reuse_text"

    hits = retrieve_knowledge(q, top_k=4)
    sources = [
        {
            "id": h["id"],
            "title": h["title"],
            "category": h["category"],
            "action": h.get("action") or "",
            "action_label": h.get("action_label") or "",
            "snippet": (h.get("content") or "")[:160],
        }
        for h in hits[:4]
    ]

    mode_used, llm_cfg = resolve_effective_assistant_llm(cfg)
    if mode_used == "local_index" or not llm_cfg:
        answer = _format_local_index_answer(q, hits, configured_mode)
        return {
            "answer": answer,
            "mode_used": "local_index",
            "model_used": "内置系统知识库索引",
            "sources": sources,
            "elapsed_ms": int((time.time() - t0) * 1000),
        }

    kb_context = "\n\n".join(
        f"### [{h['category']}] {h['title']}\n{h['content']}"
        for h in hits
    )
    live_ctx = _build_live_status_context(cfg)
    sys_prompt = (
        "你是「妙手铺货上架工作台」的内置 AI 智能索引助手。\n"
        "请严格基于下方提供的【系统知识库检索结果】与【当前工作台实时状态】用简洁清晰的中文回答用户问题：\n"
        "1. 给出具体可操作的界面按钮名称、配置弹窗页签路径或命令；\n"
        "2. 结合用户当前实时状态指出可能缺少的配置（如未填 Key、开梯子超时等）；\n"
        "3. 不要编造系统不存在的功能或接口；若知识库未提及，请如实说明。\n\n"
        f"{live_ctx}\n\n"
        f"【系统知识库检索结果】\n{kb_context}"
    )

    msgs: list[dict[str, str]] = [{"role": "system", "content": sys_prompt}]
    for h in (history or [])[-6:]:
        role = h.get("role")
        txt = str(h.get("content") or "").strip()
        if role in ("user", "assistant") and txt:
            msgs.append({"role": role, "content": txt[:1500]})
    msgs.append({"role": "user", "content": q})

    answer = _call_openai_chat(llm_cfg, msgs)
    return {
        "answer": answer,
        "mode_used": mode_used,
        "model_used": llm_cfg.get("model") or "llm",
        "sources": sources,
        "elapsed_ms": int((time.time() - t0) * 1000),
    }


def test_assistant_model(patch: dict[str, Any] | None = None) -> dict[str, Any]:
    """测试 AI 助手模型配置（支持直接测试表单未保存值）。"""
    cfg = config.resolve_runtime_config({"assistant_model": patch} if patch else None)
    acfg = cfg.get("assistant_model") or {}
    req_mode = acfg.get("mode") or "reuse_text"

    if req_mode == "local_index":
        t0 = time.time()
        hits = retrieve_knowledge("如何配置生图API中转站", top_k=2)
        return {
            "ok": True,
            "mode_used": "local_index",
            "model_used": "内置系统知识库索引",
            "elapsed_ms": int((time.time() - t0) * 1000),
            "sample": f"本地知识库索引正常（共 {len(SYSTEM_KNOWLEDGE_CHUNKS)} 篇系统文档 + {len(catalog.endpoints())} 个妙手接口），命中：《{hits[0]['title']}》",
        }

    mode_used, llm_cfg = resolve_effective_assistant_llm(cfg)
    if not llm_cfg:
        if req_mode == "reuse_text":
            raise models.ModelError("当前选择「复用翻译模型」，但翻译模型尚未配置 LLM 模式及 API Key（请先在 Tab 1 填 Key，或改为独立配置/本地索引）")
        raise models.ModelError("请先填写 AI 助手的 Base URL 和 API Key")

    t0 = time.time()
    reply = _call_openai_chat(
        llm_cfg,
        [
            {"role": "system", "content": "你是妙手铺货上架工作台 AI 助手，请用一句话回复「连接测试成功」并简述你能协助什么。"},
            {"role": "user", "content": "请做连通性测试"},
        ],
        timeout=45,
    )
    return {
        "ok": True,
        "mode_used": mode_used,
        "model_used": llm_cfg.get("model") or "",
        "elapsed_ms": int((time.time() - t0) * 1000),
        "sample": reply[:200],
    }


def list_knowledge_index(query: str = "") -> dict[str, Any]:
    """供前端「知识库索引」面板浏览与即时搜索整个系统知识库及 196 个妙手接口。"""
    q = (query or "").strip()
    if not q:
        docs = [
            {
                "id": ch["id"],
                "category": ch["category"],
                "title": ch["title"],
                "tags": ch.get("tags") or [],
                "action": ch.get("action") or "",
                "action_label": ch.get("action_label") or "",
                "content": ch["content"],
            }
            for ch in SYSTEM_KNOWLEDGE_CHUNKS
        ]
        apis = []
    else:
        q_tokens = _tokenize(q)
        scored = [(_score_chunk(q, q_tokens, ch), ch) for ch in SYSTEM_KNOWLEDGE_CHUNKS]
        scored.sort(key=lambda kv: kv[0], reverse=True)
        docs = [
            {
                "id": ch["id"],
                "category": ch["category"],
                "title": ch["title"],
                "tags": ch.get("tags") or [],
                "action": ch.get("action") or "",
                "action_label": ch.get("action_label") or "",
                "content": ch["content"],
                "score": round(sc, 2),
            }
            for sc, ch in scored
            if sc > 0
        ]
        apis = [
            {"category": e["category"], "title": e["title"], "path": e["path"]}
            for e in _search_miaoshou_endpoints(q, limit=12)
        ]

    try:
        total_apis = len(catalog.endpoints())
    except Exception:
        total_apis = 0

    return {
        "total_docs": len(SYSTEM_KNOWLEDGE_CHUNKS),
        "total_apis": total_apis,
        "docs": docs,
        "apis": apis,
    }
