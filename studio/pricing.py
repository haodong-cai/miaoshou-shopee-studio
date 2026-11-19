"""跨境定价公式引擎（站点预设 + 标准利润公式 + 安全 AST 自定义公式）。

支持：
1. 标准跨境利润公式：
   - 采购成本(RMB) + 首重/续重国际运费(RMB) + 附加杂费(RMB)
   - 平台佣金率 + 交易手续费率 + 税费率 + 目标利润率(或加价率)
   - 汇率换算 -> 可选活动折前涨价 -> 尾数取整（整数/.99/.90/千位等）
2. 自定义公式表达式：
   - 使用 Python AST 白名单安全求值（绝不执行任意代码）
   - 可用变量：cost, weight, weight_g, rate, shipping, extra_fee, commission, tx_fee, tax_rate, profit_rate, fixed_profit, orig_price
   - 可用函数：max, min, round, ceil, floor, abs
"""
from __future__ import annotations

import ast
import copy
import math
import operator
from typing import Any

import requests

BUILTIN_PRICING_PRESETS: dict[str, dict[str, Any]] = {
    "shopee_ph": {
        "id": "shopee_ph",
        "name": "Shopee 菲律宾 (PHP)",
        "site": "PH",
        "currency": "PHP",
        "mode": "margin",  # margin | markup | custom
        "exchange_rate": 9.57,
        "shipping_currency": "local",
        "first_weight_g": 50,
        "first_shipping_local": 23.0,   # ≤50g: 23 PHP
        "step_weight_g": 10,
        "step_shipping_local": 4.5,     # >50g: 4.5 PHP / 10g (200g=90.5 PHP)
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.12,        # 2026-01 起跨境直邮(SLS)含税佣金 12%
        "tx_fee_rate": 0.0224,          # 交易手续费 2.15%~2.24% (含VAT)
        "tech_fee_rate": 0.0,           # 技术支持费 (PH 暂未列入 5% 公告)
        "fixed_order_fee_local": 5.0,   # 平台基础设施费 5 PHP/单 (含税，前50净单及新店90天免)
        "tax_rate": 0.0,
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "int",  # none | int | ceil | dot99 | dot90 | k1000
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS官方默认标准渠道(内地)：≤50g 23 PHP，>50g 每10g +4.5 PHP（普特货同价）；佣金12%+交易费2.24%+基础设施费5 PHP/单",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "月销不多免 5 比索：每月前 50 单、以及开店前 90 天内免扣每单 5 PHP 基础设施费；符合条件可把左边该项改 0",
            "新首店免佣期：新开的第 1 个菲律宾店，前 3 个月(月 500 单内)通常免佣金，免佣期间可把左边佣金改 0",
            "不同物流价不同：默认按「内地空运」算；如走海运(>140g 只要 1.9/10g)或香港仓(5.5/10g)要改左边单价",
            "参加了活动再多预留：如果店铺报名了免运/返现活动或分期付款，在上面预留框点 0.03 或 0.05 即可",
        ],
    },
    "shopee_my": {
        "id": "shopee_my",
        "name": "Shopee 马来西亚 (MYR)",
        "site": "MY",
        "currency": "MYR",
        "mode": "margin",
        "exchange_rate": 0.61,
        "shipping_currency": "local",
        "first_weight_g": 10,
        "first_shipping_local": 0.15,   # ≤10g: 0.15 MYR
        "step_weight_g": 10,
        "step_shipping_local": 0.15,    # >10g: 0.15 MYR / 10g (200g=3.0 MYR)
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.1836,      # 2026 跨境直邮(SLS)含SST佣金 18.36%
        "tx_fee_rate": 0.0378,          # 交易手续费含SST 3.78%
        "tech_fee_rate": 0.05,          # 2026-02 起技术支持费 5% (可按含SST微调)
        "fixed_order_fee_local": 0.54,  # 平台基础设施费 0.54 MYR/单
        "tax_rate": 0.0,
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "dot90",
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS官方默认标准渠道：全程 0.15 MYR/10g（普特货同价，200g=3 MYR）；佣金18.36%+交易费3.78%+技术支持费5%+0.54 MYR/单",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "5% 技术费可能会微调：有时叠加本地服务税或返广告金，出第一单后对照后台实扣调整就行",
            "买家分期会多扣手续费：如果买家选分期付款，交易费可能从 3.78% 涨到 4.86%~8.1%，怕亏可多预留 0.01~0.02",
            "改发海运/重货要改左边：海运经济渠道和重货渠道的运费标准和默认空运不一样",
        ],
    },
    "shopee_sg": {
        "id": "shopee_sg",
        "name": "Shopee 新加坡 (SGD)",
        "site": "SG",
        "currency": "SGD",
        "mode": "margin",
        "exchange_rate": 0.192,
        "shipping_currency": "local",
        "first_weight_g": 40,
        "first_shipping_local": 1.26,   # ≤40g: 1.26 SGD
        "step_weight_g": 10,
        "step_shipping_local": 0.15,    # >40g: 0.15 SGD / 10g (200g=3.66 SGD)
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.16,        # 2026-01 起跨境直邮含税佣金 16%
        "tx_fee_rate": 0.03,            # 标准交易手续费约 3%
        "tech_fee_rate": 0.05,          # 2026-02 起技术支持费 5%
        "fixed_order_fee_local": 0.0,
        "tax_rate": 0.0,                # 上述佣金已为含税率；如有额外GST可填入此处
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "dot90",
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS官方默认标准渠道：≤40g 1.26 SGD，>40g 每10g +0.15 SGD（普特货同价，200g=3.66 SGD）；佣金16%+交易费3%+技术支持费5%",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "海外仓佣金更低：默认按跨境直邮 16% 算；如果是官方海外仓发货，左边佣金只需填 0.11",
            "特殊商品/大促：开了预售(多扣3%)、大促日(多扣1%)或涉及进口商品消费税，填到上面预留框里",
            "海运还看体积：走海运渠道会按包裹体积额外加收藏价，大体积商品请把克重往大里填",
        ],
    },
    "shopee_th": {
        "id": "shopee_th",
        "name": "Shopee 泰国 (THB)",
        "site": "TH",
        "currency": "THB",
        "mode": "margin",
        "exchange_rate": 5.06,
        "shipping_currency": "local",
        "first_weight_g": 10,
        "first_shipping_local": 1.0,    # ≤10g: 1 THB
        "step_weight_g": 10,
        "step_shipping_local": 1.0,     # >10g: 1 THB / 10g (南宁仓 0.9/10g; 200g=20 THB)
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.1819,      # 非商城跨境直邮参考 18.19% (部分类目/店铺20%-24%)
        "tx_fee_rate": 0.0321,          # 交易手续费含7% VAT约 3.21%
        "tech_fee_rate": 0.0535,        # 技术支持费 5% + 7% VAT = 5.35%
        "fixed_order_fee_local": 1.07,  # 平台基础设施费 1.07 THB/单
        "tax_rate": 0.0,
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "int",
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS官方默认标准渠道：全程 1 THB/10g（南宁仓0.9 THB/10g，普特货同价）；佣金~18.19%+交易费3.21%+技术支持费5.35%+1.07 THB/单",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "泰国不同类目佣金差很大：2026 年不少类目/商城实际佣金涨到了 20%~24%，默认只按 18.19% 算，记得看后台账单",
            "南宁仓更省运费：如果从南宁仓发货，泰国续重只有 0.9 THB/10g（比默认 1 THB 便宜）",
            "技术支持费已含本地税：已按 5%+7% 本地税 (=5.35%) 预填，出首单后核对一次即可",
        ],
    },
    "shopee_tw": {
        "id": "shopee_tw",
        "name": "Shopee 台湾 (TWD)",
        "site": "TW",
        "currency": "TWD",
        "mode": "margin",
        "exchange_rate": 4.93,
        "shipping_currency": "local",
        "first_weight_g": 500,
        "first_shipping_local": 25.0,   # ≤500g: 25 TWD (普货; 特货≤500g为45 TWD)
        "step_weight_g": 500,
        "step_shipping_local": 30.0,    # 首段续重 30 TWD / 500g，大重量见 shipping_tiers
        "shipping_tiers": [
            {"up_to_g": 500, "base": 25.0},
            {"up_to_g": 1000, "step_g": 500, "step_fee": 30.0},
            {"up_to_g": 2000, "step_g": 500, "step_fee": 40.0},
            {"up_to_g": 2500, "step_g": 500, "step_fee": 50.0},
            {"up_to_g": None, "step_g": 500, "step_fee": 60.0},
        ],
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.14,        # 当前14%含税 (官方公告2026年12月起统一调至15.8%)
        "tx_fee_rate": 0.025,           # 交易手续费 2.5% (预售服务费另+3%)
        "tech_fee_rate": 0.0,
        "fixed_order_fee_local": 0.0,
        "tax_rate": 0.0,
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "int",
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS台湾普货(7-11/全家/宅配)：≤500g 25 TWD，之后 30/40/40/50/60 TWD 每500g阶梯（特货每段+20/10 TWD）；佣金14%+交易费2.5%",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "2026 年 12 月起官方统一涨佣金：由 14% 涨到 15.8%，到时候记得把左边佣金改成 0.158",
            "发较长备货(预售)会多扣 3%：如果上架预售品，在上面预留框填 0.03",
            "带电/液体特货更贵：默认按普货算(首重 25 TWD)；发特货要把左边首重改成 45，每档续重也贵 10",
        ],
    },
    "shopee_vn": {
        "id": "shopee_vn",
        "name": "Shopee 越南 (VND)",
        "site": "VN",
        "currency": "VND",
        "mode": "margin",
        "exchange_rate": 3846.0,
        "shipping_currency": "local",
        "first_weight_g": 10,
        "first_shipping_local": 900.0,  # ≤10g: 900 VND
        "step_weight_g": 10,
        "step_shipping_local": 900.0,   # >10g: 900 VND / 10g (南宁仓 750/10g; 200g=18000 VND)
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.1533,      # 跨境直邮参考 ~15.33%
        "tx_fee_rate": 0.0491,          # 交易手续费约 4.91% (视渠道最高近6%)
        "tech_fee_rate": 0.054,         # 技术支持费 5% + 8% VAT = 5.4%
        "fixed_order_fee_local": 3000.0,  # 平台基础设施费 3,000 VND/单 (含VAT)
        "tax_rate": 0.0,
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "k1000",
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS官方默认标准渠道：全程 900 VND/10g（南宁仓750 VND/10g，普特货同价）；佣金~15.33%+交易费~4.91%+技术支持费5.4%+3,000 VND/单",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "支付手续费不同方式会变：越南交易手续费最高接近 6%，建议出了几单后对照后台账单修改",
            "发南宁仓更便宜：默认按内地 900 VND/10g；走南宁仓只要 750/10g，香港仓要 3,220/10g",
            "部分快消品/三方仓费率不同：不懂可以先用默认值，或上面多留 0.02~0.03 兜底",
        ],
    },
    "shopee_br": {
        "id": "shopee_br",
        "name": "Shopee 巴西 (BRL)",
        "site": "BR",
        "currency": "BRL",
        "mode": "margin",
        "exchange_rate": 0.845,
        "shipping_currency": "local",
        "first_weight_g": 30,
        "first_shipping_local": 5.0,    # ≤30g: 5 BRL
        "step_weight_g": 10,
        "step_shipping_local": 1.4,     # 30-100g: 1.4/10g; >100g: 0.9/10g (见 shipping_tiers)
        "shipping_tiers": [
            {"up_to_g": 30, "base": 5.0},
            {"up_to_g": 100, "step_g": 10, "step_fee": 1.4},
            {"up_to_g": None, "step_g": 10, "step_fee": 0.9},
        ],
        "extra_fee_rmb": 2.0,
        "commission_rate": 0.16,        # 2026 跨境直邮常规佣金 16% (含FSS合并)
        "tx_fee_rate": 0.02,            # 交易手续费 2%
        "tech_fee_rate": 0.0,
        "fixed_order_fee_local": 0.0,
        "tax_rate": 0.0,
        "profit_rate": 0.25,
        "fixed_profit_rmb": 0.0,
        "promo_discount": 0.0,
        "rounding": "dot90",
        "custom_formula": "(cost + shipping + extra_fee + fixed_order_fee) / max(0.1, 1 - commission - tx_fee - tech_fee - tax_rate - profit_rate) * rate",
        "rate_source": "SLS官方标准(Expresso padrão)：≤30g 5 BRL，30-100g 1.4/10g，>100g 0.9/10g (200g=23.8 BRL)；佣金16%+交易费2%",
        "weight_buffer_g": 0,
        "uncertain_items": [
            "巴西税费较多：可能有约 0.38% 的当地支付操作费或清关州税差，不懂可先在上面多留 0.01~0.03",
            "新首店可能有佣金减免：2026 年新开通的首个巴西店前几个月享 10% 佣金直减，可按实际修改左边佣金",
        ],
    },
}


_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}
_FUNCS = {
    "max": max,
    "min": min,
    "round": round,
    "ceil": math.ceil,
    "floor": math.floor,
    "abs": abs,
}


def eval_formula(expr: str, variables: dict[str, float]) -> float:
    """使用 AST 白名单安全求值自定义定价公式。"""
    src = (expr or "").strip()
    if not src:
        raise ValueError("定价公式不能为空")
    try:
        tree = ast.parse(src, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"公式语法错误: {e.msg}") from e

    def _eval(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id not in variables:
                raise ValueError(f"未知公式变量: {node.id}")
            return float(variables[node.id])
        if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
            left = _eval(node.left)
            right = _eval(node.right)
            if isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)) and right == 0:
                raise ValueError("公式出现除以 0")
            return float(_BIN_OPS[type(node.op)](left, right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
            return float(_UNARY_OPS[type(node.op)](_eval(node.operand)))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            fn_name = node.func.id
            if fn_name not in _FUNCS or node.keywords:
                raise ValueError(f"不支持的公式函数: {fn_name}")
            args = [_eval(a) for a in node.args]
            return float(_FUNCS[fn_name](*args))
        raise ValueError(f"公式包含不支持的语法: {type(node).__name__}")

    val = _eval(tree)
    if math.isnan(val) or math.isinf(val):
        raise ValueError("公式计算结果无效")
    return val


def fetch_live_fx_rates(base: str = "CNY") -> dict[str, Any]:
    """从公开汇率接口（open.er-api.com）获取实时中间价汇率。"""
    url = f"https://open.er-api.com/v6/latest/{base.upper()}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if data.get("result") != "success" or not isinstance(data.get("rates"), dict):
        raise ValueError(f"汇率接口返回异常: {data}")
    return {
        "base": data.get("base_code", base.upper()),
        "updated_at": data.get("time_last_update_utc", ""),
        "source": "open.er-api.com",
        "rates": data["rates"],
    }


def list_pricing_presets(custom_presets: dict[str, dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    out = copy.deepcopy(BUILTIN_PRICING_PRESETS)
    for pid, pdata in (custom_presets or {}).items():
        if isinstance(pdata, dict):
            base = copy.deepcopy(out.get(pid) or BUILTIN_PRICING_PRESETS["shopee_ph"])
            base.update(pdata)
            base["id"] = pid
            out[pid] = base
    return out


def get_pricing_preset(pricing_id: str | None, custom_presets: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    all_presets = list_pricing_presets(custom_presets)
    if pricing_id and pricing_id in all_presets:
        return all_presets[pricing_id]
    return all_presets["shopee_ph"]


def calc_shipping_detail(weight_kg: float, cfg: dict[str, Any]) -> dict[str, Any]:
    """根据重量(kg)和站点配置计算 SLS 跨境物流成本（支持当地币官方表与人民币线性表）。"""
    rate = max(0.0001, float(cfg.get("exchange_rate") or 1.0))
    ship_cur = cfg.get("shipping_currency") or (
        "local" if ("first_shipping_local" in cfg or cfg.get("shipping_tiers")) else "rmb"
    )
    buffer_g = max(0.0, float(cfg.get("weight_buffer_g") or 0.0))
    raw_w_g = round(max(0.0, float(weight_kg or 0.0)) * 1000.0, 4)
    w_g = (raw_w_g if raw_w_g > 0 else float(cfg.get("first_weight_g") or 50.0)) + buffer_g

    tiers = cfg.get("shipping_tiers")
    if isinstance(tiers, list) and tiers and ship_cur == "local":
        fee = 0.0
        prev_cap = 0.0
        for idx, tier in enumerate(tiers):
            up_to = tier.get("up_to_g")
            if idx == 0 and "base" in tier:
                fee = float(tier.get("base") or 0.0)
                prev_cap = float(up_to or cfg.get("first_weight_g") or 0.0)
                if up_to is not None and w_g <= prev_cap:
                    break
                continue
            if w_g <= prev_cap:
                break
            hi = w_g if up_to is None else min(w_g, float(up_to))
            if hi > prev_cap:
                step_g = max(1.0, float(tier.get("step_g") or 10.0))
                step_fee = float(tier.get("step_fee") or 0.0)
                fee += math.ceil(round((hi - prev_cap) / step_g, 6)) * step_fee
            if up_to is None or w_g <= float(up_to):
                break
            prev_cap = float(up_to)
    else:
        first_g = max(1.0, float(cfg.get("first_weight_g") or 50.0))
        step_g = max(1.0, float(cfg.get("step_weight_g") or 10.0))
        if ship_cur == "local":
            first_fee = float(cfg.get("first_shipping_local") or 0.0)
            step_fee = float(cfg.get("step_shipping_local") or 0.0)
        else:
            first_fee = float(cfg.get("first_shipping_rmb") or 0.0)
            step_fee = float(cfg.get("step_shipping_rmb") or 0.0)
        if w_g <= first_g:
            fee = first_fee
        else:
            fee = first_fee + math.ceil(round((w_g - first_g) / step_g, 6)) * step_fee

    if ship_cur == "local":
        return {
            "shipping_local": round(fee, 2),
            "shipping_rmb": round(fee / rate, 2),
            "shipping_currency": "local",
            "effective_weight_kg": round(w_g / 1000.0, 3),
        }
    return {
        "shipping_local": round(fee * rate, 2),
        "shipping_rmb": round(fee, 2),
        "shipping_currency": "rmb",
        "effective_weight_kg": round(w_g / 1000.0, 3),
    }


def calc_shipping_rmb(weight_kg: float, cfg: dict[str, Any]) -> float:
    return calc_shipping_detail(weight_kg, cfg)["shipping_rmb"]


def apply_rounding(price: float, mode: str) -> float:
    p = max(0.01, float(price))
    if mode == "int":
        return float(max(1, round(p)))
    if mode == "ceil":
        return float(max(1, math.ceil(p)))
    if mode == "dot99":
        whole = max(0, int(math.floor(p)))
        return round(whole + 0.99, 2)
    if mode == "dot90":
        whole = max(0, int(math.floor(p)))
        return round(whole + 0.90, 2)
    if mode == "k1000":
        return float(max(1000, round(p / 1000.0) * 1000))
    return round(p, 2)


def calculate_price(
    cost_rmb: float,
    weight_kg: float,
    cfg: dict[str, Any],
    orig_sell_price: float = 0.0,
) -> dict[str, Any]:
    """计算单条 SKU 定价并返回完整拆解明细。"""
    cost = max(0.0, float(cost_rmb or 0.0))
    weight = max(0.0, float(weight_kg or 0.0))
    rate = max(0.0001, float(cfg.get("exchange_rate") or 1.0))
    ship_info = calc_shipping_detail(weight, cfg)
    shipping = ship_info["shipping_rmb"]
    extra_fee = float(cfg.get("extra_fee_rmb") or 0.0)
    commission = max(0.0, min(0.8, float(cfg.get("commission_rate") or 0.0)))
    tx_fee = max(0.0, min(0.5, float(cfg.get("tx_fee_rate") or 0.0)))
    tech_fee = max(0.0, min(0.5, float(cfg.get("tech_fee_rate") or 0.0)))
    tax_rate = max(0.0, min(0.5, float(cfg.get("tax_rate") or 0.0)))
    fixed_order_local = max(0.0, float(cfg.get("fixed_order_fee_local") or 0.0))
    fixed_order_rmb = fixed_order_local / rate
    profit_rate = float(cfg.get("profit_rate") or 0.0)
    fixed_profit = float(cfg.get("fixed_profit_rmb") or 0.0)
    promo_discount = max(0.0, min(0.8, float(cfg.get("promo_discount") or 0.0)))
    mode = cfg.get("mode") or "margin"

    goods_base_rmb = cost + shipping + extra_fee
    total_base_rmb = goods_base_rmb + fixed_order_rmb
    fee_ratio = commission + tx_fee + tech_fee + tax_rate

    if mode == "custom":
        variables = {
            "cost": cost,
            "weight": weight,
            "weight_g": weight * 1000.0,
            "rate": rate,
            "shipping": shipping,
            "extra_fee": extra_fee,
            "fixed_order_fee": fixed_order_rmb,
            "commission": commission,
            "tx_fee": tx_fee,
            "tech_fee": tech_fee,
            "tax_rate": tax_rate,
            "profit_rate": profit_rate,
            "fixed_profit": fixed_profit,
            "orig_price": float(orig_sell_price or 0.0),
        }
        raw_local = eval_formula(cfg.get("custom_formula") or "", variables)
    elif mode == "markup":
        denom = max(0.05, 1.0 - fee_ratio)
        sell_rmb = (total_base_rmb * (1.0 + profit_rate) + fixed_profit) / denom
        raw_local = sell_rmb * rate
    else:  # margin (销售利润率模式)
        denom = max(0.05, 1.0 - fee_ratio - profit_rate)
        sell_rmb = (total_base_rmb + fixed_profit) / denom
        raw_local = sell_rmb * rate

    # 如果设置折前膨胀（例如前台打8折，则标价 = 折后目标价 / (1 - 0.2)）
    if promo_discount > 0:
        raw_local = raw_local / (1.0 - promo_discount)

    final_local = apply_rounding(raw_local, cfg.get("rounding") or "none")
    effective_local = final_local * (1.0 - promo_discount) if promo_discount > 0 else final_local
    revenue_rmb = effective_local / rate
    platform_fee_rmb = revenue_rmb * fee_ratio + fixed_order_rmb
    net_profit_rmb = revenue_rmb - platform_fee_rmb - goods_base_rmb
    actual_margin = (net_profit_rmb / revenue_rmb) if revenue_rmb > 0 else 0.0

    return {
        "cost_rmb": round(cost, 2),
        "weight_kg": round(weight, 3),
        "effective_weight_kg": ship_info["effective_weight_kg"],
        "shipping_rmb": round(shipping, 2),
        "shipping_local": round(ship_info["shipping_local"], 2),
        "extra_fee_rmb": round(extra_fee, 2),
        "fixed_order_rmb": round(fixed_order_rmb, 2),
        "raw_local_price": round(raw_local, 2),
        "final_price": final_local,
        "currency": cfg.get("currency") or "PHP",
        "revenue_rmb": round(revenue_rmb, 2),
        "platform_fee_rmb": round(platform_fee_rmb, 2),
        "profit_rmb": round(net_profit_rmb, 2),
        "margin_pct": round(actual_margin * 100.0, 1),
    }


def evaluate_manual_price(
    final_price: float,
    cost_rmb: float,
    weight_kg: float,
    cfg: dict[str, Any],
) -> dict[str, Any]:
    """根据用户手动指定的售价(当地币)与当前成本/重量/站点配置，精确计算藏价运费、平台费与净利润。"""
    fp = max(0.0, float(final_price or 0.0))
    cost = max(0.0, float(cost_rmb or 0.0))
    weight = max(0.0, float(weight_kg or 0.0))
    rate = max(0.0001, float(cfg.get("exchange_rate") or 1.0))
    ship_info = calc_shipping_detail(weight, cfg)
    shipping = ship_info["shipping_rmb"]
    extra_fee = float(cfg.get("extra_fee_rmb") or 0.0)
    commission = max(0.0, min(0.8, float(cfg.get("commission_rate") or 0.0)))
    tx_fee = max(0.0, min(0.5, float(cfg.get("tx_fee_rate") or 0.0)))
    tech_fee = max(0.0, min(0.5, float(cfg.get("tech_fee_rate") or 0.0)))
    tax_rate = max(0.0, min(0.5, float(cfg.get("tax_rate") or 0.0)))
    fixed_order_local = max(0.0, float(cfg.get("fixed_order_fee_local") or 0.0))
    fixed_order_rmb = fixed_order_local / rate
    promo_discount = max(0.0, min(0.8, float(cfg.get("promo_discount") or 0.0)))

    goods_base_rmb = cost + shipping + extra_fee
    fee_ratio = commission + tx_fee + tech_fee + tax_rate
    effective_local = fp * (1.0 - promo_discount) if promo_discount > 0 else fp
    revenue_rmb = effective_local / rate
    platform_fee_rmb = revenue_rmb * fee_ratio + fixed_order_rmb
    net_profit_rmb = revenue_rmb - platform_fee_rmb - goods_base_rmb
    actual_margin = (net_profit_rmb / revenue_rmb) if revenue_rmb > 0 else 0.0

    return {
        "final_price": round(fp, 2),
        "currency": cfg.get("currency") or "PHP",
        "shipping_rmb": round(shipping, 2),
        "shipping_local": round(ship_info["shipping_local"], 2),
        "effective_weight_kg": ship_info["effective_weight_kg"],
        "revenue_rmb": round(revenue_rmb, 2),
        "platform_fee_rmb": round(platform_fee_rmb, 2),
        "profit_rmb": round(net_profit_rmb, 2),
        "margin_pct": round(actual_margin * 100.0, 1),
    }
