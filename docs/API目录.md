# 妙手ERP开放平台 接口目录

共 196 个接口。基础域名 `https://openapi-erp.91miaoshou.com`，全部为 `POST` + `application/json`。
签名：`x-sign = HmacSHA256(appSecret, appSecret + path + timestamp + appKey + bodyJson + appSecret)`（小写 hex）。

## 总览

| 分类 | 接口 | 路径 |
|---|---|---|
| 商品 > 店铺 | 获取店铺数据列表 | `/open/v1/product/shop/shop/get_shop_list` |
| 商品 > 公共采集箱 | 通过货源链接采集货源 | `/open/v1/product/common_collect_box/common_collect_box/fetch_item` |
| 商品 > 公共采集箱 | 创建公共采集箱产品 | `/open/v1/product/common_collect_box/common_collect_box/add_common_collect_box_detail` |
| 商品 > 公共采集箱 | 获取公共采集箱列表 | `/open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_list` |
| 商品 > 公共采集箱 | 编辑公共采集箱产品 | `/open/v1/product/common_collect_box/common_collect_box/edit_common_collect_box_detail` |
| 商品 > 公共采集箱 | 获取公共采集箱详情 | `/open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_detail` |
| 商品 > 公共采集箱 | 批量删除公共采集箱产品 | `/open/v1/product/common_collect_box/common_collect_box/batch_delete_common_collect_box_detail` |
| 商品 > 公共采集箱 | 认领到平台采集箱 | `/open/v1/product/common_collect_box/common_collect_box/claimed` |
| 商品 > TK采集箱 > 采集箱 | 获取类目列表 | `/open/v1/product/collect_box/tiktok/collect_box/get_category_tree_by_site` |
| 商品 > TK采集箱 > 采集箱 | 获取类目属性信息 | `/open/v1/product/collect_box/tiktok/collect_box/get_category_metadata` |
| 商品 > TK采集箱 > 采集箱 | 获取店铺仓库列表 | `/open/v1/product/collect_box/tiktok/collect_box/get_shop_warehouse_list` |
| 商品 > TK采集箱 > 采集箱 | 获取制造商列表 | `/open/v1/product/collect_box/tiktok/collect_box/get_manufacturer_list` |
| 商品 > TK采集箱 > 采集箱 | 获取欧盟责任人列表 | `/open/v1/product/collect_box/tiktok/collect_box/get_responsible_person_list` |
| 商品 > TK采集箱 > 采集箱 | 认领预发布店铺 | `/open/v1/product/collect_box/tiktok/collect_box/claim_to_shop` |
| 商品 > TK采集箱 > 采集箱 | 获取采集箱列表 | `/open/v1/product/collect_box/tiktok/collect_box/search_collect_box_detail_list` |
| 商品 > TK采集箱 > 采集箱 | 获取采集箱店铺模式详情 | `/open/v1/product/collect_box/tiktok/collect_box/get_shop_collect_item_info` |
| 商品 > TK采集箱 > 采集箱 | 保存采集箱店铺模式详情 | `/open/v1/product/collect_box/tiktok/collect_box/save_shop_collect_item_info` |
| 商品 > TK采集箱 > 采集箱 | 获取采集箱站点模式详情 | `/open/v1/product/collect_box/tiktok/collect_box/get_site_collect_item_info` |
| 商品 > TK采集箱 > 采集箱 | 保存采集箱站点模式详情 | `/open/v1/product/collect_box/tiktok/collect_box/save_site_collect_item_info` |
| 商品 > TK采集箱 > 采集箱 | 产品翻译 | `/open/v1/product/collect_box/tiktok/collect_box/translate_collect_item_info` |
| 商品 > TK采集箱 > 采集箱 | AI匹配类目 | `/open/v1/product/collect_box/tiktok/collect_box/ai_match_cid_by_shop_ids` |
| 商品 > TK采集箱 > 采集箱 | 批量删除采集箱产品接口 | `/open/v1/product/collect_box/tiktok/collect_box/delete_collect_box_detail` |
| 商品 > TK采集箱 > 采集箱 | AI属性匹配 | `/open/v1/product/collect_box/tiktok/collect_box/ai_match_product_attribute` |
| 商品 > TK采集箱 > 采集箱 | 获取品牌列表 | `/open/v1/product/collect_box/tiktok/collect_box/get_brand_list` |
| 商品 > TK采集箱 > 产品发布 | 发布产品 | `/open/v1/product/collect_box/tiktok/collect_box/save_move_collect_task` |
| 商品 > TK采集箱 > 产品发布 | 发布记录列表 | `/open/v1/product/collect_box/tiktok/move_collect/search_move_collect_list` |
| 商品 > TK采集箱 > 定价模板 | 获取定价模板列表 | `/open/v1/product/collect_box/tiktok/price_template/get_price_template_list` |
| 商品 > TK采集箱 > 定价模板 | 获取各个站点的默认配置 | `/open/v1/product/collect_box/tiktok/price_template/get_site_default_setting` |
| 商品 > TEMU全托采集箱 > 产品发布 | 发布产品 | `/open/v1/product/collect_box/pddkj/move_collect/save_move_collect_task` |
| 商品 > TEMU全托采集箱 > 产品发布 | 发布记录列表 | `/open/v1/product/collect_box/pddkj/move_collect/search_move_collect_list` |
| 商品 > TEMU全托采集箱 > 车型库 | 获取车型库站点列表 | `/open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_list` |
| 商品 > TEMU全托采集箱 > 车型库 | 获取车型库站点属性结构映射 | `/open/v1/product/collect_box/pddkj/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map` |
| 商品 > TEMU全托采集箱 > 车型库 | 获取站点顶级车型节点列表 | `/open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list` |
| 商品 > TEMU全托采集箱 > 车型库 | 获取车型属性依赖树 | `/open/v1/product/collect_box/pddkj/vehicle_library/get_vehicle_library_prop_dependency_tree` |
| 商品 > TEMU全托采集箱 > 车型库 | 根据类目ID查询有车型库数据的类目列表 | `/open/v1/product/collect_box/pddkj/vehicle_library/get_has_vehicle_library_cids_by_search_cids` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取类目属性规则 | `/open/v1/product/collect_box/pddkj/collect_box/get_category_attribute_rules` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取商品基本选项 | `/open/v1/product/collect_box/pddkj/collect_box/get_item_options` |
| 商品 > TEMU全托采集箱 > 采集箱 | 创建采集箱商品 | `/open/v1/product/collect_box/pddkj/collect_box/create_collect_box_item` |
| 商品 > TEMU全托采集箱 > 采集箱 | 认领预发布店铺 | `/open/v1/product/collect_box/pddkj/collect_box/claim_to_shop` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取采集箱店铺模式详情 | `/open/v1/product/collect_box/pddkj/collect_box/get_shop_collect_item_info` |
| 商品 > TEMU全托采集箱 > 采集箱 | 保存采集箱店铺模式详情 | `/open/v1/product/collect_box/pddkj/collect_box/save_shop_collect_item_info` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取采集箱站点模式详情 | `/open/v1/product/collect_box/pddkj/collect_box/get_site_collect_item_info` |
| 商品 > TEMU全托采集箱 > 采集箱 | 保存采集箱站点模式详情 | `/open/v1/product/collect_box/pddkj/collect_box/save_site_collect_item_info` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取原产地国家列表 | `/open/v1/product/collect_box/pddkj/collect_box/get_country_short_name_and_name_map` |
| 商品 > TEMU全托采集箱 > 采集箱 | 店铺模特列表 | `/open/v1/product/collect_box/pddkj/collect_box/search_model_list` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取类目列表 | `/open/v1/product/collect_box/pddkj/collect_box/get_category_tree_by_site` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取尺码模板列表 | `/open/v1/product/collect_box/pddkj/collect_box/get_size_template_list` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取尺码表详情 | `/open/v1/product/collect_box/pddkj/collect_box/get_size_charts_by_size_template_id` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取模特分类配置 | `/open/v1/product/collect_box/pddkj/collect_box/get_model_cat_info` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取采集箱列表 | `/open/v1/product/collect_box/pddkj/collect_box/search_collect_box_detail_list` |
| 商品 > TEMU全托采集箱 > 采集箱 | 批量删除采集箱产品接口 | `/open/v1/product/collect_box/pddkj/collect_box/delete_collect_box_detail` |
| 商品 > TEMU全托采集箱 > 采集箱 | 获取需要设置净重的类目列表 | `/open/v1/product/collect_box/pddkj/collect_box/get_need_set_net_weight_cid_list` |
| 商品 > TEMU半托采集箱 > 商品发布 | 发布产品 | `/open/v1/product/collect_box/pddkj_choice/move_collect/save_move_collect_task` |
| 商品 > TEMU半托采集箱 > 商品发布 | 发布记录列表 | `/open/v1/product/collect_box/pddkj_choice/move_collect/search_move_collect_list` |
| 商品 > TEMU半托采集箱 > 车型库 | 获取车型库站点列表 | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_list` |
| 商品 > TEMU半托采集箱 > 车型库 | 获取车型库站点属性结构映射 | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map` |
| 商品 > TEMU半托采集箱 > 车型库 | 获取站点顶级车型节点列表 | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list` |
| 商品 > TEMU半托采集箱 > 车型库 | 获取车型属性依赖树 | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_vehicle_library_prop_dependency_tree` |
| 商品 > TEMU半托采集箱 > 车型库 | 根据类目ID查询有车型库数据的类目列表 | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_has_vehicle_library_cids_by_search_cids` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取类目属性规则 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_category_attribute_rules` |
| 商品 > TEMU半托采集箱 > 采集箱 | 店铺模特列表 | `/open/v1/product/collect_box/pddkj_choice/collect_box/search_model_list` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取商品基本选项 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_item_options` |
| 商品 > TEMU半托采集箱 > 采集箱 | 创建采集箱商品 | `/open/v1/product/collect_box/pddkj_choice/collect_box/create_collect_box_item` |
| 商品 > TEMU半托采集箱 > 采集箱 | 认领预发布店铺 | `/open/v1/product/collect_box/pddkj_choice/collect_box/claim_to_shop` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取采集箱站点模式详情 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_site_collect_item_info` |
| 商品 > TEMU半托采集箱 > 采集箱 | 保存采集箱店铺模式详情 | `/open/v1/product/collect_box/pddkj_choice/collect_box/save_shop_collect_item_info` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取采集箱店铺模式详情 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_collect_item_info` |
| 商品 > TEMU半托采集箱 > 采集箱 | 保存采集箱站点模式详情 | `/open/v1/product/collect_box/pddkj_choice/collect_box/save_site_collect_item_info` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取原产地国家列表 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_country_short_name_and_name_map` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取发布站点选项 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_publish_site_options` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取店铺运费模板 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_freight_template` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取店铺发货仓库（支持同步） | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_warehouse` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取类目列表 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_category_tree_by_site` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取尺码模板列表 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_size_template_list` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取尺码表详情 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_size_charts_by_size_template_id` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取模特分类配置 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_model_cat_info` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取采集箱列表 | `/open/v1/product/collect_box/pddkj_choice/collect_box/search_collect_box_detail_list` |
| 商品 > TEMU半托采集箱 > 采集箱 | 批量删除采集箱产品接口 | `/open/v1/product/collect_box/pddkj_choice/collect_box/delete_collect_box_detail` |
| 商品 > TEMU半托采集箱 > 采集箱 | 获取包装清单属性值列表 | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_goods_accessories_list` |
| 商品 > OZON采集箱 > 采集箱 | 获取采集箱编辑币种 | `/open/v1/product/collect_box/ozon/collect_box/get_account_setting_edit_currency` |
| 商品 > OZON采集箱 > 采集箱 | 获取类目列表 | `/open/v1/product/collect_box/ozon/collect_box/get_category_tree_by_site` |
| 商品 > OZON采集箱 > 采集箱 | 获取类目属性信息 | `/open/v1/product/collect_box/ozon/collect_box/get_category_attributes` |
| 商品 > OZON采集箱 > 采集箱 | 获取采集箱列表 | `/open/v1/product/collect_box/ozon/collect_box/search_collect_box_detail_list` |
| 商品 > OZON采集箱 > 采集箱 | 获取店铺仓库列表 | `/open/v1/product/collect_box/ozon/collect_box/get_shop_warehouse_info_list` |
| 商品 > OZON采集箱 > 采集箱 | 获取采集箱站点模式详情 | `/open/v1/product/collect_box/ozon/collect_box/get_site_collect_item_info` |
| 商品 > OZON采集箱 > 采集箱 | 创建采集箱站点模式数据 | `/open/v1/product/collect_box/ozon/collect_box/create_collect_box_item` |
| 商品 > OZON采集箱 > 采集箱 | 编辑采集箱站点模式数据 | `/open/v1/product/collect_box/ozon/collect_box/save_site_detail_data` |
| 商品 > OZON采集箱 > 产品发布 | 发布记录列表 | `/open/v1/product/collect_box/ozon/move_collect/search_move_collect_list` |
| 商品 > OZON采集箱 > 产品发布 | 发布产品 | `/open/v1/product/collect_box/ozon/move_collect/save_move_collect_task` |
| 商品 > Shopee采集箱 > 采集箱 | 获取站点编辑信息 | `/open/v1/product/collect_box/shopee/collect_box/get_site_detail_simple_data` |
| 商品 > Shopee采集箱 > 采集箱 | 保存站点编辑数据 | `/open/v1/product/collect_box/shopee/collect_box/save_site_detail_data` |
| 商品 > Shopee采集箱 > 采集箱 | 创建采集箱SPU（手动添加商品） | `/open/v1/product/collect_box/shopee/collect_box/create_collect_box_item` |
| 商品 > Shopee采集箱 > 采集箱 | 获取采集箱产品的源数据 | `/open/v1/product/collect_box/shopee/collect_box/get_collect_box_item_detail` |
| 商品 > Shopee采集箱 > 采集箱 | 保存采集箱产品源数据信息 | `/open/v1/product/collect_box/shopee/collect_box/save_edit_item` |
| 商品 > Shopee采集箱 > 采集箱 | 获取采集箱列表 | `/open/v1/product/collect_box/shopee/collect_box/search_collect_box_detail_list` |
| 商品 > Shopee采集箱 > 采集箱 | 获取品牌列表 | `/open/v1/product/collect_box/shopee/collect_box/get_brand_list` |
| 商品 > Shopee采集箱 > 采集箱 | 根据站点获取运费模板(物流方式) | `/open/v1/product/collect_box/shopee/collect_box/get_logistic_options_by_site` |
| 商品 > Shopee采集箱 > 采集箱 | 获取类目树 | `/open/v1/product/collect_box/shopee/collect_box/get_category_tree_by_site` |
| 商品 > Shopee采集箱 > 采集箱 | 获取类目属性信息 | `/open/v1/product/collect_box/shopee/collect_box/get_category_attributes` |
| 商品 > Shopee采集箱 > 采集箱 | 获取仓库信息列表 | `/open/v1/product/collect_box/shopee/collect_box/get_global_shop_warehouse` |
| 商品 > Shopee采集箱 > 商品发布 | 发布记录列表 | `/open/v1/product/collect_box/shopee/move_collect/search_move_collect_list` |
| 商品 > Shopee采集箱 > 商品发布 | 提交全球商品发布到店铺任务 | `/open/v1/product/collect_box/shopee/move_collect/save_move_collect_global_task` |
| 商品 > Shopee采集箱 > 商品发布 | 采集箱产品发布任务 | `/open/v1/product/collect_box/shopee/move_collect/save_move_collect_task` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 全球产品搜索 | `/open/v1/product/item/shopee_global/item/search_item_list` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 全球产品详情（返回官方 | `/open/v1/product/item/shopee_global/item/get_item_detail` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 保存产品编辑 | `/open/v1/product/item/shopee_global/item/save_edit_item` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 获取属性列表 | `/open/v1/product/item/shopee_global/item/get_attribute_list` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 获取全球店铺类目尺寸模板列表 | `/open/v1/product/item/shopee_global/item/get_shop_id_and_size_chart_list_map` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 上传商品视频 | `/open/v1/product/item/shopee_global/item/upload_item_video` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 同步产品 | `/open/v1/product/item/shopee_global/item/rsync_item_single` |
| 商品 > 在线产品管理 > Shopee全球在线产品管理 | 全球产品删除 | `/open/v1/product/item/shopee_global/item/delete_item` |
| 商品 > Mercadolibre采集箱 > 发布产品 | 发布产品 | `/open/v1/product/collect_box/mercadolibre/move_collect/save_move_collect_task` |
| 商品 > Mercadolibre采集箱 > 发布产品 | 发布记录列表 | `/open/v1/product/collect_box/mercadolibre/move_collect/search_move_collect_list` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取类目属性规则 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_category_attribute_rules` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取类目配置 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_category_setting` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取尺码表domain列表 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_domain_list` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取尺码表表头和主属性信息 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_attribute_info` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取尺码表所需填写属性信息 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_need_attribute_info` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取授权站点和名称映射 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_auth_site_and_site_name_map` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取商品基本选项 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_item_options` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 查询尺码表模板列表 | `/open/v1/product/collect_box/mercadolibre/collect_box/search_size_chart_template` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取采集箱详情 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_site_collect_item_info` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 创建采集箱商品 | `/open/v1/product/collect_box/mercadolibre/collect_box/create_collect_box_item` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 保存采集箱站点详情 | `/open/v1/product/collect_box/mercadolibre/collect_box/save_site_collect_item_info` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 同步店铺尺码表 | `/open/v1/product/collect_box/mercadolibre/collect_box/rsync_size_chart_template` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取采集箱列表 | `/open/v1/product/collect_box/mercadolibre/collect_box/search_collect_box_detailList` |
| 商品 > Mercadolibre采集箱 > 采集箱 | 获取类目列表 | `/open/v1/product/collect_box/mercadolibre/collect_box/get_category_tree_by_site` |
| 商品 > AI公共服务 > 图片处理 | AI白底图 | `/open/v1/product/picture/matting/auto_ai_matting_multi` |
| 商品 > AI公共服务 > 图片处理 | AI智能消除 | `/open/v1/product/common/image_removal/remove_image` |
| 商品 > AI公共服务 > 图片处理 | 搜索水印列表 | `/open/v1/product/item/tiktok/watermark/search_watermark_list` |
| 商品 > AI公共服务 > 图片处理 | 图片打水印 | `/open/v1/product/item/tiktok/watermark/watermark_images` |
| 商品 > AI公共服务 > 图片处理 | 获取支持的翻译语言配置 | `/open/v1/product/common/translate/get_support_language_config` |
| 商品 > AI公共服务 > 图片处理 | 图片翻译 | `/open/v1/product/common/translate/translate_image` |
| 商品 > AI公共服务 > AI润色 | AI生成产品信息（标题/描述） | `/open/v1/product/common/open_ai/generate_product_info` |
| 商品 > AI公共服务 > AI润色 | AI生成支持的语言map | `/open/v1/product/common/open_ai/get_language_name_code_map` |
| 商品 > AI公共服务 > AI润色 | 获取支持的AI名称列表 | `/open/v1/product/common/open_ai/get_generate_product_info_support_ai_name_list` |
| 商品 > AI公共服务 > AI润色 | AI润色销售规格 | `/open/v1/product/common/open_ai/generate_sku_spec_name` |
| 商品 > 图片空间 | 通过图片URL上传图片到图片空间 | `/open/v1/product/picture/picture_space/upload_picture_link` |
| 包裹 > 履约 > 基础管理 | 获取当前账号有效的线下物流列表 | `/open/v1/order/logistics_agent/manage/get_enable_offline_product_list` |
| 包裹 > 履约 > 基础管理 | 获取当前包裹有效的线上物流列表 | `/open/v1/order/logistics_agent/manage/get_enable_online_product_list` |
| 包裹 > 售后 | 获取退货退款列表 | `/open/v1/order/after_sales/fetch/order_return_list` |
| 包裹 > 售后 | 获取取消订单列表 | `/open/v1/order/after_sales/fetch/order_cancel_list` |
| 包裹 > 包裹 > 运单 | 申请运单号 | `/open/v1/order/package/logistics/tracking_no/apply` |
| 包裹 > 包裹 > 运单 | 批量申请运单号 | `/open/v1/order/package/logistics/tracking_no/batch_apply` |
| 包裹 > 包裹 > 运单 | 设置包裹物流 | `/open/v1/order/package/logistics/tracking_no/save_logistics_agent_product` |
| 包裹 > 包裹 > 运单 | 获取包裹物流轨迹 | `/open/v1/order/package/logistics/tracking/get_tracking_list` |
| 包裹 > 包裹 > 运单 | 获取运单面单 | `/open/v1/order/package/logistics/waybill/get_waybill` |
| 包裹 > 包裹 > 运单 | 批量获取面单 | `/open/v1/order/package/logistics/waybill/batch_get_waybill` |
| 包裹 > 包裹 > 基础信息修改 | 保存包裹本地备注 | `/open/v1/order/package/base_info_modify/saveOrderPackageAppNote` |
| 包裹 > 包裹 > 基础信息修改 | 保存包裹商家备注 | `/open/v1/order/package/base_info_modify/saveSellerNote` |
| 包裹 > 包裹 > 获取包裹 | 获取订单包裹详情 | `/open/v1/order/package/fetch/get_package_info` |
| 包裹 > 包裹 > 获取包裹 | 获取订单包裹列表 | `/open/v1/order/package/fetch/search_package_list` |
| 包裹 > 包裹 > 发货 | 包裹发货 | `/open/v1/order/package/ship_package/ship_packages` |
| 包裹 > 采购记录 | 采购记录列表 | `/open/v1/order/purchase_order/purchase_record/search_list` |
| 包裹 > 采购记录 | 采购记录详情 | `/open/v1/order/purchase_order/purchase_record/get_detail` |
| 采购 > 采购单 | 添加采购单 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order` |
| 采购 > 采购单 | 创建1688采购单 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order` |
| 采购 > 采购单 | 编辑采购单 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order` |
| 采购 > 采购单 | 采购单动手填写运单号 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order_shipping` |
| 采购 > 采购单 | 采购单修改运单信息 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_shipping` |
| 采购 > 采购单 | 采购单更新平台运单信息 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_outer_shipping` |
| 采购 > 采购单 | 取消采购单 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/cancel_goods_purchase_order` |
| 采购 > 采购单 | 标记采购单结束 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/finish_goods_purchase_order` |
| 采购 > 采购单 | 向1688下单 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order_by_goods_purchase_order_ids` |
| 采购 > 采购单 | 获取采购单列表 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/fetch/search_goods_purchase_order_page` |
| 采购 > 采购单 | 签收记录列表 | `/open/v1/ewm/goods_purchase_order/goods_purchase_order_receive/fetch/search_goods_purchase_order_receive_page` |
| 采购 > 采购单 | 根据货源链接获取1688商品SKU列表 | `/open/v1/ewm/supplier/fetch/get_ali1688_item_by_source_url` |
| 采购 > 采购单 | 获取缺货、备货建议列表 | `/open/v1/ewm/goods_purchase_order/goods_purchase_suggest/fetch/search_goods_purchase_suggest_page` |
| 采购 > 供应商 | 获取供应商列表 | `/open/v1/ewm/supplier/fetch/search_supplier_page` |
| 采购 > 供应商 | 获取供应商信息 | `/open/v1/ewm/supplier/fetch/get_supplier_info` |
| 采购 > 供应商 | 获取供应商类型列表 | `/open/v1/ewm/supplier/fetch/get_supplier_platform_list` |
| 采购 > 供应商 | 修改供应商 | `/open/v1/ewm/supplier/operate/edit_supplier` |
| 采购 > 供应商 | 创建供应商 | `/open/v1/ewm/supplier/operate/add_supplier` |
| 仓储 > 商品 > 商品 | 获取多规格商品列表 | `/open/v1/ewm/goods/goods/fetch/search_goods_page` |
| 仓储 > 商品 > 商品 | 获取商品详情 | `/open/v1/ewm/goods/goods/fetch/get_goods_info` |
| 仓储 > 商品 > 商品 | 添加商品 | `/open/v1/ewm/goods/goods/operate/add_goods` |
| 仓储 > 商品 > 商品 | 修改商品 | `/open/v1/ewm/goods/goods/operate/edit_goods` |
| 仓储 > 商品 > 商品 | 安全库存批量设置 | `/open/v1/ewm/goods/goods/operate/batch_save_goods_suggest_config` |
| 仓储 > 商品 > 商品品牌 | 获取列表 | `/open/v1/ewm/goods/goods_brand/fetch/search_goods_brand_page` |
| 仓储 > 商品 > 商品分组 | 获取商品分组列表 | `/open/v1/ewm/goods/goods_group/fetch/get_goods_group_list` |
| 仓储 > 商品 > 商品sku | 获取商品SKU列表 | `/open/v1/ewm/goods/goods_sku/fetch/search_goods_sku_page` |
| 仓储 > 商品包材 | 获取列表 | `/open/v1/ewm/packaging/fetch/search_packaging_page` |
| 仓储 > 数据统计 > 销售数据 | 获取商品销售数据列表 | `/open/v1/ewm/stat/goods_sale_data/fetch/search_goods_sale_data_page` |
| 仓储 > 数据统计 > 商品周转分析 | 获取商品周转数据列表 | `/open/v1/ewm/stat/goods_turnover_data/fetch/search_goods_turnover_data_page` |
| 仓储 > 库存 > 三方仓sku库存 | 获取三方仓商品库存列表 | `/open/v1/ewm/storage/third_warehouse/fetch/search_third_goods_sku_warehouse_page` |
| 仓储 > 库存 > 自营仓库存 | 获取自营仓商品库存列表 | `/open/v1/ewm/storage/warehouse/fetch/search_goods_sku_warehouse_page` |
| 仓储 > 库存 > 自营仓库存 | 获取商品SKU安全库存列表 | `/open/v1/ewm/storage/warehouse/fetch/get_goods_sku_safe_stock_num_list` |
| 仓储 > 仓库 > 自营仓仓库 | 获取供应商仓库列表 | `/open/v1/ewm/warehouse/fetch/supplier_warehouse_list` |
| 仓储 > 仓库 > 自营仓仓库 | 获取自营仓仓库列表 | `/open/v1/ewm/warehouse/fetch/search_warehouse_page` |
| 仓储 > 仓库 > 三方仓仓库 | 获取三方仓授权列表 | `/open/v1/ewm/third_warehouse/fetch/search_third_provider_auth_page` |
| 仓储 > 仓库 > 三方仓仓库 | 获取平台仓库列表 | `/open/v1/ewm/third_warehouse/fetch/search_platform_warehouse_page` |
| 仓储 > 出入库 | 查询出入库记录列表 | `/open/v1/ewm/goods_out_in/fetch/search_goods_sku_warehouse_log_page` |
| 仓储 > 出入库 | 新建入库申请单 | `/open/v1/ewm/goods_out_in/operate/add_in_apply_order` |
| 仓储 > 出入库 | 新建出库申请单 | `/open/v1/ewm/goods_out_in/operate/add_out_apply_order` |
| 货源账号 | 获取货源账号列表 | `/open/v1/resell_account/fetch/search_reseller_account_page` |
| 货源账号 | 获取账号地址列表 | `/open/v1/resell_account/fetch/get_reseller_account_address_list` |

## 接口详情

### 商品 > 店铺

#### 获取店铺数据列表

`POST /open/v1/product/shop/shop/get_shop_list`  (文档: api-446814596)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platform` | string | 是 | 平台（TK普通店铺 = tiktok，TK全球店铺 = tiktokGlobal，TEMU全托=pddkj，TEMU半托=pddkjChoice，虾皮=shopee，虾皮全球=shopeeGlobal，美客多=mercadolibre，Ozon = ozon） |
| `site` | string | 是 | TK站点：站点（印尼 = ID, 越南 = VN, 泰国 = TH, 马来 = MY, 菲律宾 = PH, 巴西 = BR, 墨西哥 = MX, 西班牙 = ES, 法国 = FR, 英国 = GB, 全球 = TIKTOKGLOBAL, 全球 - 美国 = TIKTOKGLOBALUS, 欧盟 = TIKTOKGLOBALEU, 美国 = US, 德国 = DE, 意大利 = IT, 日本 = JP） TEMU全托：站点 PDDKJ TEMU半托：站点 PDDKJCHOICE 虾皮站点：站点（印尼 = ID, 台湾 = TW, 越南 = VN, 泰国 = TH, 马来西亚 = MY, 新加坡 = SG, 菲律宾 = PH, 巴西 = BR, 墨西哥 = MX, 智利 = CL, 哥伦比亚 = CO, 波兰 = PL, 西班牙 = ES, 法国 = FR, 阿根廷 = AR） 虾皮全球站点：站点（全球 = SHOPEEGLOBAL）美客多站点:传统模式=CBT,新UP发品模式=UP Ozon站点：站点 OZON  |
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:100 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopList` | array<object> | 店铺列表 |
| `shopList[].shopId` | integer | 店铺ID |
| `shopList[].site` | string | 站点 |
| `shopList[].siteName` | string | 站点名称 |
| `shopList[].platformShopName` | string | 平台店铺名称 |
| `shopList[].shopNick` | string | 店铺别名 |
| `shopList[].platform` | string | 平台 |
| `shopList[].parentShopId` | integer | 全球主店铺ID |
| `shopList[].isCb` | integer | 是否是跨境店铺 |
| `shopList[].isCnsc` | integer | 是否是全球店铺 |
| `shopList[].status` | string | 店铺状态 |
| `shopList[].gmtExpire` | string | 过期时间 |
| `shopList[].gmtLastAuth` | string | 最后授权时间 |

### 商品 > 公共采集箱

#### 通过货源链接采集货源

`POST /open/v1/product/common_collect_box/common_collect_box/fetch_item`  (文档: api-446814581)

**必填**：`collectLinks` (string[])

> 🔴 **高危**：不存在的链接也会 `success` 并采到**无关的真实商品**。采集前务必自行校验链接有效性。

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectLinks` | array<string> |  | （见接口说明） |

#### 创建公共采集箱产品

`POST /open/v1/product/common_collect_box/common_collect_box/add_common_collect_box_detail`  (文档: api-446814585)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | 是 | 产品标题 |
| `itemNum` | string |  | 产品主编号 |
| `notesText` | string |  | 简易描述 |
| `notes` | string |  | 详细描述（富文本格式） |
| `sourceAttrs` | array<object> |  | 属性列表 |
| `sourceAttrs[].name` | string |  | 属性名 |
| `sourceAttrs[].value` | string |  | 属性值 |
| `price` | number |  | SPU货源价格，币种CNY，单规格的时候必填 max:99999.99 |
| `stock` | integer |  | 总库存 max:99999 |
| `imgUrls` | array<string> |  | 图片URL列表 |
| `weight` | number |  | 重量(kg) max:99999.99 |
| `packageLength` | number |  | 包装长度(cm) max:99999 |
| `packageWidth` | number |  | 包装宽度(cm) max:99999 |
| `packageHeight` | number |  | 包装高度(cm) max:99999 |
| `colorPropName` | string |  | 颜色属性名 |
| `colorMap` | object |  | 颜色Map（key=颜色值，value=颜色条目） |
| `sizePropName` | string |  | 尺码属性名 |
| `sizeMap` | object |  | 尺码Map（key=尺码值，value=尺码条目） |
| `saleProp3Name` | string |  | 第三销售属性名 |
| `saleProp3Map` | object |  | 第三销售属性Map（key=属性ID，value=属性条目） |
| `skuMap` | object |  | SKU Map，key为SKU规格组合串，格式为「;颜色值;尺码值;」（分号分隔，首尾带分号），value为SKU数据 |
| `sizeChart` | string |  | 尺码表URL |
| `mainImgVideoUrl` | string |  | 主图视频URL |
| `mainImgAppVideoId` | string |  | 主图APP视频ID |
| `productCertifications` | array<object> |  | 产品认证列表 |
| `productCertifications[].fileName` | string |  | 文件名称 |
| `productCertifications[].fileUrl` | string |  | 文件URL |
| `guideInfo` | object |  | 说明书信息 |
| `guideInfo.productGuideFileName` | string |  | 文件名称 |
| `guideInfo.productGuideFileUrl` | string |  | 文件URL |
| `sourceList` | array<object> |  | 货源信息列表 |
| `sourceList[].remark` | string |  | 备注 |
| `sourceList[].sourceItemId` | string |  | 来源商品ID |
| `sourceList[].source` | string |  | 来源平台 |
| `sourceList[].sourceSite` | string |  | 来源站点 |
| `sourceList[].sourceItemUrl` | string |  | 来源商品链接 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `commonCollectBoxDetailId` | integer | 公共采集箱ID |

#### 获取公共采集箱列表

`POST /open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_list`  (文档: api-446814582)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer |  | 当前页码 |
| `pageSize` | integer |  | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.tabPaneName` | string |  | 状态(all-全部、noClaimed-未认领、claimed-已认领、collectFail-采集失败、collectSuccess-采集成功) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `detailList` | array<object> | 列表页数据列表 |
| `detailList[].commonCollectBoxDetailId` | integer | 公共采集箱详情ID |
| `detailList[].appAccountId` | integer | 主账号ID |
| `detailList[].subAppAccountId` | integer | 子账号ID |
| `detailList[].itemNum` | string | 货号 |
| `detailList[].title` | string | 标题 |
| `detailList[].thumbnail` | string | 主图缩略图 |
| `detailList[].price` | number | 价格 |
| `detailList[].minSkuPrice` | number | 最低SKU价格 |
| `detailList[].maxSkuPrice` | number | 最高SKU价格 |
| `detailList[].stock` | integer | 库存 |
| `detailList[].remark` | string | 备注 |
| `detailList[].status` | string | 状态 |
| `detailList[].reason` | string | 失败原因 |
| `detailList[].gmtCreate` | string | 创建时间 |
| `detailList[].gmtModified` | string | 修改时间 |
| `detailList[].weight` | number | 重量 |
| `detailList[].maxSkuWeight` | number | 最高SKU重量 |
| `detailList[].minSkuWeight` | number | 最低SKU重量 |
| `detailList[].commonCollectBoxGroupId` | integer | 采集箱分组ID |
| `detailList[].commonCollectBoxGroupName` | string | 采集箱分组名称 |
| `detailList[].sourceList` | array<object> | 来源信息列表 |
| `detailList[].sourceList[].remark` | string | 备注 |
| `detailList[].sourceList[].sourceItemId` | string | 来源商品ID |
| `detailList[].sourceList[].source` | string | 来源平台 |
| `detailList[].sourceList[].sourceSite` | string | 来源站点 |
| `detailList[].sourceList[].sourceItemUrl` | string | 来源商品链接 |
| `detailList[].ownerSubAccountAliasName` | string | 子账号别名 |
| `detailList[].listThumbnail` | string | 列表缩略图 |
| `detailList[].isMark` | string | 是否标记 |
| `total` | integer | 总数 |
| `isCommonCollectHuger` | boolean | 是否数量巨大 |

#### 编辑公共采集箱产品

`POST /open/v1/product/common_collect_box/common_collect_box/edit_common_collect_box_detail`  (文档: api-446814586)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailId` | integer | 是 | 公共采集箱ID |
| `editCommonCollectBoxDetail` | object | 是 | 公共采集箱详情数据 |
| `editCommonCollectBoxDetail.title` | string | 是 | 产品标题 |
| `editCommonCollectBoxDetail.itemNum` | string |  | 产品主编号 |
| `editCommonCollectBoxDetail.notesText` | string |  | 简易描述 |
| `editCommonCollectBoxDetail.notes` | string |  | 详细描述（富文本格式） |
| `editCommonCollectBoxDetail.sourceAttrs` | array<object> |  | 属性列表 |
| `editCommonCollectBoxDetail.sourceAttrs[].name` | string |  | 属性名 |
| `editCommonCollectBoxDetail.sourceAttrs[].value` | string |  | 属性值 |
| `editCommonCollectBoxDetail.price` | number |  | SPU货源价格，币种CNY，单规格的时候必填 max:99999.99 |
| `editCommonCollectBoxDetail.stock` | integer |  | 总库存 max:99999 |
| `editCommonCollectBoxDetail.imgUrls` | array<string> |  | 图片URL列表 |
| `editCommonCollectBoxDetail.weight` | number |  | 重量(kg) max:99999.99 |
| `editCommonCollectBoxDetail.packageLength` | number |  | 包装长度(cm) max:99999 |
| `editCommonCollectBoxDetail.packageWidth` | number |  | 包装宽度(cm) max:99999 |
| `editCommonCollectBoxDetail.packageHeight` | number |  | 包装高度(cm) max:99999 |
| `editCommonCollectBoxDetail.colorPropName` | string |  | 颜色属性名 |
| `editCommonCollectBoxDetail.colorMap` | object |  | 颜色Map（key=颜色值，value=颜色条目） |
| `editCommonCollectBoxDetail.sizePropName` | string |  | 尺码属性名 |
| `editCommonCollectBoxDetail.sizeMap` | object |  | 尺码Map（key=尺码值，value=尺码条目） |
| `editCommonCollectBoxDetail.saleProp3Name` | string |  | 第三销售属性名 |
| `editCommonCollectBoxDetail.saleProp3Map` | object |  | 第三销售属性Map（key=属性ID，value=属性条目） |
| `editCommonCollectBoxDetail.skuMap` | object |  | SKU Map，key为SKU规格组合串，格式为「;颜色值;尺码值;」（分号分隔，首尾带分号），value为SKU数据 |
| `editCommonCollectBoxDetail.sizeChart` | string |  | 尺码表URL |
| `editCommonCollectBoxDetail.mainImgVideoUrl` | string |  | 主图视频URL |
| `editCommonCollectBoxDetail.mainImgAppVideoId` | string |  | 主图APP视频ID |
| `editCommonCollectBoxDetail.productCertifications` | array<object> |  | 产品认证列表 |
| `editCommonCollectBoxDetail.productCertifications[].fileName` | string |  | 文件名称 |
| `editCommonCollectBoxDetail.productCertifications[].fileUrl` | string |  | 文件URL |
| `editCommonCollectBoxDetail.guideInfo` | object |  | 说明书信息 |
| `editCommonCollectBoxDetail.guideInfo.productGuideFileName` | string |  | 文件名称 |
| `editCommonCollectBoxDetail.guideInfo.productGuideFileUrl` | string |  | 文件URL |
| `editCommonCollectBoxDetail.sourceList` | array<object> |  | 货源信息列表 |
| `editCommonCollectBoxDetail.sourceList[].remark` | string |  | 备注 |
| `editCommonCollectBoxDetail.sourceList[].sourceItemId` | string |  | 来源商品ID |
| `editCommonCollectBoxDetail.sourceList[].source` | string |  | 来源平台 |
| `editCommonCollectBoxDetail.sourceList[].sourceSite` | string |  | 来源站点 |
| `editCommonCollectBoxDetail.sourceList[].sourceItemUrl` | string |  | 来源商品链接 |
| `ossMd5` | string | 是 | 公共采集箱详情OssMd5标识 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string | 公共采集箱详情OssMd5标识 |

#### 获取公共采集箱详情

`POST /open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_detail`  (文档: api-446814583)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailId` | integer | 是 | 公共采集箱ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `editCommonCollectBoxDetail` | object | 公共采集箱详情 |
| `editCommonCollectBoxDetail.commonCollectBoxDetailId` | integer | 公共采集箱ID |
| `editCommonCollectBoxDetail.title` | string | 产品标题 |
| `editCommonCollectBoxDetail.itemNum` | string | 产品主编号 |
| `editCommonCollectBoxDetail.notesText` | string | 简易描述 |
| `editCommonCollectBoxDetail.notes` | string | 详细描述 |
| `editCommonCollectBoxDetail.cateList` | array<string> | 类目列表 |
| `editCommonCollectBoxDetail.sourceAttrs` | array<object> | 属性列表 |
| `editCommonCollectBoxDetail.sourceAttrs[].name` | string | 属性名 |
| `editCommonCollectBoxDetail.sourceAttrs[].value` | string | 属性值 |
| `editCommonCollectBoxDetail.price` | number | SPU货源价格 |
| `editCommonCollectBoxDetail.stock` | integer | 总库存 |
| `editCommonCollectBoxDetail.imgUrls` | array<string> | 图片URL列表 |
| `editCommonCollectBoxDetail.colorMap` | object | 颜色Map（key=颜色值，value=颜色条目） |
| `editCommonCollectBoxDetail.sizeMap` | object | 尺码Map（key=尺码值，value=尺码条目） |
| `editCommonCollectBoxDetail.skuMap` | object | SKU Map（key=SKU规格组合串，value=SKU条目） |
| `editCommonCollectBoxDetail.weight` | number | 重量(kg) |
| `editCommonCollectBoxDetail.packageLength` | number | 包装长度(cm) |
| `editCommonCollectBoxDetail.packageWidth` | number | 包装宽度(cm) |
| `editCommonCollectBoxDetail.packageHeight` | number | 包装高度(cm) |
| `editCommonCollectBoxDetail.colorPropName` | string | 颜色属性名（对应 sourceAttrs 中的 name） |
| `editCommonCollectBoxDetail.sizePropName` | string | 尺码属性名（对应 sourceAttrs 中的 name） |
| `editCommonCollectBoxDetail.saleProp3Name` | string | 第三销售属性名 |
| `editCommonCollectBoxDetail.saleProp3Map` | object | 第三销售属性Map（key=属性ID，value=属性条目） |
| `editCommonCollectBoxDetail.sizeChart` | string | 尺码表URL |
| `editCommonCollectBoxDetail.mainImgVideoUrl` | string | 主图视频URL |
| `editCommonCollectBoxDetail.mainImgAppVideoId` | string | 主图APP视频ID |
| `editCommonCollectBoxDetail.productCertifications` | array<object> | 产品认证列表 |
| `editCommonCollectBoxDetail.productCertifications[].fileName` | string | 文件名称 |
| `editCommonCollectBoxDetail.productCertifications[].fileUrl` | string | 文件URL |
| `editCommonCollectBoxDetail.guideInfo` | object | 说明书信息 |
| `editCommonCollectBoxDetail.guideInfo.productGuideFileName` | string | 文件名称 |
| `editCommonCollectBoxDetail.guideInfo.productGuideFileUrl` | string | 文件URL |
| `editCommonCollectBoxDetail.sourceMataInfo` | object | 货源元信息 |
| `editCommonCollectBoxDetail.sourceList` | array<object> | 货源信息列表 |
| `editCommonCollectBoxDetail.sourceList[].remark` | string | 备注 |
| `editCommonCollectBoxDetail.sourceList[].sourceItemId` | string | 来源商品ID |
| `editCommonCollectBoxDetail.sourceList[].source` | string | 来源平台 |
| `editCommonCollectBoxDetail.sourceList[].sourceSite` | string | 来源站点 |
| `editCommonCollectBoxDetail.sourceList[].sourceItemUrl` | string | 来源商品链接 |
| … | | 共 42 个字段，详见 openapi.json |

#### 批量删除公共采集箱产品

`POST /open/v1/product/common_collect_box/common_collect_box/batch_delete_common_collect_box_detail`  (文档: api-446814584)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailIds` | array<integer> | 是 | 公共采集箱ID列表 |

#### 认领到平台采集箱

`POST /open/v1/product/common_collect_box/common_collect_box/claimed`  (文档: api-446814587)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailSerialNumberPlatformList` | array<object> | 是 | 认领数据列表 |
| `detailSerialNumberPlatformList[].detailId` | integer | 是 | 公共采集箱ID |
| `detailSerialNumberPlatformList[].platform` | string | 是 | 认领的平台(TK-tiktok, temu全托-pddkj, temu半托-pddkjChoice, 虾皮-shopee, ozon-ozon,美客多-mercadolibre) |
| `detailSerialNumberPlatformList[].serialNumber` | integer | 是 | 序列号（默认传1） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `platformCollectBoxDetailIdMap` | object | 各平台采集箱详情ID映射 key: 平台名（如 tiktok），value: collectBoxId => detailId 的映射 |

### 商品 > TK采集箱 > 采集箱

#### 获取类目列表

`POST /open/v1/product/collect_box/tiktok/collect_box/get_category_tree_by_site`  (文档: api-446814588)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cateTree` | object | 分类树 Map（key=cid, value=分类节点） |

#### 获取类目属性信息

`POST /open/v1/product/collect_box/tiktok/collect_box/get_category_metadata`  (文档: api-446814589)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string |  | 站点(shopIds为空时必传) |
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array<integer> |  | 店铺ID列表 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `categoryMetadata` | object | 分类元数据 |
| `categoryMetadata.categoryConfig` | object | 分类配置 |
| `categoryMetadata.categoryConfig.isSuppSizechart` | string | 是否支持尺码表 |
| `categoryMetadata.categoryConfig.isSuppCod` | boolean | 是否支持货到付款 |
| `categoryMetadata.categoryConfig.productCertifications` | array<object> | 商品认证列表 |
| `categoryMetadata.categoryConfig.productCertifications[].documentDetails` | string | 认证文件说明 |
| `categoryMetadata.categoryConfig.productCertifications[].id` | string | 认证ID |
| `categoryMetadata.categoryConfig.productCertifications[].isRequired` | boolean | 是否必填 |
| `categoryMetadata.categoryConfig.productCertifications[].name` | string | 认证名称 |
| `categoryMetadata.categoryConfig.productCertifications[].sampleImageUrl` | string | 示例图片URL |
| `categoryMetadata.categoryConfig.productCertifications[].isMandatory` | boolean | 是否强制要求 |
| `categoryMetadata.categoryConfig.productCertifications[].requirementConditions` | array<object> | 需求条件列表 |
| `categoryMetadata.categoryConfig.productCertifications[].requirementConditions[].attributeId` | string | 属性ID |
| `categoryMetadata.categoryConfig.productCertifications[].requirementConditions[].attributeValueId` | string | 属性值ID |
| `categoryMetadata.categoryConfig.productCertifications[].requirementConditions[].conditionType` | string | 条件类型 |
| `categoryMetadata.categoryConfig.isSupportExemptionIdentifierCode` | string | 是否支持豁免标识码 |
| `categoryMetadata.categoryConfig.sizeChartIsSupported` | string | 尺码表是否支持 |
| `categoryMetadata.categoryConfig.sizeChartIsRequired` | string | 尺码表是否必填 |
| `categoryMetadata.categoryConfig.codIsSupported` | string | 货到付款是否支持 |
| `categoryMetadata.categoryConfig.packageDimensionIsRequired` | string | 包装尺寸是否必填 |
| `categoryMetadata.categoryConfig.eprIsRequired` | string | EPR是否必填 |
| `categoryMetadata.categoryConfig.responsiblePersonIsRequired` | string | 责任人是否必填 |
| `categoryMetadata.categoryConfig.manufacturerIsRequired` | string | 制造商是否必填 |
| `categoryMetadata.categoryConfig.isSizeChartMandatory` | string | 尺码表是否强制 |
| `categoryMetadata.categorySaleAttrList` | array<object> | 销售属性列表 |
| `categoryMetadata.categorySaleAttrList[].attrId` | string | 属性ID |
| `categoryMetadata.categorySaleAttrList[].name` | string | 属性名称（英文） |
| `categoryMetadata.categorySaleAttrList[].attributeNameAlias` | string | 属性名称别名（中文） |
| `categoryMetadata.categorySaleAttrList[].attributeType` | integer | 属性类型 |
| `categoryMetadata.categorySaleAttrList[].isMandatory` | boolean | 是否必填 |
| `categoryMetadata.categorySaleAttrList[].isMultipleSelected` | boolean | 是否可多选 |
| `categoryMetadata.categorySaleAttrList[].isCustomized` | boolean | 是否可自定义 |
| `categoryMetadata.categorySaleAttrList[].valueDataFormat` | object | 值数据格式 |
| `categoryMetadata.categorySaleAttrList[].isCertificationAttr` | boolean | 是否认证属性 |
| `categoryMetadata.categorySaleAttrList[].requirementConditions` | object | 需求条件 |
| `categoryMetadata.categorySaleAttrList[].valueIdAndRequiredAttrIdsMap` | object | 值ID与必填属性ID映射 |
| `categoryMetadata.categorySaleAttrList[].valueIdAndRequiredCertificationIdsMap` | object | 值ID与必填认证ID映射 |
| `categoryMetadata.categorySaleAttrList[].values` | array<object> | 属性值列表 |
| `categoryMetadata.categorySaleAttrList[].values[].id` | string | 属性值ID |
| `categoryMetadata.categorySaleAttrList[].values[].name` | string | 属性值名称（英文） |
| … | | 共 62 个字段，详见 openapi.json |

#### 获取店铺仓库列表

`POST /open/v1/product/collect_box/tiktok/collect_box/get_shop_warehouse_list`  (文档: api-446814590)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopWarehouseList` | array<object> | 店铺仓库列表 |
| `shopWarehouseList[].shopId` | integer | 店铺ID |
| `shopWarehouseList[].shopName` | string | 店铺名称 |
| `shopWarehouseList[].platform` | string | 平台 |
| `shopWarehouseList[].site` | string | 站点 |
| `shopWarehouseList[].warehouseList` | array<object> | 仓库列表 |
| `shopWarehouseList[].warehouseList[].shopId` | string | 店铺ID |
| `shopWarehouseList[].warehouseList[].warehouseId` | string | 仓库ID |
| `shopWarehouseList[].warehouseList[].warehouseName` | string | 仓库名称 |
| `shopWarehouseList[].warehouseList[].warehouseSubType` | string | 仓库子类型 |
| `shopWarehouseList[].warehouseList[].warehouseEffectStatus` | string | 仓库生效状态 |
| `shopWarehouseList[].warehouseList[].isDefault` | string | 是否默认仓库 |
| `shopWarehouseList[].warehouseList[].inventoryRule` | object | 库存规则 |
| `shopWarehouseList[].warehouseList[].inventoryRule.allocationMode` | string | 库存分配模式 |
| `shopWarehouseList[].warehouseList[].inventoryRule.associatedWarehouses` | array<object> | 关联仓库列表 |
| `shopWarehouseList[].warehouseList[].inventoryRule.associatedWarehouses[].region` | string | 区域 |
| `shopWarehouseList[].warehouseList[].inventoryRule.associatedWarehouses[].warehouseId` | string | 仓库ID |

#### 获取制造商列表

`POST /open/v1/product/collect_box/tiktok/collect_box/get_manufacturer_list`  (文档: api-449869292)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `refresh` | integer | 是 | 是否重新刷新数据（0=否，1=是） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `manufacturerList` | array<object> | 制造商列表 |
| `manufacturerList[].id` | string | 制造商ID |
| `manufacturerList[].name` | string | 制造商名称 |

#### 获取欧盟责任人列表

`POST /open/v1/product/collect_box/tiktok/collect_box/get_responsible_person_list`  (文档: api-449869293)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `refresh` | integer | 是 | 是否重新刷新数据（0=否，1=是） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `responsiblePersonList` | array<object> | 欧盟责任人列表 |
| `responsiblePersonList[].id` | string | 欧盟责任人ID |
| `responsiblePersonList[].name` | string | 欧盟责任人名称 |

#### 认领预发布店铺

`POST /open/v1/product/collect_box/tiktok/collect_box/claim_to_shop`  (文档: api-446814594)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

#### 获取采集箱列表

`POST /open/v1/product/collect_box/tiktok/collect_box/search_collect_box_detail_list`  (文档: api-446814591)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer |  | 当前页码 |
| `pageSize` | integer |  | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `detailList` | array<object> | 采集箱数据列表 |
| `detailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `detailList[].itemNum` | string | 商品编号 |
| `detailList[].stock` | string | 库存 |
| `detailList[].price` | string | 价格 |
| `detailList[].thumbnail` | string | 缩略图 |
| `detailList[].gmtCreate` | string | 创建时间 |
| `detailList[].editModel` | string | 编辑模式 |
| `detailList[].commonCollectBoxDetailId` | string | 公共采集箱详情ID |
| `detailList[].appAccountId` | string | 应用账户ID |
| `detailList[].subAppAccountId` | string | 子应用账户ID |
| `detailList[].platform` | string | 平台 |
| `detailList[].title` | string | 商品标题 |
| `detailList[].remark` | string | 备注 |
| `detailList[].copyType` | string | 复制类型 |
| `detailList[].collectBoxGroupId` | string | 采集箱分组ID |
| `detailList[].collectBoxGroupName` | string | 采集箱分组名称 |
| `detailList[].collectBoxDetailShopList` | array<object> | 预发布店铺信息列表 |
| `detailList[].collectBoxDetailShopList[].shopId` | string | 店铺ID |
| `detailList[].isSupportReplicateProduct` | boolean | 是否支持新链路 |

#### 获取采集箱店铺模式详情

`POST /open/v1/product/collect_box/tiktok/collect_box/get_shop_collect_item_info`  (文档: api-446814592)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string | ossMd5值 |
| `editModel` | string | 编辑模式 |
| `claimToShopIds` | array<integer> | 已认领的店铺IDS |
| `isSupportMultiWarehouse` | integer | 是否支持多仓库 |
| `shopCollectItemInfo` | object | 店铺模式数据 |
| `shopCollectItemInfo.site` | string | 站点代码（如 MY、SG） |
| `shopCollectItemInfo.shopId` | integer | 店铺ID |
| `shopCollectItemInfo.detailId` | integer | 详情ID |
| `shopCollectItemInfo.title` | string | 商品标题 |
| `shopCollectItemInfo.oriTitle` | string | 商品原始标题 |
| `shopCollectItemInfo.notes` | string | 备注 |
| `shopCollectItemInfo.cid` | string | 类目ID |
| `shopCollectItemInfo.brandId` | string | 品牌ID |
| `shopCollectItemInfo.brandName` | string | 品牌名称 |
| `shopCollectItemInfo.productAttributes` | array<object> | 商品属性列表 |
| `shopCollectItemInfo.productAttributes[].attributeId` | string | 属性ID |
| `shopCollectItemInfo.productAttributes[].attributeName` | string | 属性名称 |
| `shopCollectItemInfo.productAttributes[].attributeNameAlias` | string | 属性名称别名（中文） |
| `shopCollectItemInfo.productAttributes[].attributeValues` | array<object> | 属性值列表 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 属性值名称 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 属性值ID |
| `shopCollectItemInfo.skuMap` | object | SKU Map（key=SKU标识码，value=SKU条目） |
| `shopCollectItemInfo.skuPropertyList` | array<object> | SKU销售属性列表 |
| `shopCollectItemInfo.skuPropertyList[].attrId` | string | 属性ID |
| `shopCollectItemInfo.skuPropertyList[].attrName` | string | 属性名称 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList` | array<object> | 属性值列表 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 属性值ID |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 属性值 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 属性图片URL |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 补充SKU图片URL列表 |
| `shopCollectItemInfo.imgUrls` | array<string> | 商品图片URL列表 |
| `shopCollectItemInfo.weight` | number | 重量（kg） |
| `shopCollectItemInfo.packageLength` | number | 包裹长度（cm） |
| `shopCollectItemInfo.packageWidth` | number | 包裹宽度（cm） |
| `shopCollectItemInfo.packageHeight` | number | 包裹高度（cm） |
| `shopCollectItemInfo.isCodOpen` | string | 是否开启货到付款（1-是，0-否） |
| `shopCollectItemInfo.productCertifications` | array<object> | 商品认证列表 |
| `shopCollectItemInfo.productCertifications[].id` | string | 认证ID |
| `shopCollectItemInfo.productCertifications[].files` | array<object> | 认证文件列表 |
| `shopCollectItemInfo.productCertifications[].files[].fileId` | string | 文件ID（上传到TK的会有这个ID） |
| … | | 共 51 个字段，详见 openapi.json |

#### 保存采集箱店铺模式详情

`POST /open/v1/product/collect_box/tiktok/collect_box/save_shop_collect_item_info`  (文档: api-446814593)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ossMd5` | string | 是 | ossMd5值 |
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.notes` | string | 是 | 商品描述 |
| `shopCollectItemInfo.imgUrls` | array<string> | 是 | 商品图片URL列表 |
| `shopCollectItemInfo.brandId` | string |  | 品牌ID |
| `shopCollectItemInfo.weight` | number | 是 | 重量（kg） max:100 |
| `shopCollectItemInfo.packageLength` | number | 是 | 包装长度（cm） max:1000 |
| `shopCollectItemInfo.packageWidth` | number | 是 | 包装宽度（cm） max:1000 |
| `shopCollectItemInfo.packageHeight` | number | 是 | 包装高度（cm） max:1000 |
| `shopCollectItemInfo.productCertifications` | array<object> |  | 商品认证列表 |
| `shopCollectItemInfo.productCertifications[].id` | string |  | 认证ID |
| `shopCollectItemInfo.productCertifications[].files` | array<object> |  | 认证文件列表 |
| `shopCollectItemInfo.productCertifications[].files[].fileId` | string |  | 文件ID（如果文件是TK的需要传这个ID） |
| `shopCollectItemInfo.productCertifications[].files[].fileName` | string |  | 文件名 |
| `shopCollectItemInfo.productCertifications[].files[].fileType` | string |  | 文件类型（如 PDF） |
| `shopCollectItemInfo.productCertifications[].files[].fileUrl` | string |  | 文件URL |
| `shopCollectItemInfo.productCertifications[].gmtExpirationDate` | string |  | 认证到期日期 |
| `shopCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `shopCollectItemInfo.isCodOpen` | string | 是 | 是否开启货到付款（1=是，0=否） |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.editModel` | string |  | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.version` | string |  | 版本号 |
| `shopCollectItemInfo.shopId` | integer |  | 店铺ID |
| `shopCollectItemInfo.detailId` | integer |  | 采集箱详情ID |
| `shopCollectItemInfo.sizeChartType` | string |  | 尺码表类型（仅支持image） |
| `shopCollectItemInfo.sizeChart` | string |  | 尺码表图片URL |
| `shopCollectItemInfo.deliveryOptionSetType` | string | 是 | 配送选项设置类型仅支持（仅default） |
| `shopCollectItemInfo.skuMap` | object |  | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `shopCollectItemInfo.skuPropertyList` | array<object> |  | SKU 规格属性列表 |
| `shopCollectItemInfo.skuPropertyList[].attrName` | string |  | 属性名称，如 Color、Size |
| `shopCollectItemInfo.skuPropertyList[].attrId` | string |  | 属性ID |
| `shopCollectItemInfo.skuPropertyList[].attrValueList` | array<object> |  | 属性值列表 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string |  | 属性值ID（构造SkuMap的key时使用该值） |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string |  | 属性值名称 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string |  | 属性值图片URL |
| `shopCollectItemInfo.productAttributes` | array<object> |  | 商品属性列表 |
| `shopCollectItemInfo.productAttributes[].attributeId` | string |  | 属性ID |
| `shopCollectItemInfo.productAttributes[].attributeName` | string |  | 属性名称 |
| `shopCollectItemInfo.productAttributes[].attributeNameAlias` | string |  | 属性名称别名（中文） |
| `shopCollectItemInfo.productAttributes[].attributeValues` | array<object> |  | 属性值列表 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueName` | string |  | 属性值名称 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueId` | string |  | 属性值ID |
| `shopCollectItemInfo.manufacturerIds` | array<string> |  | 制造商ID列表 |
| `shopCollectItemInfo.responsiblePersonIds` | array<string> |  | 责任人ID列表 |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string | 采集箱详情OssMd5标识 |

#### 获取采集箱站点模式详情

`POST /open/v1/product/collect_box/tiktok/collect_box/get_site_collect_item_info`  (文档: api-449650816)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `site` | string | 是 | 站点 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string | ossMd5值 |
| `editModel` | string | 编辑模式 |
| `claimToShopIds` | array<integer> | 已认领的店铺IDS |
| `isSupportMultiWarehouse` | integer | 是否支持多仓库 |
| `siteCollectItemInfo` | object | 店铺模式数据 |
| `siteCollectItemInfo.site` | string | 站点代码（如 PH、MY） |
| `siteCollectItemInfo.detailId` | integer | 详情ID |
| `siteCollectItemInfo.title` | string | 商品标题 |
| `siteCollectItemInfo.notes` | string | 备注 |
| `siteCollectItemInfo.imgUrls` | array<string> | 商品图片URL列表 |
| `siteCollectItemInfo.weight` | number | 重量（kg） |
| `siteCollectItemInfo.packageLength` | number | 包裹长度（cm） |
| `siteCollectItemInfo.packageWidth` | number | 包裹宽度（cm） |
| `siteCollectItemInfo.packageHeight` | number | 包裹高度（cm） |
| `siteCollectItemInfo.productCertifications` | array<object> | 商品认证列表 |
| `siteCollectItemInfo.productCertifications[].id` | string | 认证ID |
| `siteCollectItemInfo.productCertifications[].files` | array<object> | 认证文件列表 |
| `siteCollectItemInfo.productCertifications[].files[].fileId` | string | 文件ID（上传到TK的会有这个ID） |
| `siteCollectItemInfo.productCertifications[].files[].fileName` | string | 文件名 |
| `siteCollectItemInfo.productCertifications[].files[].fileType` | string | 文件类型（如 PDF） |
| `siteCollectItemInfo.productCertifications[].files[].fileUrl` | string | 文件URL |
| `siteCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 认证到期日期 |
| `siteCollectItemInfo.sizeChartType` | string | 尺码表类型 |
| `siteCollectItemInfo.sizeChart` | string | 尺码表图片URL |
| `siteCollectItemInfo.skuMap` | object | SKU Map（key=SKU标识码，value=SKU条目） |
| `siteCollectItemInfo.skuPropertyList` | array<object> | SKU销售属性列表 |
| `siteCollectItemInfo.skuPropertyList[].attrId` | string | 属性ID |
| `siteCollectItemInfo.skuPropertyList[].attrName` | string | 属性名称 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList` | array<object> | 属性值列表 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 属性值ID |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 属性值 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 属性图片URL |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 补充SKU图片URL列表 |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 主图视频URL |
| `siteCollectItemInfo.mainImgAppVideoId` | string | 主图App端视频ID |
| `siteCollectItemInfo.mainImgPlatformVideoId` | string | 主图平台视频ID |
| `siteCollectItemInfo.isCodOpen` | string | 是否开启货到付款（1-是，0-否） |
| `siteCollectItemInfo.cid` | string | 类目ID |
| `siteCollectItemInfo.editModel` | string | 编辑模式 |
| `siteCollectItemInfo.productAttributes` | array<object> | 商品属性列表 |
| … | | 共 56 个字段，详见 openapi.json |

#### 保存采集箱站点模式详情

`POST /open/v1/product/collect_box/tiktok/collect_box/save_site_collect_item_info`  (文档: api-449650817)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ossMd5` | string | 是 | ossMd5值 |
| `site` | string | 是 | 站点 |
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 商品描述 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 商品图片URL列表 |
| `siteCollectItemInfo.brandId` | string |  | 品牌ID |
| `siteCollectItemInfo.weight` | number | 是 | 重量（kg） max:100 |
| `siteCollectItemInfo.packageLength` | number | 是 | 包装长度（cm） max:1000 |
| `siteCollectItemInfo.packageWidth` | number | 是 | 包装宽度（cm） max:1000 |
| `siteCollectItemInfo.packageHeight` | number | 是 | 包装高度（cm） max:1000 |
| `siteCollectItemInfo.productCertifications` | array<object> |  | 商品认证列表 |
| `siteCollectItemInfo.productCertifications[].id` | string |  | 认证ID |
| `siteCollectItemInfo.productCertifications[].files` | array<object> |  | 认证文件列表 |
| `siteCollectItemInfo.productCertifications[].files[].fileId` | string |  | 文件ID（如果文件是TK的需要传这个ID） |
| `siteCollectItemInfo.productCertifications[].files[].fileName` | string |  | 文件名 |
| `siteCollectItemInfo.productCertifications[].files[].fileType` | string |  | 文件类型（如 PDF） |
| `siteCollectItemInfo.productCertifications[].files[].fileUrl` | string |  | 文件URL |
| `siteCollectItemInfo.productCertifications[].gmtExpirationDate` | string |  | 认证到期日期 |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.isCodOpen` | string | 是 | 是否开启货到付款（1=是，0=否） |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.editModel` | string |  | 编辑模式（shop=店铺模式，site=站点模式） |
| `siteCollectItemInfo.version` | string |  | 版本号 |
| `siteCollectItemInfo.shopId` | integer |  | 店铺ID |
| `siteCollectItemInfo.detailId` | integer |  | 采集箱详情ID |
| `siteCollectItemInfo.sizeChartType` | string |  | 尺码表类型（仅支持image） |
| `siteCollectItemInfo.sizeChart` | string |  | 尺码表图片URL |
| `siteCollectItemInfo.deliveryOptionSetType` | string | 是 | 配送选项设置类型仅支持（仅default） |
| `siteCollectItemInfo.skuMap` | object |  | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `siteCollectItemInfo.skuPropertyList` | array<object> |  | SKU 规格属性列表 |
| `siteCollectItemInfo.skuPropertyList[].attrName` | string |  | 属性名称，如 Color、Size |
| `siteCollectItemInfo.skuPropertyList[].attrId` | string |  | 属性ID |
| `siteCollectItemInfo.skuPropertyList[].attrValueList` | array<object> |  | 属性值列表 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string |  | 属性值ID（构造SkuMap的key时使用该值） |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string |  | 属性值名称 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string |  | 属性值图片URL |
| `siteCollectItemInfo.productAttributes` | array<object> |  | 商品属性列表 |
| `siteCollectItemInfo.productAttributes[].attributeId` | string |  | 属性ID |
| `siteCollectItemInfo.productAttributes[].attributeName` | string |  | 属性名称 |
| `siteCollectItemInfo.productAttributes[].attributeNameAlias` | string |  | 属性名称别名（中文） |
| `siteCollectItemInfo.productAttributes[].attributeValues` | array<object> |  | 属性值列表 |
| `siteCollectItemInfo.productAttributes[].attributeValues[].valueName` | string |  | 属性值名称 |
| `siteCollectItemInfo.productAttributes[].attributeValues[].valueId` | string |  | 属性值ID |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> |  | 店铺特殊数据信息列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 是 | 站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].brandId` | string |  | 品牌ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].manufacturerIds` | array<string> |  | 制造商ID列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].responsiblePersonIds` | array<string> |  | 责任人ID列表 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string | 采集箱详情OssMd5标识 |

#### 产品翻译

`POST /open/v1/product/collect_box/tiktok/collect_box/translate_collect_item_info`  (文档: api-482189160)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `sourceLanguage` | string | 是 | 原始语言 可选值：auto(自动识别), zh(简体中文), zh-tw(中繁体), en(英文), th(泰文), vi(越南文), id(印尼文), ms(马来语), es(西班牙文), pt(葡萄牙语), pl(波兰语), fr(法文), bn(孟加拉语), it(意大利文), de(德语), fi(芬兰语), cs(捷克语), ja(日文), he(希伯来语), ur(乌尔都语), uk(乌克兰语), el(希腊语), kk(哈萨克语), nl(荷兰语), sv(瑞典语), ko(韩文), ru(俄文), ar(阿拉伯语), tr(土耳其语), ro(罗马尼亚语), bg(保加利亚语), hu(匈牙利语), se(瑞典语), ga(爱尔兰语) |
| `targetLanguage` | string | 是 | 目标语言 可选值：zh(简体中文), zh-tw(中繁体), en(英文), th(泰文), vi(越南文), id(印尼文), ms(马来语), es(西班牙文), pt(葡萄牙语), pl(波兰语), fr(法文), bn(孟加拉语), it(意大利文), de(德语), fi(芬兰语), cs(捷克语), ja(日文), he(希伯来语), ur(乌尔都语), uk(乌克兰语), el(希腊语), kk(哈萨克语), nl(荷兰语), sv(瑞典语), ko(韩文), ru(俄文), ar(阿拉伯语), tr(土耳其语), ro(罗马尼亚语), bg(保加利亚语), hu(匈牙利语), se(瑞典语), ga(爱尔兰语) |
| `collectItemInfo` | object | 是 | 需翻译的产品详情 |
| `collectItemInfo.title` | string |  | 商品标题 |
| `collectItemInfo.notes` | string |  | 备注 |
| `collectItemInfo.warrantyPolicy` | string |  | 保修政策 |
| `collectItemInfo.skuMap` | object |  | SKU Map（key=SKU标识码，value=SKU条目） |
| `collectItemInfo.skuPropertyList` | array<object> |  | SKU销售属性列表 |
| `collectItemInfo.skuPropertyList[].attrId` | string |  | 属性ID |
| `collectItemInfo.skuPropertyList[].attrName` | string |  | 属性名称 |
| `collectItemInfo.skuPropertyList[].attrValueList` | array<object> |  | 属性值列表 |
| `collectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string |  | 属性值ID |
| `collectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string |  | 属性值 |
| `collectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string |  | 属性图片URL |
| `collectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> |  | 补充SKU图片URL列表 |
| `collectItemInfo.productAttributes` | array<object> |  | 商品属性列表 |
| `collectItemInfo.productAttributes[].attributeId` | string |  | 属性ID |
| `collectItemInfo.productAttributes[].attributeName` | string |  | 属性名称 |
| `collectItemInfo.productAttributes[].attributeValues` | array<object> |  | 属性值列表 |
| `collectItemInfo.productAttributes[].attributeValues[].valueName` | string |  | 属性值名称 |
| `collectItemInfo.productAttributes[].attributeValues[].valueId` | string |  | 属性值ID |
| `isTranslateSkuItemNum` | integer | 是 | 是否翻译平台sku（0=否，1=是） |
| `isTranslateSkuProperty` | integer | 是 | 是否翻译SKU规格名称（0=否，1=是） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectItemInfo` | object | 翻译后的产品详情（只翻译，没有保存翻译后的数据，用户需自行保存） |

#### AI匹配类目

`POST /open/v1/product/collect_box/tiktok/collect_box/ai_match_cid_by_shop_ids`  (文档: api-482189162)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | integer | 是 | 采集箱详情ID |
| `shopIds` | array<integer> | 是 | 店铺ID列表 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopIdAndCidMap` | object | 店铺与匹配CID的映射 示例：{ 100001 : 11231, 100002 : 12345 } |
| `failedShopIds` | array<integer> | 匹配失败的店铺ID列表，失败就代表没有这个店铺没有匹配上类目 |

#### 批量删除采集箱产品接口

`POST /open/v1/product/collect_box/tiktok/collect_box/delete_collect_box_detail`  (文档: api-496804330)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successNum` | integer | 删除成功数量 |
| `failNum` | integer | 删除失败数量 |
| `errorMap` | object | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `errorMsg` | string | 拼接后的错误信息 |

#### AI属性匹配

`POST /open/v1/product/collect_box/tiktok/collect_box/ai_match_product_attribute`  (文档: api-482189161)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | integer | 是 | 采集箱详情ID |
| `cid` | string | 是 | 类目ID |
| `site` | string | 是 | 站点 |
| `shopIds` | array<integer> |  | 店铺ID列表 当产品与店铺关联时传入，用于精确查找 |
| `productAttributes` | array<object> |  | 当前产品属性列表 |
| `productAttributes[].attributeId` | string |  | 属性ID |
| `productAttributes[].attributeName` | string |  | 属性名称 |
| `productAttributes[].attributeValues` | array<object> |  | 属性值列表 |
| `productAttributes[].attributeValues[].valueName` | string |  | 属性值名称 |
| `productAttributes[].attributeValues[].valueId` | string |  | 属性值ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `productAttributes` | array<object> | AI匹配后的产品属性列表 |
| `productAttributes[].attributeId` | string | 属性ID |
| `productAttributes[].attributeName` | string | 属性名称 |
| `productAttributes[].attributeValues` | array<object> | 属性值列表 |
| `productAttributes[].attributeValues[].valueName` | string | 属性值名称 |
| `productAttributes[].attributeValues[].valueId` | string | 属性值ID |

#### 获取品牌列表

`POST /open/v1/product/collect_box/tiktok/collect_box/get_brand_list`  (文档: api-497001483)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `brandName` | string |  | 品牌名搜索关键字 |
| `nextPageToken` | string |  | 获取下一页数据的Token |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `brandList` | array<object> | 品牌列表 |
| `brandList[].authorizedStatus` | string | 该品牌的授权状态（只有授权通过的品牌才会在前台展示）授权通过-AUTHORIZED，授权未通过-UNAUTHORIEZD |
| `brandList[].brandId` | string | 品牌ID |
| `brandList[].brandName` | string | 品牌名称 |
| `nextPageToken` | string | 获取下一页数据的Token |
| `totalCount` | integer | 品牌总数 |

### 商品 > TK采集箱 > 产品发布

#### 发布产品

`POST /open/v1/product/collect_box/tiktok/collect_box/save_move_collect_task`  (文档: api-446814595)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

#### 发布记录列表

`POST /open/v1/product/collect_box/tiktok/move_collect/search_move_collect_list`  (文档: api-482189163)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:20 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string |  | 产品ID |
| `filter.sourceItemId` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectDetailList` | array<object> | 发布记录列表 |
| `moveCollectDetailList[].moveCollectTaskDetailId` | string | 发布任务详情ID |
| `moveCollectDetailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `moveCollectDetailList[].shopId` | string | 店铺ID |
| `moveCollectDetailList[].itemNum` | string | 商品编号 |
| `moveCollectDetailList[].cid` | string | 类目ID |
| `moveCollectDetailList[].source` | string | 来源平台 |
| `moveCollectDetailList[].sourceSite` | string | 来源站点 |
| `moveCollectDetailList[].sourceItemId` | string | 来源商品ID |
| `moveCollectDetailList[].title` | string | 商品标题 |
| `moveCollectDetailList[].thumbnail` | string | 缩略图 |
| `moveCollectDetailList[].isTiming` | string | 是否定时发布 |
| `moveCollectDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].reason` | string | 失败原因 |
| `moveCollectDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].gmtModified` | string | 修改时间 |
| `moveCollectDetailList[].platformItemId` | string | 平台商品ID |
| `moveCollectDetailList[].isRenewItem` | boolean | 是否翻新 |
| `moveCollectDetailList[].shopName` | string | 店铺名称 |
| `moveCollectDetailList[].siteName` | string | 站点名称 |
| `moveCollectDetailList[].site` | string | 站点 |
| `moveCollectDetailList[].sourceItemUrl` | string | 来源商品链接 |
| `moveCollectDetailList[].itemEditUrl` | string | 商品编辑链接 |
| `moveCollectDetailList[].breadcrumb` | string | 类目路径 |
| `moveCollectDetailList[].ownerSubAppAccountId` | integer | 归属子账号ID |
| `moveCollectDetailList[].ownerSubAccountAliasName` | string | 归属子账号名称 |
| `total` | integer | 总数 |

### 商品 > TK采集箱 > 定价模板

#### 获取定价模板列表

`POST /open/v1/product/collect_box/tiktok/price_template/get_price_template_list`  (文档: api-482189164)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string |  | 模板名称（模糊搜索） |
| `site` | string |  | 站点 |
| `siteType` | string |  | 站点类型：cross_border 跨境 / mainland 本土 |
| `pageNo` | integer | 是 | 页码 |
| `pageSize` | integer | 是 | 每页条数 max:20 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `priceTemplateList` | array<object> | 定价模板列表 |
| `priceTemplateList[].priceTemplateId` | integer | 定价模板 ID |
| `priceTemplateList[].appAccountId` | integer | 主账号 ID |
| `priceTemplateList[].subAppAccountId` | integer | 子账号 ID |
| `priceTemplateList[].platform` | string | 平台标识，如 tiktok |
| `priceTemplateList[].site` | string | 站点，如 MY / PH / US |
| `priceTemplateList[].name` | string | 模板名称 |
| `priceTemplateList[].remark` | string | 备注 |
| `priceTemplateList[].currency` | string | 站点币种，如 MYR / PHP / USD |
| `priceTemplateList[].displayWeightUnit` | string | 重量单位显示类型：kilogram / gram |
| `priceTemplateList[].profitType` | string | 利润计算类型：percent 百分比 / fixed 固定金额 |
| `priceTemplateList[].profitPercent` | number | 利润百分比（profitType=percent 时生效） |
| `priceTemplateList[].fixedProfitAmount` | number | 固定利润金额（profitType=fixed 时生效） |
| `priceTemplateList[].exchangeRate` | number | 汇率（人民币兑站点币种） |
| `priceTemplateList[].discount` | number | 折扣率（0~1，如 0.9 表示九折） |
| `priceTemplateList[].priceTailComputeType` | string | 价格尾数处理类型：process_decimal / fixed_tail |
| `priceTemplateList[].priceTail` | string | 价格尾数值（priceTailComputeType=fixed_tail 时生效） |
| `priceTemplateList[].priceProcessDecimalType` | string | 小数处理类型：floor 向下 / ceil 向上 / round 四舍五入 |
| `priceTemplateList[].logisticsComputeType` | string | 国际物流计算类型：fixed / first_continued / weight_interval / official_freight_tpl |
| `priceTemplateList[].weightRefType` | string | 重量参考类型：weight / volume_weight / max_weight |
| `priceTemplateList[].firstWeightCharge` | number | 首重费用（国际物流 first_continued 类型时生效） |
| `priceTemplateList[].firstWeightInterval` | number | 首重区间（g 或 kg，取决于 displayWeightUnit） |
| `priceTemplateList[].continuedWeightCharge` | number | 续重费用（国际物流 first_continued 类型时生效） |
| `priceTemplateList[].continuedWeightInterval` | number | 续重区间（g 或 kg，取决于 displayWeightUnit） |
| `priceTemplateList[].logisticsCharge` | number | 固定物流费用（国际物流 fixed 类型时生效） |
| `priceTemplateList[].platformChargePercent` | number | 平台费率（百分比，如 2.12 表示 2.12%） |
| `priceTemplateList[].paymentChargePercent` | number | 支付手续费率 |
| `priceTemplateList[].activityChargePercent` | number | 活动费率 |
| `priceTemplateList[].withdrawChargePercent` | number | 提现手续费率 |
| `priceTemplateList[].otherCharge` | number | 其他杂费（站点币种） |
| `priceTemplateList[].isCalLightCargo` | integer | 是否计算抛货（轻货）：1 是 / 0 否 |
| `priceTemplateList[].lightCargoCoefficient` | integer | 抛货体积重系数（isCalLightCargo=1 时生效，单位：cm³/g） |
| `priceTemplateList[].weightLogisticsChargeList` | string | 分段重量物流费用列表（logisticsComputeType=weight_interval 时生效） 格式：[['minWeight'=>0, 'maxWeight'=>1000, 'charge'=>5.00], ...] |
| `priceTemplateList[].domesticLogisticsComputeType` | string | 国内物流计算类型：fixed / first_continued |
| `priceTemplateList[].domesticLogisticsFirstWeightCharge` | number | 国内物流首重费用 |
| `priceTemplateList[].domesticLogisticsFirstWeightInterval` | number | 国内物流首重区间 |
| `priceTemplateList[].domesticLogisticsContinuedWeightCharge` | number | 国内物流续重费用 |
| `priceTemplateList[].domesticLogisticsContinuedWeightInterval` | number | 国内物流续重区间 |
| `priceTemplateList[].domesticLogisticsCharge` | number | 国内物流固定费用（domesticLogisticsComputeType=fixed 时生效） |
| `priceTemplateList[].buyerLogisticCharge` | number | 买家承担物流费用 |
| … | | 共 50 个字段，详见 openapi.json |

#### 获取各个站点的默认配置

`POST /open/v1/product/collect_box/tiktok/price_template/get_site_default_setting`  (文档: api-482189165)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `siteAndBuyerLogisticDefaultChargeMap` | object | 站点买家物流默认运费（站点币种） |
| `siteAndBuyerLogisticDefaultChargeCNYMap` | object | 站点买家物流默认运费（人民币） |
| `siteAndDefaultPlatformInfrastructureChargeMap` | object | 站点默认平台基础设施费（站点币种） |
| `siteAndDefaultPlatformInfrastructureChargeCNYMap` | object | 站点默认平台基础设施费（人民币） |
| `tiktokCbSiteAndDefaultChargePercentMap` | object | 跨境站点默认费率 key=站点代码，value=各项费率明细 |
| `tiktokLocalDefaultChargePercentMap` | object | 本土站点默认费率 |
| `siteAndDefaultPlatformSupportChargeMap` | object | 站点默认平台支持费（站点币种） |
| `siteAndDefaultPlatformSupportChargeCNYMap` | object | 站点默认平台支持费（人民币） |

### 商品 > TEMU全托采集箱 > 产品发布

#### 发布产品

`POST /open/v1/product/collect_box/pddkj/move_collect/save_move_collect_task`  (文档: api-468724006)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

#### 发布记录列表

`POST /open/v1/product/collect_box/pddkj/move_collect/search_move_collect_list`  (文档: api-511668107)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:20 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string |  | 产品ID |
| `filter.sourceItemId` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectDetailList` | array<object> | 发布记录列表 |
| `moveCollectDetailList[].moveCollectTaskDetailId` | string | 发布任务详情ID |
| `moveCollectDetailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `moveCollectDetailList[].shopId` | string | 店铺ID |
| `moveCollectDetailList[].itemNum` | string | 商品编号 |
| `moveCollectDetailList[].cid` | string | 类目ID |
| `moveCollectDetailList[].source` | string | 来源平台 |
| `moveCollectDetailList[].sourceSite` | string | 来源站点 |
| `moveCollectDetailList[].sourceItemId` | string | 来源商品ID |
| `moveCollectDetailList[].title` | string | 商品标题 |
| `moveCollectDetailList[].thumbnail` | string | 缩略图 |
| `moveCollectDetailList[].isTiming` | string | 是否定时发布 |
| `moveCollectDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].reason` | string | 失败原因 |
| `moveCollectDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].gmtModified` | string | 修改时间 |
| `moveCollectDetailList[].platformItemId` | string | 平台商品ID |
| `moveCollectDetailList[].isRenewItem` | boolean | 是否翻新 |
| `moveCollectDetailList[].shopName` | string | 店铺名称 |
| `moveCollectDetailList[].siteName` | string | 站点名称 |
| `moveCollectDetailList[].site` | string | 站点 |
| `moveCollectDetailList[].sourceItemUrl` | string | 来源商品链接 |
| `moveCollectDetailList[].itemEditUrl` | string | 商品编辑链接 |
| `moveCollectDetailList[].breadcrumb` | string | 类目路径 |
| `moveCollectDetailList[].ownerSubAppAccountId` | integer | 归属子账号ID |
| `moveCollectDetailList[].ownerSubAccountAliasName` | string | 归属子账号名称 |
| `total` | integer | 总数 |

### 商品 > TEMU全托采集箱 > 车型库

#### 获取车型库站点列表

`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_list`  (文档: api-468724008)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer |  | 类目ID，区分摩托车和汽车 ，不传返回全部 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsVehicleLibrarySiteList` | array<object> | 车型库站点列表，每项代表一个销售地区的车型库（如美国、欧洲等）。 根据产品的销售地区选择对应站点，取其 vehicleLibraryId 用于后续接口 |
| `goodsVehicleLibrarySiteList[].vehicleLibraryId` | integer | 车型库站点ID，选定站点后传入 getGoodsVehicleLibrarySiteTopPropDependencyList 获取顶级车型节点 |
| `goodsVehicleLibrarySiteList[].name` | string | 站点名称，如"美国"、"欧洲"，用于展示给用户选择 |
| `goodsVehicleLibrarySiteList[].pid` | integer | 属性ID |
| `goodsVehicleLibrarySiteList[].pidName` | string | 属性名称（中文），如"品牌"、"车系" |
| `goodsVehicleLibrarySiteList[].pidNameEn` | string | 属性名称（英文） |
| `goodsVehicleLibrarySiteList[].level` | integer | 层级（1=品牌，2=车系，3=年份，4=车型，5=发动机类型） |

#### 获取车型库站点属性结构映射

`POST /open/v1/product/collect_box/pddkj/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map`  (文档: api-468724009)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer |  | 类目ID，区分摩托车和汽车 ，不传返回全部 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsVehicleLibraryIdAndSitePidInfoMap` | object | 车型库站点属性结构映射，key 为 vehicleLibraryId，value 为该站点的属性层级信息列表。 用于了解某站点车型库包含哪些层级属性（品牌/车系/年款等）及其对应的 pid， 结合 getVehicleLibraryPropDependencyTree 的树形数据使用 SitePidInfo 结构： - pddkjGoodsVehicleLibraryId: string 平台商品车型库ID - vehicleLibraryId: string 车型库ID - name: string 站点名称，如"美国站、加拿大站" - pidNameEn: string 属性英文名，如"Make"、"Model"、"Year" - parentPropertyDependencyId: string 父属性依赖ID - propertyDependencyId: string 属性依赖ID - pid: string 属性pid - pidName: string 属性中文名，如"汽车品牌"、"汽车型号" - level: string 层级序号 - status: string 状态，1=启用 |

#### 获取站点顶级车型节点列表

`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list`  (文档: api-468724010)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `topGoodsVehicleLibraryPropDependencyList` | array<object> | 顶级车型节点列表（通常为品牌层），每项含 propertyValueDependencyId、vidValue 等字段。 取每项的 propertyValueDependencyId 作为 topPropertyValueDependencyId， 传入 getVehicleLibraryPropDependencyTree 获取该品牌下完整的车型树 |
| `topGoodsVehicleLibraryPropDependencyList[].pddkjGoodsVehicleLibraryPropDependencyId` | integer | 平台车型库属性依赖ID |
| `topGoodsVehicleLibraryPropDependencyList[].vehicleLibraryId` | integer | 车型库ID |
| `topGoodsVehicleLibraryPropDependencyList[].topPropertyValueDependencyId` | integer | 顶级节点propertyValueDependencyId |
| `topGoodsVehicleLibraryPropDependencyList[].parentPropertyValueDependencyId` | integer | 父节点propertyValueDependencyId，顶级节点为0 |
| `topGoodsVehicleLibraryPropDependencyList[].propertyValueDependencyId` | integer | 当前节点propertyValueDependencyId |
| `topGoodsVehicleLibraryPropDependencyList[].propertyDependencyId` | integer | 属性依赖ID |
| `topGoodsVehicleLibraryPropDependencyList[].vid` | integer | 属性值ID |
| `topGoodsVehicleLibraryPropDependencyList[].vidValue` | string | 属性值文本，如品牌名"Country Coach" |
| `topGoodsVehicleLibraryPropDependencyList[].level` | integer | 层级序号 |
| `topGoodsVehicleLibraryPropDependencyList[].isLeaf` | integer | 是否为叶子节点，0=否，1=是 |
| `topGoodsVehicleLibraryPropDependencyList[].md5BreadcrumbVidValue` | string | 面包屑属性值的MD5 |
| `topGoodsVehicleLibraryPropDependencyList[].breadcrumbVidValue` | string | 面包屑属性值文本 |
| `topGoodsVehicleLibraryPropDependencyList[].breadcrumbPropertyValueDependencyId` | integer | 面包屑属性值依赖ID |

#### 获取车型属性依赖树

`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_vehicle_library_prop_dependency_tree`  (文档: api-468724011)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |
| `topPropertyValueDependencyId` | integer | 是 | 顶级节点ID，从 getGoodsVehicleLibrarySiteTopPropDependencyList 返回的列表中取 propertyValueDependencyId |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `vehicleLibraryPropDependencyTree` | object | 车型属性依赖树，key 为顶级节点的 propertyValueDependencyId，value 为节点数据（含 children 子节点）。 树形结构按品牌→车系→年份→车型→发动机类型逐级展开，isLeaf=1 的节点为叶子节点。 选中叶子节点后，将从根节点到该叶子节点的完整路径组装为一条车型路径， 每个路径节点取 propertyValueDependencyId、vidValue、level 填入 vehicleLibraryRelationList[].productPropValueDependencyList 中 |

#### 根据类目ID查询有车型库数据的类目列表

`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_has_vehicle_library_cids_by_search_cids`  (文档: api-468724007)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cids` | array<integer> | 是 | 待查询的类目ID列表，传入产品所在类目的cid， 返回结果中包含的cid表示该类目支持车型库，发品时需填写车型适配信息 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `hasVehicleLibraryCids` | array<integer> | 有车型库的类目ID列表，如果产品所属类目在此列表中， 则发品时需要填写车型适配信息（vehicleLibrary相关字段） |

### 商品 > TEMU全托采集箱 > 采集箱

#### 获取类目属性规则

`POST /open/v1/product/collect_box/pddkj/collect_box/get_category_attribute_rules`  (文档: api-471545320)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array<integer> |  | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `saleAttributeRules` | array<object> | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `saleAttributeRules[].pid` | integer | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `saleAttributeRules[].templatePid` | integer | 模板属性ID，用于关联模板中的属性定义 |
| `saleAttributeRules[].refPid` | integer | 引用属性ID，表示该属性引用自哪个基础属性 |
| `saleAttributeRules[].name` | string | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `saleAttributeRules[].lang2Name` | string | 第二语言属性名称 |
| `saleAttributeRules[].isSale` | boolean | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `saleAttributeRules[].mainSale` | boolean | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `saleAttributeRules[].required` | boolean | 是否必填，为true时创建产品必须填写该属性 |
| `saleAttributeRules[].valueType` | string | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `saleAttributeRules[].controlType` | integer | 控件类型，决定前端展示方式 |
| `saleAttributeRules[].feature` | integer | 特征标记 |
| `saleAttributeRules[].chooseMaxNum` | integer | 最多可选数量，SELECT类型时最多可选几个value |
| `saleAttributeRules[].inputMaxNum` | integer | 输入最大数量，自定义输入的规格上限 |
| `saleAttributeRules[].minValue` | string | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `saleAttributeRules[].maxValue` | string | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `saleAttributeRules[].valuePrecision` | integer | 小数精度，数值保留几位小数 |
| `saleAttributeRules[].valueUnit` | array<string> | 合法单位列表，输入时必须使用列表中的单位 |
| `saleAttributeRules[].valueRule` | integer | 值规则 |
| `saleAttributeRules[].propertyValueType` | integer | 属性值类型 |
| `saleAttributeRules[].parentSpecId` | integer | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `saleAttributeRules[].parentTemplatePid` | integer | 父模板属性ID |
| `saleAttributeRules[].templatePropertyValueParentList` | array<object> | 父属性值模板ID列表，非string类型属性时使用 |
| `saleAttributeRules[].templatePropertyValueParentList[].parentVidList` | array<integer> | 父属性值ID列表 |
| `saleAttributeRules[].showCondition` | array<object> | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `saleAttributeRules[].showCondition[].parentRefPid` | integer | 父引用属性ID |
| `saleAttributeRules[].showCondition[].parentVids` | array<integer> | 父属性值ID列表 |
| `saleAttributeRules[].showType` | integer | 展示类型 |
| `saleAttributeRules[].propertyChooseTitle` | string | 属性选择标题，SELECT类型时的选择提示文字 |
| `saleAttributeRules[].numberInputTitle` | string | 数字输入标题，INPUT类型时的输入提示文字 |
| `saleAttributeRules[].referenceType` | integer | 引用类型 |
| `saleAttributeRules[].valueInputSum` | integer | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `saleAttributeRules[].values` | array<object> | 可选值列表，SELECT类型时从中选取vid和name |
| `saleAttributeRules[].values[].specId` | integer | 规格ID，自定义输入的值为null |
| `saleAttributeRules[].values[].vid` | integer | 属性值ID，填写属性时通过vid指定选中的值 |
| `saleAttributeRules[].values[].name` | string | 属性值名称，如"白色"、"XL"、"棉" |
| `saleAttributeRules[].values[].lang2Value` | string | 第二语言值 |
| `saleAttributeRules[].values[].extendInfo` | string | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `saleAttributeRules[].values[].group` | object | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `saleAttributeRules[].values[].parentVidList` | array<integer> | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| … | | 共 86 个字段，详见 openapi.json |

#### 获取商品基本选项

`POST /open/v1/product/collect_box/pddkj/collect_box/get_item_options`  (文档: api-471545321)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `outerPackageShapeOptions` | array<object> | 外包装形状选项，key/value 数组，保存到 outerPackageShape |
| `outerPackageShapeOptions[].key` | integer | 选项键值 |
| `outerPackageShapeOptions[].value` | string | 选项显示文本 |
| `outerPackageTypeOptions` | array<object> | 外包装类型选项，key/value 数组，保存到 outerPackageType |
| `outerPackageTypeOptions[].key` | integer | 选项键值 |
| `outerPackageTypeOptions[].value` | string | 选项显示文本 |
| `goodsModelTryOnResultMap` | array<object> | 模特试穿结果枚举，格式为 [{key: modelType, value: {tryOnResult: label}}]。 保存时按 modelType 取对应枚举，将所选 tryOnResult 填入 goodsModelReqs[].tryOnResult |
| `goodsModelTryOnResultMap[].key` | integer | 模特类型（modelType） |
| `goodsModelTryOnResultMap[].value` | object | 试穿结果枚举映射，key 为 tryOnResult，value 为显示文本 |
| `catIdAndProductNameMaxLengthMap` | object | 类目标题最大长度映射，key 为 cid，value 为最大字符数 |
| `suggestedPriceCurrencyTypeAndNameList` | array<object> | 建议售价币种列表，key/value 数组，保存到 skuMap[key].suggestedPriceCurrencyType |
| `suggestedPriceCurrencyTypeAndNameList[].key` | string | 选项键值 |
| `suggestedPriceCurrencyTypeAndNameList[].value` | string | 选项显示文本 |
| `skuClassificationList` | array<object> | SKU 分类类型，key/value 数组，保存到 skuMap[key].skuClassification。 1=单品（numberOfPieces 只能为1）；2=同款多件装（numberOfPieces 必须>1）； 3=混合套装（需额外填写 individuallyPacked 和 productSkuAccessories）。 部分类目此字段必填 |
| `skuClassificationList[].key` | integer | 选项键值 |
| `skuClassificationList[].value` | string | 选项显示文本 |
| `skuPieceUnitCodeList` | array<object> | 件数单位，key/value 数组，保存到 skuMap[key].pieceUnitCode。部分类目必填 |
| `skuPieceUnitCodeList[].key` | integer | 选项键值 |
| `skuPieceUnitCodeList[].value` | string | 选项显示文本 |
| `individuallyPackedList` | array<object> | 是否独立包装，key/value 数组，保存到 skuMap[key].individuallyPacked。 skuClassification 为2或3时必填 |
| `individuallyPackedList[].key` | integer | 选项键值 |
| `individuallyPackedList[].value` | string | 选项显示文本 |
| `packageLimitConfig` | object | 包装限制配置 |
| `descModuleLimitConfig` | object | 描述模块限制配置，包含 descModuleMaxTextLength（最大文本长度） |
| `netContentCidList` | array<integer> | 需要填写净含量的类目 cid 列表。 当商品 cid 在此列表中，skuClassification 为1或2时需填 netContentNumber/netContentUnitCode（取值见 netContentOptions）； skuClassification 为3时需填 totalNetContentNumber/totalNetContentUnitCode |
| `netContentOptions` | array<object> | 净含量单位选项，key/value 数组，保存到 skuMap[key].netContentUnitCode |
| `netContentOptions[].key` | integer | 选项键值 |
| `netContentOptions[].value` | string | 选项显示文本 |
| `enTitleRefTypeList` | array<object> | 英文标题参考类型选项 |
| `enTitleRefTypeList[].key` | string | 选项键值 |
| `enTitleRefTypeList[].value` | string | 选项显示文本 |
| `pieceNewUnitCodeList` | array<object> | 共计内含单位选项，key/value 数组，保存到 skuMap[key].pieceNewUnitCode |
| `pieceNewUnitCodeList[].key` | integer | 选项键值 |
| `pieceNewUnitCodeList[].value` | string | 选项显示文本 |
| `mixTypeList` | array<object> | 混合套装类型选项，key/value 数组，保存到 skuMap[key].mixedType。1=不同品，2=同品不同规格 |
| `mixTypeList[].key` | integer | 选项键值 |
| `mixTypeList[].value` | string | 选项显示文本 |
| `totalNetContentCidList` | array<integer> | 需要填写总净含量的类目 cid 列表（混合套装场景） |
| `vehicleLibraryRequiredCidList` | array<integer> | 需要填写车型库信息的类目 cid 列表 |
| `saleAttributeClothingColorMaxNum` | integer | 销售属性颜色最大数量 |
| … | | 共 41 个字段，详见 openapi.json |

#### 创建采集箱商品

`POST /open/v1/product/collect_box/pddkj/collect_box/create_collect_box_item`  (文档: api-471545322)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 SiteCollectItemInfoForSaveRo 注释。 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 保存时会校验每个店铺的存在性、运费模板、仓库配置； 每个子项的 shopId 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string |  | 站点 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object |  | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.itemNum` | string |  | 货号 |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string |  | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> |  | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string |  | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string |  | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object |  | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版，2=套版） |
| `siteCollectItemInfo.basePlateSkuKey` | string |  | 底版 SKU Key |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状，取值参考 getItemOptions 接口返回的 outerPackageShapeOptions |
| `siteCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型，取值参考 getItemOptions 接口返回的 outerPackageTypeOptions |
| `siteCollectItemInfo.outerPackageImgUrls` | array<string> | 是 | 外包装图片URL列表 |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string |  | 图片URL（type=image时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string |  | 文本内容（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object |  | 文本模块详情（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer |  | 字体大小 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string |  | 字体粗细 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string |  | 对齐方式 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string |  | 字体颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string |  | 背景颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer |  | 字体族 |
| `siteCollectItemInfo.productGuideFileUrl` | string |  | 产品说明书URL |
| `siteCollectItemInfo.productGuideFileName` | string |  | 产品说明书文件名 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<string> |  | 展示尺码模板ID列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.sizeCharts` | array<object> |  | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> |  | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> |  | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string |  | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer |  | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer |  | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer |  | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer |  | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer |  | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> |  | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string |  | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写 |
| `siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> |  | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | integer | 创建成功的采集箱详情ID |

#### 认领预发布店铺

`POST /open/v1/product/collect_box/pddkj/collect_box/claim_to_shop`  (文档: api-471545323)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

#### 获取采集箱店铺模式详情

`POST /open/v1/product/collect_box/pddkj/collect_box/get_shop_collect_item_info`  (文档: api-471545324)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |
| `cid` | integer |  | 新类目id（需要切换类目时填写新的cid，可以快速匹配相同属性，需要保存才能生效新的类目） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `editModel` | string | 编辑模式 |
| `claimToShopIds` | array<integer> | 已认领的店铺IDS |
| `shopCollectItemInfo` | object | 店铺模式数据 |
| `shopCollectItemInfo.title` | string | 商品标题 |
| `shopCollectItemInfo.itemNum` | string | 非服饰类货号 |
| `shopCollectItemInfo.saleAttributes` | array<object> | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer | 基础属性id |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer | 属性id |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].name` | string | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].values` | array<object> | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | SKU标识码 |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 服饰类货号（服饰类的货号是SKC级别的） |
| `shopCollectItemInfo.attributes` | array<object> | 商品属性列表（成分/材质等） |
| `shopCollectItemInfo.attributes[].templatePid` | integer | 模板属性ID |
| `shopCollectItemInfo.attributes[].pid` | integer | 基础属性id |
| `shopCollectItemInfo.attributes[].refPid` | integer | 属性id |
| `shopCollectItemInfo.attributes[].name` | string | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array<object> | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 属性值id |
| `shopCollectItemInfo.attributes[].values[].name` | string | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string | 属性值单位 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer | 成分比例(所有成分比例之和需等于100) |
| `shopCollectItemInfo.skuMap` | object | SKU映射（key=SKU标识码，value=SKU条目） |
| `shopCollectItemInfo.sizeCharts` | array<object> | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 分组ID与值映射 |
| … | | 共 93 个字段，详见 openapi.json |

#### 保存采集箱店铺模式详情

`POST /open/v1/product/collect_box/pddkj/collect_box/save_shop_collect_item_info`  (文档: api-471545325)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.detailId` | integer | 是 | 采集箱详情ID |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.itemNum` | string |  | 非服饰类货号 |
| `shopCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `shopCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string |  | 图片URL（type=image时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string |  | 文本内容（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object |  | 文本模块详情（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer |  | 字体大小 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string |  | 字体粗细 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string |  | 对齐方式 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string |  | 字体颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string |  | 背景颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer |  | 字体族 |
| `shopCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `shopCollectItemInfo.productOriginProvince` | string |  | 原产省编码（原产国为中国时需要填写省份） |
| `shopCollectItemInfo.productOriginCertFiles` | array<object> |  | 原产地认证文件列表 |
| `shopCollectItemInfo.productOriginCertFiles[].fileUrl` | string |  | 文件URL |
| `shopCollectItemInfo.productOriginCertFiles[].fileName` | string |  | 文件名 |
| `shopCollectItemInfo.currency` | string |  | 店铺币种 |
| `shopCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `shopCollectItemInfo.productGuideFileUrl` | string |  | 产品说明书URL |
| `shopCollectItemInfo.productGuideFileName` | string |  | 产品说明书文件名 |
| `shopCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状 |
| `shopCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型 |
| `shopCollectItemInfo.outerPackageImgUrls` | array<string> | 是 | 外包装图片URL列表 |
| `shopCollectItemInfo.site` | string |  | 站点（temu全托 目前只有PDDKJ） |
| `shopCollectItemInfo.editModel` | string | 是 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.brandId` | string |  | 品牌ID |
| `shopCollectItemInfo.multiLanguageTitleMap` | object |  | 多语言标题映射 |
| `shopCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版 2=套版） |
| `shopCollectItemInfo.basePlateSkuKey` | string |  | 底板SKU Key |
| `shopCollectItemInfo.sizeCharts` | array<object> |  | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> |  | 手动录入ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `shopCollectItemInfo.vehicleLibraryRelationList` | array<object> |  | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `shopCollectItemInfo.translateLanguages` | array<string> |  | 说明书需翻译语言列表 |
| `shopCollectItemInfo.goodsModelReqs` | array<object> |  | 模特信息列表。requiredGoodsModel 为 true 的类目必填。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举 |
| `shopCollectItemInfo.goodsModelReqs[].modelId` | string | 是 | 模特ID |
| `shopCollectItemInfo.goodsModelReqs[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.goodsModelReqs[].modelName` | string | 是 | 模特名称 |
| `shopCollectItemInfo.goodsModelReqs[].modelType` | string | 是 | 模特类型 |
| `shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 是 | 模特图片URL |
| `shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 是 | 身高（cm） |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 是 | 试穿尺码规格名称 |
| `shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 是 | 试穿结果 |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 是 | 尺码规格ID |
| `shopCollectItemInfo.goodsModelReqs[].modelBust` | string |  | 胸围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelWaist` | string |  | 腰围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelHip` | string |  | 臀围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string |  | 脚长（cm），鞋类专用 |
| `shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string |  | 脚宽（cm），鞋类专用 |
| `shopCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表 |
| `shopCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `shopCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string |  | 属性值单位，没有的情况传空字符串 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer |  | 成分比例 总合需要为100 |
| `shopCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `shopCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `shopCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer |  | 属性ID |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer |  | 引用属性ID |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer |  | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer |  | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> |  | 服饰类颜色图（服饰类必填） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string |  | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `shopCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表 |
| `shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> |  | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |

#### 获取采集箱站点模式详情

`POST /open/v1/product/collect_box/pddkj/collect_box/get_site_collect_item_info`  (文档: api-471545326)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `editModel` | string | 编辑模式 |
| `claimToShopIds` | array<integer> | 已认领的店铺IDS |
| `siteCollectItemInfo` | object | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 商品标题 |
| `siteCollectItemInfo.itemNum` | string | 非服饰类货号 |
| `siteCollectItemInfo.saleAttributes` | array<object> | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 基础属性id |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 属性id |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].name` | string | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | SKU标识码 |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 服饰类货号（服饰类的货号是SKC级别的） |
| `siteCollectItemInfo.attributes` | array<object> | 商品属性列表（成分/材质等） |
| `siteCollectItemInfo.attributes[].templatePid` | integer | 模板属性ID |
| `siteCollectItemInfo.attributes[].pid` | integer | 基础属性id |
| `siteCollectItemInfo.attributes[].refPid` | integer | 属性id |
| `siteCollectItemInfo.attributes[].name` | string | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 属性值id |
| `siteCollectItemInfo.attributes[].values[].name` | string | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 属性值单位 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 成分比例(所有成分比例之和需等于100) |
| `siteCollectItemInfo.skuMap` | object | SKU映射（key=SKU标识码，value=SKU条目） |
| `siteCollectItemInfo.sizeCharts` | array<object> | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 分组ID与值映射 |
| … | | 共 97 个字段，详见 openapi.json |

#### 保存采集箱站点模式详情

`POST /open/v1/product/collect_box/pddkj/collect_box/save_site_collect_item_info`  (文档: api-471545327)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 保存时会校验每个店铺的存在性、运费模板、仓库配置； 每个子项的 shopId 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string |  | 站点 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object |  | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.itemNum` | string |  | 货号 |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string |  | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> |  | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string |  | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string |  | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object |  | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版，2=套版） |
| `siteCollectItemInfo.basePlateSkuKey` | string |  | 底版 SKU Key |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状，取值参考 getItemOptions 接口返回的 outerPackageShapeOptions |
| `siteCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型，取值参考 getItemOptions 接口返回的 outerPackageTypeOptions |
| `siteCollectItemInfo.outerPackageImgUrls` | array<string> | 是 | 外包装图片URL列表 |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string |  | 图片URL（type=image时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string |  | 文本内容（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object |  | 文本模块详情（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer |  | 字体大小 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string |  | 字体粗细 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string |  | 对齐方式 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string |  | 字体颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string |  | 背景颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer |  | 字体族 |
| `siteCollectItemInfo.productGuideFileUrl` | string |  | 产品说明书URL |
| `siteCollectItemInfo.productGuideFileName` | string |  | 产品说明书文件名 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<string> |  | 展示尺码模板ID列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.sizeCharts` | array<object> |  | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> |  | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> |  | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string |  | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer |  | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer |  | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer |  | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer |  | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer |  | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> |  | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string |  | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写 |

#### 获取原产地国家列表

`POST /open/v1/product/collect_box/pddkj/collect_box/get_country_short_name_and_name_map`  (文档: api-471545328)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `countryShortNameAndNameMap` | object | 国家简码→中文名映射，key 为 shortName（如 CN），value 为中文名（如 中国大陆）。 可用于将已保存的 productOriginCountry 短码转换为可读名称展示 |
| `productOriginCountries` | array<object> | 完整国家列表，用于渲染原产地下拉选择器。 选择某个国家后将其 shortName 填入 productOriginCountry； 选择中国（shortName=CN）时，还需从 province 列表中选择省份，将省份 code 填入 productOriginProvince |
| `productOriginCountries[].code` | string | 国家编码（如 43） |
| `productOriginCountries[].name` | string | 英文名 |
| `productOriginCountries[].shortName` | string | 国家简码，填入 productOriginCountry（如 CN、US） |
| `productOriginCountries[].chineseName` | string | 中文名 |
| `productOriginCountries[].province` | array<object> | 省份列表，仅原产国为 CN 时有值。 选择中国后需从此列表选择省份，将省份 code 填入 productOriginProvince |
| `productOriginCountries[].province[].code` | string | 省份编码，原产国为 CN 时填入 productOriginProvince |
| `productOriginCountries[].province[].name` | string | 英文名 |
| `productOriginCountries[].province[].chineseName` | string | 中文名 |

#### 店铺模特列表

`POST /open/v1/product/collect_box/pddkj/collect_box/search_model_list`  (文档: api-471545329)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `modelType` | integer |  | 模特类型（0=成衣模特，1=鞋模） |
| `modelName` | string |  | 模特名称模糊搜索 |
| `pageNo` | integer |  | 页码，默认1 |
| `pageSize` | integer |  | 每页条数，默认20 max:1000 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `modelList` | array<object> | 模特列表，用户从中选择模特绑定到商品。 选择后需额外选择试穿尺码（sizeSpecId/sizeSpecName）和试穿结果（tryOnResult）， 将各字段对应填入 goodsModelReqs 后提交保存。部分类目必填 requiredGoodsModel 为 true。 |
| `modelList[].pddkjShopModelId` | integer | 店铺模特记录ID |
| `modelList[].shopId` | integer | 店铺ID |
| `modelList[].platformModelId` | integer | 平台模特ID，保存时填入 goodsModelReqs.modelId |
| `modelList[].headPortrait` | string | 头像URL，保存时填入 goodsModelReqs.modelProfileUrl |
| `modelList[].modelType` | integer | 模特类型（0=成衣模特，1=鞋模），保存时填入 goodsModelReqs.modelType |
| `modelList[].canEdit` | integer | 是否可编辑（1=可编辑，0=不可编辑） |
| `modelList[].modelName` | string | 模特名称，保存时填入 goodsModelReqs.modelName |
| `modelList[].hipline` | string | 臀围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHip |
| `modelList[].bust` | string | 胸围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelBust |
| `modelList[].height` | string | 身高（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHeight |
| `modelList[].waist` | string | 腰围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelWaist |
| `modelList[].footLength` | string | 脚长（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootLength |
| `modelList[].footWidth` | string | 脚宽（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootWidth |
| `total` | integer | 总数 |

#### 获取类目列表

`POST /open/v1/product/collect_box/pddkj/collect_box/get_category_tree_by_site`  (文档: api-471545330)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cateTree` | object | 分类树 Map（key=cid, value=分类节点） |

#### 获取尺码模板列表

`POST /open/v1/product/collect_box/pddkj/collect_box/get_size_template_list`  (文档: api-471545331)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `isRsync` | integer |  | 是否同步 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `sizeTemplateList` | array<object> | 尺码表模板列表，先选择一个模板，再取其sizeTemplateId调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `sizeTemplateList[].sizeTemplateId` | string | 尺码表模板ID，用于调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `sizeTemplateList[].name` | string | 模板名称 |
| `sizeTemplateList[].sizeTemplateSource` | string | 模板来源 |
| `minSizeChartNum` | integer | 最少尺码表数量，创建产品时需要填写的尺码表数量 |
| `classType` | integer | 是否需要多尺码表 0否 1是 为1是 需要填写重点展示部件 collectShowSizeTemplateIds |

#### 获取尺码表详情

`POST /open/v1/product/collect_box/pddkj/collect_box/get_size_charts_by_size_template_id`  (文档: api-471545332)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `sizeTemplateId` | integer | 是 | 尺码表模板ID |
| `sizeTemplateSource` | string | 是 | 尺码表模板来源（api/erp 尺码表模板列表中有返回这个字段） |
| `refresh` | integer |  | 是否刷新 1是 0否 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `sizeTemplateId` | string | 尺码表模板ID，创建产品时sizeCharts中需传此ID |
| `sizeCharts` | object | 尺码表数据，创建产品时按此结构填写sizeCharts |
| `sizeCharts.elementIds` | array<integer> | 启用的尺码参数ID列表，必须包含sizeSpecMeta.elementList中所有necessary=true的项 |
| `sizeCharts.sizeItems` | array<object> | 尺码行数据，每行对应一个尺码（如S/M/L），sizeName必须与saleAttributes中的尺码值一致 |
| `sizeCharts.sizeItems[].sizeName` | string | 尺码名称，如"one-size"、"S"、"M"、"L"，必须与saleAttributes中尺码属性的某个值完全一致 |
| `sizeCharts.sizeItems[].elementValueList` | array<object> | 元素值列表 |
| `sizeCharts.sizeItems[].elementValueList[].elementId` | integer | 元素ID |
| `sizeCharts.sizeItems[].elementValueList[].elementValue` | string | 元素值 |
| `sizeCharts.sizeItems[].groupIdAndValueMap` | object | 分组ID与尺码名称映射 |
| `sizeCharts.elementIdAndIsRangeMap` | object | 参数ID是否支持范围值（如"12-13"），key为elementId，value为true表示支持范围 |
| `groupId` | integer | 尺码分组ID |
| `sizeSpecMeta` | object | 尺码规格元数据，elementList中的necessary=true项必须在sizeCharts.elementIds中包含 |
| `sizeSpecMeta.groupList` | array<object> | 尺码分组列表 |
| `sizeSpecMeta.groupList[].id` | integer | 分组ID |
| `sizeSpecMeta.groupList[].name` | string | 分组名称 |
| `sizeSpecMeta.groupList[].unnecessary` | boolean | 是否非必填 |
| `sizeSpecMeta.elementList` | array<object> | 所有可用的尺码参数列表，创建产品时参考此列表确定要填哪些参数，necessary=true的项必须在sizeCharts.elementIds中包含 |
| `sizeSpecMeta.elementList[].necessary` | boolean | 是否必填，为true时该参数必须包含在sizeCharts.elementIds中 |
| `sizeSpecMeta.elementList[].name` | string | 参数名称，如"胸围全围"、"衣长" |
| `sizeSpecMeta.elementList[].id` | integer | 参数ID，对应sizeItems中elementValueList的elementId |
| `sizeSpecMeta.elementList[].unit` | string | 单位，如"cm" |

#### 获取模特分类配置

`POST /open/v1/product/collect_box/pddkj/collect_box/get_model_cat_info`  (文档: api-471545333)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID，从类目选择接口获取，切换类目后传入查询该类目的模特配置 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `modelCat` | object | 模特分类配置，为 null 表示该类目不支持模特功能 enabled=1 时展示模特绑定区域，按 modelType 区分成衣模特(0)或鞋模(1)进行筛选绑定。 |
| `modelCat.cid` | integer | 类目ID |
| `modelCat.modelType` | integer | 模特类型（0=成衣模特，1=鞋模），展示模特绑定区域时按此类型筛选可用模特 |
| `modelCat.enabled` | integer | 是否启用模特（1=启用，0=禁用），为1时展示模特绑定区域 |

#### 获取采集箱列表

`POST /open/v1/product/collect_box/pddkj/collect_box/search_collect_box_detail_list`  (文档: api-471545334)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer |  | 当前页码 |
| `pageSize` | integer |  | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | string | 采集箱详情ID |
| `itemNum` | string | 商品编号 |
| `stock` | string | 库存 |
| `price` | string | 价格 |
| `thumbnail` | string | 缩略图 |
| `gmtCreate` | string | 创建时间 |
| `editModel` | string | 编辑模式 |
| `commonCollectBoxDetailId` | string | 公共采集箱详情ID |
| `appAccountId` | string | 应用账户ID |
| `subAppAccountId` | string | 子应用账户ID |
| `platform` | string | 平台 |
| `title` | string | 商品标题 |
| `remark` | string | 备注 |
| `copyType` | string | 复制类型 |
| `collectBoxGroupId` | string | 采集箱分组ID |
| `collectBoxDetailShopList` | array<object> | 预发布店铺信息列表 |
| `collectBoxDetailShopList[].shopId` | string | 店铺ID |

#### 批量删除采集箱产品接口

`POST /open/v1/product/collect_box/pddkj/collect_box/delete_collect_box_detail`  (文档: api-471545335)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successNum` | integer | 删除成功数量 |
| `failNum` | integer | 删除失败数量 |
| `errorMap` | object | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `errorMsg` | string | 拼接后的错误信息 |

#### 获取需要设置净重的类目列表

`POST /open/v1/product/collect_box/pddkj/collect_box/get_need_set_net_weight_cid_list`  (文档: api-490449047)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cidList` | array<integer> | 需要设置净重的类目列表 |

### 商品 > TEMU半托采集箱 > 商品发布

#### 发布产品

`POST /open/v1/product/collect_box/pddkj_choice/move_collect/save_move_collect_task`  (文档: api-468726294)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |
| `shopIdAndSitesMap` | object | 是 | 需要发布的店铺shopId和站点映射 key为shopId，value为该店铺下需要发布的站点列表 示例：{"shopId值":["CA","EU"],"shopId值":["CA"]} |

#### 发布记录列表

`POST /open/v1/product/collect_box/pddkj_choice/move_collect/search_move_collect_list`  (文档: api-511667358)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:20 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string |  | 产品ID |
| `filter.sourceItemId` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectDetailList` | array<object> | 发布记录列表 |
| `moveCollectDetailList[].moveCollectTaskDetailId` | string | 发布任务详情ID |
| `moveCollectDetailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `moveCollectDetailList[].shopId` | string | 店铺ID |
| `moveCollectDetailList[].itemNum` | string | 商品编号 |
| `moveCollectDetailList[].cid` | string | 类目ID |
| `moveCollectDetailList[].source` | string | 来源平台 |
| `moveCollectDetailList[].sourceSite` | string | 来源站点 |
| `moveCollectDetailList[].sourceItemId` | string | 来源商品ID |
| `moveCollectDetailList[].title` | string | 商品标题 |
| `moveCollectDetailList[].thumbnail` | string | 缩略图 |
| `moveCollectDetailList[].isTiming` | string | 是否定时发布 |
| `moveCollectDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].reason` | string | 失败原因 |
| `moveCollectDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].gmtModified` | string | 修改时间 |
| `moveCollectDetailList[].platformItemId` | string | 平台商品ID |
| `moveCollectDetailList[].isRenewItem` | boolean | 是否翻新 |
| `moveCollectDetailList[].shopName` | string | 店铺名称 |
| `moveCollectDetailList[].siteName` | string | 站点名称 |
| `moveCollectDetailList[].site` | string | 站点 |
| `moveCollectDetailList[].sourceItemUrl` | string | 来源商品链接 |
| `moveCollectDetailList[].itemEditUrl` | string | 商品编辑链接 |
| `moveCollectDetailList[].breadcrumb` | string | 类目路径 |
| `moveCollectDetailList[].ownerSubAppAccountId` | integer | 归属子账号ID |
| `moveCollectDetailList[].ownerSubAccountAliasName` | string | 归属子账号名称 |
| `total` | integer | 总数 |

### 商品 > TEMU半托采集箱 > 车型库

#### 获取车型库站点列表

`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_list`  (文档: api-468726296)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer |  | 类目ID，区分摩托车和汽车 ，不传返回全部 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsVehicleLibrarySiteList` | array<object> | 车型库站点列表，每项代表一个销售地区的车型库（如美国、欧洲等）。 根据产品的销售地区选择对应站点，取其 vehicleLibraryId 用于后续接口 |
| `goodsVehicleLibrarySiteList[].vehicleLibraryId` | integer | 车型库站点ID，选定站点后传入 getGoodsVehicleLibrarySiteTopPropDependencyList 获取顶级车型节点 |
| `goodsVehicleLibrarySiteList[].name` | string | 站点名称，如"美国"、"欧洲"，用于展示给用户选择 |
| `goodsVehicleLibrarySiteList[].pid` | integer | 属性ID |
| `goodsVehicleLibrarySiteList[].pidName` | string | 属性名称（中文），如"品牌"、"车系" |
| `goodsVehicleLibrarySiteList[].pidNameEn` | string | 属性名称（英文） |
| `goodsVehicleLibrarySiteList[].level` | integer | 层级（1=品牌，2=车系，3=年份，4=车型，5=发动机类型） |

#### 获取车型库站点属性结构映射

`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map`  (文档: api-468726297)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer |  | 类目ID，区分摩托车和汽车 ，不传返回全部 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsVehicleLibraryIdAndSitePidInfoMap` | object | 车型库站点属性结构映射，key 为 vehicleLibraryId，value 为该站点的属性层级信息列表。 用于了解某站点车型库包含哪些层级属性（品牌/车系/年款等）及其对应的 pid， 结合 getVehicleLibraryPropDependencyTree 的树形数据使用 SitePidInfo 结构： - pddkjGoodsVehicleLibraryId: string 平台商品车型库ID - vehicleLibraryId: string 车型库ID - name: string 站点名称，如"美国站、加拿大站" - pidNameEn: string 属性英文名，如"Make"、"Model"、"Year" - parentPropertyDependencyId: string 父属性依赖ID - propertyDependencyId: string 属性依赖ID - pid: string 属性pid - pidName: string 属性中文名，如"汽车品牌"、"汽车型号" - level: string 层级序号 - status: string 状态，1=启用 |

#### 获取站点顶级车型节点列表

`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list`  (文档: api-468726298)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `topGoodsVehicleLibraryPropDependencyList` | array<object> | 顶级车型节点列表（通常为品牌层），每项含 propertyValueDependencyId、vidValue 等字段。 取每项的 propertyValueDependencyId 作为 topPropertyValueDependencyId， 传入 getVehicleLibraryPropDependencyTree 获取该品牌下完整的车型树 |
| `topGoodsVehicleLibraryPropDependencyList[].pddkjGoodsVehicleLibraryPropDependencyId` | integer | 平台车型库属性依赖ID |
| `topGoodsVehicleLibraryPropDependencyList[].vehicleLibraryId` | integer | 车型库ID |
| `topGoodsVehicleLibraryPropDependencyList[].topPropertyValueDependencyId` | integer | 顶级节点propertyValueDependencyId |
| `topGoodsVehicleLibraryPropDependencyList[].parentPropertyValueDependencyId` | integer | 父节点propertyValueDependencyId，顶级节点为0 |
| `topGoodsVehicleLibraryPropDependencyList[].propertyValueDependencyId` | integer | 当前节点propertyValueDependencyId |
| `topGoodsVehicleLibraryPropDependencyList[].propertyDependencyId` | integer | 属性依赖ID |
| `topGoodsVehicleLibraryPropDependencyList[].vid` | integer | 属性值ID |
| `topGoodsVehicleLibraryPropDependencyList[].vidValue` | string | 属性值文本，如品牌名"Country Coach" |
| `topGoodsVehicleLibraryPropDependencyList[].level` | integer | 层级序号 |
| `topGoodsVehicleLibraryPropDependencyList[].isLeaf` | integer | 是否为叶子节点，0=否，1=是 |
| `topGoodsVehicleLibraryPropDependencyList[].md5BreadcrumbVidValue` | string | 面包屑属性值的MD5 |
| `topGoodsVehicleLibraryPropDependencyList[].breadcrumbVidValue` | string | 面包屑属性值文本 |
| `topGoodsVehicleLibraryPropDependencyList[].breadcrumbPropertyValueDependencyId` | integer | 面包屑属性值依赖ID |

#### 获取车型属性依赖树

`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_vehicle_library_prop_dependency_tree`  (文档: api-468726299)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |
| `topPropertyValueDependencyId` | integer | 是 | 顶级节点ID，从 getGoodsVehicleLibrarySiteTopPropDependencyList 返回的列表中取 propertyValueDependencyId |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `vehicleLibraryPropDependencyTree` | object | 车型属性依赖树，key 为顶级节点的 propertyValueDependencyId，value 为节点数据（含 children 子节点）。 树形结构按品牌→车系→年份→车型→发动机类型逐级展开，isLeaf=1 的节点为叶子节点。 选中叶子节点后，将从根节点到该叶子节点的完整路径组装为一条车型路径， 每个路径节点取 propertyValueDependencyId、vidValue、level 填入 vehicleLibraryRelationList[].productPropValueDependencyList 中 |

#### 根据类目ID查询有车型库数据的类目列表

`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_has_vehicle_library_cids_by_search_cids`  (文档: api-468726295)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cids` | array<integer> | 是 | 待查询的类目ID列表，传入产品所在类目的cid， 返回结果中包含的cid表示该类目支持车型库，发品时需填写车型适配信息 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `hasVehicleLibraryCids` | array<integer> | 有车型库的类目ID列表，如果产品所属类目在此列表中， 则发品时需要填写车型适配信息（vehicleLibrary相关字段） |

### 商品 > TEMU半托采集箱 > 采集箱

#### 获取类目属性规则

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_category_attribute_rules`  (文档: api-477347599)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array<integer> |  | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `saleAttributeRules` | array<object> | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `saleAttributeRules[].pid` | integer | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `saleAttributeRules[].templatePid` | integer | 模板属性ID，用于关联模板中的属性定义 |
| `saleAttributeRules[].refPid` | integer | 引用属性ID，表示该属性引用自哪个基础属性 |
| `saleAttributeRules[].name` | string | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `saleAttributeRules[].lang2Name` | string | 第二语言属性名称 |
| `saleAttributeRules[].isSale` | boolean | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `saleAttributeRules[].mainSale` | boolean | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `saleAttributeRules[].required` | boolean | 是否必填，为true时创建产品必须填写该属性 |
| `saleAttributeRules[].valueType` | string | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `saleAttributeRules[].controlType` | integer | 控件类型，决定前端展示方式 |
| `saleAttributeRules[].feature` | integer | 特征标记 |
| `saleAttributeRules[].chooseMaxNum` | integer | 最多可选数量，SELECT类型时最多可选几个value |
| `saleAttributeRules[].inputMaxNum` | integer | 输入最大数量，自定义输入的规格上限 |
| `saleAttributeRules[].minValue` | string | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `saleAttributeRules[].maxValue` | string | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `saleAttributeRules[].valuePrecision` | integer | 小数精度，数值保留几位小数 |
| `saleAttributeRules[].valueUnit` | array<string> | 合法单位列表，输入时必须使用列表中的单位 |
| `saleAttributeRules[].valueRule` | integer | 值规则 |
| `saleAttributeRules[].propertyValueType` | integer | 属性值类型 |
| `saleAttributeRules[].parentSpecId` | integer | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `saleAttributeRules[].parentTemplatePid` | integer | 父模板属性ID |
| `saleAttributeRules[].templatePropertyValueParentList` | array<object> | 父属性值模板ID列表，非string类型属性时使用 |
| `saleAttributeRules[].templatePropertyValueParentList[].parentVidList` | array<integer> | 父属性值ID列表 |
| `saleAttributeRules[].showCondition` | array<object> | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `saleAttributeRules[].showCondition[].parentRefPid` | integer | 父引用属性ID |
| `saleAttributeRules[].showCondition[].parentVids` | array<integer> | 父属性值ID列表 |
| `saleAttributeRules[].showType` | integer | 展示类型 |
| `saleAttributeRules[].propertyChooseTitle` | string | 属性选择标题，SELECT类型时的选择提示文字 |
| `saleAttributeRules[].numberInputTitle` | string | 数字输入标题，INPUT类型时的输入提示文字 |
| `saleAttributeRules[].referenceType` | integer | 引用类型 |
| `saleAttributeRules[].valueInputSum` | integer | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `saleAttributeRules[].values` | array<object> | 可选值列表，SELECT类型时从中选取vid和name |
| `saleAttributeRules[].values[].specId` | integer | 规格ID，自定义输入的值为null |
| `saleAttributeRules[].values[].vid` | integer | 属性值ID，填写属性时通过vid指定选中的值 |
| `saleAttributeRules[].values[].name` | string | 属性值名称，如"白色"、"XL"、"棉" |
| `saleAttributeRules[].values[].lang2Value` | string | 第二语言值 |
| `saleAttributeRules[].values[].extendInfo` | string | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `saleAttributeRules[].values[].group` | object | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `saleAttributeRules[].values[].parentVidList` | array<integer> | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| … | | 共 89 个字段，详见 openapi.json |

#### 店铺模特列表

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/search_model_list`  (文档: api-477347600)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `modelType` | integer |  | 模特类型（0=成衣模特，1=鞋模） |
| `modelName` | string |  | 模特名称模糊搜索 |
| `pageNo` | integer |  | 页码，默认1 |
| `pageSize` | integer |  | 每页条数，默认20 max:1000 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `modelList` | array<object> | 模特列表，用户从中选择模特绑定到商品。 选择后需额外选择试穿尺码（sizeSpecId/sizeSpecName）和试穿结果（tryOnResult）， 将各字段对应填入 goodsModelReqs 后提交保存。部分类目必填 requiredGoodsModel 为 true。 |
| `modelList[].pddkjChoiceShopModelId` | integer | 店铺模特记录ID |
| `modelList[].shopId` | integer | 店铺ID |
| `modelList[].platformModelId` | integer | 平台模特ID，保存时填入 goodsModelReqs.modelId |
| `modelList[].headPortrait` | string | 头像URL，保存时填入 goodsModelReqs.modelProfileUrl |
| `modelList[].modelType` | integer | 模特类型（0=成衣模特，1=鞋模），保存时填入 goodsModelReqs.modelType |
| `modelList[].canEdit` | integer | 是否可编辑（1=可编辑，0=不可编辑） |
| `modelList[].modelName` | string | 模特名称，保存时填入 goodsModelReqs.modelName |
| `modelList[].hipline` | string | 臀围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHip |
| `modelList[].bust` | string | 胸围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelBust |
| `modelList[].height` | string | 身高（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHeight |
| `modelList[].waist` | string | 腰围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelWaist |
| `modelList[].footLength` | string | 脚长（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootLength |
| `modelList[].footWidth` | string | 脚宽（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootWidth |
| `total` | integer | 总数 |

#### 获取商品基本选项

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_item_options`  (文档: api-477347601)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `outerPackageShapeOptions` | array<object> | 外包装形状选项，key/value 数组，保存到 outerPackageShape |
| `outerPackageShapeOptions[].key` | integer | 选项键值 |
| `outerPackageShapeOptions[].value` | string | 选项显示文本 |
| `outerPackageTypeOptions` | array<object> | 外包装类型选项，key/value 数组，保存到 outerPackageType |
| `outerPackageTypeOptions[].key` | integer | 选项键值 |
| `outerPackageTypeOptions[].value` | string | 选项显示文本 |
| `goodsModelTryOnResultMap` | array<object> | 模特试穿结果枚举，格式为 [{key: modelType, value: {tryOnResult: label}}]。 保存时按 modelType 取对应枚举，将所选 tryOnResult 填入 goodsModelReqs[].tryOnResult |
| `goodsModelTryOnResultMap[].key` | integer | 模特类型（modelType） |
| `goodsModelTryOnResultMap[].value` | object | 试穿结果枚举映射，key 为 tryOnResult，value 为显示文本 |
| `catIdAndProductNameMaxLengthMap` | object | 类目标题最大长度映射，key 为 cid，value 为最大字符数 |
| `suggestedPriceCurrencyTypeAndNameList` | array<object> | 建议售价币种列表，key/value 数组，保存到 skuMap[key].suggestedPriceCurrencyType |
| `suggestedPriceCurrencyTypeAndNameList[].key` | string | 选项键值 |
| `suggestedPriceCurrencyTypeAndNameList[].value` | string | 选项显示文本 |
| `skuClassificationList` | array<object> | SKU 分类类型，key/value 数组，保存到 skuMap[key].skuClassification。 1=单品（numberOfPieces 只能为1）；2=同款多件装（numberOfPieces 必须>1）； 3=混合套装（需额外填写 individuallyPacked 和 productSkuAccessories）。 部分类目此字段必填 |
| `skuClassificationList[].key` | integer | 选项键值 |
| `skuClassificationList[].value` | string | 选项显示文本 |
| `skuPieceUnitCodeList` | array<object> | 件数单位，key/value 数组，保存到 skuMap[key].pieceUnitCode。部分类目必填 |
| `skuPieceUnitCodeList[].key` | integer | 选项键值 |
| `skuPieceUnitCodeList[].value` | string | 选项显示文本 |
| `individuallyPackedList` | array<object> | 是否独立包装，key/value 数组，保存到 skuMap[key].individuallyPacked。 skuClassification 为2或3时必填 |
| `individuallyPackedList[].key` | integer | 选项键值 |
| `individuallyPackedList[].value` | string | 选项显示文本 |
| `packageLimitConfig` | object | 包装限制配置 |
| `descModuleLimitConfig` | object | 描述模块限制配置，包含 descModuleMaxTextLength（最大文本长度） |
| `netContentCidList` | array<integer> | 需要填写净含量的类目 cid 列表。 当商品 cid 在此列表中，skuClassification 为1或2时需填 netContentNumber/netContentUnitCode（取值见 netContentOptions）； skuClassification 为3时需填 totalNetContentNumber/totalNetContentUnitCode |
| `netContentOptions` | array<object> | 净含量单位选项，key/value 数组，保存到 skuMap[key].netContentUnitCode |
| `netContentOptions[].key` | integer | 选项键值 |
| `netContentOptions[].value` | string | 选项显示文本 |
| `enTitleRefTypeList` | array<object> | 英文标题参考类型选项 |
| `enTitleRefTypeList[].key` | string | 选项键值 |
| `enTitleRefTypeList[].value` | string | 选项显示文本 |
| `pieceNewUnitCodeList` | array<object> | 共计内含单位选项，key/value 数组，保存到 skuMap[key].pieceNewUnitCode |
| `pieceNewUnitCodeList[].key` | integer | 选项键值 |
| `pieceNewUnitCodeList[].value` | string | 选项显示文本 |
| `mixTypeList` | array<object> | 混合套装类型选项，key/value 数组，保存到 skuMap[key].mixedType。1=不同品，2=同品不同规格 |
| `mixTypeList[].key` | integer | 选项键值 |
| `mixTypeList[].value` | string | 选项显示文本 |
| `totalNetContentCidList` | array<integer> | 需要填写总净含量的类目 cid 列表（混合套装场景） |
| `vehicleLibraryRequiredCidList` | array<integer> | 需要填写车型库信息的类目 cid 列表 |
| `saleAttributeClothingColorMaxNum` | integer | 销售属性颜色最大数量 |
| … | | 共 45 个字段，详见 openapi.json |

#### 创建采集箱商品

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/create_collect_box_item`  (文档: api-477347602)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口。 pddkjChoice 特有：需填写 publishSiteList（发布站点）、siteAndSkuPriceMap（站点维度价格）、 siteAndWarehouseIdAndStockMap（站点+仓库库存）等 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array<string> |  | 发布站点列表，pddkjChoice 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishEuSiteList` | array<string> |  | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array<object> |  | 站点仓库列表，US 站直接填 warehouseId，EU 站填 subSiteWarehouseList |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string |  | 仓库ID，非 EU 站点时必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array<object> |  | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array<object> |  | 站点运费模板列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguageType` | integer |  | 多语言素材类型 |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguages` | array<string> |  | 多语言素材语言列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object |  | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.translateLanguages` | array<string> |  | 翻译语言列表，指定需要自动翻译的目标语言编码（如 ["en","de","es"]） |
| `siteCollectItemInfo.itemNum` | string |  | 非服饰类主货号（skuMap 同级字段，与 skuMap 内各 SKU 的 itemNum 含义不同） |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string |  | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> |  | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string |  | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string |  | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.multiLanguageImgUrlsMap` | object |  | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object |  | 店铺维度的模特信息映射，key 为 shopId，value 为该店铺对应的单条 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在此处独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.productMaterialImageUrl` | string |  | 实拍素材图URL |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string |  | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object |  | 内容 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string |  | 图片URL（type=image时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string |  | 文本内容（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object |  | 文本模块详情（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer |  | 字体大小 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string |  | 字体粗细 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string |  | 对齐方式 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string |  | 字体颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string |  | 背景颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer |  | 字体族 |
| `siteCollectItemInfo.productGuideFileUrl` | string |  | 产品说明书URL |
| `siteCollectItemInfo.productGuideFileName` | string |  | 产品说明书文件名，最多25个字 |
| `siteCollectItemInfo.outerGoodsUrl` | string |  | 外部商品链接 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<integer> |  | 展示尺码模板ID列表 |
| `siteCollectItemInfo.sizeAttributeValueGroupId` | integer |  | 尺码属性值组ID |
| `siteCollectItemInfo.sizeCharts` | array<object> |  | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> |  | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> |  | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [ {"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string |  | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer |  | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer |  | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer |  | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer |  | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer |  | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> |  | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string |  | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `siteCollectItemInfo.publishSiteList` | array<string> | 是 | 发布站点列表，如['US','JP'] 取值参考 getPublishSiteOptions接口返回的站点列表 |
| `siteCollectItemInfo.publishEuSiteList` | array<string> |  | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.siteAndSkuPriceMap` | object |  | 按站点维度的 SKU 价格映射。 key 为站点编码，value 为该站点下各 SKU 的价格信息。 欧盟站点下还需填写 subSiteAndPriceMap（子站点价格），法国站点价格必填 |
| `siteCollectItemInfo.siteShipmentLimitDayMap` | object |  | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `siteCollectItemInfo.materialMultiLanguageType` | string |  | 多语言素材类型，取值参考 PddkjChoiceConst |
| `siteCollectItemInfo.materialMultiLanguages` | array<string> |  | 多语言素材语言列表，与 materialMultiLanguageType 配合使用， 决定哪些语言需要提供多语言图片素材 |
| `siteCollectItemInfo.discreetShipping` | string |  | 保密发货，0=关闭，1=开启 |
| `siteCollectItemInfo.currency` | string |  | 币种，如 CNY、USD |
| `siteCollectItemInfo.shipmentLimitDay` | integer |  | 其他站点承诺发货时效 非定制品可选值只有 1,2 |
| `siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> |  | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | integer | 创建成功的采集箱详情ID |

#### 认领预发布店铺

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/claim_to_shop`  (文档: api-477347603)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID（需要全量保存不在这里的店铺会被取消认领） |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

#### 获取采集箱站点模式详情

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_site_collect_item_info`  (文档: api-477347606)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `editModel` | string | 编辑模式 |
| `claimToShopIds` | array<integer> | 已认领的店铺IDS |
| `siteCollectItemInfo` | object | 站点模式数据，包含商品基础信息、属性、SKU、店铺列表、发布站点等 |
| `siteCollectItemInfo.title` | string | 商品标题 |
| `siteCollectItemInfo.itemNum` | string | 非服饰类货号 |
| `siteCollectItemInfo.saleAttributes` | array<object> | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 基础属性id |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 属性id |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].name` | string | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | SKU标识码 |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 服饰类货号（服饰类的货号是SKC级别的） |
| `siteCollectItemInfo.attributes` | array<object> | 商品属性列表（成分/材质等） |
| `siteCollectItemInfo.attributes[].templatePid` | integer | 模板属性ID |
| `siteCollectItemInfo.attributes[].pid` | integer | 基础属性id |
| `siteCollectItemInfo.attributes[].refPid` | integer | 属性id |
| `siteCollectItemInfo.attributes[].name` | string | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 属性值id |
| `siteCollectItemInfo.attributes[].values[].name` | string | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 属性值单位 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 成分比例(所有成分比例之和需等于100) |
| `siteCollectItemInfo.skuMap` | object | SKU映射（key=SKU标识码，value=SKU条目） |
| `siteCollectItemInfo.sizeCharts` | array<object> | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 分组ID与值映射 |
| … | | 共 120 个字段，详见 openapi.json |

#### 保存采集箱店铺模式详情

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/save_shop_collect_item_info`  (文档: api-477347605)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.detailId` | integer | 是 | 采集箱详情ID |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.itemNum` | string |  | 非服饰类货号 |
| `shopCollectItemInfo.imgUrls` | array<string> | 是 | 类轮播图 |
| `shopCollectItemInfo.multiLanguageImgUrlsMap` | object |  | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `shopCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string |  | 类型（image=图片，text=文本） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object |  | 内容 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string |  | 图片URL（type=image时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string |  | 文本内容（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object |  | 文本模块详情（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer |  | 字体大小 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string |  | 字体粗细 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string |  | 对齐方式 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string |  | 字体颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string |  | 背景颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer |  | 字体族 |
| `shopCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `shopCollectItemInfo.productOriginProvince` | string |  | 原产省编码（原产国为中国时需要填写省份） |
| `shopCollectItemInfo.productOriginCertFiles` | array<object> |  | 原产地认证文件列表 |
| `shopCollectItemInfo.productOriginCertFiles[].fileUrl` | string |  | 文件URL |
| `shopCollectItemInfo.productOriginCertFiles[].fileName` | string |  | 文件名 |
| `shopCollectItemInfo.currency` | string |  | 店铺币种 |
| `shopCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `shopCollectItemInfo.productGuideFileUrl` | string |  | 产品说明书URL |
| `shopCollectItemInfo.productGuideFileName` | string |  | 产品说明书文件名 |
| `shopCollectItemInfo.site` | string |  | 站点（pddkjChoice 半托目前只有 sitePddKjChoice） |
| `shopCollectItemInfo.editModel` | string | 是 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.brandId` | string |  | 品牌ID |
| `shopCollectItemInfo.multiLanguageTitleMap` | object |  | 多语言标题映射 |
| `shopCollectItemInfo.sizeAttributeValueGroupId` | integer |  | 尺码属性值组ID |
| `shopCollectItemInfo.sizeCharts` | array<object> |  | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> |  | 手动录入ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `shopCollectItemInfo.vehicleLibraryRelationList` | array<object> |  | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表 |
| `shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `shopCollectItemInfo.translateLanguages` | array<string> |  | 说明书需翻译语言列表 |
| `shopCollectItemInfo.goodsModelReqs` | array<object> |  | 模特信息列表。requiredGoodsModel 为 true 的类目必填。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举 |
| `shopCollectItemInfo.goodsModelReqs[].modelId` | string | 是 | 模特ID |
| `shopCollectItemInfo.goodsModelReqs[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.goodsModelReqs[].modelName` | string | 是 | 模特名称 |
| `shopCollectItemInfo.goodsModelReqs[].modelType` | string | 是 | 模特类型 |
| `shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 是 | 模特图片URL |
| `shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 是 | 身高（cm） |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 是 | 试穿尺码规格名称 |
| `shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 是 | 试穿结果 |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 是 | 尺码规格ID |
| `shopCollectItemInfo.goodsModelReqs[].modelBust` | string |  | 胸围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelWaist` | string |  | 腰围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelHip` | string |  | 臀围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string |  | 脚长（cm），鞋类专用 |
| `shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string |  | 脚宽（cm），鞋类专用 |
| `shopCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表 |
| `shopCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `shopCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string |  | 属性值单位，没有的情况传空字符串 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer |  | 成分比例 总合需要为100 |
| `shopCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `shopCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `shopCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer |  | 属性ID |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer |  | 引用属性ID |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer |  | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer |  | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> |  | 服饰类颜色图（服饰类必填） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string |  | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `shopCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `shopCollectItemInfo.publishSiteList` | array<string> |  | 发布站点列表，pddkjChoice 必填，不能为空 |
| `shopCollectItemInfo.publishEuSiteList` | array<string> |  | 欧盟发布站点列表，有值时不能小于2个 |
| `shopCollectItemInfo.siteShipmentLimitDayMap` | object |  | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `shopCollectItemInfo.materialMultiLanguageType` | string |  | 多语言素材类型 |
| `shopCollectItemInfo.materialMultiLanguages` | array<string> |  | 多语言素材语言列表 |
| `shopCollectItemInfo.isSetSitePrice` | integer |  | 是否设置了站点价格 |
| `shopCollectItemInfo.isSetSiteStock` | integer |  | 是否设置了站点库存 |
| `shopCollectItemInfo.shipmentLimitDay` | integer |  | 其他站点承诺发货时效 非定制品可选值只有 1,2 |
| `shopCollectItemInfo.siteFreightTemplateList` | array<object> |  | 按站点维度的运费模板列表 |
| `shopCollectItemInfo.siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `shopCollectItemInfo.siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `shopCollectItemInfo.siteWarehouseList` | array<object> |  | 按站点维度的仓库列表，EU 站点下还包含 subSiteWarehouseList（欧盟子站点仓库列表） |
| `shopCollectItemInfo.siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `shopCollectItemInfo.siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.siteWarehouseList[].warehouseId` | string |  | 仓库ID，非 EU 站点时必填 |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList` | array<object> |  | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> |  | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |

#### 获取采集箱店铺模式详情

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_collect_item_info`  (文档: api-477347604)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |
| `cid` | integer |  | 新类目id（需要切换类目时填写新的cid，可以快速匹配相同属性，需要保存才能生效新的类目） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `editModel` | string | 编辑模式 |
| `claimToShopIds` | array<integer> | 已认领的店铺IDS |
| `shopCollectItemInfo` | object | 店铺模式数据，包含商品基础信息、属性、SKU、发布站点、仓库库存等 |
| `shopCollectItemInfo.title` | string | 商品标题 |
| `shopCollectItemInfo.itemNum` | string | 非服饰类货号 |
| `shopCollectItemInfo.saleAttributes` | array<object> | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer | 基础属性id |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer | 属性id |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].name` | string | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].values` | array<object> | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | SKU标识码 |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 服饰类货号（服饰类的货号是SKC级别的） |
| `shopCollectItemInfo.attributes` | array<object> | 商品属性列表（成分/材质等） |
| `shopCollectItemInfo.attributes[].templatePid` | integer | 模板属性ID |
| `shopCollectItemInfo.attributes[].pid` | integer | 基础属性id |
| `shopCollectItemInfo.attributes[].refPid` | integer | 属性id |
| `shopCollectItemInfo.attributes[].name` | string | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array<object> | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 属性值id |
| `shopCollectItemInfo.attributes[].values[].name` | string | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string | 属性值单位 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer | 成分比例(所有成分比例之和需等于100) |
| `shopCollectItemInfo.skuMap` | object | SKU映射（key=SKU标识码，value=SKU条目） |
| `shopCollectItemInfo.sizeCharts` | array<object> | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 分组ID与值映射 |
| … | | 共 111 个字段，详见 openapi.json |

#### 保存采集箱站点模式详情

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/save_site_collect_item_info`  (文档: api-477347607)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 PddkjChoice\CollectItemInfoForSave\SiteCollectItemInfoForSaveRo 注释 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array<string> |  | 发布站点列表，pddkjChoice 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishEuSiteList` | array<string> |  | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array<object> |  | 站点仓库列表，US 站直接填 warehouseId，EU 站填 subSiteWarehouseList |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string |  | 仓库ID，非 EU 站点时必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array<object> |  | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array<object> |  | 站点运费模板列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguageType` | integer |  | 多语言素材类型 |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguages` | array<string> |  | 多语言素材语言列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object |  | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.translateLanguages` | array<string> |  | 翻译语言列表，指定需要自动翻译的目标语言编码（如 ["en","de","es"]） |
| `siteCollectItemInfo.itemNum` | string |  | 非服饰类主货号（skuMap 同级字段，与 skuMap 内各 SKU 的 itemNum 含义不同） |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string |  | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> |  | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string |  | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string |  | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.multiLanguageImgUrlsMap` | object |  | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object |  | 店铺维度的模特信息映射，key 为 shopId，value 为该店铺对应的单条 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在此处独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.productMaterialImageUrl` | string |  | 实拍素材图URL |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string |  | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object |  | 内容 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string |  | 图片URL（type=image时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string |  | 文本内容（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object |  | 文本模块详情（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer |  | 字体大小 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string |  | 字体粗细 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string |  | 对齐方式 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string |  | 字体颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string |  | 背景颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer |  | 字体族 |
| `siteCollectItemInfo.productGuideFileUrl` | string |  | 产品说明书URL |
| `siteCollectItemInfo.productGuideFileName` | string |  | 产品说明书文件名，最多25个字 |
| `siteCollectItemInfo.outerGoodsUrl` | string |  | 外部商品链接 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<integer> |  | 展示尺码模板ID列表 |
| `siteCollectItemInfo.sizeAttributeValueGroupId` | integer |  | 尺码属性值组ID |
| `siteCollectItemInfo.sizeCharts` | array<object> |  | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> |  | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> |  | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [ {"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string |  | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer |  | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer |  | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer |  | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer |  | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer |  | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> |  | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string |  | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `siteCollectItemInfo.publishSiteList` | array<string> | 是 | 发布站点列表，如['US','JP'] 取值参考 getPublishSiteOptions接口返回的站点列表 |
| `siteCollectItemInfo.publishEuSiteList` | array<string> |  | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.siteAndSkuPriceMap` | object |  | 按站点维度的 SKU 价格映射。 key 为站点编码，value 为该站点下各 SKU 的价格信息。 欧盟站点下还需填写 subSiteAndPriceMap（子站点价格），法国站点价格必填 |
| `siteCollectItemInfo.siteShipmentLimitDayMap` | object |  | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `siteCollectItemInfo.materialMultiLanguageType` | string |  | 多语言素材类型，取值参考 PddkjChoiceConst |
| `siteCollectItemInfo.materialMultiLanguages` | array<string> |  | 多语言素材语言列表，与 materialMultiLanguageType 配合使用， 决定哪些语言需要提供多语言图片素材 |
| `siteCollectItemInfo.discreetShipping` | string |  | 保密发货，0=关闭，1=开启 |
| `siteCollectItemInfo.currency` | string |  | 币种，如 CNY、USD |
| `siteCollectItemInfo.shipmentLimitDay` | integer |  | 其他站点承诺发货时效 非定制品可选值只有 1,2 |

#### 获取原产地国家列表

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_country_short_name_and_name_map`  (文档: api-477347608)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `countryShortNameAndNameMap` | object | 国家简码→中文名映射，key 为 shortName（如 CN），value 为中文名（如 中国大陆）。 可用于将已保存的 productOriginCountry 短码转换为可读名称展示 |
| `productOriginCountries` | array<object> | 完整国家列表，用于渲染原产地下拉选择器。 选择某个国家后将其 shortName 填入 productOriginCountry； 选择中国（shortName=CN）时，还需从 province 列表中选择省份，将省份 code 填入 productOriginProvince |
| `productOriginCountries[].code` | string | 国家编码（如 43） |
| `productOriginCountries[].name` | string | 英文名 |
| `productOriginCountries[].shortName` | string | 国家简码，填入 productOriginCountry（如 CN、US） |
| `productOriginCountries[].chineseName` | string | 中文名 |
| `productOriginCountries[].province` | array<object> | 省份列表，仅原产国为 CN 时有值。 选择中国后需从此列表选择省份，将省份 code 填入 productOriginProvince |
| `productOriginCountries[].province[].code` | string | 省份编码，原产国为 CN 时填入 productOriginProvince |
| `productOriginCountries[].province[].name` | string | 英文名 |
| `productOriginCountries[].province[].chineseName` | string | 中文名 |

#### 获取发布站点选项

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_publish_site_options`  (文档: api-477347609)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `publishSiteOptions` | array<object> | 发布站点选项列表，用于渲染 publishSiteList 下拉框。 将选中项的 key 填入 publishSiteList； 若选择了 EU（欧盟地区），还需从 getEuropeanRegionSiteList 中选取子站点填入 publishEuSiteList， 且 publishEuSiteList 不能少于 2 个 |
| `publishSiteOptions[].key` | string | 站点编码，填入 publishSiteList（如 US、EU、DE） |
| `publishSiteOptions[].value` | string | 站点中文名，用于展示（如 美国站、欧盟地区） |
| `getEuropeanRegionSiteList` | array<object> | 欧盟子站点列表，用于渲染 publishEuSiteList 多选框。 仅当 publishSiteList 包含 EU 时需要填写； 将选中项的 site 填入 publishEuSiteList，isOpen 为 false 的子站点不可选 |
| `getEuropeanRegionSiteList[].site` | string | 欧盟子站点编码（如 DE、FR、IT），填入 publishEuSiteList |
| `getEuropeanRegionSiteList[].name` | string | 子站点中文名，用于展示（如 德国、法国） |
| `getEuropeanRegionSiteList[].siteId` | integer | 站点ID |
| `getEuropeanRegionSiteList[].isOpen` | boolean | 是否已开放，false 时前端置灰不可选 |
| `siteIdAndSiteMap` | object | siteId → 站点编码映射，key 为 siteId，value 为站点编码（如 US、DE） |

#### 获取店铺运费模板

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_freight_template`  (文档: api-477347610)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `isRsync` | integer |  | 是否同步最新数据，1 同步，0 不同步（默认 0） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopIdAndFreightTemplateListMap` | object | 店铺运费模板映射，key 为 shopId，value 为该店铺下所有站点的运费模板列表。 使用方式： 1. 取 shopIdAndFreightTemplateListMap[shopId] 获取当前店铺的模板列表； 2. 列表已按站点分组，同一站点可能有多个模板可选（展示 templateName 供用户选择）； 3. 用户为每个发布站点选定模板后，将所选条目的 templateId 作为 freightTemplateId、 site 原样填入，组成 siteFreightTemplateList 的每一项； 4. siteFreightTemplateList 须覆盖 publishSiteList 中的每个站点，否则校验失败 Map value 为运费模板列表，每一项结构如下： - templateId   string  运费模板ID - templateName string  运费模板名称，用于展示 - site         string  站点编码（如 US、EU、DE） - siteName     string  站点中文名，用于展示 |

#### 获取店铺发货仓库（支持同步）

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_warehouse`  (文档: api-477347611)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `isRsync` | integer |  | 是否同步最新数据，1 同步，0 不同步（默认 0） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopIdAndWarehouseListMap` | object | 店铺仓库映射，key 为 shopId，value 为该店铺下所有站点的仓库列表。 使用方式： 1. 取 shopIdAndWarehouseListMap[shopId] 获取当前店铺的仓库列表； 2. warehouseDisable 该字段暂时不用 不需要判断； 3. 列表已按站点分组，同一站点下可选一个或多个仓库； 4. 为每个发布站点选定仓库后，将 warehouseId 填入 siteWarehouseList[].warehouseId、 site 填入 siteWarehouseList[].site，组成 siteWarehouseList 的每一项； Map value 为仓库列表，每一项结构如下： - warehouseId    string  仓库ID，填入 siteWarehouseList[].warehouseId - warehouseName  string  仓库名称，用于展示 - site           string  站点编码（如 US、DE），填入 siteWarehouseList[].site - shopId         string  所属店铺ID - siteName       string  站点中文名，用于展示 - warehouseDisable string 该字段暂时不用 不需要判断 - managementType string  仓库管理类型。null 或 "0" 为普通仓；"3" 为其他类型仓库 |

#### 获取类目列表

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_category_tree_by_site`  (文档: api-477347612)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cateTree` | object | 分类树 Map（key=cid, value=分类节点） |

#### 获取尺码模板列表

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_size_template_list`  (文档: api-477347613)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `isRsync` | integer |  | 是否同步 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `sizeTemplateList` | array<object> | 尺码表模板列表，先选择一个模板，再取其sizeTemplateId调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `sizeTemplateList[].sizeTemplateId` | string | 尺码表模板ID，用于调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `sizeTemplateList[].name` | string | 模板名称 |
| `sizeTemplateList[].sizeTemplateSource` | string | 模板来源 |
| `minSizeChartNum` | integer | 最少尺码表数量，创建产品时需要填写的尺码表数量 |
| `classType` | integer | 是否需要多尺码表 0否 1是 为1是 需要填写重点展示部件 collectShowSizeTemplateIds |

#### 获取尺码表详情

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_size_charts_by_size_template_id`  (文档: api-477347614)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `sizeTemplateId` | integer | 是 | 尺码表模板ID |
| `sizeTemplateSource` | string | 是 | 尺码表模板来源（api/erp 尺码表模板列表中有返回这个字段） |
| `refresh` | integer |  | 是否刷新 1是 0否 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `sizeTemplateId` | string | 尺码表模板ID，创建产品时sizeCharts中需传此ID |
| `sizeCharts` | object | 尺码表数据，创建产品时按此结构填写sizeCharts |
| `sizeCharts.elementIds` | array<integer> | 启用的尺码参数ID列表，必须包含sizeSpecMeta.elementList中所有necessary=true的项 |
| `sizeCharts.sizeItems` | array<object> | 尺码行数据，每行对应一个尺码（如S/M/L），sizeName必须与saleAttributes中的尺码值一致 |
| `sizeCharts.sizeItems[].sizeName` | string | 尺码名称，如"one-size"、"S"、"M"、"L"，必须与saleAttributes中尺码属性的某个值完全一致 |
| `sizeCharts.sizeItems[].elementValueList` | array<object> | 元素值列表 |
| `sizeCharts.sizeItems[].elementValueList[].elementId` | integer | 元素ID |
| `sizeCharts.sizeItems[].elementValueList[].elementValue` | string | 元素值 |
| `sizeCharts.sizeItems[].groupIdAndValueMap` | object | 分组ID与尺码名称映射 |
| `sizeCharts.elementIdAndIsRangeMap` | object | 参数ID是否支持范围值（如"12-13"），key为elementId，value为true表示支持范围 |
| `groupId` | integer | 尺码分组ID |
| `sizeSpecMeta` | object | 尺码规格元数据，elementList中的necessary=true项必须在sizeCharts.elementIds中包含 |
| `sizeSpecMeta.groupList` | array<object> | 尺码分组列表 |
| `sizeSpecMeta.groupList[].id` | integer | 分组ID |
| `sizeSpecMeta.groupList[].name` | string | 分组名称 |
| `sizeSpecMeta.groupList[].unnecessary` | boolean | 是否非必填 |
| `sizeSpecMeta.elementList` | array<object> | 所有可用的尺码参数列表，创建产品时参考此列表确定要填哪些参数，necessary=true的项必须在sizeCharts.elementIds中包含 |
| `sizeSpecMeta.elementList[].necessary` | boolean | 是否必填，为true时该参数必须包含在sizeCharts.elementIds中 |
| `sizeSpecMeta.elementList[].name` | string | 参数名称，如"胸围全围"、"衣长" |
| `sizeSpecMeta.elementList[].id` | integer | 参数ID，对应sizeItems中elementValueList的elementId |
| `sizeSpecMeta.elementList[].unit` | string | 单位，如"cm" |

#### 获取模特分类配置

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_model_cat_info`  (文档: api-477347615)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID，从类目选择接口获取，切换类目后传入查询该类目的模特配置 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `modelCat` | object | 模特分类配置，为 null 表示该类目不支持模特功能 enabled=1 时展示模特绑定区域，按 modelType 区分成衣模特(0)或鞋模(1)进行筛选绑定。 |
| `modelCat.cid` | integer | 类目ID |
| `modelCat.modelType` | integer | 模特类型（0=成衣模特，1=鞋模），展示模特绑定区域时按此类型筛选可用模特 |
| `modelCat.enabled` | integer | 是否启用模特（1=启用，0=禁用），为1时展示模特绑定区域 |

#### 获取采集箱列表

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/search_collect_box_detail_list`  (文档: api-477347616)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer |  | 当前页码 |
| `pageSize` | integer |  | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | string | 采集箱详情ID |
| `itemNum` | string | 商品编号 |
| `stock` | string | 库存 |
| `price` | string | 价格 |
| `thumbnail` | string | 缩略图 |
| `gmtCreate` | string | 创建时间 |
| `editModel` | string | 编辑模式 |
| `commonCollectBoxDetailId` | string | 公共采集箱详情ID |
| `appAccountId` | string | 应用账户ID |
| `subAppAccountId` | string | 子应用账户ID |
| `platform` | string | 平台 |
| `title` | string | 商品标题 |
| `remark` | string | 备注 |
| `copyType` | string | 复制类型 |
| `collectBoxGroupId` | string | 采集箱分组ID |
| `collectBoxDetailShopList` | array<object> | 预发布店铺信息列表 |
| `collectBoxDetailShopList[].shopId` | string | 店铺ID |

#### 批量删除采集箱产品接口

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/delete_collect_box_detail`  (文档: api-477347617)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successNum` | integer | 删除成功数量 |
| `failNum` | integer | 删除失败数量 |
| `errorMap` | object | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `errorMsg` | string | 拼接后的错误信息 |

#### 获取包装清单属性值列表

`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_goods_accessories_list`  (文档: api-501791146)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `fuzzyValue` | string |  | 属性值模糊搜索关键词（可选 未填写默认返回前100条数据） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsAccessoriesList` | array<object> | 包装清单属性值列表，用于用户选择包装清单内容 最多返回 100 条 |
| `goodsAccessoriesList[].vid` | integer | 属性值ID |
| `goodsAccessoriesList[].unitCode` | integer | 单位编码 |
| `goodsAccessoriesList[].unitName` | string | 单位名称，用于展示 |
| `goodsAccessoriesList[].value` | string | 属性值名称 |

### 商品 > OZON采集箱 > 采集箱

#### 获取采集箱编辑币种

`POST /open/v1/product/collect_box/ozon/collect_box/get_account_setting_edit_currency`  (文档: api-474774623)

ozon采集箱涉及售价、原价、最低售价均为该币种，货源价格为CNY

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `editCurrency` | string | 编辑币种 |

#### 获取类目列表

`POST /open/v1/product/collect_box/ozon/collect_box/get_category_tree_by_site`  (文档: api-474774625)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 (暂时只支持OZON) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cateTree` | object | 分类树 Map（key=cid, value=分类节点） |

#### 获取类目属性信息

`POST /open/v1/product/collect_box/ozon/collect_box/get_category_attributes`  (文档: api-474774626)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `categoryAttributes` | array<object> | 类目属性列表 |
| `categoryAttributes[].cid` | integer | 类目ID |
| `categoryAttributes[].attrId` | integer | 属性ID |
| `categoryAttributes[].name` | string | 属性名称 |
| `categoryAttributes[].nameZh` | string | 属性中文名称 |
| `categoryAttributes[].key` | string | 属性所属类型，可以理解为该属性所代表的类型（Brand-品牌，ColorSample-颜色样本，Season-季节，Material-材料，RichContentJson-富文本JSON，SizeGridJson-尺码表JSON，DuvetCoversSize-被套尺寸，SexMaster-性别） |
| `categoryAttributes[].type` | string | 属性值填写的类型（String-字符串，Integer-整数，Decimal-浮点数） |
| `categoryAttributes[].isVariant` | integer | 是否是销售属性，（1-是，0-否） |
| `categoryAttributes[].isCollection` | integer | 是否是下来选项，（1-是，0-否） |
| `categoryAttributes[].isRequired` | integer | 是否是必填选项，（1-是，0-否） |
| `categoryAttributes[].dictionaryId` | integer | 下拉选项字典ID |
| `categoryAttributes[].dictionaryValues` | array<object> | 下拉选项值列表（前1000个） |
| `categoryAttributes[].dictionaryValues[].id` | integer | 属性值ID |
| `categoryAttributes[].dictionaryValues[].value` | string | 属性值数据 |
| `categoryAttributes[].dictionaryValues[].valueZh` | string | 属性值中文数据 |
| `categoryAttributes[].description` | string | 属性详细描述 |
| `categoryAttributes[].descriptionZh` | string | 属性中文详细描述 |
| `categoryAttributes[].tooltip` | string | 属性填写提示 |
| `categoryAttributes[].tooltipZh` | string | 属性中文填写提示 |

#### 获取采集箱列表

`POST /open/v1/product/collect_box/ozon/collect_box/search_collect_box_detail_list`  (文档: api-474774624)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer |  | 当前页码 |
| `pageSize` | integer |  | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(空字符串-全部、notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `detailList` | array<object> | 采集箱数据列表 |
| `detailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `detailList[].itemNum` | string | 商品编号 |
| `detailList[].stock` | string | 库存 |
| `detailList[].minSkuPrice` | string | 最小sku价格 |
| `detailList[].maxSkuPrice` | string | 最大sku价格 |
| `detailList[].thumbnail` | string | 缩略图 |
| `detailList[].gmtCreate` | string | 创建时间 |
| `detailList[].commonCollectBoxDetailId` | string | 公共采集箱详情ID |
| `detailList[].appAccountId` | string | 应用账户ID |
| `detailList[].subAppAccountId` | string | 子应用账户ID |
| `detailList[].platform` | string | 平台 |
| `detailList[].title` | string | 商品标题 |
| `detailList[].remark` | string | 备注 |
| `detailList[].copyType` | string | 复制类型 |
| `detailList[].collectBoxGroupId` | string | 采集箱分组ID |

#### 获取店铺仓库列表

`POST /open/v1/product/collect_box/ozon/collect_box/get_shop_warehouse_info_list`  (文档: api-474774627)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopWarehouseInfoList` | array<object> | 店铺仓库列表 |
| `shopWarehouseInfoList[].shopId` | integer | 店铺ID |
| `shopWarehouseInfoList[].shopNick` | string | 店铺名称 |
| `shopWarehouseInfoList[].warehouseList` | array<object> | 仓库列表 |
| `shopWarehouseInfoList[].warehouseList[].shopId` | string | 店铺ID |
| `shopWarehouseInfoList[].warehouseList[].warehouseId` | string | 仓库ID |
| `shopWarehouseInfoList[].warehouseList[].name` | string | 仓库名称 |
| `shopWarehouseInfoList[].warehouseList[].warehouseType` | string | 仓库类型 |
| `shopWarehouseInfoList[].warehouseList[].isRfbs` | string | 是否是RFBS仓库 |

#### 获取采集箱站点模式详情

`POST /open/v1/product/collect_box/ozon/collect_box/get_site_collect_item_info`  (文档: api-474774628)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `siteCollectItemInfo` | object | 站点数据 |
| `siteCollectItemInfo.detailId` | string | 采集箱详情ID |
| `siteCollectItemInfo.site` | string | 站点 |
| `siteCollectItemInfo.title` | string | 商品标题 |
| `siteCollectItemInfo.itemNum` | string | 合并编号 |
| `siteCollectItemInfo.notes` | string | 商品描述 |
| `siteCollectItemInfo.cid` | string | 类目ID |
| `siteCollectItemInfo.packageInfoType` | string | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `siteCollectItemInfo.packageInfo` | object | 商品级别包裹尺寸信息 |
| `siteCollectItemInfo.packageInfo.depth` | integer | 深度(长) max:99999 |
| `siteCollectItemInfo.packageInfo.height` | integer | 高度 max:99999 |
| `siteCollectItemInfo.packageInfo.width` | integer | 宽度 max:99999 |
| `siteCollectItemInfo.packageInfo.dimensionUnit` | string | 尺寸单位(毫米mm) |
| `siteCollectItemInfo.weightInfo` | object | 商品级别重量信息 |
| `siteCollectItemInfo.weightInfo.weight` | number | 重量数值 max:99999.99 |
| `siteCollectItemInfo.weightInfo.weightUnit` | string | 重量单位(g/kg) |
| `siteCollectItemInfo.vat` | string | 增值税税率(0-豁免，10-10%，20-20%) |
| `siteCollectItemInfo.skuSelectedAttrs` | array<string> | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `siteCollectItemInfo.skuMap` | object | SKU映射关系，key为saleAttributeList销售属性里valueKey用分号加首尾分号的拼接值，如：“;红色;S;” |
| `siteCollectItemInfo.saleAttributeList` | array<object> | 销售属性列表(定义变体维度及其可选值) |
| `siteCollectItemInfo.saleAttributeList[].attrId` | string | 销售属性ID |
| `siteCollectItemInfo.saleAttributeList[].name` | string | 销售属性俄文名称(如Цвет товара) |
| `siteCollectItemInfo.saleAttributeList[].nameZh` | string | 销售属性中文名称(如商品颜色) |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string | 关联属性ID |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string | 关联属性俄文名称 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string | 关联属性中文名称 |
| `siteCollectItemInfo.saleAttributeList[].attrValues` | array<object> | 销售属性值列表(所有变体选项) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 变体值唯一键(如"红色") |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 主属性值(如ColorBase的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.complexId` | integer | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.id` | string | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values` | array<object> | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].value` | string | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].dictionaryValueId` | integer | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object | 关联属性值(如ColorName的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.complexId` | integer | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.id` | string | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values` | array<object> | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].value` | string | 属性值文本值 |
| … | | 共 53 个字段，详见 openapi.json |

#### 创建采集箱站点模式数据

`POST /open/v1/product/collect_box/ozon/collect_box/create_collect_box_item`  (文档: api-474774629)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 产品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 产品描述 |
| `siteCollectItemInfo.itemNum` | string | 是 | 合并编号 |
| `siteCollectItemInfo.vat` | string | 是 | 增值税税率(0-豁免，10-10%，20-20%) |
| `siteCollectItemInfo.packageInfoType` | string | 是 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `siteCollectItemInfo.packageInfo` | object | 是 | 商品级别包裹尺寸信息 |
| `siteCollectItemInfo.packageInfo.depth` | integer |  | 深度(长) max:99999 |
| `siteCollectItemInfo.packageInfo.height` | integer |  | 高度 max:99999 |
| `siteCollectItemInfo.packageInfo.width` | integer |  | 宽度 max:99999 |
| `siteCollectItemInfo.packageInfo.dimensionUnit` | string |  | 尺寸单位(毫米mm) |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.skuSelectedAttrs` | array<string> | 是 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `siteCollectItemInfo.weightInfo` | object | 是 | 商品级别重量信息 |
| `siteCollectItemInfo.weightInfo.weight` | number |  | 重量数值 max:99999.99 |
| `siteCollectItemInfo.weightInfo.weightUnit` | string |  | 重量单位(g/kg) |
| `siteCollectItemInfo.reviewsPromoOperation` | string | 是 | 是否付费推广积分评价(enable-开启，disable-关闭) |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.mainImgAppVideoId` | integer |  | 主图应用视频ID |
| `siteCollectItemInfo.normalAttributes` | array<object> | 是 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `siteCollectItemInfo.normalAttributes[].complexId` | integer |  | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.normalAttributes[].values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.normalAttributes[].values[].value` | string |  | 属性值文本值 |
| `siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList` | array<object> | 是 | 销售属性列表(定义变体维度及其可选值) |
| `siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `siteCollectItemInfo.saleAttributeList[].nameZh` | string |  | 销售属性中文名称(如商品颜色) |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object |  | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string |  | 关联属性ID |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string |  | 关联属性俄文名称 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string |  | 关联属性中文名称 |
| `siteCollectItemInfo.saleAttributeList[].attrValues` | array<object> | 是 | 销售属性值列表(所有变体选项) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.complexId` | integer |  | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].value` | string |  | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object |  | 关联属性值(如ColorName的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.complexId` | integer |  | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].value` | string |  | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.skuMap` | object |  | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |

#### 编辑采集箱站点模式数据

`POST /open/v1/product/collect_box/ozon/collect_box/save_site_detail_data`  (文档: api-474774630)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 产品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 产品描述 |
| `siteCollectItemInfo.itemNum` | string | 是 | 合并编号 |
| `siteCollectItemInfo.vat` | string | 是 | 增值税税率(0-豁免，10-10%，20-20%) |
| `siteCollectItemInfo.packageInfoType` | string | 是 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `siteCollectItemInfo.packageInfo` | object | 是 | 商品级别包裹尺寸信息 |
| `siteCollectItemInfo.packageInfo.depth` | integer |  | 深度(长) max:99999 |
| `siteCollectItemInfo.packageInfo.height` | integer |  | 高度 max:99999 |
| `siteCollectItemInfo.packageInfo.width` | integer |  | 宽度 max:99999 |
| `siteCollectItemInfo.packageInfo.dimensionUnit` | string |  | 尺寸单位(毫米mm) |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.skuSelectedAttrs` | array<string> | 是 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `siteCollectItemInfo.weightInfo` | object | 是 | 商品级别重量信息 |
| `siteCollectItemInfo.weightInfo.weight` | number |  | 重量数值 max:99999.99 |
| `siteCollectItemInfo.weightInfo.weightUnit` | string |  | 重量单位(g/kg) |
| `siteCollectItemInfo.reviewsPromoOperation` | string | 是 | 是否付费推广积分评价(enable-开启，disable-关闭) |
| `siteCollectItemInfo.mainImgVideoUrl` | string |  | 主图视频URL |
| `siteCollectItemInfo.mainImgAppVideoId` | integer |  | 主图应用视频ID |
| `siteCollectItemInfo.normalAttributes` | array<object> | 是 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `siteCollectItemInfo.normalAttributes[].complexId` | integer |  | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.normalAttributes[].values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.normalAttributes[].values[].value` | string |  | 属性值文本值 |
| `siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList` | array<object> | 是 | 销售属性列表(定义变体维度及其可选值) |
| `siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `siteCollectItemInfo.saleAttributeList[].nameZh` | string |  | 销售属性中文名称(如商品颜色) |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object |  | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string |  | 关联属性ID |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string |  | 关联属性俄文名称 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string |  | 关联属性中文名称 |
| `siteCollectItemInfo.saleAttributeList[].attrValues` | array<object> | 是 | 销售属性值列表(所有变体选项) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.complexId` | integer |  | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].value` | string |  | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object |  | 关联属性值(如ColorName的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.complexId` | integer |  | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].value` | string |  | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.skuMap` | object |  | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |
| `detailId` | integer | 是 | 采集箱ID |

### 商品 > OZON采集箱 > 产品发布

#### 发布记录列表

`POST /open/v1/product/collect_box/ozon/move_collect/search_move_collect_list`  (文档: api-511671956)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:20 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string |  | 产品ID |
| `filter.sourceItemId` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectDetailList` | array<object> | 发布记录列表 |
| `moveCollectDetailList[].subDetailList` | array<object> | SKU对应产品发布详情 |
| `moveCollectDetailList[].subDetailList[].ozonOfferId` | string | 平台SKU |
| `moveCollectDetailList[].subDetailList[].platformItemId` | string | 产品ID |
| `moveCollectDetailList[].subDetailList[].stock` | string | 库存 |
| `moveCollectDetailList[].subDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].subDetailList[].reason` | string | 发布失败原因 |
| `moveCollectDetailList[].subDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].subDetailList[].gmtModified` | string | 更新时间 |
| `moveCollectDetailList[].moveCollectTaskDetailId` | string | 发布任务详情ID |
| `moveCollectDetailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `moveCollectDetailList[].shopId` | string | 店铺ID |
| `moveCollectDetailList[].itemNum` | string | 商品编号 |
| `moveCollectDetailList[].cid` | string | 类目ID |
| `moveCollectDetailList[].source` | string | 来源平台 |
| `moveCollectDetailList[].sourceSite` | string | 来源站点 |
| `moveCollectDetailList[].sourceItemId` | string | 来源商品ID |
| `moveCollectDetailList[].title` | string | 商品标题 |
| `moveCollectDetailList[].thumbnail` | string | 缩略图 |
| `moveCollectDetailList[].isTiming` | string | 是否定时发布 |
| `moveCollectDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].reason` | string | 失败原因 |
| `moveCollectDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].gmtModified` | string | 修改时间 |
| `moveCollectDetailList[].platformItemId` | string | 平台商品ID |
| `moveCollectDetailList[].isRenewItem` | boolean | 是否翻新 |
| `moveCollectDetailList[].shopName` | string | 店铺名称 |
| `moveCollectDetailList[].siteName` | string | 站点名称 |
| `moveCollectDetailList[].site` | string | 站点 |
| `moveCollectDetailList[].sourceItemUrl` | string | 来源商品链接 |
| `moveCollectDetailList[].itemEditUrl` | string | 商品编辑链接 |
| `moveCollectDetailList[].breadcrumb` | string | 类目路径 |
| `moveCollectDetailList[].ownerSubAppAccountId` | integer | 归属子账号ID |
| `moveCollectDetailList[].ownerSubAccountAliasName` | string | 归属子账号名称 |
| `total` | integer | 总数 |

#### 发布产品

`POST /open/v1/product/collect_box/ozon/move_collect/save_move_collect_task`  (文档: api-474774631)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

### 商品 > Shopee采集箱 > 采集箱

#### 获取站点编辑信息

`POST /open/v1/product/collect_box/shopee/collect_box/get_site_detail_simple_data`  (文档: api-480434496)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `supportSizeChartInfo` | object | 尺码图支持信息 |
| `supportSizeChartInfo.shopeeCategorySupportSizeChartId` | integer | ID |
| `supportSizeChartInfo.site` | string | 站点 |
| `supportSizeChartInfo.cid` | integer | 类目ID |
| `supportSizeChartInfo.isSupportSizeChart` | integer | 是否支持尺码图表(0,1) |
| `supportSizeChartInfo.sizeChartMandatory` | integer | 尺码表是否强制 |
| `supportSizeChartInfo.supportImageSizeChart` | integer | 是否支持图片尺码表 |
| `supportSizeChartInfo.supportTemplateSizeChart` | integer | 是否支持模板尺码表 |
| `supportSizeChartInfo.gmtCreate` | string | 创建时间 |
| `supportSizeChartInfo.gmtModified` | string | 更新时间 |
| `siteDetailSimpleData` | object | 站点信息详情 |
| `siteDetailSimpleData.cid` | integer | 类目ID |
| `siteDetailSimpleData.title` | string | 商品标题 |
| `siteDetailSimpleData.itemNum` | string | 主货号 |
| `siteDetailSimpleData.price` | string | 销售价(单规格产品时必填) |
| `siteDetailSimpleData.stock` | string | 库存(单规格产品时必填) |
| `siteDetailSimpleData.sellerStock` | array<object> | 按仓库分配库存(单规格产品时选填) |
| `siteDetailSimpleData.sellerStock[].locationId` | string | 仓库ID |
| `siteDetailSimpleData.sellerStock[].stock` | integer | 库存数量 |
| `siteDetailSimpleData.sellerStock[].shopId` | integer | 店铺ID |
| `siteDetailSimpleData.colorPropName` | string | 颜色属性名称 |
| `siteDetailSimpleData.sizePropName` | string | 尺码属性名称 |
| `siteDetailSimpleData.colorMap` | object | 颜色Map，key为颜色名 |
| `siteDetailSimpleData.sizeMap` | object | 尺码Map，key为尺码名 |
| `siteDetailSimpleData.skuMap` | object | SKU Map，key为规格组合（如;121201;;） |
| `siteDetailSimpleData.imgUrls` | array<string> | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `siteDetailSimpleData.weight` | number | 重量（kg） |
| `siteDetailSimpleData.packageLength` | string | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageWidth` | string | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageHeight` | string | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.notes` | string | 商品描述 |
| `siteDetailSimpleData.richTextDesc` | string | 富文本描述 |
| `siteDetailSimpleData.wholesaleList` | array<object> | 批发列表 |
| `siteDetailSimpleData.wholesaleList[].min` | integer | 最小数量 |
| `siteDetailSimpleData.wholesaleList[].max` | integer | 最大数量 |
| `siteDetailSimpleData.wholesaleList[].price` | number | 批发单价 |
| `siteDetailSimpleData.attributeMaps` | object | 属性Map，key为属性ID |
| `siteDetailSimpleData.brand` | object | 品牌信息 |
| `siteDetailSimpleData.brand.brandId` | integer | 品牌ID |
| `siteDetailSimpleData.brand.brandName` | string | 品牌名称 |
| … | | 共 80 个字段，详见 openapi.json |

#### 保存站点编辑数据

`POST /open/v1/product/collect_box/shopee/collect_box/save_site_detail_data`  (文档: api-516157439)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `ossMd5` | string | 是 | OSS数据的MD5值 |
| `siteDetailSimpleData` | object | 是 | 站点编辑数据（完整siteDetailSimpleData对象） |
| `siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `siteDetailSimpleData.itemNum` | string |  | 主货号 |
| `siteDetailSimpleData.price` | string |  | 销售价(单规格产品时必填) |
| `siteDetailSimpleData.stock` | string |  | 库存(单规格产品时必填) |
| `siteDetailSimpleData.sellerStock` | array<object> |  | 按仓库分配库存(单规格产品时选填) |
| `siteDetailSimpleData.sellerStock[].locationId` | string |  | 仓库ID |
| `siteDetailSimpleData.sellerStock[].stock` | integer |  | 库存数量 |
| `siteDetailSimpleData.sellerStock[].shopId` | integer |  | 店铺ID |
| `siteDetailSimpleData.colorPropName` | string |  | 颜色属性名称 |
| `siteDetailSimpleData.sizePropName` | string |  | 尺码属性名称 |
| `siteDetailSimpleData.colorMap` | object |  | 颜色Map，key为颜色名 |
| `siteDetailSimpleData.sizeMap` | object |  | 尺码Map，key为尺码名 |
| `siteDetailSimpleData.skuMap` | object |  | SKU Map，key为规格组合（如;121201;;） |
| `siteDetailSimpleData.imgUrls` | array<string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `siteDetailSimpleData.packageLength` | string |  | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageWidth` | string |  | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageHeight` | string |  | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `siteDetailSimpleData.richTextDesc` | string |  | 富文本描述 |
| `siteDetailSimpleData.wholesaleList` | array<object> |  | 批发列表 |
| `siteDetailSimpleData.wholesaleList[].min` | integer |  | 最小数量 |
| `siteDetailSimpleData.wholesaleList[].max` | integer |  | 最大数量 |
| `siteDetailSimpleData.wholesaleList[].price` | number |  | 批发单价 |
| `siteDetailSimpleData.attributeMaps` | object |  | 属性Map，key为属性ID |
| `siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `siteDetailSimpleData.brand.brandId` | integer |  | 品牌ID |
| `siteDetailSimpleData.brand.brandName` | string |  | 品牌名称 |
| `siteDetailSimpleData.logisticList` | array<object> | 是 | 物流方式列表 |
| `siteDetailSimpleData.logisticList[].logisticId` | string |  | 物流方式ID |
| `siteDetailSimpleData.logisticList[].logisticName` | string |  | 物流方式名称 |
| `siteDetailSimpleData.logisticList[].enabled` | boolean |  | 是否启用 |
| `siteDetailSimpleData.logisticList[].estimatedShippingFee` | number |  | 预估运费 |
| `siteDetailSimpleData.logisticList[].isFree` | boolean |  | 是否包邮 |
| `siteDetailSimpleData.logisticList[].sizeId` | integer |  | 尺寸ID |
| `siteDetailSimpleData.logisticList[].customPrice` | string |  | 自定义运费 |
| `siteDetailSimpleData.logisticList[].site` | string |  | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `siteDetailSimpleData.daysToShip` | integer |  | 发货天数 |
| `siteDetailSimpleData.sizeChart` | string |  | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `siteDetailSimpleData.mainImgVideoUrl` | string |  | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `siteDetailSimpleData.mainImgAppVideoId` | integer |  | 产品视频AppVideoId |
| `siteDetailSimpleData.mainImgVideoExpire` | string |  | 产品视频过期时间 |
| `siteDetailSimpleData.isMainImgVideoExpire` | integer |  | 产品视频是否过期 |
| `siteDetailSimpleData.originPrice` | string |  | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `siteDetailSimpleData.colorPropGroupName` | string |  | 颜色属性分组名称 |
| `siteDetailSimpleData.sizePropGroupName` | string |  | 尺码属性分组名称 |
| `siteDetailSimpleData.preOrderType` | string |  | 否按SKU配置出货天数，枚举值：spu/sku |
| `siteDetailSimpleData.sizeChartType` | string |  | 尺码表类型，部分类目必填，枚举值：template/image |
| `siteDetailSimpleData.shopIdAndSizeChartIdMap` | object |  | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `siteDetailSimpleData.certificationInfoList` | array<object> |  | 商品认证信息列表 |
| `siteDetailSimpleData.certificationInfoList[].certificationType` | integer |  | 认证类型ID |
| `siteDetailSimpleData.certificationInfoList[].certificationNo` | string |  | 认证编码 |
| `siteDetailSimpleData.certificationInfoList[].expireTime` | integer |  | 过期时间(时间戳，例如1782748800) |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs` | array<object> |  |  |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string |  | 文件类型 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string |  | 文件名 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string |  | 文件URL |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer |  | 文件UUID(例如：1782467304138) |
| `siteDetailSimpleData.certificationInfoList[].permitId` | integer |  | 认证ID |
| `siteDetailSimpleData.certificationInfoList[].name` | string |  | 认证名称 |
| `siteDetailSimpleData.isSuppSizechart` | integer |  | 是否支持尺码表 |
| `siteDetailSimpleData.hasTranslate` | integer |  | 是否已翻译（1=是） |
| `siteDetailSimpleData.barcode` | string |  | 识别码 |
| `siteDetailSimpleData.barcodeType` | string |  | 识别码类型 |
| `syncSites` | array<string> |  | 需要同步的其他站点列表 |
| `syncSiteFields` | array<string> |  | 需要同步的站点字段列表 |
| `shopIdAndSizeChartIdMap` | object |  | 店铺ID与尺码表ID映射 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string | OSS数据的MD5值 |
| `syncErrors` | array<object> | 同步错误列表 |
| `syncErrors[].site` | string | 站点 |
| `syncErrors[].errorMsg` | string | 错误信息 |

#### 创建采集箱SPU（手动添加商品）

`POST /open/v1/product/collect_box/shopee/collect_box/create_collect_box_item`  (文档: api-516157440)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData` | object | 是 | 站点编辑数据（完整siteDetailSimpleData对象） |
| `siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `siteDetailSimpleData.itemNum` | string |  | 主货号 |
| `siteDetailSimpleData.price` | string |  | 销售价(单规格产品时必填) |
| `siteDetailSimpleData.stock` | string |  | 库存(单规格产品时必填) |
| `siteDetailSimpleData.sellerStock` | array<object> |  | 按仓库分配库存(单规格产品时选填) |
| `siteDetailSimpleData.sellerStock[].locationId` | string |  | 仓库ID |
| `siteDetailSimpleData.sellerStock[].stock` | integer |  | 库存数量 |
| `siteDetailSimpleData.sellerStock[].shopId` | integer |  | 店铺ID |
| `siteDetailSimpleData.colorPropName` | string |  | 颜色属性名称 |
| `siteDetailSimpleData.sizePropName` | string |  | 尺码属性名称 |
| `siteDetailSimpleData.colorMap` | object |  | 颜色Map，key为颜色名 |
| `siteDetailSimpleData.sizeMap` | object |  | 尺码Map，key为尺码名 |
| `siteDetailSimpleData.skuMap` | object |  | SKU Map，key为规格组合（如;121201;;） |
| `siteDetailSimpleData.imgUrls` | array<string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `siteDetailSimpleData.packageLength` | string |  | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageWidth` | string |  | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageHeight` | string |  | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `siteDetailSimpleData.richTextDesc` | string |  | 富文本描述 |
| `siteDetailSimpleData.wholesaleList` | array<object> |  | 批发列表 |
| `siteDetailSimpleData.wholesaleList[].min` | integer |  | 最小数量 |
| `siteDetailSimpleData.wholesaleList[].max` | integer |  | 最大数量 |
| `siteDetailSimpleData.wholesaleList[].price` | number |  | 批发单价 |
| `siteDetailSimpleData.attributeMaps` | object |  | 属性Map，key为属性ID |
| `siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `siteDetailSimpleData.brand.brandId` | integer |  | 品牌ID |
| `siteDetailSimpleData.brand.brandName` | string |  | 品牌名称 |
| `siteDetailSimpleData.logisticList` | array<object> | 是 | 物流方式列表 |
| `siteDetailSimpleData.logisticList[].logisticId` | string |  | 物流方式ID |
| `siteDetailSimpleData.logisticList[].logisticName` | string |  | 物流方式名称 |
| `siteDetailSimpleData.logisticList[].enabled` | boolean |  | 是否启用 |
| `siteDetailSimpleData.logisticList[].estimatedShippingFee` | number |  | 预估运费 |
| `siteDetailSimpleData.logisticList[].isFree` | boolean |  | 是否包邮 |
| `siteDetailSimpleData.logisticList[].sizeId` | integer |  | 尺寸ID |
| `siteDetailSimpleData.logisticList[].customPrice` | string |  | 自定义运费 |
| `siteDetailSimpleData.logisticList[].site` | string |  | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `siteDetailSimpleData.daysToShip` | integer |  | 发货天数 |
| `siteDetailSimpleData.sizeChart` | string |  | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `siteDetailSimpleData.mainImgVideoUrl` | string |  | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `siteDetailSimpleData.mainImgAppVideoId` | integer |  | 产品视频AppVideoId |
| `siteDetailSimpleData.mainImgVideoExpire` | string |  | 产品视频过期时间 |
| `siteDetailSimpleData.isMainImgVideoExpire` | integer |  | 产品视频是否过期 |
| `siteDetailSimpleData.originPrice` | string |  | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `siteDetailSimpleData.colorPropGroupName` | string |  | 颜色属性分组名称 |
| `siteDetailSimpleData.sizePropGroupName` | string |  | 尺码属性分组名称 |
| `siteDetailSimpleData.preOrderType` | string |  | 否按SKU配置出货天数，枚举值：spu/sku |
| `siteDetailSimpleData.sizeChartType` | string |  | 尺码表类型，部分类目必填，枚举值：template/image |
| `siteDetailSimpleData.shopIdAndSizeChartIdMap` | object |  | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `siteDetailSimpleData.certificationInfoList` | array<object> |  | 商品认证信息列表 |
| `siteDetailSimpleData.certificationInfoList[].certificationType` | integer |  | 认证类型ID |
| `siteDetailSimpleData.certificationInfoList[].certificationNo` | string |  | 认证编码 |
| `siteDetailSimpleData.certificationInfoList[].expireTime` | integer |  | 过期时间(时间戳，例如1782748800) |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs` | array<object> |  |  |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string |  | 文件类型 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string |  | 文件名 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string |  | 文件URL |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer |  | 文件UUID(例如：1782467304138) |
| `siteDetailSimpleData.certificationInfoList[].permitId` | integer |  | 认证ID |
| `siteDetailSimpleData.certificationInfoList[].name` | string |  | 认证名称 |
| `siteDetailSimpleData.isSuppSizechart` | integer |  | 是否支持尺码表 |
| `siteDetailSimpleData.hasTranslate` | integer |  | 是否已翻译（1=是） |
| `siteDetailSimpleData.barcode` | string |  | 识别码 |
| `siteDetailSimpleData.barcodeType` | string |  | 识别码类型 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | integer | 采集箱详情ID |

#### 获取采集箱产品的源数据

`POST /open/v1/product/collect_box/shopee/collect_box/get_collect_box_item_detail`  (文档: api-516157441)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `itemDetail` | object | 采集箱详情数据 |
| `itemDetail.title` | string | 标题 |
| `itemDetail.notes` | string | 简易描述 |
| `itemDetail.richTextDesc` | string | 图文描述 |
| `itemDetail.colorPropName` | string | 颜色属性名称（规格1属性名称） |
| `itemDetail.sizePropName` | string | 尺码属性名称(规格2属性名称) |
| `itemDetail.skuMap` | object | SKU映射 (多规格产品必填 |
| `itemDetail.colorMap` | object | 颜色映射 (多规格产品必填) |
| `itemDetail.sizeMap` | object | 尺寸映射 (多规格产品必填 |
| `itemDetail.imagePaths` | array<string> | 图片路径列表 |
| `itemDetail.sourceAttrs` | array<object> | 来源属性列表 |
| `itemDetail.sourceAttrs[].name` | string | 属性名 |
| `itemDetail.sourceAttrs[].value` | string | 属性值 |
| `itemDetail.brandName` | string | 品牌名称 |
| `itemDetail.itemNum` | string | 商品编码 |
| `itemDetail.width` | string | 宽度 |
| `itemDetail.length` | string | 长度 |
| `itemDetail.height` | string | 高度 |
| `itemDetail.weight` | number | 重量（kg） |
| `itemDetail.videoInfo` | object | 视频信息 |
| `itemDetail.videoInfo.videoUrl` | string | 视频url |
| `itemDetail.videoInfo.coverUrl` | string | 封面视频url |
| `itemDetail.appAccountId` | string | 应用账户ID |
| `itemDetail.subAppAccountId` | string | 子应用账户ID |
| `itemDetail.sourceItemId` | string | 来源商品ID |
| `itemDetail.source` | string | 来源 |
| `itemDetail.site` | string | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `itemDetail.price` | number | 价格 (单规格产品时必填) |
| `itemDetail.stock` | integer | 库存 (单规格产品时必填) |
| `itemDetail.packageLength` | string | 包裹长度 |
| `itemDetail.packageWidth` | string | 包裹宽度 |
| `itemDetail.packageHeight` | string | 包裹高度 |
| `itemDetail.imgUrls` | array<string> | 图片URL列表 |
| `itemDetail.mainImgVideoUrl` | string | 主图视频URL |
| `itemDetail.mainImgAppVideoId` | integer | 主图应用视频ID |
| `itemDetail.isPreOrder` | integer | 是否预售 (0,1) |
| `itemDetail.daysToShip` | integer | 预购天数（当isPreOrder=1时必填） |
| `itemDetail.preOrderType` | string | 是否按SKU配置出货天数，枚举值：spu/sku |
| `ossMd5` | string | OSS数据的MD5值 |

#### 保存采集箱产品源数据信息

`POST /open/v1/product/collect_box/shopee/collect_box/save_edit_item`  (文档: api-516157442)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | string | 是 | 采集箱ID |
| `itemDetail` | object | 是 | 采集箱详情数据 |
| `itemDetail.title` | string | 是 | 标题 |
| `itemDetail.notes` | string | 是 | 简易描述 |
| `itemDetail.richTextDesc` | string |  | 图文描述 |
| `itemDetail.colorPropName` | string |  | 颜色属性名称（规格1属性名称） |
| `itemDetail.sizePropName` | string |  | 尺码属性名称(规格2属性名称) |
| `itemDetail.skuMap` | object |  | SKU映射 (多规格产品必填 |
| `itemDetail.colorMap` | object |  | 颜色映射 (多规格产品必填) |
| `itemDetail.sizeMap` | object |  | 尺寸映射 (多规格产品必填 |
| `itemDetail.imagePaths` | array<string> |  | 图片路径列表 |
| `itemDetail.sourceAttrs` | array<object> |  | 来源属性列表 |
| `itemDetail.sourceAttrs[].name` | string |  | 属性名 |
| `itemDetail.sourceAttrs[].value` | string |  | 属性值 |
| `itemDetail.brandName` | string |  | 品牌名称 |
| `itemDetail.itemNum` | string |  | 商品编码 |
| `itemDetail.width` | string |  | 宽度 |
| `itemDetail.length` | string |  | 长度 |
| `itemDetail.height` | string |  | 高度 |
| `itemDetail.weight` | number | 是 | 重量（kg） |
| `itemDetail.videoInfo` | object |  | 视频信息 |
| `itemDetail.videoInfo.videoUrl` | string |  | 视频url |
| `itemDetail.videoInfo.coverUrl` | string |  | 封面视频url |
| `itemDetail.appAccountId` | string |  | 应用账户ID |
| `itemDetail.subAppAccountId` | string |  | 子应用账户ID |
| `itemDetail.sourceItemId` | string |  | 来源商品ID |
| `itemDetail.source` | string |  | 来源 |
| `itemDetail.site` | string |  | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `itemDetail.price` | number |  | 价格 (单规格产品时必填) |
| `itemDetail.stock` | integer |  | 库存 (单规格产品时必填) |
| `itemDetail.packageLength` | string |  | 包裹长度 |
| `itemDetail.packageWidth` | string |  | 包裹宽度 |
| `itemDetail.packageHeight` | string |  | 包裹高度 |
| `itemDetail.imgUrls` | array<string> | 是 | 图片URL列表 |
| `itemDetail.mainImgVideoUrl` | string |  | 主图视频URL |
| `itemDetail.mainImgAppVideoId` | integer |  | 主图应用视频ID |
| `itemDetail.isPreOrder` | integer | 是 | 是否预售 (0,1) |
| `itemDetail.daysToShip` | integer |  | 预购天数（当isPreOrder=1时必填） |
| `itemDetail.preOrderType` | string |  | 是否按SKU配置出货天数，枚举值：spu/sku |
| `ossMd5` | string | 是 | OSS标识 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `ossMd5` | string |  |

#### 获取采集箱列表

`POST /open/v1/product/collect_box/shopee/collect_box/search_collect_box_detail_list`  (文档: api-516157443)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer |  | 当前页码 |
| `pageSize` | integer |  | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `detailList` | array<object> | 采集箱数据列表 |
| `detailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `detailList[].itemNum` | string | 商品编号 |
| `detailList[].stock` | string | 库存 |
| `detailList[].price` | string | 价格 |
| `detailList[].thumbnail` | string | 缩略图 |
| `detailList[].gmtCreate` | string | 创建时间 |
| `detailList[].editModel` | string | 编辑模式 |
| `detailList[].commonCollectBoxDetailId` | string | 公共采集箱详情ID |
| `detailList[].appAccountId` | string | 应用账户ID |
| `detailList[].subAppAccountId` | string | 子应用账户ID |
| `detailList[].platform` | string | 平台 |
| `detailList[].title` | string | 商品标题 |
| `detailList[].remark` | string | 备注 |
| `detailList[].copyType` | string | 复制类型 |
| `detailList[].collectBoxGroupId` | string | 采集箱分组ID |
| `detailList[].collectBoxDetailShopList` | array<object> | 预发布店铺信息列表 |
| `detailList[].collectBoxDetailShopList[].shopId` | string | 店铺ID |

#### 获取品牌列表

`POST /open/v1/product/collect_box/shopee/collect_box/get_brand_list`  (文档: api-516157444)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `isMandatory` | boolean | 品牌是否必填 |
| `inputType` | string | 输入类型 |
| `brandList` | array<object> | 品牌列表 |
| `brandList[].brandId` | integer | 品牌ID |
| `brandList[].brandName` | string | 品牌名称 |
| `gmtModified` | string | 最后修改时间 |
| `isFromOss` | boolean | 是否来自OSS缓存 |

#### 根据站点获取运费模板(物流方式)

`POST /open/v1/product/collect_box/shopee/collect_box/get_logistic_options_by_site`  (文档: api-516157445)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `label` | string | 物流选项标签 |
| `value` | string | 物流选项值 |
| `feeType` | string | 运费类型 |
| `isEnableEditShippingFee` | boolean | 是否允许编辑运费 |

#### 获取类目树

`POST /open/v1/product/collect_box/shopee/collect_box/get_category_tree_by_site`  (文档: api-516157446)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 如: TW, ID, MY, SHOPEEGLOBAL |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cateTree` | object | 分类树 Map（key=cid, value=分类节点） |

#### 获取类目属性信息

`POST /open/v1/product/collect_box/shopee/collect_box/get_category_attributes`  (文档: api-516158667)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `categoryAttributes` | array<object> | 类目属性列表 |
| `categoryAttributes[].attributeId` | integer | 属性ID |
| `categoryAttributes[].attributeUnit` | array<string> | 属性参数单位值（单选，前面一般跟数字配对） |
| `categoryAttributes[].attributeValueList` | array<object> | 属性选项（单选选或者多选） |
| `categoryAttributes[].attributeValueList[].valueId` | integer | 属性值ID |
| `categoryAttributes[].attributeValueList[].displayValueName` | string | 属性值名称 |
| `categoryAttributes[].attributeValueList[].originalValueName` | string | 原始属性值名称 |
| `categoryAttributes[].displayAttributeName` | string | 属性别名（一般中文） |
| `categoryAttributes[].formatType` | string | 属性参数格式类型（NORMAL，QUANTITATIVE，YEAR_MONTH_DATE，YEAR_MONTH） |
| `categoryAttributes[].inputType` | string | 属性内容类型（DROP_DOWN,MULTIPLE_SELECT,TEXT_FILED,COMBO_BOX,MULTIPLE_SELECT_COMBO_BOX） |
| `categoryAttributes[].inputValidationType` | string | 属性内容校验类型（INT_TYPE STRING_TYPE ENUM_TYPE FLOAT_TYPE DATE_TYPE TIMESTAMP_TYPE） |
| `categoryAttributes[].isMandatory` | boolean | 是否必填 |
| `categoryAttributes[].maxInputValueNumber` | integer | 最大输入值数量（一般选项限制使用） |
| `categoryAttributes[].originalAttributeName` | string | 接口原始属性名 |

#### 获取仓库信息列表

`POST /open/v1/product/collect_box/shopee/collect_box/get_global_shop_warehouse`  (文档: api-516158668)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `warehouseLocationList` | array<object> | 仓库信息列表 |
| `warehouseLocationList[].locationId` | string | 属性ID |
| `warehouseLocationList[].shopName` | string | 店铺别名 |
| `warehouseLocationList[].warehouseLocationType` | string | 仓库类型（local本土，cb跨境） |
| `warehouseLocationList[].warehouseName` | string | 仓库名称 |

### 商品 > Shopee采集箱 > 商品发布

#### 发布记录列表

`POST /open/v1/product/collect_box/shopee/move_collect/search_move_collect_list`  (文档: api-511672303)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:20 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string |  | 产品ID |
| `filter.sourceItemId` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectDetailList` | array<object> | 发布记录列表 |
| `moveCollectDetailList[].moveCollectTaskDetailId` | string | 发布任务详情ID |
| `moveCollectDetailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `moveCollectDetailList[].shopId` | string | 店铺ID |
| `moveCollectDetailList[].itemNum` | string | 商品编号 |
| `moveCollectDetailList[].cid` | string | 类目ID |
| `moveCollectDetailList[].source` | string | 来源平台 |
| `moveCollectDetailList[].sourceSite` | string | 来源站点 |
| `moveCollectDetailList[].sourceItemId` | string | 来源商品ID |
| `moveCollectDetailList[].title` | string | 商品标题 |
| `moveCollectDetailList[].thumbnail` | string | 缩略图 |
| `moveCollectDetailList[].isTiming` | string | 是否定时发布 |
| `moveCollectDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].reason` | string | 失败原因 |
| `moveCollectDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].gmtModified` | string | 修改时间 |
| `moveCollectDetailList[].platformItemId` | string | 平台商品ID |
| `moveCollectDetailList[].isRenewItem` | boolean | 是否翻新 |
| `moveCollectDetailList[].shopName` | string | 店铺名称 |
| `moveCollectDetailList[].siteName` | string | 站点名称 |
| `moveCollectDetailList[].site` | string | 站点 |
| `moveCollectDetailList[].sourceItemUrl` | string | 来源商品链接 |
| `moveCollectDetailList[].itemEditUrl` | string | 商品编辑链接 |
| `moveCollectDetailList[].breadcrumb` | string | 类目路径 |
| `moveCollectDetailList[].ownerSubAppAccountId` | integer | 归属子账号ID |
| `moveCollectDetailList[].ownerSubAccountAliasName` | string | 归属子账号名称 |
| `total` | integer | 总数 |

#### 提交全球商品发布到店铺任务

`POST /open/v1/product/collect_box/shopee/move_collect/save_move_collect_global_task`  (文档: api-480434554)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopeeGlobalItemIds` | array<integer> | 是 | 全球商品ID |
| `shopIds` | array<integer> | 是 | 店铺ID |
| `isUseShopeeGlobalSetting` | integer |  | 是否使用全球发布配置;1是,0否 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectTaskDetailIds` | array<integer> | 任务ID |

#### 采集箱产品发布任务

`POST /open/v1/product/collect_box/shopee/move_collect/save_move_collect_task`  (文档: api-480434555)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

### 商品 > 在线产品管理 > Shopee全球在线产品管理

#### 全球产品搜索

`POST /open/v1/product/item/shopee_global/item/search_item_list`  (文档: api-480434401)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 页码，默认1 |
| `pageSize` | integer | 是 | 每页条数，默认20 max:100 |
| `filter` | object | 是 | 搜索条件 |
| `filter.shopId` | string | 是 | 店铺ID(必传,性能问题无法支持多店铺检索) |
| `filter.platformItemId` | string |  | 平台产品ID |
| `filter.itemNum` | string |  | 主货号 |
| `filter.cids` | array<integer> |  | 类目ID |
| `filter.status` | string |  | 产品状态 |
| `filter.title` | string |  | 标题 |
| `filter.minStock` | string |  | 最小库存 |
| `filter.maxStock` | string |  | 最大库存 |
| `filter.publishedProductStatus` | string |  | 发布产品状态 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `itemList` | array<object> | 产品列表 |
| `itemList[].shopId` | string | 店铺ID |
| `itemList[].itemId` | string | 产品ID |
| `itemList[].platformItemId` | string | 平台产品ID |
| `itemList[].title` | string | 标题 |
| `itemList[].picUrl` | string | 产品图片链接 |
| `itemList[].salePrice` | string | 售价 |
| `itemList[].stock` | string | 库存 |
| `itemList[].itemNum` | string | 主货号 |
| `itemList[].platformStatus` | string | 发布状态 |
| `itemList[].status` | string | 产品状态 |
| `itemList[].weight` | string | 重量 |
| `itemList[].gmtCreate` | string | 创建时间 |
| `total` | integer | 总数 |

#### 全球产品详情（返回官方

`POST /open/v1/product/item/shopee_global/item/get_item_detail`  (文档: api-480434402)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemId` | string | 是 | 平台产品ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `itemInfo` | object | 全球商品详情 |
| `itemInfo.globalItemId` | integer | Shopee 全球商品唯一标识 |
| `itemInfo.globalItemName` | string | 全球商品名称 |
| `itemInfo.description` | string | 全球商品描述 |
| `itemInfo.globalItemSku` | string | 全球商品 SKU |
| `itemInfo.globalItemStatus` | string | 商品状态（NORMAL） |
| `itemInfo.createTime` | integer | 创建时间戳 |
| `itemInfo.updateTime` | integer | 更新时间戳 |
| `itemInfo.stockInfo` | array<object> | 库存信息（无规格时返回） |
| `itemInfo.stockInfo[].stockType` | integer | 库存类型 |
| `itemInfo.stockInfo[].stockLocationId` | string | 库存位置 ID |
| `itemInfo.stockInfo[].normalStock` | integer | 正常库存 |
| `itemInfo.stockInfo[].reservedStock` | integer | 预留库存 |
| `itemInfo.priceInfo` | array<object> | 价格信息（无规格时返回） |
| `itemInfo.priceInfo[].currency` | string | 币种 |
| `itemInfo.priceInfo[].originalPrice` | number | 原价 |
| `itemInfo.priceInfo[].sipItemPrice` | number | SIP 商品价格 |
| `itemInfo.priceInfo[].sipItemPriceSource` | string | SIP 价格来源（auto / manual） |
| `itemInfo.image` | object | 图片信息 |
| `itemInfo.image.imageIdList` | array<string> | 图片 ID 列表 |
| `itemInfo.image.imageUrlList` | array<string> | 图片 URL 列表 |
| `itemInfo.weight` | string | 重量，单位 KG |
| `itemInfo.dimension` | object | 包裹尺寸 |
| `itemInfo.dimension.packageLength` | integer | 包裹长度，单位 CM |
| `itemInfo.dimension.packageWidth` | integer | 包裹宽度，单位 CM |
| `itemInfo.dimension.packageHeight` | integer | 包裹高度，单位 CM |
| `itemInfo.preOrder` | object | 预售信息 |
| `itemInfo.preOrder.daysToShip` | integer | 发货天数（DTS） |
| `itemInfo.sizeChart` | string | 尺码表图片 URL |
| `itemInfo.condition` | string | 是否二手（NEW / USED） |
| `itemInfo.hasModel` | boolean | 是否包含规格 |
| `itemInfo.video` | array<object> | 视频信息(获取商品详情时此字段有值, 编辑时此字段无效) |
| `itemInfo.video[].videoUrl` | string | 视频 URL |
| `itemInfo.video[].thumbnailUrl` | string | 视频缩略图 URL |
| `itemInfo.video[].duration` | integer | 视频时长，单位秒 |
| `itemInfo.videoUploadId` | string | 视频ID (通过上传视频接口获取，编辑商品时此字段用于更新商品视频) |
| `itemInfo.categoryId` | integer | 分类 ID |
| `itemInfo.brand` | object | 品牌信息 |
| `itemInfo.brand.brandId` | integer | 品牌 ID |
| `itemInfo.brand.originalBrandName` | string | 品牌原始名称 |
| … | | 共 95 个字段，详见 openapi.json |

#### 保存产品编辑

`POST /open/v1/product/item/shopee_global/item/save_edit_item`  (文档: api-480434403)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `itemInfo` | object | 是 | 全球商品详情（前端修改后的 GetItemDetailVo.itemInfo，仅传新数据） |
| `itemInfo.globalItemId` | integer | 是 | Shopee 全球商品唯一标识 |
| `itemInfo.globalItemName` | string |  | 全球商品名称 |
| `itemInfo.description` | string |  | 全球商品描述 |
| `itemInfo.globalItemSku` | string |  | 全球商品 SKU |
| `itemInfo.globalItemStatus` | string |  | 商品状态（NORMAL） |
| `itemInfo.createTime` | integer |  | 创建时间戳 |
| `itemInfo.updateTime` | integer |  | 更新时间戳 |
| `itemInfo.stockInfo` | array<object> |  | 库存信息（无规格时返回） |
| `itemInfo.stockInfo[].stockType` | integer |  | 库存类型 |
| `itemInfo.stockInfo[].stockLocationId` | string |  | 库存位置 ID |
| `itemInfo.stockInfo[].normalStock` | integer |  | 正常库存 |
| `itemInfo.stockInfo[].reservedStock` | integer |  | 预留库存 |
| `itemInfo.priceInfo` | array<object> |  | 价格信息（无规格时返回） |
| `itemInfo.priceInfo[].currency` | string |  | 币种 |
| `itemInfo.priceInfo[].originalPrice` | number |  | 原价 |
| `itemInfo.priceInfo[].sipItemPrice` | number |  | SIP 商品价格 |
| `itemInfo.priceInfo[].sipItemPriceSource` | string |  | SIP 价格来源（auto / manual） |
| `itemInfo.image` | object |  | 图片信息 |
| `itemInfo.image.imageIdList` | array<string> | 是 | 图片 ID 列表 |
| `itemInfo.image.imageUrlList` | array<string> |  | 图片 URL 列表 |
| `itemInfo.weight` | string |  | 重量，单位 KG |
| `itemInfo.dimension` | object |  | 包裹尺寸 |
| `itemInfo.dimension.packageLength` | integer |  | 包裹长度，单位 CM |
| `itemInfo.dimension.packageWidth` | integer |  | 包裹宽度，单位 CM |
| `itemInfo.dimension.packageHeight` | integer |  | 包裹高度，单位 CM |
| `itemInfo.preOrder` | object |  | 预售信息 |
| `itemInfo.preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `itemInfo.sizeChart` | string |  | 尺码表图片 URL |
| `itemInfo.condition` | string |  | 是否二手（NEW / USED） |
| `itemInfo.hasModel` | boolean |  | 是否包含规格 |
| `itemInfo.video` | array<object> |  | 视频信息(获取商品详情时此字段有值, 编辑时此字段无效) |
| `itemInfo.video[].videoUrl` | string |  | 视频 URL |
| `itemInfo.video[].thumbnailUrl` | string |  | 视频缩略图 URL |
| `itemInfo.video[].duration` | integer |  | 视频时长，单位秒 |
| `itemInfo.videoUploadId` | string |  | 视频ID (通过上传视频接口获取，编辑商品时此字段用于更新商品视频) |
| `itemInfo.categoryId` | integer |  | 分类 ID |
| `itemInfo.brand` | object |  | 品牌信息 |
| `itemInfo.brand.brandId` | integer |  | 品牌 ID |
| `itemInfo.brand.originalBrandName` | string |  | 品牌原始名称 |
| `itemInfo.attributeList` | array<object> |  | 属性列表 |
| `itemInfo.attributeList[].attributeId` | integer |  | 属性 ID |
| `itemInfo.attributeList[].originalAttributeName` | string |  | 属性名称 |
| `itemInfo.attributeList[].attributeValueList` | array<object> |  | 属性值列表 |
| `itemInfo.attributeList[].attributeValueList[].valueId` | integer |  | 属性值 ID |
| `itemInfo.attributeList[].attributeValueList[].originalValueName` | string |  | 属性值名称 |
| `itemInfo.attributeList[].attributeValueList[].valueUnit` | string |  | 属性值单位 |
| `itemInfo.descriptionInfo` | object |  | 新版描述信息 |
| `itemInfo.descriptionInfo.extendedDescription` | object |  | 扩展描述 |
| `itemInfo.descriptionInfo.extendedDescription.fieldList` | array<object> |  | 扩展描述字段列表 |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].fieldType` | string |  | 字段类型：text / image |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].text` | string |  | 文本内容（field_type 为 text 时返回） |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo` | object |  | 图片信息（field_type 为 image 时返回） |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo.imageId` | string |  | 图片 ID |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo.imageUrl` | string |  | 图片 URL |
| `itemInfo.descriptionInfo.descriptionType` | string |  | 描述类型：normal / extended |
| `itemInfo.isFulfillmentByShopee` | boolean |  | 是否为 Shopee 履约商品 |
| `itemInfo.sizeChartId` | integer |  | 尺码表模板 ID |
| `modelList` | object |  | 全球规格列表（前端修改后的 GetItemDetailVo.modelList，仅传新数据） |
| `modelList.tierVariation` | array<object> |  | 层级规格信息 |
| `modelList.tierVariation[].name` | string |  | 层级规格名称 |
| `modelList.tierVariation[].optionList` | array<object> |  | 层级规格选项列表 |
| `modelList.tierVariation[].optionList[].option` | string |  | 层级规格选项值 |
| `modelList.tierVariation[].image` | object |  | 层级规格图片 |
| `modelList.tierVariation[].image.imageUrl` | string |  | 图片 URL |
| `modelList.tierVariation[].image.imageId` | string |  | 图片 ID |
| `modelList.globalModel` | array<object> |  | 全球规格列表(SKU列表) |
| `modelList.globalModel[].globalModelId` | integer |  | 全球规格 ID |
| `modelList.globalModel[].globalModelSku` | string |  | 全球规格 SKU |
| `modelList.globalModel[].priceInfo` | object |  | 价格信息 |
| `modelList.globalModel[].priceInfo.originalPrice` | number |  | 原价 |
| `modelList.globalModel[].stockInfo` | array<object> |  | 库存信息 |
| `modelList.globalModel[].stockInfo[].stockType` | integer |  | 库存类型：1 = WMS 在库，2 = 卖家在库 |
| `modelList.globalModel[].stockInfo[].stockLocationId` | string |  | 库存位置 ID |
| `modelList.globalModel[].stockInfo[].currentStock` | integer |  | 当前库存 |
| `modelList.globalModel[].stockInfo[].normalStock` | integer |  | 正常库存 |
| `modelList.globalModel[].stockInfo[].reservedStock` | integer |  | 预留库存 |
| `modelList.globalModel[].tierIndex` | array<integer> |  | 层级索引 |
| `modelList.globalModel[].weight` | string |  | 重量，单位 KG |
| `modelList.globalModel[].dimension` | object |  | 包裹尺寸 |
| `modelList.globalModel[].dimension.packageHeight` | integer | 是 | 包裹高度，单位 CM |
| `modelList.globalModel[].dimension.packageLength` | integer | 是 | 包裹长度，单位 CM |
| `modelList.globalModel[].dimension.packageWidth` | integer | 是 | 包裹宽度，单位 CM |
| `modelList.globalModel[].preOrder` | object |  | 预售信息 |
| `modelList.globalModel[].preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `modelList.globalModel[].isFulfillmentByShopee` | boolean |  | 是否为 FBS 规格 |
| `modelList.standardiseTierVariation` | array<object> |  | 标准化层级规格信息 |
| `modelList.standardiseTierVariation[].variationId` | integer |  | 标准化层级规格 ID |
| `modelList.standardiseTierVariation[].variationName` | string |  | 标准化层级规格名称 |
| `modelList.standardiseTierVariation[].variationGroupId` | integer |  | 标准化层级规格组 ID |
| `modelList.standardiseTierVariation[].variationOptionList` | array<object> |  | 标准化层级规格选项列表 |
| `modelList.standardiseTierVariation[].variationOptionList[].variationOptionId` | integer |  | 标准化层级规格选项 ID |
| `modelList.standardiseTierVariation[].variationOptionList[].variationOptionName` | string |  | 标准化层级规格选项名称 |
| `modelList.standardiseTierVariation[].imageId` | string |  | 图片 ID |
| `modelList.standardiseTierVariation[].imageUrl` | string |  | 图片 URL |

#### 获取属性列表

`POST /open/v1/product/item/shopee_global/item/get_attribute_list`  (文档: api-480434404)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer |  | 店铺ID |
| `site` | string |  | 站点 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `attributes` | array<object> | 属性列表 |
| `attributes[].attributeId` | integer |  |
| `attributes[].originalAttributeName` | string |  |
| `attributes[].displayAttributeName` | string |  |
| `attributes[].isMandatory` | boolean |  |
| `attributes[].inputValidationType` | string |  |
| `attributes[].formatType` | string |  |
| `attributes[].inputType` | string |  |
| `attributes[].attributeUnit` | array<string> |  |
| `attributes[].attributeValueList` | array<object> |  |
| `attributes[].attributeValueList[].valueId` | integer |  |
| `attributes[].attributeValueList[].originalValueName` | string |  |
| `attributes[].attributeValueList[].displayValueName` | string |  |
| `attributes[].attributeValueList[].parentAttributeList` | array<object> |  |
| `attributes[].attributeValueList[].parentAttributeList[].parentAttributeId` | integer |  |
| `attributes[].attributeValueList[].parentAttributeList[].parentValueId` | integer |  |
| `attributes[].maxInputValueNumber` | integer |  |
| `attributes[].introduction` | string |  |
| `attributes[].mandatoryRegion` | array<string> |  |
| `lang` | string | 语言 |

#### 获取全球店铺类目尺寸模板列表

`POST /open/v1/product/item/shopee_global/item/get_shop_id_and_size_chart_list_map`  (文档: api-480434405)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |
| `cid` | integer | 是 | 类目ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopIdAndSizeChartListMap` | object | 店铺ID与尺寸模板列表映射 |

#### 上传商品视频

`POST /open/v1/product/item/shopee_global/item/upload_item_video`  (文档: api-480434406)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `sourceVideoUrl` | string | 是 | 视频URL |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `videoUploadId` | integer |  |

#### 同步产品

`POST /open/v1/product/item/shopee_global/item/rsync_item_single`  (文档: api-480434407)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemIds` | array<string> | 是 | 平台产品ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successPlatformItemIds` | array<string> |  |
| `failedPlatformItemIds` | array<string> |  |
| `errorMap` | object |  |

#### 全球产品删除

`POST /open/v1/product/item/shopee_global/item/delete_item`  (文档: api-480434408)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemId` | string | 是 | 平台产品ID |

### 商品 > Mercadolibre采集箱 > 发布产品

#### 发布产品

`POST /open/v1/product/collect_box/mercadolibre/move_collect/save_move_collect_task`  (文档: api-482757484)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |

#### 发布记录列表

`POST /open/v1/product/collect_box/mercadolibre/move_collect/search_move_collect_list`  (文档: api-511672449)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:20 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string |  | 产品ID |
| `filter.sourceItemId` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `moveCollectDetailList` | array<object> | 发布记录列表 |
| `moveCollectDetailList[].subDetailList` | array<object> | SKU对应产品发布详情（传统模式） |
| `moveCollectDetailList[].subDetailList[].platformItemId` | string | 对应站点产品ID |
| `moveCollectDetailList[].subDetailList[].site` | string | 对应站点 |
| `moveCollectDetailList[].subDetailList[].siteName` | string | 对应站点别名 |
| `moveCollectDetailList[].subDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].subDetailList[].reason` | string | 发布失败原因 |
| `moveCollectDetailList[].subDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].subDetailList[].gmtModified` | string | 更新时间 |
| `moveCollectDetailList[].skuSubDetailList` | array<object> | SKU对应产品发布详情（UP模式） |
| `moveCollectDetailList[].skuSubDetailList[].cbtItemId` | string | CBT产品ID |
| `moveCollectDetailList[].skuSubDetailList[].platformItemId` | string | 对应站点产品ID |
| `moveCollectDetailList[].skuSubDetailList[].site` | string | 对应站点 |
| `moveCollectDetailList[].skuSubDetailList[].siteName` | string | 对应站点别名 |
| `moveCollectDetailList[].skuSubDetailList[].sku` | string | sku |
| `moveCollectDetailList[].skuSubDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].skuSubDetailList[].reason` | string | 发布失败原因 |
| `moveCollectDetailList[].skuSubDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].skuSubDetailList[].gmtModified` | string | 更新时间 |
| `moveCollectDetailList[].moveCollectTaskDetailId` | string | 发布任务详情ID |
| `moveCollectDetailList[].collectBoxDetailId` | string | 采集箱详情ID |
| `moveCollectDetailList[].shopId` | string | 店铺ID |
| `moveCollectDetailList[].itemNum` | string | 商品编号 |
| `moveCollectDetailList[].cid` | string | 类目ID |
| `moveCollectDetailList[].source` | string | 来源平台 |
| `moveCollectDetailList[].sourceSite` | string | 来源站点 |
| `moveCollectDetailList[].sourceItemId` | string | 来源商品ID |
| `moveCollectDetailList[].title` | string | 商品标题 |
| `moveCollectDetailList[].thumbnail` | string | 缩略图 |
| `moveCollectDetailList[].isTiming` | string | 是否定时发布 |
| `moveCollectDetailList[].status` | string | 发布状态 |
| `moveCollectDetailList[].reason` | string | 失败原因 |
| `moveCollectDetailList[].gmtCreate` | string | 创建时间 |
| `moveCollectDetailList[].gmtModified` | string | 修改时间 |
| `moveCollectDetailList[].platformItemId` | string | 平台商品ID |
| `moveCollectDetailList[].isRenewItem` | boolean | 是否翻新 |
| `moveCollectDetailList[].shopName` | string | 店铺名称 |
| `moveCollectDetailList[].siteName` | string | 站点名称 |
| `moveCollectDetailList[].site` | string | 站点 |
| `moveCollectDetailList[].sourceItemUrl` | string | 来源商品链接 |
| … | | 共 45 个字段，详见 openapi.json |

### 商品 > Mercadolibre采集箱 > 采集箱

#### 获取类目属性规则

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_attribute_rules`  (文档: api-482753632)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `saleAttributeRules` | array<object> | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `saleAttributeRules[].attributeGroupId` | string | 属性组ID,暂无用 |
| `saleAttributeRules[].attributeGroupName` | string | 属性组名称,暂无用 |
| `saleAttributeRules[].displayName` | string | 属性显示名称 |
| `saleAttributeRules[].hierarchy` | string | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `saleAttributeRules[].id` | string | 属性ID |
| `saleAttributeRules[].name` | string | 属性英文名称，如"Color"等 |
| `saleAttributeRules[].relevance` | integer | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `saleAttributeRules[].tags` | object | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `saleAttributeRules[].valueType` | string | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `saleAttributeRules[].values` | array<object> | 可选值列表,从中选取name |
| `saleAttributeRules[].values[].id` | string | 选项id |
| `saleAttributeRules[].values[].displayName` | string | 选项显示名称 |
| `saleAttributeRules[].values[].name` | string | 选项英文名称 |
| `saleAttributeRules[].values[].metadata` | object | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `productAttributeRules` | array<object> | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `productAttributeRules[].attributeGroupId` | string | 属性组ID,暂无用 |
| `productAttributeRules[].attributeGroupName` | string | 属性组名称,暂无用 |
| `productAttributeRules[].displayName` | string | 属性显示名称 |
| `productAttributeRules[].hierarchy` | string | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `productAttributeRules[].id` | string | 属性ID |
| `productAttributeRules[].name` | string | 属性英文名称，如"Color"等 |
| `productAttributeRules[].relevance` | integer | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `productAttributeRules[].tags` | object | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `productAttributeRules[].valueType` | string | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `productAttributeRules[].values` | array<object> | 可选值列表,从中选取name |
| `productAttributeRules[].values[].id` | string | 选项id |
| `productAttributeRules[].values[].displayName` | string | 选项显示名称 |
| `productAttributeRules[].values[].name` | string | 选项英文名称 |
| `productAttributeRules[].values[].metadata` | object | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `skuAttributeRules` | array<object> | SKU属性规则列表，创建产品时需按此规则填写attributes |
| `skuAttributeRules[].attributeGroupId` | string | 属性组ID,暂无用 |
| `skuAttributeRules[].attributeGroupName` | string | 属性组名称,暂无用 |
| `skuAttributeRules[].displayName` | string | 属性显示名称 |
| `skuAttributeRules[].hierarchy` | string | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `skuAttributeRules[].id` | string | 属性ID |
| `skuAttributeRules[].name` | string | 属性英文名称，如"Color"等 |
| `skuAttributeRules[].relevance` | integer | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `skuAttributeRules[].tags` | object | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `skuAttributeRules[].valueType` | string | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| … | | 共 45 个字段，详见 openapi.json |

#### 获取类目配置

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_setting`  (文档: api-482753633)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `catalogDomain` | string | 类目domain |
| `maxDescriptionLength` | integer | 类目最大描述长度 |
| `maxTitleLength` | integer | 类目最大标题长度 |

#### 获取尺码表domain列表

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_domain_list`  (文档: api-482753635)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer |  | 店铺ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `domains` | array<object> | domain列表 |
| `domains[].domainId` | string | domain ID |
| `domains[].domainName` | string | domain英文名称 |
| `domains[].domainZhName` | string | domain中文名称 |

#### 获取尺码表表头和主属性信息

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_attribute_info`  (文档: api-482753636)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `domainId` | string | 是 | 尺码表domain ID(对应getSizeChartDomainList返回的domainId) |
| `genderId` | string | 是 | 1.类目属性中的性别ID(getSiteCollectItemInfo中attributes->GENDER属性values中的name值； 2.在获取类目属性规则接口返回数据的productAttributeRules中对应GENDER属性规则values值的id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `mainAttributeList` | object | 主属性列表，格式{MANUFACTURER_SIZE:{name:"Manufacturer size",nameZh:"自定义尺码",unit:"US"}} |
| `measureTypeList` | object | 测量属性列表，格式{BODY_MEASURE:{name:"With body measurements",nameZh:"身体尺寸",relevanceRequired:["FILTRABLE_SIZE","CHEST_CIRCUMFERENCE_FROM"],unit:"US"}} |
| `isTopsAndBottoms` | boolean | 是否为上衣或下装 |

#### 获取尺码表所需填写属性信息

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_need_attribute_info`  (文档: api-482753637)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `domainId` | string | 是 | domain ID(对应getSizeChartDomainList返回的domainId) |
| `genderId` | string | 是 | 1.类目属性中的性别ID(getSiteCollectItemInfo中attributes->GENDER属性values中的name值； 2.在获取类目属性规则接口返回数据的productAttributeRules中对应GENDER属性规则values值的id |
| `measureType` | string | 是 | 测量类型(对应getSizeChartAttributeInfo返回的measureTypeList key) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `sizeChartIdAndInfoMap` | object | 尺码ID和尺码内容映射 |
| `equivalencies` | array<string> | 尺码列表(XL,XXL等) |

#### 获取授权站点和名称映射

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_auth_site_and_site_name_map`  (文档: api-482753639)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer |  | 店铺ID |
| `includeCbt` | integer | 是 | 是否包含CBT全球站点（1是 0否） max:1 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `siteAndSiteNameMap` | object | 站点和站点名称映射，格式:{"AR":"阿根廷","BR":"巴西"} |

#### 获取商品基本选项

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_item_options`  (文档: api-482753640)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `weightUnitOptions` | array<object> | 重量单位选项，key/value 数组，保存到 siteCollectItemInfo.skuMap.weightUnit |
| `weightUnitOptions[].key` | string | 选项键值 |
| `weightUnitOptions[].value` | string | 选项显示文本 |
| `warrantyTypeOptions` | array<object> | 保修类型选项，key/value 数组，保存到 siteCollectItemInfo.warrantyType,siteCollectItemInfo.warrantyTimeUnit |
| `warrantyTypeOptions[].key` | string | 选项键值 |
| `warrantyTypeOptions[].value` | string | 选项显示文本 |
| `warrantyTimeUnitOptions` | array<object> | 保修时间单位选项，key/value 数组，保存到 siteCollectItemInfo.warrantyTimeUnit |
| `warrantyTimeUnitOptions[].key` | string | 选项键值 |
| `warrantyTimeUnitOptions[].value` | string | 选项显示文本 |
| `lengthUnitOptions` | array<object> | 包裹尺寸单位选项，key/value 数组，保存到 siteCollectItemInfo.skuMap.lengthWidthHeightUnit |
| `lengthUnitOptions[].key` | string | 选项键值 |
| `lengthUnitOptions[].value` | string | 选项显示文本 |
| `siteAndSupportListingTypeOptions` | object | 站点和支持产品类型映射,格式:{"BR":[{"label":"经典（Classic）","value":"gold_special"}]} |

#### 查询尺码表模板列表

`POST /open/v1/product/collect_box/mercadolibre/collect_box/search_size_chart_template`  (文档: api-482753641)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |
| `filter` | object |  |  |
| `filter.domainId` | string |  | 尺码表domain ID(对应getSizeChartDomainList返回的domainId) |
| `filter.genderId` | string |  | 类目属性中的性别ID |
| `filter.templateName` | string |  | 模板名称（模糊搜索） |
| `pageSize` | integer |  | 每页数量 max:500 |
| `pageNo` | integer |  | 当前页码 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `sizeChartTemplateList` | array<object> | 尺码表列表 |
| `sizeChartTemplateList[].attributes` | array<object> | 尺码表模板属性列表 |
| `sizeChartTemplateList[].attributes[].id` | string | 属性ID |
| `sizeChartTemplateList[].attributes[].values` | array<object> | 属性值列表 |
| `sizeChartTemplateList[].attributes[].values[].id` | string | 属性值ID |
| `sizeChartTemplateList[].attributes[].values[].name` | string | 属性值名称 |
| `sizeChartTemplateList[].chartId` | string | 平台尺码表ID |
| `sizeChartTemplateList[].copySerialNumber` | integer | 复制模板序列号 |
| `sizeChartTemplateList[].domainId` | string | 尺码表domainId |
| `sizeChartTemplateList[].genderId` | string | 性别ID |
| `sizeChartTemplateList[].mainAttributeId` | string | 主属性ID |
| `sizeChartTemplateList[].mainAttribute` | array<object> | 主属性映射 |
| `sizeChartTemplateList[].mainAttribute[].attributes` | array<object> | 表头英文名称 |
| `sizeChartTemplateList[].mainAttribute[].attributes[].siteId` | string | 站点ID |
| `sizeChartTemplateList[].mainAttribute[].attributes[].id` | string | 主属性属性ID |
| `sizeChartTemplateList[].measureType` | string | 测量类型 |
| `sizeChartTemplateList[].names` | object | 站点ID对应名称映射,格式{MCO:"renzituo"} |
| `sizeChartTemplateList[].rows` | array<object> |  |
| `sizeChartTemplateList[].rows[].attributes` | array<object> | 表头英文名称 |
| `sizeChartTemplateList[].rows[].attributes[].id` | string | 行属性ID |
| `sizeChartTemplateList[].rows[].attributes[].values` | array<object> | 行属性值列表 |
| `sizeChartTemplateList[].rows[].attributes[].values[].name` | string | 行属性值名称 |
| `sizeChartTemplateList[].rows[].attributes[].values[].struct` | object |  |
| `sizeChartTemplateList[].rows[].attributes[].values[].struct.number` | number | 行属性值名称拆分:数字部分 |
| `sizeChartTemplateList[].rows[].attributes[].values[].struct.unit` | string | 行属性值名称拆分:单位部分 |
| `sizeChartTemplateList[].rows[].id` | string | 行ID |
| `sizeChartTemplateList[].rows[].sites` | array<string> | 站点ID列表 |
| `sizeChartTemplateList[].shopId` | integer | 店铺ID |
| `sizeChartTemplateList[].siteId` | string | 站点ID |
| `sizeChartTemplateList[].templateName` | string | 尺码模板名称 |
| `sizeChartTemplateList[].type` | string | 尺码模板类型 |
| `total` | integer | 总数 |

#### 获取采集箱详情

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_site_collect_item_info`  (文档: api-482753644)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer |  | 店铺ID（切换店铺的时候调用） |
| `cid` | integer |  | 新类目id（切换类目时填写） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `saleAttributeRules` | array<object> | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `saleAttributeRules[].attributeGroupId` | string | 属性组ID,暂无用 |
| `saleAttributeRules[].attributeGroupName` | string | 属性组名称,暂无用 |
| `saleAttributeRules[].displayName` | string | 属性显示名称 |
| `saleAttributeRules[].hierarchy` | string | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `saleAttributeRules[].id` | string | 属性ID |
| `saleAttributeRules[].name` | string | 属性英文名称，如"Color"等 |
| `saleAttributeRules[].relevance` | integer | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `saleAttributeRules[].tags` | object | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `saleAttributeRules[].valueType` | string | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `saleAttributeRules[].values` | array<object> | 可选值列表,从中选取name |
| `saleAttributeRules[].values[].id` | string | 选项id |
| `saleAttributeRules[].values[].displayName` | string | 选项显示名称 |
| `saleAttributeRules[].values[].name` | string | 选项英文名称 |
| `saleAttributeRules[].values[].metadata` | object | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `productAttributeRules` | array<object> | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `productAttributeRules[].attributeGroupId` | string | 属性组ID,暂无用 |
| `productAttributeRules[].attributeGroupName` | string | 属性组名称,暂无用 |
| `productAttributeRules[].displayName` | string | 属性显示名称 |
| `productAttributeRules[].hierarchy` | string | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `productAttributeRules[].id` | string | 属性ID |
| `productAttributeRules[].name` | string | 属性英文名称，如"Color"等 |
| `productAttributeRules[].relevance` | integer | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `productAttributeRules[].tags` | object | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `productAttributeRules[].valueType` | string | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `productAttributeRules[].values` | array<object> | 可选值列表,从中选取name |
| `productAttributeRules[].values[].id` | string | 选项id |
| `productAttributeRules[].values[].displayName` | string | 选项显示名称 |
| `productAttributeRules[].values[].name` | string | 选项英文名称 |
| `productAttributeRules[].values[].metadata` | object | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `skuAttributeRules` | array<object> | SKU属性规则列表，创建产品时需按此规则填写attributes |
| `skuAttributeRules[].attributeGroupId` | string | 属性组ID,暂无用 |
| `skuAttributeRules[].attributeGroupName` | string | 属性组名称,暂无用 |
| `skuAttributeRules[].displayName` | string | 属性显示名称 |
| `skuAttributeRules[].hierarchy` | string | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `skuAttributeRules[].id` | string | 属性ID |
| `skuAttributeRules[].name` | string | 属性英文名称，如"Color"等 |
| `skuAttributeRules[].relevance` | integer | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `skuAttributeRules[].tags` | object | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `skuAttributeRules[].valueType` | string | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| … | | 共 113 个字段，详见 openapi.json |

#### 创建采集箱商品

`POST /open/v1/product/collect_box/mercadolibre/collect_box/create_collect_box_item`  (文档: api-482753646)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 SiteCollectItemInfoForSaveRo 注释。 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口 |
| `siteCollectItemInfo.price` | number | 是 | 价格 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string |  | 商品备注/描述 |
| `siteCollectItemInfo.warrantyType` | string | 是 | 保修类型(sellerWarranty:卖家保修,factoryWarranty:工厂保修,noWarranty:无保修) |
| `siteCollectItemInfo.warrantyTime` | integer | 是 | 保修时长 |
| `siteCollectItemInfo.warrantyTimeUnit` | string | 是 | 保修时长单位(days:天,years:年,months:月) |
| `siteCollectItemInfo.videoUrl` | string |  | 视频URL |
| `siteCollectItemInfo.sourceList` | array<object> |  | 货源列表 |
| `siteCollectItemInfo.sourceList[].source` | string |  | 货源来源标识 |
| `siteCollectItemInfo.sourceList[].sourceItemId` | string |  | 货源商品ID |
| `siteCollectItemInfo.sourceList[].sourceSite` | string |  | 货源站点 |
| `siteCollectItemInfo.sourceList[].sourceItemUrl` | string |  | 货源商品URL |
| `siteCollectItemInfo.detailId` | string |  | 明细ID |
| `siteCollectItemInfo.firstSkuKey` | string |  | 第一个SKU的key,对应skuMap中的key |
| `siteCollectItemInfo.siteAndListingTypeList` | array<object> |  | 站点与刊登类型列表 |
| `siteCollectItemInfo.siteAndListingTypeList[].site` | string |  | 站点标识 |
| `siteCollectItemInfo.siteAndListingTypeList[].listingType` | string |  | 刊登类型 |
| `siteCollectItemInfo.siteAndTitleList` | array<object> |  | 站点与标题列表 |
| `siteCollectItemInfo.siteAndTitleList[].site` | string |  | 站点标识 |
| `siteCollectItemInfo.siteAndTitleList[].title` | string |  | 站点商品标题 |
| `siteCollectItemInfo.pricingMode` | string |  | 售价模式(sellPrice:售价, netProceeds:净收益) |
| `siteCollectItemInfo.shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.attributes` | array<object> |  | 商品属性列表（品牌/型号等） |
| `siteCollectItemInfo.attributes[].name` | string |  | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> |  | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].name` | string |  | 属性值名称 |
| `siteCollectItemInfo.saleAttributes` | array<object> |  | 销售属性列表(如: 颜色/尺码) |
| `siteCollectItemInfo.saleAttributes[].name` | string |  | 销售属性名称(如: Color, Size) |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> |  | 销售属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | integer |  | SKU标识key |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string |  | 销售属性值名称 |
| `siteCollectItemInfo.saleAttributes[].id` | string |  | 销售属性ID(如: COLOR, SIZE) |
| `siteCollectItemInfo.sites` | array<string> | 是 | 已选择的站点列表,结构["BR","BR(Full)(Up)"] |
| `siteCollectItemInfo.siteAndPriceMap` | object | 是 | 站点价格映射,结构 {"MX": 100, "AR": 100} |
| `siteCollectItemInfo.skuMap` | object |  | SKU映射表,key为SKU组合key,value为SKU详情(当类目规则saleAttributes不为空时必填) |
| `siteCollectItemInfo.hasSaveSite` | integer |  | 是否已保存站点(1:是;0:否) max:1 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | integer | 创建成功的采集箱详情ID |

#### 保存采集箱站点详情

`POST /open/v1/product/collect_box/mercadolibre/collect_box/save_site_collect_item_info`  (文档: api-482753647)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.price` | number | 是 | 价格 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string |  | 商品备注/描述 |
| `siteCollectItemInfo.warrantyType` | string | 是 | 保修类型(sellerWarranty:卖家保修,factoryWarranty:工厂保修,noWarranty:无保修) |
| `siteCollectItemInfo.warrantyTime` | integer | 是 | 保修时长 |
| `siteCollectItemInfo.warrantyTimeUnit` | string | 是 | 保修时长单位(days:天,years:年,months:月) |
| `siteCollectItemInfo.videoUrl` | string |  | 视频URL |
| `siteCollectItemInfo.sourceList` | array<object> |  | 货源列表 |
| `siteCollectItemInfo.sourceList[].source` | string |  | 货源来源标识 |
| `siteCollectItemInfo.sourceList[].sourceItemId` | string |  | 货源商品ID |
| `siteCollectItemInfo.sourceList[].sourceSite` | string |  | 货源站点 |
| `siteCollectItemInfo.sourceList[].sourceItemUrl` | string |  | 货源商品URL |
| `siteCollectItemInfo.detailId` | string |  | 明细ID |
| `siteCollectItemInfo.firstSkuKey` | string |  | 第一个SKU的key,对应skuMap中的key |
| `siteCollectItemInfo.siteAndListingTypeList` | array<object> |  | 站点与刊登类型列表 |
| `siteCollectItemInfo.siteAndListingTypeList[].site` | string |  | 站点标识 |
| `siteCollectItemInfo.siteAndListingTypeList[].listingType` | string |  | 刊登类型 |
| `siteCollectItemInfo.siteAndTitleList` | array<object> |  | 站点与标题列表 |
| `siteCollectItemInfo.siteAndTitleList[].site` | string |  | 站点标识 |
| `siteCollectItemInfo.siteAndTitleList[].title` | string |  | 站点商品标题 |
| `siteCollectItemInfo.pricingMode` | string |  | 售价模式(sellPrice:售价, netProceeds:净收益) |
| `siteCollectItemInfo.shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.attributes` | array<object> |  | 商品属性列表（品牌/型号等） |
| `siteCollectItemInfo.attributes[].name` | string |  | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> |  | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].name` | string |  | 属性值名称 |
| `siteCollectItemInfo.saleAttributes` | array<object> |  | 销售属性列表(如: 颜色/尺码) |
| `siteCollectItemInfo.saleAttributes[].name` | string |  | 销售属性名称(如: Color, Size) |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> |  | 销售属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string |  | SKU标识key |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string |  | 销售属性值名称 |
| `siteCollectItemInfo.saleAttributes[].id` | string |  | 销售属性ID(如: COLOR, SIZE) |
| `siteCollectItemInfo.sites` | array<string> | 是 | 已选择的站点列表,结构["BR","BR(Full)(Up)"] |
| `siteCollectItemInfo.siteAndPriceMap` | object | 是 | 站点价格映射 |
| `siteCollectItemInfo.skuMap` | object |  | SKU映射表,key为SKU组合key,value为SKU详情(当类目规则saleAttributes不为空时必填) |
| `siteCollectItemInfo.hasSaveSite` | integer |  | 是否已保存站点(1:是;0:否) max:1 |

#### 同步店铺尺码表

`POST /open/v1/product/collect_box/mercadolibre/collect_box/rsync_size_chart_template`  (文档: api-482753643)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shopIdAndRsyncRet` | object | 店铺Id同步结果映射 key 为 shopId，value 为该店铺同步结果。 Map value 为该店铺同步结果，每一项结构如下： -result : 同步结果，success 表示成功，fail 表示失败 -reason : 同步失败原因，如果同步成功则为空 |

#### 获取采集箱列表

`POST /open/v1/product/collect_box/mercadolibre/collect_box/search_collect_box_detailList`  (文档: api-482753630)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 max:500 |
| `filter` | object |  | 过滤器 |
| `filter.status` | string |  | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.filterCidSite` | string |  | 过滤类目站点(固定值-CBT) |
| `filter.sourceItemIdKeyword` | string |  | 货源ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `collectBoxDetailId` | string | 采集箱详情ID |
| `itemNum` | string | 商品编号 |
| `breadcrumb` | string | 类目面包屑 |
| `cid` | string | 类目ID |
| `globalPrice` | string | 全球净收益/售价 |
| `stock` | string | 库存 |
| `price` | string | 货源价格 |
| `thumbnail` | string | 缩略图 |
| `gmtCreate` | string | 创建时间 |
| `editModel` | string | 编辑模式 |
| `commonCollectBoxDetailId` | string | 公共采集箱详情ID |
| `appAccountId` | string | 应用账户ID |
| `subAppAccountId` | string | 子应用账户ID |
| `platform` | string | 平台 |
| `title` | string | 商品标题 |
| `remark` | string | 备注 |
| `copyType` | string | 复制类型 |
| `collectBoxGroupId` | string | 采集箱分组ID |
| `collectBoxDetailShop` | object | 预发布店铺信息 |
| `collectBoxDetailShop.shopId` | string | 店铺ID |
| `collectBoxDetailShop.pricingMode` | string | 售价模式 |
| `collectBoxDetailShop.siteAndMaxPriceMap` | object | 站点最大价格映射 |
| `collectBoxDetailShop.siteAndMinPriceMap` | object | 站点最小价格映射 |
| `collectBoxDetailShop.siteAndPriceMap` | object | 站点价格映射 |
| `collectBoxDetailShop.sites` | array<string> | 已选择的站点列表(BR(Full)(Up)、BR(Full)等) |

#### 获取类目列表

`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_tree_by_site`  (文档: api-484103119)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 美客多站点，固定值“CBT” |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cateTree` | object | 分类树 Map（key=cid, value=分类节点） |

### 商品 > AI公共服务 > 图片处理

#### AI白底图

`POST /open/v1/product/picture/matting/auto_ai_matting_multi`  (文档: api-482201652)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imgUrls` | array<string> | 是 | 图片URL列表，（不计重复） |
| `imageScene` | integer | 是 | 图片应用场景 1-产品图片 2-描述图片 3-sku或产品属性图片 4-证书图片 5-尺寸图图片 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `imgMattingList` | array<object> | AI白底图结果列表 |
| `imgMattingList[].result` | string | 单张AI白底图结果（success/fail） |
| `imgMattingList[].width` | integer | 图片宽度 |
| `imgMattingList[].height` | integer | 图片高度 |
| `imgMattingList[].md5` | string | 图片MD5 |
| `imgMattingList[].newImageUrl` | string | 抠图后图片URL |
| `imgMattingList[].oriImageUrl` | string | 原始图片URL |

#### AI智能消除

`POST /open/v1/product/common/image_removal/remove_image`  (文档: api-482190901)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array<string> | 是 | 待消除图片URL列表 |
| `traceInfo` | object | 是 | 调用场景信息 |
| `traceInfo.imageRemovalSource` | string | 是 | 图片消除业务来源 必传，可选值： collect_box-平台采集箱 collect_box_add-采集箱创建产品 common_collect_box-公共采集箱 common_collect_box_add-公共采集箱创建产品 item-在线产品 item_add-添加产品 |
| `traceInfo.collectBoxDetailId` | integer |  | 平台采集箱DetailId，imageRemovalSource=collect_box 时必传 |
| `traceInfo.commonCollectBoxDetailId` | integer |  | 公共采集箱DetailId，imageRemovalSource=common_collect_box 时必传 |
| `traceInfo.platform` | string |  | 平台（平台采集箱和在线产品必传） |
| `removeConfig` | object | 是 | 消除配置 |
| `removeConfig.isRemoveWatermark` | integer | 是 | 消除对象，是否去除水印（0=否，1=是） |
| `removeConfig.isRemoveLogo` | integer | 是 | 消除对象，是否去除logo（0=否，1=是） |
| `removeConfig.isRemoveText` | integer | 是 | 消除对象，是否去除文字（0=否，1=是） |
| `removeConfig.isRemovePsoriasis` | integer |  | 消除对象，是否去除牛皮藓（0=否，1=是） |
| `removeConfig.removeAreas` | array<string> | 是 | 消除区域，可选值：background（背景区域）、subject（主体区域） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `imageRemovalUrlResultList` | array<object> | 消除结果列表 |
| `imageRemovalUrlResultList[].result` | string | 单张消除结果（success/fail） |
| `imageRemovalUrlResultList[].reason` | string | 单张消除失败原因 |
| `imageRemovalUrlResultList[].oriImageUrl` | string | 原始图片URL |
| `imageRemovalUrlResultList[].newImageUrl` | string | 消除后图片URL |
| `imageRemovalUseNum` | integer | 图片消除使用次数 |
| `appResourceCode` | string | 应用资源编码 |
| `appResourceUseNum` | integer | 应用资源使用次数 |
| `freeUseNum` | integer | 免费使用次数 |

#### 搜索水印列表

`POST /open/v1/product/item/tiktok/watermark/search_watermark_list`  (文档: api-482200257)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `watermarkIds` | string |  | 水印ID列表，多个以英文逗号分隔 |
| `watermarkName` | string |  | 水印名称（支持模糊搜索） |
| `watermarkSubType` | string | 是 | 水印子类型（normal=普通水印，byLayer=描述图水印） |
| `pageNo` | integer | 是 | $pageNo |
| `pageSize` | integer | 是 | 每页数量 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `watermarkList` | array<object> | 水印列表 |
| `watermarkList[].watermarkId` | string | 水印ID |
| `watermarkList[].appAccountId` | string | 应用账号ID |
| `watermarkList[].platform` | string | 平台 |
| `watermarkList[].watermarkImageUrl` | string | 水印图片URL |
| `watermarkList[].watermarkType` | string | 水印类型 |
| `watermarkList[].watermarkSubType` | string | 水印子类型 |
| `watermarkList[].name` | string | 水印名称 |
| `total` | integer | 总数 |

#### 图片打水印

`POST /open/v1/product/item/tiktok/watermark/watermark_images`  (文档: api-482200258)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array<string> | 是 | 需要打水印的图片链接列表 |
| `watermarkId` | string | 是 | 用于打水印的水印ID |
| `collectBoxDetailId` | integer |  | 采集箱详情ID 若有就传 |
| `isAutoMatchImageSize` | boolean | 是 | 是否自动匹配图片大小 若开启，添加水印时将自动适配原图尺寸比例；若关闭，添加水印后输出的图片尺寸默认为 800×800 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `watermarkDetail` | array<object> | 打水印结果列表，每项对应一张图片的处理结果 |
| `watermarkDetail[].imageUrl` | string | 原图片URL |
| `watermarkDetail[].result` | string | 打水印结果（success: 成功；fail: 失败） |
| `watermarkDetail[].watermarkImageUrl` | string | 打完水印后的图片URL，result 为 success 时有值 |
| `watermarkDetail[].msg` | string | 失败原因，result 为 fail 时有值 |

#### 获取支持的翻译语言配置

`POST /open/v1/product/common/translate/get_support_language_config`  (文档: api-484286513)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `supportLanguageConfig` | object | 支持的语言配置 结构为 {平台: {类型: {源语言: [目标语言列表]}}} 平台可选值：aeAi / tosoiot / ykt / aidoubao，分别代表 阿里翻译 / 象寄翻译 / 易可图翻译 / AI翻译 类型可选值：realTime（实时翻译）/ idle（闲时翻译） 源语言和目标语言为语言编码，如 zh、en、ja 等 示例：{"ali": {"realTime": {"zh": ["en", "ja"], "en": ["zh", "ja"]}}} |

#### 图片翻译

`POST /open/v1/product/common/translate/translate_image`  (文档: api-484286514)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array<string> | 是 | 待翻译图片URL列表 |
| `sourceLang` | string | 是 | 源语言编码（如 zh、en），可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig |
| `targetLang` | string | 是 | 目标语言编码，可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig |
| `translatePlatform` | string | 是 | 翻译平台（ali / aeAi / tosoiot / ykt），可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig 的键 |
| `noTranslateImageTextOptions` | array<string> |  | 不翻译的图片文字选项，可选值：textInTheProduct（不翻译产品文案）、brand（不翻译品牌），不传则都翻译 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `translateImageUrlResultList` | array<object> | 翻译成功结果列表 |
| `translateImageUrlResultList[].oriImageUrl` | string | 原始图片URL |
| `translateImageUrlResultList[].newImageUrl` | string | 翻译后图片URL |
| `translateImageUrlResultList[].result` | string | 单张翻译结果（success/fail） |
| `translateImageUrlErrorResultList` | array<object> | 翻译失败结果列表 |
| `translateImageUrlErrorResultList[].failImageCount` | integer | 失败图片数量 |
| `translateImageUrlErrorResultList[].failImageUrls` | array<string> | 失败图片URL列表 |
| `translateImageUrlErrorResultList[].reason` | string | 失败原因 |

### 商品 > AI公共服务 > AI润色

#### AI生成产品信息（标题/描述）

`POST /open/v1/product/common/open_ai/generate_product_info`  (文档: api-482190902)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `generateTypeList` | array<string> | 是 | 生成类型列表 必传，可选值： title-生成标题 notes-生成描述 |
| `functionModule` | string | 是 | 功能模块 必传，可选值： createCollectBox-手动创建采集箱 editCollectBox-编辑采集箱 createItem-手动创建在线产品 editItem-编辑在线产品 |
| `functionModuleProductId` | integer |  | 功能模块产品ID 当functionModule为editCollectBox/editItem时必传 |
| `platform` | string | 是 | 平台 |
| `aiName` | string | 是 | AI名称 （使用接口 get_ai_name_list 获取的name） |
| `title` | string | 是 | 原始标题 |
| `originalContent` | string |  | 原始描述内容（生成描述时使用） |
| `titleLengthLimit` | integer |  | 标题长度限制 |
| `languageName` | string | 是 | 目标语言名称（使用接口 get_language_name_code_map 获取的code） |
| `keywordsList` | array<string> |  | 关键词列表 |
| `negativeWordsList` | array<string> |  | 排除词列表 |
| `categoryName` | string |  | 类目名称 |
| `site` | string |  | 站点 |
| `cid` | string |  | 类目ID |
| `imageInfoList` | array<object> |  | 图片信息列表 |
| `imageInfoList[].imageUrl` | string | 是 | 图片URL |
| `imageInfoList[].imageSource` | string |  | 图片来源 可选值：productImage-产品图片 otherImage-其他图片 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `titleResult` | object | 标题生成结果 |
| `titleResult.result` | string | 结果状态：success/fail |
| `titleResult.contents` | array<string> | 标题内容列表 |
| `notesResult` | object | 描述生成结果 |
| `notesResult.result` | string | 结果状态：success/fail |
| `notesResult.contents` | array<string> | 描述内容列表 |

#### AI生成支持的语言map

`POST /open/v1/product/common/open_ai/get_language_name_code_map`  (文档: api-482190903)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `languageNameCodeMap` | object | 语言名称与语言代码的映射 key: 语言名称（如"繁体中文"、"泰语"） value: 语言代码（如"zh-TW"、"th"） |

#### 获取支持的AI名称列表

`POST /open/v1/product/common/open_ai/get_generate_product_info_support_ai_name_list`  (文档: api-482190904)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `aiNameList` | array<string> | 支持的AI名称列表 可选值：deepSeekR1/douBao1.6/tongYiQianWen |

#### AI润色销售规格

`POST /open/v1/product/common/open_ai/generate_sku_spec_name`  (文档: api-484286515)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platform` | string | 是 | 平台（目前只支持tiktok） |
| `title` | string |  | 原始标题（作为AI润色上下文） |
| `aiName` | string | 是 | AI模型名称（目前只支持 douBao1.6） |
| `languageName` | string |  | 目标语言名称（取值见 getLanguageNameCodeMap 接口，默认"当前语言"） |
| `functionModule` | string | 是 | 功能模块，可选值：createCollectBox / editCollectBox / createItem / editItem |
| `skuPropertyList` | array<object> | 是 | SKU属性列表 |
| `skuPropertyList[].attrName` | string |  | 属性名称（如 Color、规格） |
| `skuPropertyList[].attrId` | string |  | 属性ID（可为空字符串） |
| `skuPropertyList[].attrValueList` | array<object> |  | 属性值列表 每项包含 attrValueId/attrValue/imgUrl/supplementarySkuImageUrls |
| `skuPropertyList[].attrValueList[].attrValueId` | string |  | 属性值ID |
| `skuPropertyList[].attrValueList[].attrValue` | string |  | 属性值名称 |
| `skuPropertyList[].attrValueList[].imgUrl` | string |  | 属性值主图URL（无图时为空字符串） |
| `skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> |  | 补充SKU图片URL列表 |
| `productId` | integer |  | 产品ID（functionModule 为 editCollectBox / editItem 时传入） |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `newSkuPropertyList` | array<object> | AI润色后的SKU规格列表 格式：[{"name": "Color", "valueList": ["Red", "Blue"]}, ...] |
| `newSkuPropertyList[].attrName` | string | 属性名称（如 Color、规格） |
| `newSkuPropertyList[].attrId` | string | 属性ID（可为空字符串） |
| `newSkuPropertyList[].attrValueList` | array<object> | 属性值列表 每项包含 attrValueId/attrValue/imgUrl/supplementarySkuImageUrls |
| `newSkuPropertyList[].attrValueList[].attrValueId` | string | 属性值ID |
| `newSkuPropertyList[].attrValueList[].attrValue` | string | 属性值名称 |
| `newSkuPropertyList[].attrValueList[].imgUrl` | string | 属性值主图URL（无图时为空字符串） |
| `newSkuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 补充SKU图片URL列表 |
| `reasoningContent` | string | AI思考过程内容（部分AI模型返回的推理过程） |
| `openaiRequestLogId` | integer | AI请求日志ID（对应历史记录ID，默认0） |

### 商品 > 图片空间

#### 通过图片URL上传图片到图片空间

`POST /open/v1/product/picture/picture_space/upload_picture_link`  (文档: api-519663381)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imgUrl` | string | 是 | 图片URL |
| `scene` | string | 是 | 图片场景，产品：product，分销：distributionGoods，仓库产品：stockGoods |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `appPictureId` | integer | 图片空间中的图片ID，成功时有值 |
| `picturePath` | string | 上传后的图片URL，成功时有值 |
| `width` | integer | 图片宽度，成功时有值 |
| `height` | integer | 图片高度，成功时有值 |
| `md5` | string | 图片MD5，成功时有值 |

### 包裹 > 履约 > 基础管理

#### 获取当前账号有效的线下物流列表

`POST /open/v1/order/logistics_agent/manage/get_enable_offline_product_list`  (文档: api-455528071)

三方物流商以及三方仓

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `logisticsAgentId` | integer |  | 物流id |
| `opOrderPackageIds` | array<integer> |  | 包裹ids |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `logisticsAgentAuthConfigOption` | object |  |
| `logisticsAgentAuthConfigOption.` | object |  |
| `logisticsAgentAuthConfigOption..label` | string | 标签 |
| `logisticsAgentAuthConfigOption..agentCode` | string | 物流商代码 |
| `logisticsAgentAuthConfigOption..agentName` | string | 物流商名称 |
| `logisticsAgentAuthConfigOption..options` | array<object> | 渠道信息 |
| `logisticsAgentAuthConfigOption..options[].label` | string | 渠道标签 |
| `logisticsAgentAuthConfigOption..options[].logisticsAgentAuthId` | integer | 物流授权id |
| `logisticsAgentAuthConfigOption..options[].logisticsAgentProductId` | integer | 物流渠道id |
| `logisticsAgentAuthConfigOption..options[].productCode` | string | 物流渠道编码 |
| `logisticsAgentAuthConfigOption..options[].logisticsCompany` | string | 物流公司 |
| `logisticsAgentAuthConfigOption..options[].status` | string | 渠道状态 |
| `logisticsAgentAuthConfigOption..options[].isEnabled` | boolean | 是否启用 |
| `logisticsAgentAuthConfigOption..options[].isSupportPlatformLastMile` | integer | 是否支持尾程平台 |
| `logisticsAgentAuthConfigOption..options[].productName` | string | 物流渠道名称 |
| `logisticsAgentAuthConfigOption..options[].platformLogisticsProductMap` | object | 平台渠道映射表 |
| `logisticsAgentAuthConfigOption..options[].platformLogisticsProductMap.pddkjChoice` | object | 支持的平台 |
| `logisticsAgentAuthConfigOption..options[].platformLogisticsProductMap.pddkjChoice.platform` | null | 支持的平台 |
| `logisticsAgentAuthConfigOption..options[].platformLogisticsProductMap.pddkjChoice.productKeyword` | array<string> | 面单打印设置 |
| `logisticsAgentAuthConfigOption..options[].platformLogisticsProductMap.pddkjChoice.printWaybillType` | string | firstMile 头程面单,lastMile 尾程面单 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo` | object |  |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.label` | string | 标签 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.logisticsAgentAuthId` | string | 授权id |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.logisticsAgentProductId` | string | 渠道id |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.productCode` | string | 渠道编码 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.productName` | string | 渠道名称 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.logisticsCompany` | string | 物流公司 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.status` | string | 状态 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.isEnabled` | string | 是否启用 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.platformLogisticsProductMap` | object | 渠道配置 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.platformLogisticsProductMap.pddkjChoice` | object | 支持的平台 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.platformLogisticsProductMap.pddkjChoice.platform` | null | 支持的平台 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.platformLogisticsProductMap.pddkjChoice.productKeyword` | array<string> | 面单打印设置 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.platformLogisticsProductMap.pddkjChoice.printWaybillType` | string | firstMile 头程面单,lastMile 尾程面单 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.isSupportPlatformLastMile` | string | 是否支持尾程 |
| `logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo.agentCode` | string | 物流渠道 |
| `logisticsAgentAuthConfigOption..options[].value` | string | 映射尾程配置id |
| `logisticsAgentAuthConfigOption..logisticsAgentWarehouseName` | string | 仓库id |
| `logisticsAgentAuthConfigOption..logisticsAgentWarehouseId` | string | 仓库名称 |
| `logisticsAgentAuthConfigOption..type` | string | logisticsAgent/物流商物流渠道，thirdWarehouse/三方仓物流渠道， supplier/供应商渠道 selfWarehouse/自营仓渠道 |

#### 获取当前包裹有效的线上物流列表

`POST /open/v1/order/logistics_agent/manage/get_enable_online_product_list`  (文档: api-455611090)

在线发货以及拼接物流

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹id |
| `logisticsAgentAuthId` | integer | 是 | 物流授权id |
| `agentCode` | string | 是 | 物流商编码 |
| `weight` | string |  | 小数点后两位 |
| `length` | string |  | 长 |
| `width` | string |  | 宽 |
| `height` | string |  | 高 |
| `weightUnit` | string |  | 枚举值 g、mg、kg、oz、lbs |
| `dimensionUnit` | string |  | 枚举值 cm、in、mm、m、ft |
| `signatureOnDelivery` | boolean |  | temu 专属字段 |
| `warehouseId` | string |  | 仓库id |

### 包裹 > 售后

#### 获取退货退款列表

`POST /open/v1/order/after_sales/fetch/order_return_list`  (文档: api-477739260)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `gmtStartFrom` | string |  | 售后/订单起始时间 |
| `gmtStartTo` | string |  | 售后/订单结束时间 |
| `platformReturnSns` | string |  | 平台售后单号 |
| `platformOrderSns` | string |  | 平台订单号 |
| `platform` | string |  | 平台 |
| `page` | integer |  | 页码 |
| `pageSize` | integer |  | 每页数量 max:50 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `returnList` | array<object> | 退货退款单列表 |
| `returnList[].opOrderReturnId` | string | 售后单ID |
| `returnList[].opOrderId` | string | 订单ID |
| `returnList[].platformReturnSn` | string | 平台售后单号 |
| `returnList[].platformOrderSn` | string | 平台订单号 |
| `returnList[].shopId` | string | 店铺ID |
| `returnList[].shopName` | string | 店铺名称 |
| `returnList[].shopNickName` | string | 店铺自定义名称 |
| `returnList[].platform` | string | 平台 |
| `returnList[].site` | string | 站点 |
| `returnList[].siteName` | string | 站点名称 |
| `returnList[].status` | string | 售后状态 |
| `returnList[].platformReturnStatus` | string | 平台售后状态 |
| `returnList[].appReturnStatusText` | string | 妙手售后状态文案 |
| `returnList[].reverseType` | string | 售后类型 |
| `returnList[].textReason` | string | 售后/退货原因文案（原文） |
| `returnList[].textReasonCn` | string | 售后/退货原因文案（中文） |
| `returnList[].refundAmount` | string | 退款金额 |
| `returnList[].currency` | string | 币种 |
| `returnList[].returnTrackingNo` | string | 退回运单号 |
| `returnList[].returnLogisticsCompany` | string | 退货物流商 |
| `returnList[].needsLogistics` | string | 是否需要退回物流 |
| `returnList[].gmtCreateTime` | string | 售后时间 |
| `returnList[].gmtDueDate` | string | 最晚处理时间 |
| `returnList[].items` | array<object> | 商品列表 |
| `returnList[].items[].title` | string | 商品标题 |
| `returnList[].items[].picUrl` | string | 商品图片URL |
| `returnList[].items[].platformOuterSkuId` | string | 平台SKU |
| `returnList[].items[].platformSkuId` | string | 平台SKUID |
| `returnList[].items[].quantity` | string | 数量 |
| `returnList[].consigneeInfo` | object | 退货人信息 |
| `returnList[].consigneeInfo.opOrderId` | string | 订单ID |
| `returnList[].consigneeInfo.name` | string | 收件人姓名 |
| `returnList[].consigneeInfo.katakana` | string | 收件人假名/日语假名 |
| `returnList[].consigneeInfo.phone` | string | 收件人主电话 |
| `returnList[].consigneeInfo.phone1` | string | 收件人备用电话1 |
| `returnList[].consigneeInfo.phone2` | string | 收件人备用电话2 |
| `returnList[].consigneeInfo.email` | string | 收件人邮箱 |
| `returnList[].consigneeInfo.company` | string | 公司名称 |
| `returnList[].consigneeInfo.country` | string | 国家二字码 |
| … | | 共 56 个字段，详见 openapi.json |

#### 获取取消订单列表

`POST /open/v1/order/after_sales/fetch/order_cancel_list`  (文档: api-477739261)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platformOrderSns` | string |  | 平台订单号 |
| `platform` | string |  | 平台 |
| `gmtStartFrom` | string |  | 售后起始时间 |
| `gmtStartTo` | string |  | 售后结束时间 |
| `page` | integer |  | 页码 |
| `pageSize` | integer |  | 每页数量 max:50 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cancelList` | array<object> | 取消订单列表 |
| `cancelList[].platformOrderSn` | string | 平台订单号 |
| `cancelList[].shopId` | string | 店铺ID |
| `cancelList[].shopName` | string | 店铺名称 |
| `cancelList[].platform` | string | 平台 |
| `cancelList[].platformName` | string | 平台名称 |
| `cancelList[].site` | string | 站点 |
| `cancelList[].siteName` | string | 站点名称 |
| `cancelList[].textReason` | string | 取消原因（原文） |
| `cancelList[].textReasonCn` | string | 取消原因（中文） |
| `cancelList[].appReturnStatusText` | string | 妙手取消状态文案 |
| `cancelList[].appOrderStatus` | string | 订单状态 |
| `cancelList[].reverseTypeText` | string | 售后类型文案 |
| `cancelList[].gmtCreateTime` | string | 售后时间 |
| `cancelList[].items` | array<object> | 商品列表 |
| `cancelList[].items[].title` | string | 商品标题 |
| `cancelList[].items[].picUrl` | string | 商品图片URL |
| `cancelList[].items[].platformOuterSkuId` | string | 平台SKU |
| `cancelList[].items[].platformSkuId` | string | 平台SKUID |
| `cancelList[].items[].quantity` | string | 数量 |
| `total` | integer | 总数 |
| `page` | integer | 当前页码 |
| `pageSize` | integer | 每页数量 |

### 包裹 > 包裹 > 运单

#### 申请运单号

`POST /open/v1/order/package/logistics/tracking_no/apply`  (文档: api-457255661)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹ID |

#### 批量申请运单号

`POST /open/v1/order/package/logistics/tracking_no/batch_apply`  (文档: api-523411121)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 订单包裹IDs |
| `shippingMethod` | string |  | 配送方式 (shopee专用) |
| `addressId` | string |  | 取件地址 (shopee专用) shippingMethod为pickup时必填 |
| `pickupTimeId` | integer |  | 取件时间ID (shopee专用) |
| `trackingNo` | string |  | 运单号(shopee专用) |
| `slug` | string |  | 物流渠道(shopee专用) |
| `senderRealName` | string |  | 发件人名称(shopee专用) |
| `isShipAfterHasLogisticsNo` | string |  | 是否获取跟踪单号并发货 |
| `isSetDefaultAddress` | string |  | 是否设置为默认地址(shopee专用) |
| `partItemRelationSupplierGoodsProcessType` | string |  | 部分商品关联了分销商品时候处理方式，skipPackage 跳过整个包裹， skipNotRelationItem 跳过没关联的商品 |
| `isConfirmSupplierGoodsSkuIdChange` | integer |  | 推送供应商商品是否改变0、1 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `trackingNoInfos` | array<object> | 运单号数据列表 |
| `trackingNoInfos[].opOrderPackageId` | integer | 妙手包裹id |
| `trackingNoInfos[].platformOrderSn` | string | 平台订单号 |
| `trackingNoInfos[].platformPackageId` | string | 平台包裹id |
| `trackingNoInfos[].logisticsNo` | string | 运单号 |
| `errors` | array<object> | 错误数据 |
| `errors[].errMsg` | string | 错误描述 |
| `errors[].errCode` | string | 错误code |
| `errors[].opOrderPackageId` | integer | 妙手包裹id |
| `errors[].opOrderId` | integer | 妙手订单id |
| `errors[].platformOrderSn` | string | 妙手订单编号 |
| `errors[].platformPackageId` | string | 平台包裹id |
| `errors[].appPackageNo` | string | 包裹号 |
| `errors[].logisticsNo` | string | 跟踪号 |
| `errors[].logisticsCompany` | string | 物流公司 |
| `errors[].logisticsAgentAuthId` | string | 授权id |
| `errors[].logisticsAgentProductId` | integer | 物流渠道id |
| `errors[].logisticsAgentId` | integer | 物流id |
| `errors[].agentName` | string | 物流名称 |

#### 设置包裹物流

`POST /open/v1/order/package/logistics/tracking_no/save_logistics_agent_product`  (文档: api-457269520)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 包裹IDs |
| `logisticsAgentAuthConfigId` | integer | 是 | 授权物流配置ID |
| `type` | string | 是 | logisticsAgent-物流商，thirdWarehouse-三方仓物流 |
| `logisticsAgentWarehouseChannelConfigId` | integer |  | type=thirdWarehouse时必填 |
| `aliexpressDomesticLogisticsCompanyName` | string |  | 速卖通国内物流公司 |
| `aliexpressDomesticLogisticsCompanyId` | integer |  | 速卖通国内物流公司ID |
| `aliexpressDomesticTrackingNo` | string |  | 速卖通国内物流单号 |
| `warehouseId` | integer |  | 暂时只对temu在线物流生效 |
| `partItemRelationSupplierGoodsProcessType` | string |  | skipPackage 跳过整个包裹， skipNotRelationItem 跳过没关联的商品 |
| `isShipLater` | string |  | 暂时只对temu在线物流生效 |
| `packageWeightAndDimension` | object | 是 | {"1044122969":{"length":1,"width":1,"height":1,"dimensionUnit":"in","weight":1,"weightUnit":"lb","isSavePackageWeightAndDimension":0}} |

#### 获取包裹物流轨迹

`POST /open/v1/order/package/logistics/tracking/get_tracking_list`  (文档: api-477263048)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 订单包裹ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `trackingInfoList` | array<object> | 物流轨迹列表 |
| `trackingInfoList[].description` | string | 物流轨迹明细 |
| `trackingInfoList[].descriptionCn` | string | 物流轨迹明细（中文） |
| `trackingInfoList[].gmtCreate` | string | 时间 |

#### 获取运单面单

`POST /open/v1/order/package/logistics/waybill/get_waybill`  (文档: api-457264811)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | string | 是 | 包裹id |

#### 批量获取面单

`POST /open/v1/order/package/logistics/waybill/batch_get_waybill`  (文档: api-523411122)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 订单包裹IDs |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `waybillPdfInfos` | array<object> | 面单数据列表 |
| `waybillPdfInfos[].platformOrderSn` | string | 平台订单号 |
| `waybillPdfInfos[].platformPackageId` | string | 平台包裹id |
| `waybillPdfInfos[].url` | string | 面单url |
| `waybillPdfInfos[].opOrderPackageId` | integer | 妙手包裹id |
| `errors` | array<object> | 错误数据 |
| `errors[].errMsg` | string | 错误描述 |
| `errors[].errCode` | string | 错误code |
| `errors[].opOrderPackageId` | integer | 妙手包裹id |
| `errors[].opOrderId` | integer | 妙手订单id |
| `errors[].platformOrderSn` | string | 妙手订单编号 |
| `errors[].platformPackageId` | string | 平台包裹id |
| `errors[].appPackageNo` | string | 包裹号 |
| `errors[].logisticsNo` | string | 跟踪号 |
| `errors[].logisticsCompany` | string | 物流公司 |
| `errors[].logisticsAgentAuthId` | string | 授权id |
| `errors[].logisticsAgentProductId` | integer | 物流渠道id |
| `errors[].logisticsAgentId` | integer | 物流id |
| `errors[].agentName` | string | 物流名称 |

### 包裹 > 包裹 > 基础信息修改

#### 保存包裹本地备注

`POST /open/v1/order/package/base_info_modify/saveOrderPackageAppNote`  (文档: api-457235460)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹id |
| `appNote` | string | 是 | 本地备注内容 |
| `isRsyncToForwarder` | integer | 是 | 1 是 0 否 |

#### 保存包裹商家备注

`POST /open/v1/order/package/base_info_modify/saveSellerNote`  (文档: api-457240926)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderIds` | array<string> | 是 | 订单id |
| `sellerNote` | string | 是 | 备注内容 |
| `isCoverOriginalSellerNote` | integer | 是 | 1 是 0 否 |

### 包裹 > 包裹 > 获取包裹

#### 获取订单包裹详情

`POST /open/v1/order/package/fetch/get_package_info`  (文档: api-524317132)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 订单包裹id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `orderPackageInfo` | object | 订单信息 |
| `orderPackageInfo.platform` | string | 归属平台 |
| `orderPackageInfo.platformName` | string | 平台名称 |
| `orderPackageInfo.site` | string | 站点 |
| `orderPackageInfo.siteName` | string | 站点名称 |
| `orderPackageInfo.shopId` | integer | 店铺id |
| `orderPackageInfo.shopNick` | string | 店铺别名 |
| `orderPackageInfo.shopName` | string | 店铺名称 |
| `orderPackageInfo.orderInfo` | object | 订单信息 |
| `orderPackageInfo.orderInfo.opOrderId` | integer | 订单id |
| `orderPackageInfo.orderInfo.shopId` | integer | 店铺id |
| `orderPackageInfo.orderInfo.platform` | string | 订单平台 |
| `orderPackageInfo.orderInfo.platformOrderSn` | string | 平台订单号 |
| `orderPackageInfo.orderInfo.platformOrderStatus` | string | 订单平台状态 |
| `orderPackageInfo.orderInfo.site` | string | 站点 |
| `orderPackageInfo.orderInfo.currency` | string | 货币单位 |
| `orderPackageInfo.orderInfo.orderAmount` | number | 订单金额 |
| `orderPackageInfo.orderInfo.productAmount` | number | 产品金额 |
| `orderPackageInfo.orderInfo.discountAmount` | number | 优惠金额 |
| `orderPackageInfo.orderInfo.estimatedShippingFee` | number | 预估运费费用 |
| `orderPackageInfo.orderInfo.actualShippingCost` | number | 实际运费 |
| `orderPackageInfo.orderInfo.payAmount` | number | 支付金额 |
| `orderPackageInfo.orderInfo.escrowAmount` | number | 预估回款金额 |
| `orderPackageInfo.orderInfo.commissionFee` | number | 平台佣金 |
| `orderPackageInfo.orderInfo.paymentMethod` | string | 支付方式 |
| `orderPackageInfo.orderInfo.gmtOrderStart` | string | 创建时间 |
| `orderPackageInfo.orderInfo.gmtOrderModified` | string | 修改时间 |
| `orderPackageInfo.orderInfo.gmtPay` | string | 支付时间 |
| `orderPackageInfo.orderInfo.gmtLastDelivery` | string | 最迟发货时间 |
| `orderPackageInfo.orderInfo.gmtDelivery` | string | 发货时间 |
| `orderPackageInfo.orderInfo.gmtRefund` | string | 取消时间 |
| `orderPackageInfo.orderInfo.gmtFinish` | string | 完结时间 |
| `orderPackageInfo.orderInfo.gmtSettlement` | string | 结算时间 |
| `orderPackageInfo.orderInfo.isCod` | boolean | 是否货到付款 |
| `orderPackageInfo.orderInfo.appOrderStatus` | string | 妙手平台订单状态 |
| `orderPackageInfo.orderInfo.appNote` | string | 本地备注 |
| `orderPackageInfo.orderInfo.sellerNote` | string | 商家备注 |
| `orderPackageInfo.orderInfo.buyerMessage` | string | 卖家留言 |
| `orderPackageInfo.orderInfo.platformOrderDetailUrl` | string | 订单图片 url |
| `orderPackageInfo.orderInfo.platformWarehouseName` | string | 平台仓库名称 |
| … | | 共 122 个字段，详见 openapi.json |

#### 获取订单包裹列表

`POST /open/v1/order/package/fetch/search_package_list`  (文档: api-524317133)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:200 |
| `platform` | string |  | 平台 |
| `shopIds` | array<integer> |  | 店铺ids |
| `appPackageStatus` | string |  | 包裹状态 |
| `platformOrderSns` | string |  | 订单号[多个逗号分割] |
| `gmtCreateFrom` | string |  | 妙手创建时间 -开始 |
| `gmtCreateTo` | string |  | 妙手创建时间 -结束 |
| `gmtModifiedFrom` | string |  | 妙手修改时间 -开始 |
| `gmtModifiedTo` | string |  | 妙手修改时间 -结束 |
| `appPackageTab` | string |  | 妙手包裹tab(顶层tab) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `orderPackageList` | array<object> | 订单列表信息 |
| `orderPackageList[].platform` | string | 归属平台 |
| `orderPackageList[].platformName` | string | 平台名称 |
| `orderPackageList[].site` | string | 站点 |
| `orderPackageList[].siteName` | string | 站点名称 |
| `orderPackageList[].shopId` | integer | 店铺id |
| `orderPackageList[].shopNick` | string | 店铺别名 |
| `orderPackageList[].shopName` | string | 店铺名称 |
| `orderPackageList[].orderInfo` | object | 订单信息 |
| `orderPackageList[].orderInfo.opOrderId` | integer | 订单id |
| `orderPackageList[].orderInfo.shopId` | integer | 店铺id |
| `orderPackageList[].orderInfo.platform` | string | 订单平台 |
| `orderPackageList[].orderInfo.platformOrderSn` | string | 平台订单号 |
| `orderPackageList[].orderInfo.platformOrderStatus` | string | 订单平台状态 |
| `orderPackageList[].orderInfo.site` | string | 站点 |
| `orderPackageList[].orderInfo.currency` | string | 货币单位 |
| `orderPackageList[].orderInfo.orderAmount` | number | 订单金额 |
| `orderPackageList[].orderInfo.productAmount` | number | 产品金额 |
| `orderPackageList[].orderInfo.discountAmount` | number | 优惠金额 |
| `orderPackageList[].orderInfo.estimatedShippingFee` | number | 预估运费费用 |
| `orderPackageList[].orderInfo.actualShippingCost` | number | 实际运费 |
| `orderPackageList[].orderInfo.payAmount` | number | 支付金额 |
| `orderPackageList[].orderInfo.escrowAmount` | number | 预估回款金额 |
| `orderPackageList[].orderInfo.commissionFee` | number | 平台佣金 |
| `orderPackageList[].orderInfo.paymentMethod` | string | 支付方式 |
| `orderPackageList[].orderInfo.gmtOrderStart` | string | 创建时间 |
| `orderPackageList[].orderInfo.gmtOrderModified` | string | 修改时间 |
| `orderPackageList[].orderInfo.gmtPay` | string | 支付时间 |
| `orderPackageList[].orderInfo.gmtLastDelivery` | string | 最迟发货时间 |
| `orderPackageList[].orderInfo.gmtDelivery` | string | 发货时间 |
| `orderPackageList[].orderInfo.gmtRefund` | string | 取消时间 |
| `orderPackageList[].orderInfo.gmtFinish` | string | 完结时间 |
| `orderPackageList[].orderInfo.gmtSettlement` | string | 结算时间 |
| `orderPackageList[].orderInfo.isCod` | boolean | 是否货到付款 |
| `orderPackageList[].orderInfo.appOrderStatus` | string | 妙手平台订单状态 |
| `orderPackageList[].orderInfo.appNote` | string | 本地备注 |
| `orderPackageList[].orderInfo.sellerNote` | string | 商家备注 |
| `orderPackageList[].orderInfo.buyerMessage` | string | 卖家留言 |
| `orderPackageList[].orderInfo.platformOrderDetailUrl` | string | 订单图片 url |
| `orderPackageList[].orderInfo.platformWarehouseName` | string | 平台仓库名称 |
| … | | 共 125 个字段，详见 openapi.json |

### 包裹 > 包裹 > 发货

#### 包裹发货

`POST /open/v1/order/package/ship_package/ship_packages`  (文档: api-455694578)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 包裹IDs |
| `isVirtualShipment` | integer | 是 | 是否虚拟发货 |
| `tiktokLocalShopShipType` | string | 是 | 枚举值（1、2）;1、pick-up；2、drop-off |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successOpOrderPackageIds` | string |  |
| `failCount` | string |  |
| `shipFailErrors` | array<object> |  |
| `shipFailErrors[].errMsg` | string | 错误描述 |
| `shipFailErrors[].errCode` | string | 错误code |
| `shipFailErrors[].opOrderPackageId` | string | 妙手包裹id |
| `shipFailErrors[].opOrderId` | string | 妙手订单id |
| `shipFailErrors[].platformOrderSn` | string | 妙手订单编号 |
| `shipFailErrors[].platformPackageId` | string | 平台包裹id |
| `shipFailErrors[].appPackageNo` | string | 包裹号 |
| `shipFailErrors[].logisticsNo` | string | 跟踪号 |
| `shipFailErrors[].logisticsCompany` | string | 物流公司 |
| `shipFailErrors[].logisticsAgentAuthId` | string | 授权id |
| `shipFailErrors[].logisticsAgentProductId` | string | 物流渠道id |
| `shipFailErrors[].logisticsAgentId` | string | 物流id |
| `shipFailErrors[].gentName` | string | 物流名称 |
| `successCount` | string |  |

### 包裹 > 采购记录

#### 采购记录列表

`POST /open/v1/order/purchase_order/purchase_record/search_list`  (文档: api-523326861)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:500 |
| `sortType` | string |  | 排序方式 |
| `shopIds` | array<integer> |  | 店铺ids |
| `purchasePlatform` | string |  | 采购平台 |
| `purchaseOrderStatus` | string |  | 采购单状态 |
| `purchaseOrderSeller` | string |  | 采购单卖家/供应商 |
| `warningType` | string |  | 预警类型 |
| `snType` | string |  | 搜索类型: purchaseOrderSn, purchaseOrderBuyer, platformOrderSn, appPackageNo, waybillCode, logisticsName, platformOuterSkuId, platformItemId |
| `snValue` | string |  | 搜索值 |
| `gmtRangeType` | string |  | 时间范围类型: gmtPurchaseOrderStart, gmtLastRsync, gmtPay, gmtLastUrgeShip, gmtOrderStart, gmtShip, gmtSign, signDuringTime |
| `gmtRangeFrom` | string |  | 时间范围起始 |
| `gmtRangeTo` | string |  | 时间范围结束 |
| `relateStatus` | string |  | 关联状态 |
| `forwarderId` | integer |  | 货代id |
| `buyerPhone` | string |  | 收件人手机号 |
| `appPackageStatus` | string |  | 订单包裹状态 |
| `isFilterAbnormal` | integer |  | 是否过滤异常 |
| `gmtPurchaseOrderStartFrom` | string |  | 采购下单时间起始 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `list` | array<object> |  |
| `list[].purchaseOrderSn` | string | 采购单号 |
| `list[].waybillCode` | string | 采购物流单号 |
| `list[].purchasePlatformName` | string | 采购平台名称 |
| `list[].gmtPurchaseOrderStart` | string | 采购时间 |
| `list[].purchaseOrderSeller` | string | 供应商名称 |
| `list[].purchaseOrderPayment` | string | 实付金额 |
| `list[].purchaseOrderShippingFee` | string | 运费金额 |
| `list[].purchaseOrderOtherFee` | string | 其他金额 |
| `list[].purchaseItems` | array<object> | 采购商品列表 |
| `list[].purchaseItems[].sourceTitle` | string | 采购商品名称 |
| `list[].purchaseItems[].sourceSkuSubName` | string | 采购商品规格名称 |
| `list[].purchaseItems[].sourceSendGoodsAddress` | string | 采购商品发货地 |
| `list[].purchaseItems[].sourceUnitPrice` | string | 采购商品单价 |
| `list[].purchaseItems[].sourceQuantity` | string | 采购商品规格数量 |
| `list[].purchaseOrderPackages` | array<object> | 采购物流包裹列表 |
| `list[].purchaseOrderPackages[].logisticsName` | string | 物流名称 |
| `list[].purchaseOrderPackages[].waybillCode` | string | 采购物流单号 |
| `list[].purchaseOrderPackages[].signDuringTime` | integer | 签收时长(秒) |
| `list[].purchaseOrderPackages[].isSubscribeLogistics` | integer | 是否订阅物流 |
| `list[].purchaseOrderPackages[].failCode` | string | 失败码 |
| `list[].purchaseOrderPackages[].failReason` | string | 失败原因 |
| `list[].purchaseOrderPackages[].gmtLastLogisticsTrace` | string | 最新物流轨迹时间 |
| `list[].purchaseOrderPackages[].gmtSign` | string | 签收时间 |
| `list[].purchaseOrderPackages[].gmtShip` | string | 发货时间 |
| `list[].opOrderPackageList` | array<object> | 关联订单包裹列表 |
| `list[].opOrderPackageList[].platformOrderSn` | string | 订单号 |
| `list[].opOrderPackageList[].shopName` | string | 店铺 |
| `list[].opOrderPackageList[].platform` | string | 平台 |
| `list[].opOrderPackageList[].relateStatus` | string | 关联状态枚举值  normal:关联  cancel：取消关联 |
| `list[].opOrderPackageList[].purchaseItems` | array<object> | 订单商品列表 |
| `list[].opOrderPackageList[].purchaseItems[].title` | string | 产品名称 |
| `list[].opOrderPackageList[].purchaseItems[].skuSubName` | string | 规格 |
| `list[].opOrderPackageList[].purchaseItems[].platformItemId` | string | 产品ID |
| `list[].opOrderPackageList[].purchaseItems[].platformOuterSkuId` | string | 平台SKU |
| `list[].opOrderPackageList[].purchaseItems[].unitPrice` | string | 单价 |
| `list[].opOrderPackageList[].purchaseItems[].quantity` | integer | 数量 |
| `list[].opOrderPackageList[].purchaseItems[].picUrl` | string | 产品图片 |
| `total` | integer |  |

#### 采购记录详情

`POST /open/v1/order/purchase_order/purchase_record/get_detail`  (文档: api-523329034)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `purchaseOrderSn` | string |  | 采购单号 |
| `waybillCode` | string |  | 采购物流单号 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `detail` | object |  |
| `detail.purchaseOrderSn` | string | 采购单号 |
| `detail.waybillCode` | string | 采购物流单号 |
| `detail.purchasePlatformName` | string | 采购平台名称 |
| `detail.gmtPurchaseOrderStart` | string | 采购时间 |
| `detail.purchaseOrderSeller` | string | 供应商名称 |
| `detail.purchaseOrderPayment` | string | 实付金额 |
| `detail.purchaseOrderShippingFee` | string | 运费金额 |
| `detail.purchaseOrderOtherFee` | string | 其他金额 |
| `detail.purchaseItems` | array<object> | 采购商品列表 |
| `detail.purchaseItems[].sourceTitle` | string | 采购商品名称 |
| `detail.purchaseItems[].sourceSkuSubName` | string | 采购商品规格名称 |
| `detail.purchaseItems[].sourceSendGoodsAddress` | string | 采购商品发货地 |
| `detail.purchaseItems[].sourceUnitPrice` | string | 采购商品单价 |
| `detail.purchaseItems[].sourceQuantity` | string | 采购商品规格数量 |
| `detail.purchaseOrderPackages` | array<object> | 采购物流包裹列表 |
| `detail.purchaseOrderPackages[].logisticsName` | string | 物流名称 |
| `detail.purchaseOrderPackages[].waybillCode` | string | 采购物流单号 |
| `detail.purchaseOrderPackages[].signDuringTime` | integer | 签收时长(秒) |
| `detail.purchaseOrderPackages[].isSubscribeLogistics` | integer | 是否订阅物流 |
| `detail.purchaseOrderPackages[].failCode` | string | 失败码 |
| `detail.purchaseOrderPackages[].failReason` | string | 失败原因 |
| `detail.purchaseOrderPackages[].gmtLastLogisticsTrace` | string | 最新物流轨迹时间 |
| `detail.purchaseOrderPackages[].gmtSign` | string | 签收时间 |
| `detail.purchaseOrderPackages[].gmtShip` | string | 发货时间 |
| `detail.opOrderPackageList` | array<object> | 关联订单包裹列表 |
| `detail.opOrderPackageList[].platformOrderSn` | string | 订单号 |
| `detail.opOrderPackageList[].shopName` | string | 店铺 |
| `detail.opOrderPackageList[].platform` | string | 平台 |
| `detail.opOrderPackageList[].relateStatus` | string | 关联状态 |
| `detail.opOrderPackageList[].purchaseItems` | array<object> | 订单商品列表 |
| `detail.opOrderPackageList[].purchaseItems[].title` | string | 产品名称 |
| `detail.opOrderPackageList[].purchaseItems[].skuSubName` | string | 规格 |
| `detail.opOrderPackageList[].purchaseItems[].platformItemId` | string | 产品ID |
| `detail.opOrderPackageList[].purchaseItems[].platformOuterSkuId` | string | 平台SKU |
| `detail.opOrderPackageList[].purchaseItems[].unitPrice` | string | 单价 |
| `detail.opOrderPackageList[].purchaseItems[].quantity` | integer | 数量 |
| `detail.opOrderPackageList[].purchaseItems[].picUrl` | string | 产品图片 |

### 采购 > 采购单

#### 添加采购单

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order`  (文档: api-479599772)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `supplierId` | string | 是 | 供应商ID |
| `warehouseId` | string | 是 | 仓库ID |
| `warehouseType` | string | 是 | 仓库类型(self:自营仓,forwarder:货代仓库) |
| `thirdWarehouseProviderAuthId` | string |  | 三方仓授权id(仓库类型为forwarder时必填) |
| `gmtPredictArrival` | string |  | 预计到货时间 |
| `accountNote` | string |  | 采购备注 |
| `goodsShareFeeType` | string | 是 | 费用分摊方式，费用均摊方式1数量,2金额,3重量 |
| `otherFee` | string |  |  |
| `shippingFee` | string |  | 其他费用 |
| `goodsSkuList` | array<object> | 是 | 采购商品列表 |
| `goodsSkuList[].goodsSkuId` | integer | 是 | 商品SKU ID |
| `goodsSkuList[].purchaseNum` | integer | 是 | 采购数量 |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价 |
| `goodsSkuList[].thirdWarehouseGoodsSkuId` | string |  | 映射的三方仓商品SKU ID(仓库类型为forwarder时必填) |
| `saveOption` | string | 是 | 存选项save保存,submitAudit提交审核,passAudit提交并通过审核 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsPurchaseOrderInternalSn` | string | 采购单号 |

#### 创建1688采购单

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order`  (文档: api-479599773)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderList` | array<object> | 是 | 采购单列表（可批量） |
| `goodsPurchaseOrderList[].resellerAccountId` | string | 是 | 1688采购账号ID |
| `goodsPurchaseOrderList[].supplierId` | string | 是 | 供应商ID |
| `goodsPurchaseOrderList[].warehouseId` | string | 是 | 收货仓库ID |
| `goodsPurchaseOrderList[].warehouseType` | string | 是 | 仓库类型 |
| `goodsPurchaseOrderList[].thirdWarehouseProviderAuthId` | string |  | 三方仓授权ID |
| `goodsPurchaseOrderList[].shippingFee` | string |  | 采购运费 |
| `goodsPurchaseOrderList[].otherFee` | string |  | 其他费用 |
| `goodsPurchaseOrderList[].discountFee` | string |  | 优惠金额 |
| `goodsPurchaseOrderList[].goodsShareFeeType` | string | 是 | 费用均摊方式：'1'(按数量) / '2'(按金额) / '3'(按重量) |
| `goodsPurchaseOrderList[].gmtPredictArrival` | string |  | 预计到货日期 |
| `goodsPurchaseOrderList[].accountNote` | string |  | 采购备注 |
| `goodsPurchaseOrderList[].buyerRemark` | string |  | 买家留言（1688下单用） |
| `goodsPurchaseOrderList[].flow` | string | 是 | 下单方式：general-批发、fenxiao-代发 |
| `goodsPurchaseOrderList[].consigneeInfo` | object | 是 | 收货地址信息 |
| `goodsPurchaseOrderList[].consigneeInfo.province` | string | 是 | 省 |
| `goodsPurchaseOrderList[].consigneeInfo.city` | string | 是 | 市 |
| `goodsPurchaseOrderList[].consigneeInfo.county` | string |  | 区 |
| `goodsPurchaseOrderList[].consigneeInfo.town` | string |  | 镇 |
| `goodsPurchaseOrderList[].consigneeInfo.fullname` | string | 是 | 全名 |
| `goodsPurchaseOrderList[].consigneeInfo.mobile` | string | 是 | 手机 |
| `goodsPurchaseOrderList[].consigneeInfo.address` | string | 是 | 地址 |
| `goodsPurchaseOrderList[].consigneeInfo.fullAddress` | string |  | 收件人完整地址 |
| `goodsPurchaseOrderList[].goodsSkuList` | array<object> | 是 | 商品列表信息 |
| `goodsPurchaseOrderList[].goodsSkuList[].goodsPurchaseOrderSkuId` | integer |  | 采购单SKU记录ID（编辑时有值） |
| `goodsPurchaseOrderList[].goodsSkuList[].goodsSkuId` | integer | 是 | 商品SKU ID |
| `goodsPurchaseOrderList[].goodsSkuList[].purchaseNum` | integer | 是 | 采购数量 |
| `goodsPurchaseOrderList[].goodsSkuList[].purchasePrice` | string | 是 | 采购单价 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceItemId` | string | 是 | 1688商品ID |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceSkuId` | string |  | 1688 SKU ID |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceSpecId` | string |  | 1688规格ID |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceImgUrl` | string |  | 1688商品图片URL |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceSkuSubName` | string |  | 1688 SKU规格名称 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourcePrice` | string |  | 1688价格 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceTitle` | string |  | 1688商品标题 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceProductUrl` | string |  | 1688商品链接 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourcePurchaseUrl` | string |  | 1688采购链接（同 productUrl） |
| `goodsPurchaseOrderList[].goodsSkuList[].thirdWarehouseGoodsSkuId` | string |  | 映射的第三方商品SKU ID |
| `saveOption` | string | 是 | 保存选项：save-保存到草稿箱，create1688Order-保存并下单 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successDataList` | object | 成功数据列表 |
| `successDataList.index` | string | 序号 |
| `successDataList.goodsPurchaseOrderSn` | string | 采购单号 |
| `successDataList.purchaseOrderSn` | string | 1688单号 |
| `successDataList.goodsPurchaseOrderId` | string | 采购单ID |
| `errors` | object | 错误数据列表 |
| `errors.index` | string | 序号 |
| `errors.errorMsg` | string | 错误信息 |
| `errors.errorType` | string | 错误类型 |
| `errors.goodsPurchaseOrderSn` | string | 采购单号 |
| `errors.purchaseOrderSn` | string | 1688单号 |
| `errors.goodsPurchaseOrderId` | string | 采购单ID |
| `successGoodsPurchaseOrderIds` | array<integer> | 成功的采购订单ID列表 |

#### 编辑采购单

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order`  (文档: api-479599774)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |
| `supplierId` | string | 是 | 供应商ID |
| `warehouseId` | string | 是 | 仓库ID |
| `warehouseType` | string | 是 | 仓库类型(self:自营仓,forwarder:货代仓库) |
| `thirdWarehouseProviderAuthId` | string |  | 三方仓授权id(仓库类型为forwarder时必填) |
| `gmtPredictArrival` | string |  | 预计到货时间 |
| `accountNote` | string |  | 采购备注 |
| `goodsShareFeeType` | string |  | 费用分摊方式，费用均摊方式1数量,2金额,3重量 |
| `ali1688Payment` | string |  | 1688费用 |
| `totalPurchasePrice` | string |  | 总采购价格 |
| `discountFee` | string |  | 折扣费用 |
| `otherFee` | string |  | 其他费用 |
| `shippingFee` | string |  |  |
| `goodsSkuList` | array<object> |  | 采购商品列表 |
| `goodsSkuList[].goodsPurchaseOrderSkuId` | integer |  | 采购单SKU记录ID（编辑时有值） |
| `goodsSkuList[].goodsSkuId` | integer | 是 | 商品SKU ID |
| `goodsSkuList[].purchaseNum` | integer | 是 | 采购数量 |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价 |
| `goodsSkuList[].sourceItemId` | string |  | 1688商品ID |
| `goodsSkuList[].sourceSkuId` | string |  | 1688 SKU ID |
| `goodsSkuList[].sourceSpecId` | string |  | 1688规格ID |
| `goodsSkuList[].sourceImgUrl` | string |  | 1688商品图片URL |
| `goodsSkuList[].sourceSkuSubName` | string |  | 1688 SKU规格名称 |
| `goodsSkuList[].sourcePrice` | string |  | 1688价格 |
| `goodsSkuList[].sourceTitle` | string |  | 1688商品标题 |
| `goodsSkuList[].sourceProductUrl` | string |  | 1688商品链接 |
| `goodsSkuList[].sourcePurchaseUrl` | string |  | 1688采购链接（同 productUrl） |
| `goodsSkuList[].thirdWarehouseGoodsSkuId` | string | 是 | 映射的三方仓商品SKU ID(仓库类型为forwarder时必填) |
| `saveOption` | string |  | 存选项save保存,submitAudit提交审核,passAudit提交并通过审核 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsPurchaseOrderInternalSn` | string | 采购单号 |

#### 采购单动手填写运单号

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order_shipping`  (文档: api-479599775)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单id |
| `packageList` | array<object> |  | 包裹列表 |
| `packageList[].logisticsName` | string |  | 物流公司 |
| `packageList[].waybillCode` | string |  | 快递单号 |

#### 采购单修改运单信息

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_shipping`  (文档: api-479599776)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单id |
| `packageList` | array<object> |  | 包裹列表 |
| `packageList[].logisticsName` | string |  | 物流公司 |
| `packageList[].waybillCode` | string |  | 快递单号 |
| `orderShippingId` | string |  | 运单信息id |

#### 采购单更新平台运单信息

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_outer_shipping`  (文档: api-479599777)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单ID |
| `purchaseOrderInfo` | object |  | 采购单信息 |
| `purchaseOrderInfo.purchasePlatform` | string |  | 下单平台 |
| `purchaseOrderInfo.purchaseOrderSn` | string |  | 货源单号 |
| `purchaseOrderInfo.purchaseOrderBuyer` | string |  | 买家帐号 |
| `purchaseOrderInfo.purchaseOrderSeller` | string |  | 卖家帐号 |
| `purchaseOrderInfo.purchaseOrderPackages` | array<object> |  | 包裹信息 |
| `purchaseOrderInfo.purchaseOrderPackages[].purchaseOrderLogisticsName` | string |  | 物流公司 |
| `purchaseOrderInfo.purchaseOrderPackages[].purchaseOrderWaybillCode` | string |  | 快递单号 |
| `shippingId` | string |  | 运单ID |

#### 取消采购单

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/cancel_goods_purchase_order`  (文档: api-479599778)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |
| `cancelReason` | string | 是 | 取消原因 缺货：outOfStock，换货：exchangeGoods，不想要了：dontWant，其他：other |
| `cancelNote` | string |  | 备注说明 |
| `isCancel1688` | integer |  | 同时取消1688订单 |

#### 标记采购单结束

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/finish_goods_purchase_order`  (文档: api-479599779)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |

#### 向1688下单

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order_by_goods_purchase_order_ids`  (文档: api-479599780)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderIds` | array<integer> | 是 | 采购单IDs |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successDataList` | object | 成功数据列表 |
| `successDataList.index` | string | 序号 |
| `successDataList.goodsPurchaseOrderSn` | string | 采购单号 |
| `successDataList.purchaseOrderSn` | string | 1688单号 |
| `successDataList.goodsPurchaseOrderId` | string | 采购单ID |
| `errors` | object | 错误数据列表 |
| `errors.index` | string | 序号 |
| `errors.errorMsg` | string | 错误信息 |
| `errors.errorType` | string | 错误类型 |
| `errors.goodsPurchaseOrderSn` | string | 采购单号 |
| `errors.purchaseOrderSn` | string | 1688单号 |
| `errors.goodsPurchaseOrderId` | string | 采购单ID |
| `successGoodsPurchaseOrderIds` | array<integer> | 成功的采购订单ID列表 |

#### 获取采购单列表

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/fetch/search_goods_purchase_order_page`  (文档: api-479599781)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsPurchaseOrderList` | array<object> | 商品采购订单列表 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderId` | integer | 采购单ID |
| `goodsPurchaseOrderList[].goodsPurchaseOrderInternalSn` | string | 采购单号 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSn` | string | 1688货源单号；有值代表已下1688单 |
| `goodsPurchaseOrderList[].goodsPurchasePlatform` | string | 采购平台标识 other/1688 |
| `goodsPurchaseOrderList[].status` | string | 订单状态 |
| `goodsPurchaseOrderList[].goodsPurchaseTotalPrice` | string | 商品总采购价 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderAmount` | string | 订单应付金额 |
| `goodsPurchaseOrderList[].shippingFee` | string | 运费 |
| `goodsPurchaseOrderList[].otherFee` | string | 其他费用 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderDiscount` | string | 折扣金额 |
| `goodsPurchaseOrderList[].confirmPaymentAmount` | string | 已付款金额 |
| `goodsPurchaseOrderList[].applyPaymentAmount` | string | 已申请付款金额 |
| `goodsPurchaseOrderList[].goodsPurchaseTotalNum` | string | 采购总数量 |
| `goodsPurchaseOrderList[].gmtCreate` | string | 创建时间 |
| `goodsPurchaseOrderList[].gmtPredictArrival` | string | 预计到货时间 |
| `goodsPurchaseOrderList[].createSubAppAccountName` | string | 创建人（采购员）姓名 |
| `goodsPurchaseOrderList[].resellerAccount` | string | 1688货源账号 |
| `goodsPurchaseOrderList[].accountNote` | string | 备注内容 |
| `goodsPurchaseOrderList[].auditReason` | string | 审核不通过原因 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSupplier` | object | 供货商信息 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSupplier.shopName` | string | 供货商名称 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSupplier.sellerId` | string | 供货商 ID |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSupplier.homeUrl` | string | 供货商店铺主页（有值时名称可点击跳转） |
| `goodsPurchaseOrderList[].warehouse` | object | 收货仓库信息 |
| `goodsPurchaseOrderList[].warehouse.warehouseName` | string | 收货仓库名称 |
| `goodsPurchaseOrderList[].warehouse.fullAddress` | string | 仓库地址 |
| `goodsPurchaseOrderList[].warehouse.contactName` | string | 仓库联系人 |
| `goodsPurchaseOrderList[].warehouse.contactPhone` | string | 仓库联系电话 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList` | array<object> | SKU 明细列表 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsPurchaseOrderSkuId` | integer | ID |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsSkuId` | string | 商品 SKU ID |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsName` | string | 商品名称 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsSkuSubName` | string | 规格名称 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsSkuOuterId` | string | 商品 SKU |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].logoUrl` | string | 商品图片 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].purchaseNum` | string | 采购数量 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].purchasePrice` | string | 采购单价 |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].receiveNum` | string | 已收货数量（到货量列及到货量汇总用） |
| `goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].totalPurchasePrice` | string | SKU 小计金额 |
| … | | 共 85 个字段，详见 openapi.json |

#### 签收记录列表

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order_receive/fetch/search_goods_purchase_order_receive_page`  (文档: api-479599771)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `goodsSkuOuterIds` | string |  | 商品SKU |
| `goodsSkuOuterIdsRp` | string |  | 商品SKU搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsPurchaseOrderNumValue` | string |  | 采购单号，运单号 |
| `goodsPurchaseOrderNumRp` | string |  | 采购单号，运单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `waybillCode` | string |  | 采购物流单号 |
| `waybillCodeRp` | string |  | 采购物流单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsPurchaseOrderSnList` | array<string> |  | 货源单号 |
| `goodsPurchaseOrderSnListRp` | string |  | 货源单号列表搜索类型;(rss:前缀,lss:后缀,ss:模糊,eq:精确) |
| `gmtCreateStart` | string |  | 采购单创建日期开始 |
| `gmtCreateEnd` | string |  | 采购单创建日期结束 |
| `source` | string |  | 来源1688/other |
| `tab` | string |  | 订单状态：inDraft:草稿箱;waitAudit:待审核;hasSend:待收货;finish:已完成;cancelAndReturn:已取消、已退货 |
| `goodsSupplierId` | integer |  | 供应商ID |
| `warehouseId` | array<integer> |  | 收货仓库ID |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `purchaseOrderReceiveList` | array<object> | 商品采购订单收货列表 |
| `purchaseOrderReceiveList[].goodsPurchaseOrderId` | string | 采购单id |
| `purchaseOrderReceiveList[].goodsPurchaseOrderInternalSn` | string | 采购单号 |
| `purchaseOrderReceiveList[].createSubAppAccountName` | string | 创建人账号 姓名 |
| `purchaseOrderReceiveList[].gmtCreate` | string | 创建时间 |
| `purchaseOrderReceiveList[].gmtModified` | string | 更新时间 |
| `purchaseOrderReceiveList[].receiveInfo` | object | 签收明细 |
| `purchaseOrderReceiveList[].receiveInfo.goodsPurchaseOrderReceiveId` | string | 签收记录id |
| `purchaseOrderReceiveList[].receiveInfo.createSubAppAccountName` | string | 签收人姓名（子账号时展示） |
| `purchaseOrderReceiveList[].receiveInfo.gmtCreate` | string | 创建时间 |
| `purchaseOrderReceiveList[].receiveInfo.gmtReceive` | string | 签收时间 |
| `purchaseOrderReceiveList[].receiveInfo.skuList` | array<object> | 签收sku列表 |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].goodsPurchaseOrderReceiveSkuId` | string | ID |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].currentReceiveNum` | string | 本次签收数量 |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].warehouseShelfCellId` | string | 签收仓位id |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].goodsSkuId` | string | sku id |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo` | object | sku信息 |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo.goodsPurchaseOrderId` | string | 采购单id |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo.goodsId` | string | 商品id |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo.goodsSkuId` | string | 商品sku id |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo.goodsSkuOuterId` | string | 商品sku |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo.purchaseNum` | string | 采购数量 |
| `purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo.receiveNum` | string | 总签收数量 |
| `purchaseOrderReceiveList[].goodsPurchaseOrderSupplier` | object | 供应商 |
| `purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.shopName` | string | 供货商名称 |
| `purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.sellerId` | string | 供货商 ID |
| `purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.homeUrl` | string | 供货商店铺主页（有值时名称可点击跳转） |
| `purchaseOrderReceiveList[].shippingList` | array<object> | 运单列表 |
| `purchaseOrderReceiveList[].shippingList[].goodsPurchaseOrderShippingId` | string | 运单 ID |
| `purchaseOrderReceiveList[].shippingList[].goodsPurchaseOrderId` | string | 关联采购单 ID |
| `purchaseOrderReceiveList[].shippingList[].platformOrderSn` | string | 货源单号 |
| `purchaseOrderReceiveList[].shippingList[].platformOrderStatus` | string | 平台订单状态 |
| `purchaseOrderReceiveList[].shippingList[].platformBuyer` | string | 平台买家账号 |
| `purchaseOrderReceiveList[].shippingList[].platformOrderStartTime` | string | 平台下单时间 |
| `purchaseOrderReceiveList[].shippingList[].platform` | string | 物流平台标识 |
| `purchaseOrderReceiveList[].shippingList[].platformName` | string | 物流平台名称 |
| `purchaseOrderReceiveList[].shippingList[].purchaseOrderDetailUrl` | string | 1688采购订单详情链接 |
| `purchaseOrderReceiveList[].shippingList[].platformOrderFullAddress` | string | 平台订单收货地址 |
| `purchaseOrderReceiveList[].shippingList[].platformOrderOriginStatus` | string | 1688订单状态 |
| `purchaseOrderReceiveList[].shippingList[].platformOrderOriginStatusText` | string | 平台订单原始状态文案（1688 订单状态展示） |
| … | | 共 54 个字段，详见 openapi.json |

#### 根据货源链接获取1688商品SKU列表

`POST /open/v1/ewm/supplier/fetch/get_ali1688_item_by_source_url`  (文档: api-532434244)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `sourceUrl` | string | 是 | 1688货源链接 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuList` | array<object> | 商品列表信息 |
| `goodsSkuList[].sourceItemId` | string | 1688商品ID |
| `goodsSkuList[].sourceSkuId` | string | 1688 SKU ID |
| `goodsSkuList[].sourceSpecId` | string | 1688规格ID |
| `goodsSkuList[].sourceImgUrl` | string | 1688商品图片URL |
| `goodsSkuList[].sourceSkuSubName` | string | 1688 SKU规格名称 |
| `goodsSkuList[].sourcePrice` | string | 1688价格 |
| `goodsSkuList[].purchasePrice` | string | 采购价格 |
| `goodsSkuList[].sourceTitle` | string | 1688商品标题 |
| `goodsSkuList[].sourceProductUrl` | string | 1688商品链接 |

#### 获取缺货、备货建议列表

`POST /open/v1/ewm/goods_purchase_order/goods_purchase_suggest/fetch/search_goods_purchase_suggest_page`  (文档: api-479599782)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `warehouseId` | array<integer> |  | 仓库ID |
| `goodsSupplierId` | integer |  | 供货商 |
| `type` | string |  | 类型(默认是备货),stockUp备货,outOfStock缺货 |
| `source` | string |  | other/1688 |
| `shopIds` | array<integer> |  | 店铺id |
| `goodsCodeValue` | string |  | 商品sku |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `purchaseSuggestList` | array<object> | 商品采购建议列表 |
| `purchaseSuggestList[].goodsId` | integer | 商品id |
| `purchaseSuggestList[].goodsSkuId` | integer | 商品sku id |
| `purchaseSuggestList[].dailySales` | string | 日销量 |
| `purchaseSuggestList[].minTriggerSuggestNum` | string | 采购下限 |
| `purchaseSuggestList[].maxPrepareDays` | integer | 最大备货天数 |
| `purchaseSuggestList[].minPrepareDays` | integer | 最小备货天数 |
| `purchaseSuggestList[].orderNeedNum` | integer | 订单需求量 |
| `purchaseSuggestList[].recentSaleNumDt7` | integer | 近7天销量 |
| `purchaseSuggestList[].recentSaleNumDt30` | integer | 近30天销量 |
| `purchaseSuggestList[].suggestNum` | integer | 建议数量 |
| `purchaseSuggestList[].safeStockNum` | integer | 安全库存 |
| `purchaseSuggestList[].goodsSkuOuterId` | string | 商品SKU |
| `purchaseSuggestList[].warehouseId` | integer | 仓库id |
| `purchaseSuggestList[].warehouseName` | string | 仓库名称 |
| `total` | integer | 总计 |

### 采购 > 供应商

#### 获取供应商列表

`POST /open/v1/ewm/supplier/fetch/search_supplier_page`  (文档: api-479599789)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `source` | string |  | 供应商类型 |
| `settlementMethod` | string |  | 结算方式 payBeforeDelivery,payOnDelivery,payPeriod,payWeek,payHalfMonth,payMonth,installment |
| `goodsSupplierId` | integer |  | 供应商id |
| `paymentMethod` | string |  | 支付方式 bank:银行转账,thirdPay:第三方支付(支付宝等) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `supplierList` | array<object> | 供应商列表 |
| `supplierList[].goodsSupplierId` | string | 供应商ID |
| `supplierList[].source` | string | 供应商类型code |
| `supplierList[].shopName` | string | 供应商名称 |
| `supplierList[].homeUrl` | string | 主页url |
| `supplierList[].purchaseUrl` | string | 采购网址 |
| `supplierList[].address` | string | 详细地址 |
| `supplierList[].arrivalDays` | string | 到货天数 |
| `supplierList[].accountNote` | string | 账户备注 |
| `supplierList[].contactName` | string | 联系人姓名 |
| `supplierList[].contactPhone` | string | 联系人电话 |
| `supplierList[].companyPhone` | string | 公司电话 |
| `supplierList[].wangwang` | string | 淘宝旺旺 |
| `supplierList[].email` | string | 邮箱 |
| `supplierList[].qq` | string | QQ |
| `supplierList[].settlementMethod` | string | 结算方式 |
| `supplierList[].paymentMethod` | string | 付款方式 |
| `supplierList[].bankName` | string | 银行名称 |
| `supplierList[].bankCardOwnerName` | string | 开户名 |
| `supplierList[].bankCardNumber` | string | 银行卡号 |
| `supplierList[].totalPurchaseOrderNum` | string | 采购次数 |
| `supplierList[].returnPurchaseGoodsRate` | string | 退货采购商品率 |
| `supplierList[].exceptionPurchaseOrderRate` | string | 异常采购订单率 |
| `supplierList[].supplyTime` | string | 供货时效 |
| `supplierList[].totalPurchaseGoodsNum` | string | 总采购商品数 |
| `supplierList[].returnPurchaseGoodsNum` | string | 退货采购商品数 |
| `supplierList[].exceptionPurchaseOrderNum` | string | 异常采购订单数 |
| `supplierList[].provinceName` | string | 省名称 |
| `supplierList[].cityName` | string | 市名称 |
| `supplierList[].countyName` | string | 区名称 |
| `supplierList[].townName` | string | 镇名称 |
| `supplierList[].fullAddress` | string | 完整地址 |
| `supplierList[].sourceName` | string | 供应商类型名称 |
| `total` | integer | 总数 |

#### 获取供应商信息

`POST /open/v1/ewm/supplier/fetch/get_supplier_info`  (文档: api-479599790)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSupplierId` | integer | 是 | 供应商id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `supplierDetail` | object | 供应商详情 |
| `supplierDetail.goodsSupplierId` | string | 供应商ID |
| `supplierDetail.source` | string | 供应商类型code |
| `supplierDetail.shopName` | string | 供应商名称 |
| `supplierDetail.homeUrl` | string | 主页url |
| `supplierDetail.purchaseUrl` | string | 采购网址 |
| `supplierDetail.address` | string | 详细地址 |
| `supplierDetail.arrivalDays` | string | 到货天数 |
| `supplierDetail.accountNote` | string | 账户备注 |
| `supplierDetail.contactName` | string | 联系人姓名 |
| `supplierDetail.contactPhone` | string | 联系人电话 |
| `supplierDetail.companyPhone` | string | 公司电话 |
| `supplierDetail.wangwang` | string | 淘宝旺旺 |
| `supplierDetail.email` | string | 邮箱 |
| `supplierDetail.qq` | string | QQ |
| `supplierDetail.settlementMethod` | string | 结算方式 |
| `supplierDetail.paymentMethod` | string | 付款方式 |
| `supplierDetail.bankName` | string | 银行名称 |
| `supplierDetail.bankCardOwnerName` | string | 开户名 |
| `supplierDetail.bankCardNumber` | string | 银行卡号 |
| `supplierDetail.totalPurchaseOrderNum` | string | 采购次数 |
| `supplierDetail.returnPurchaseGoodsRate` | string | 退货采购商品率 |
| `supplierDetail.exceptionPurchaseOrderRate` | string | 异常采购订单率 |
| `supplierDetail.supplyTime` | string | 供货时效 |
| `supplierDetail.totalPurchaseGoodsNum` | string | 总采购商品数 |
| `supplierDetail.returnPurchaseGoodsNum` | string | 退货采购商品数 |
| `supplierDetail.exceptionPurchaseOrderNum` | string | 异常采购订单数 |
| `supplierDetail.provinceName` | string | 省名称 |
| `supplierDetail.cityName` | string | 市名称 |
| `supplierDetail.countyName` | string | 区名称 |
| `supplierDetail.townName` | string | 镇名称 |
| `supplierDetail.fullAddress` | string | 完整地址 |
| `supplierDetail.sourceName` | string | 供应商类型名称 |

#### 获取供应商类型列表

`POST /open/v1/ewm/supplier/fetch/get_supplier_platform_list`  (文档: api-479599791)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `supplierPlatformOptions` | array<object> |  |
| `supplierPlatformOptions[].label` | string | 供应商类型名称 |
| `supplierPlatformOptions[].value` | string | 供应商类型code |

#### 修改供应商

`POST /open/v1/ewm/supplier/operate/edit_supplier`  (文档: api-479653199)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSupplierId` | integer | 是 | 供应商id |
| `shopName` | string | 是 | 供应商名称 |
| `source` | string |  | 供应商类型code |
| `homeUrl` | string |  | 主页网址 |
| `purchaseUrl` | string |  | 采购网址 |
| `arrivalDays` | string |  | 到货周期 |
| `accountNote` | string |  | 备注 |
| `address` | string |  | 地址 |
| `contactName` | string |  | 联系人姓名 |
| `contactPhone` | string |  | 联系人电话 |
| `companyPhone` | string |  | 公司电话 |
| `wangwang` | string |  | 网旺号 |
| `email` | string |  | 邮箱 |
| `qq` | string |  | QQ |
| `settlementMethod` | string |  | 结算方式 |
| `paymentMethod` | string |  | 付款方式 |
| `bankName` | string |  | 银行名称 |
| `bankCardNumber` | string |  | 银行卡号 |
| `bankCardOwnerName` | string |  | 开户人姓名 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `@api` | object | POST |

#### 创建供应商

`POST /open/v1/ewm/supplier/operate/add_supplier`  (文档: api-479653198)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopName` | string | 是 | 供应商名称 |
| `source` | string | 是 | 供应商类型code |
| `homeUrl` | string |  | 主页网址 |
| `purchaseUrl` | string |  | 采购网址 |
| `arrivalDays` | string |  | 到货周期 |
| `accountNote` | string |  | 备注信息 |
| `address` | string |  | 地址 |
| `contactName` | string |  | 联系人姓名 |
| `contactPhone` | string |  | 联系人电话 |
| `companyPhone` | string |  | 公司电话 |
| `wangwang` | string |  | 网旺号 |
| `email` | string |  | 邮箱 |
| `qq` | string |  | QQ |
| `settlementMethod` | string |  | 结算方式 |
| `paymentMethod` | string |  | 付款方式 |
| `bankName` | string |  | 银行名称 |
| `bankCardNumber` | string |  | 银行账号 |
| `bankCardOwnerName` | string |  | 开户人姓名 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `@api` | object | POST |

### 仓储 > 商品 > 商品

#### 获取多规格商品列表

`POST /open/v1/ewm/goods/goods/fetch/search_goods_page`  (文档: api-479599763)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `goodsSkuOuterIds` | array<string> |  | sku |
| `groupId` | string |  | 分组ID |
| `itemNum` | array<string> |  | SPU |
| `keyword` | string |  | 商品sku |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsList` | array<object> |  |
| `goodsList[].goodsId` | string | 商品ID |
| `goodsList[].goodsGroupId` | string | 商品分组ID |
| `goodsList[].goodsName` | string | 商品名称 |
| `goodsList[].foreignGoodsName` | string | 商品英文 |
| `goodsList[].goodsType` | string | 商品类型 |
| `goodsList[].goodsMode` | string | 商品模式 single 单品 |
| `goodsList[].goodsBrandId` | string | 商品品牌ID |
| `goodsList[].units` | string | 商品单位 |
| `goodsList[].itemNum` | string | 商品编号 |
| `goodsList[].weight` | string | 商品重量 |
| `goodsList[].width` | string | 商品宽度 |
| `goodsList[].height` | string | 商品高度 |
| `goodsList[].length` | string | 商品长度 |
| `goodsList[].goodsStatus` | string | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `goodsList[].goodsSaleStatus` | string | 商品销售状态 0普通 1热销 2 滞销 |
| `goodsList[].isNew` | string | 是否新品 |
| `goodsList[].isStockEmpty` | string | 是否库存为空 |
| `goodsList[].marketName` | string | 市场名称 |
| `goodsList[].staffName` | string | 档口名称 |
| `goodsList[].invoiceNcm` | string | 发票NCM |
| `goodsList[].icmsOrigem` | string | 发票-原场地 |
| `goodsList[].invoiceNcmDesc` | string | 发票NCM描述 |
| `goodsList[].gmtCreate` | string | 创建时间 |
| `goodsList[].gmtModified` | string | 修改时间 |
| `goodsList[].minGoodsSkuPurchasePrice` | string | 最小商品SKU采购价 |
| `goodsList[].skuList` | array<object> | SKU列表 |
| `goodsList[].skuList[].goodsSkuId` | string | 商品SKU ID |
| `goodsList[].skuList[].goodsId` | string | 商品ID |
| `goodsList[].skuList[].status` | string | 商品状态 |
| `goodsList[].skuList[].isInWarehouse` | string | 是否入库 |
| `goodsList[].skuList[].goodsSkuOuterId` | string | 商品SKU |
| `goodsList[].skuList[].goodsSkuSubName` | string | 规格 |
| `goodsList[].skuList[].goodsSkuCustomCode` | string | 商品编码 |
| `goodsList[].skuList[].goodsSkuCustomBarcode` | string | 商品条码 |
| `goodsList[].skuList[].appPictureId` | string | 图片ID |
| `goodsList[].skuList[].logo` | string | 图片URL |
| `goodsList[].skuList[].logoOssPath` | string | 图片OSS路径 |
| `goodsList[].skuList[].purchasePrice` | string | 单价 |
| `goodsList[].skuList[].stockNum` | string | 库存数量 |
| … | | 共 139 个字段，详见 openapi.json |

#### 获取商品详情

`POST /open/v1/ewm/goods/goods/fetch/get_goods_info`  (文档: api-479599764)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsId` | integer | 是 | 商品id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsDetail` | object |  |
| `goodsDetail.goodsId` | string | 商品ID |
| `goodsDetail.goodsGroupId` | string | 商品分组ID |
| `goodsDetail.goodsName` | string | 商品名称 |
| `goodsDetail.foreignGoodsName` | string | 商品英文 |
| `goodsDetail.goodsType` | string | 商品类型 |
| `goodsDetail.goodsMode` | string | 商品模式 single 单品 |
| `goodsDetail.goodsBrandId` | string | 商品品牌ID |
| `goodsDetail.units` | string | 商品单位 |
| `goodsDetail.itemNum` | string | 商品编号 |
| `goodsDetail.weight` | string | 商品重量 |
| `goodsDetail.width` | string | 商品宽度 |
| `goodsDetail.height` | string | 商品高度 |
| `goodsDetail.length` | string | 商品长度 |
| `goodsDetail.goodsStatus` | string | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `goodsDetail.goodsSaleStatus` | string | 商品销售状态 0普通 1热销 2 滞销 |
| `goodsDetail.isNew` | string | 是否新品 |
| `goodsDetail.isStockEmpty` | string | 是否库存为空 |
| `goodsDetail.marketName` | string | 市场名称 |
| `goodsDetail.staffName` | string | 档口名称 |
| `goodsDetail.invoiceNcm` | string | 发票NCM |
| `goodsDetail.icmsOrigem` | string | 发票-原场地 |
| `goodsDetail.invoiceNcmDesc` | string | 发票NCM描述 |
| `goodsDetail.gmtCreate` | string | 创建时间 |
| `goodsDetail.gmtModified` | string | 修改时间 |
| `goodsDetail.minGoodsSkuPurchasePrice` | string | 最小商品SKU采购价 |
| `goodsDetail.skuList` | array<object> | SKU列表 |
| `goodsDetail.skuList[].goodsSkuId` | string | 商品SKU ID |
| `goodsDetail.skuList[].goodsId` | string | 商品ID |
| `goodsDetail.skuList[].status` | string | 商品状态 |
| `goodsDetail.skuList[].isInWarehouse` | string | 是否入库 |
| `goodsDetail.skuList[].goodsSkuOuterId` | string | 商品SKU |
| `goodsDetail.skuList[].goodsSkuSubName` | string | 规格 |
| `goodsDetail.skuList[].goodsSkuCustomCode` | string | 商品编码 |
| `goodsDetail.skuList[].goodsSkuCustomBarcode` | string | 商品条码 |
| `goodsDetail.skuList[].appPictureId` | string | 图片ID |
| `goodsDetail.skuList[].logo` | string | 图片URL |
| `goodsDetail.skuList[].logoOssPath` | string | 图片OSS路径 |
| `goodsDetail.skuList[].purchasePrice` | string | 单价 |
| `goodsDetail.skuList[].stockNum` | string | 库存数量 |
| … | | 共 139 个字段，详见 openapi.json |

#### 添加商品

`POST /open/v1/ewm/goods/goods/operate/add_goods`  (文档: api-479599765)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsGroupId` | integer |  | 商品分组ID |
| `goodsMode` | string |  | 商品模式 single(单品),multi(多品) |
| `goodsName` | string | 是 | 商品中文名称 |
| `goodsStatus` | string | 是 | 商品状态：0:停售1:在售2:热销4:新品3:滞销5:清仓 |
| `foreignGoodsName` | string |  | 商品外文名称 |
| `marketName` | string |  | 采购档口 |
| `staffName` | string |  | 采购档口 |
| `goodsGroupName` | string |  | 商品分组名称 |
| `invoiceNcm` | string |  | 巴西发票NCM编码 |
| `icmsOrigem` | string |  | 巴西ICMS原产地编码 |
| `units` | string |  | 商品单位 |
| `goodsBrandId` | string |  | 商品品牌ID |
| `goodsSkuList` | array<object> | 是 | SKU列表 |
| `goodsSkuList[].goodsSkuId` | integer |  | SKU ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsSkuOuterId` | string |  | 商品SKU编码 |
| `goodsSkuList[].platformOuterSkuIds` | array<string> |  | 平台外部SKU ID列表 |
| `goodsSkuList[].platformSkuIds` | array<string> |  | 平台内部SKU ID列表 |
| `goodsSkuList[].skuImgUrl` | string |  | SKU图片URL |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价（参考价格） |
| `goodsSkuList[].weight` | string |  | 重量(KG) |
| `goodsSkuList[].width` | string |  | 宽度 |
| `goodsSkuList[].height` | string |  | 高度 |
| `goodsSkuList[].length` | string |  | 长度 |
| `goodsSkuList[].goodsAttributeList` | array<object> |  | 规格属性列表（多规格模式必填，单品可为空） |
| `goodsSkuList[].goodsAttributeList[].goodsAttributeId` | integer |  | 规格属性ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsAttributeList[].goodsAttributeValueId` | integer |  | 规格属性值ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsAttributeList[].attributeName` | string |  | 规格属性名称（如：颜色、尺码） |
| `goodsSkuList[].goodsAttributeList[].attributeValue` | string |  | 规格属性值（如：红色、XL） |
| `goodsSkuList[].goodsSkuBundleList` | array<object> |  | 组合品子商品列表（组合品模式） |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuOuterId` | string |  | 子商品SKU编码 |
| `goodsSkuList[].goodsSkuBundleList[].goodsName` | string |  | 子商品名称 |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuSubName` | string |  | 子商品规格名称 |
| `goodsSkuList[].goodsSkuBundleList[].logoUrl` | string |  | 子商品图片URL |
| `goodsSkuList[].goodsSkuBundleList[].quantity` | string |  | 组合数量 |
| `goodsSkuList[].goodsSkuPackagingList` | array<object> |  | 包材列表 |
| `goodsSkuList[].goodsSkuPackagingList[].packagingId` | integer |  | 包材ID |
| `goodsSkuList[].goodsSkuPackagingList[].packableQuantity` | integer |  | 该包材可包装的商品数量 |
| `goodsSkuList[].customsDeclaration` | object |  | 报关/清关申报信息 |
| `goodsSkuList[].customsDeclaration.productAttrs` | array<string> |  | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
| `goodsSkuList[].customsDeclaration.productSubAttrs` | object |  | 各申报属性的详细值 |
| `goodsSkuList[].customsDeclaration.productSubAttrs.withBattery` | string |  | 带电报关属性：within_battery弱电，纯电：only_battery |
| `goodsSkuList[].customsDeclaration.productChineseName` | string |  | 申报中文名称 |
| `goodsSkuList[].customsDeclaration.productEnglishName` | string |  | 申报英文名称 |
| `goodsSkuList[].customsDeclaration.productWeight` | string |  | 申报重量(g) |
| `goodsSkuList[].customsDeclaration.productPrice` | string |  | 目的国申报金额(USD) |
| `goodsSkuList[].customsDeclaration.exportCountryDeclaredPrice` | string |  | 出口国申报金额(USD) |
| `goodsSkuList[].customsDeclaration.productMaterial` | string |  | 材质 |
| `goodsSkuList[].customsDeclaration.productPurpose` | string |  | 用途 |
| `goodsSkuList[].customsDeclaration.customCode` | string |  | 海关编码 |
| `goodsSkuList[].goodsSkuCustomCode` | string |  | 商品代码(UPC/ISBN/SN/GTIN) |
| `goodsSkuList[].goodsSkuNote` | string |  | SKU备注 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsId` | integer | 商品id |
| `goodsSkuIds` | integer | sku id |

#### 修改商品

`POST /open/v1/ewm/goods/goods/operate/edit_goods`  (文档: api-479599767)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsId` | integer | 是 | 商品ID |
| `goodsGroupId` | string |  | 商品分组ID |
| `goodsMode` | string |  | 商品模式 single(单品) |
| `goodsName` | string | 是 | 商品中文名称 |
| `goodsStatus` | string | 是 | 商品状态：0:停售1:在售2:热销4:新品3:滞销5:清仓 |
| `foreignGoodsName` | string |  | 商品外文名称 |
| `marketName` | string |  | 采购档口 |
| `staffName` | string |  | 采购档口 |
| `goodsGroupName` | string |  | 商品分组名称 |
| `invoiceNcm` | string |  | 巴西发票NCM编码 |
| `icmsOrigem` | string |  | 巴西ICMS原产地编码 |
| `units` | string |  | 商品单位 |
| `goodsBrandId` | string |  | 商品品牌ID |
| `goodsSkuList` | array<object> | 是 | SKU列表 |
| `goodsSkuList[].goodsSkuId` | integer |  | SKU ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsSkuOuterId` | string |  | 商品SKU编码 |
| `goodsSkuList[].platformOuterSkuIds` | array<string> |  | 平台外部SKU ID列表 |
| `goodsSkuList[].platformSkuIds` | array<string> |  | 平台内部SKU ID列表 |
| `goodsSkuList[].skuImgUrl` | string |  | SKU图片URL |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价（参考价格） |
| `goodsSkuList[].weight` | string |  | 重量(KG) |
| `goodsSkuList[].width` | string |  | 宽度 |
| `goodsSkuList[].height` | string |  | 高度 |
| `goodsSkuList[].length` | string |  | 长度 |
| `goodsSkuList[].goodsAttributeList` | array<object> |  | 规格属性列表（多规格模式必填，单品可为空） |
| `goodsSkuList[].goodsAttributeList[].goodsAttributeId` | integer |  | 规格属性ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsAttributeList[].goodsAttributeValueId` | integer |  | 规格属性值ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsAttributeList[].attributeName` | string |  | 规格属性名称（如：颜色、尺码） |
| `goodsSkuList[].goodsAttributeList[].attributeValue` | string |  | 规格属性值（如：红色、XL） |
| `goodsSkuList[].goodsSkuBundleList` | array<object> |  | 组合品子商品列表（组合品模式） |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuOuterId` | string |  | 子商品SKU编码 |
| `goodsSkuList[].goodsSkuBundleList[].goodsName` | string |  | 子商品名称 |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuSubName` | string |  | 子商品规格名称 |
| `goodsSkuList[].goodsSkuBundleList[].logoUrl` | string |  | 子商品图片URL |
| `goodsSkuList[].goodsSkuBundleList[].quantity` | string |  | 组合数量 |
| `goodsSkuList[].goodsSkuPackagingList` | array<object> |  | 包材列表 |
| `goodsSkuList[].goodsSkuPackagingList[].packagingId` | integer |  | 包材ID |
| `goodsSkuList[].goodsSkuPackagingList[].packableQuantity` | integer |  | 该包材可包装的商品数量 |
| `goodsSkuList[].customsDeclaration` | object |  | 报关/清关申报信息 |
| `goodsSkuList[].customsDeclaration.productAttrs` | array<string> |  | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
| `goodsSkuList[].customsDeclaration.productSubAttrs` | object |  | 各申报属性的详细值 |
| `goodsSkuList[].customsDeclaration.productSubAttrs.withBattery` | string |  | 带电报关属性：within_battery弱电，纯电：only_battery |
| `goodsSkuList[].customsDeclaration.productChineseName` | string |  | 申报中文名称 |
| `goodsSkuList[].customsDeclaration.productEnglishName` | string |  | 申报英文名称 |
| `goodsSkuList[].customsDeclaration.productWeight` | string |  | 申报重量(g) |
| `goodsSkuList[].customsDeclaration.productPrice` | string |  | 目的国申报金额(USD) |
| `goodsSkuList[].customsDeclaration.exportCountryDeclaredPrice` | string |  | 出口国申报金额(USD) |
| `goodsSkuList[].customsDeclaration.productMaterial` | string |  | 材质 |
| `goodsSkuList[].customsDeclaration.productPurpose` | string |  | 用途 |
| `goodsSkuList[].customsDeclaration.customCode` | string |  | 海关编码 |
| `goodsSkuList[].goodsSkuCustomCode` | string |  | 商品代码(UPC/ISBN/SN/GTIN) |
| `goodsSkuList[].goodsSkuNote` | string |  | SKU备注 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsId` | integer | 商品id |
| `goodsSkuIds` | integer | sku id |

#### 安全库存批量设置

`POST /open/v1/ewm/goods/goods/operate/batch_save_goods_suggest_config`  (文档: api-479599766)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSuggestConfigList` | array<object> |  | 商品建议配置列表 |
| `goodsSuggestConfigList[].goodsSkuId` | integer | 是 | 商品sku id |
| `goodsSuggestConfigList[].warehouseId` | integer | 是 | 仓库id |
| `goodsSuggestConfigList[].computeMode` | string | 是 | 计算方式 固定值：newValue |
| `goodsSuggestConfigList[].safeStock` | integer | 是 | 安全库存 |
| `goodsSuggestConfigList[].minTriggerSuggestNum` | integer |  | 库存下限 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `successCnt` | integer | 成功数量 |

### 仓储 > 商品 > 商品品牌

#### 获取列表

`POST /open/v1/ewm/goods/goods_brand/fetch/search_goods_brand_page`  (文档: api-479599768)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `brandList` | array<object> |  |
| `brandList[].goodsBrandId` | integer | 商品品牌ID |
| `brandList[].brandName` | string | 品牌名称 |
| `total` | integer | 总计 |

### 仓储 > 商品 > 商品分组

#### 获取商品分组列表

`POST /open/v1/ewm/goods/goods_group/fetch/get_goods_group_list`  (文档: api-479599769)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsGroupTree` | array<object> |  |
| `goodsGroupTree[].goodsGroupId` | string | 分组ID |
| `goodsGroupTree[].parentGoodsGroupId` | string | 父分组ID |
| `goodsGroupTree[].groupName` | string | 分组名称 |
| `goodsGroupTree[].level` | string | 级别 |
| `goodsGroupTree[].sort` | string | 排序 |
| `goodsGroupTree[].subGroups` | array<object> | 子分组 |

### 仓储 > 商品 > 商品sku

#### 获取商品SKU列表

`POST /open/v1/ewm/goods/goods_sku/fetch/search_goods_sku_page`  (文档: api-479599770)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `groupId` | string |  | 分组ID |
| `goodsMode` | string | 是 | 商品类型 single(单规格),bundle(组合) |
| `goodsSkuOuterIds` | array<string> |  | 商品sku |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuList` | array<object> | sku列表 |
| `goodsSkuList[].goodsSkuId` | string | 商品SKU ID |
| `goodsSkuList[].goodsId` | string | 商品ID |
| `goodsSkuList[].status` | string | 商品状态 |
| `goodsSkuList[].isInWarehouse` | string | 是否入库 |
| `goodsSkuList[].goodsSkuOuterId` | string | 商品SKU |
| `goodsSkuList[].goodsSkuSubName` | string | 规格 |
| `goodsSkuList[].goodsSkuCustomCode` | string | 商品编码 |
| `goodsSkuList[].goodsSkuCustomBarcode` | string | 商品条码 |
| `goodsSkuList[].appPictureId` | string | 图片ID |
| `goodsSkuList[].logo` | string | 图片URL |
| `goodsSkuList[].logoOssPath` | string | 图片OSS路径 |
| `goodsSkuList[].purchasePrice` | string | 单价 |
| `goodsSkuList[].stockNum` | string | 库存数量 |
| `goodsSkuList[].lockStockNum` | string | 锁定库存数量 |
| `goodsSkuList[].platformItemId` | string | 平台SKU ID |
| `goodsSkuList[].defaultGoodsSupplierId` | string | 默认供应商ID |
| `goodsSkuList[].weight` | string | 重量 |
| `goodsSkuList[].width` | string | 宽度 |
| `goodsSkuList[].height` | string | 高度 |
| `goodsSkuList[].length` | string | 长度 |
| `goodsSkuList[].lastPurchasePrice` | string | 最近一次购买价格 |
| `goodsSkuList[].goodsMode` | string | 商品模式 |
| `goodsSkuList[].goodsSkuNote` | string | 商品SKU备注 |
| `goodsSkuList[].gmtCreate` | string | 创建时间 |
| `goodsSkuList[].gmtModified` | string | 修改时间 |
| `goodsSkuList[].logoUrl` | string | 图片URL |
| `goodsSkuList[].goodsName` | string | 商品名称 |
| `goodsSkuList[].goodsGroupId` | string | 商品分组ID |
| `goodsSkuList[].goodsStatus` | string | 商品状态 |
| `goodsSkuList[].foreignGoodsName` | string | 商品英文名称 |
| `goodsSkuList[].goodsSaleStatus` | string | 销售状态 |
| `goodsSkuList[].isNew` | string | 是否新品 |
| `goodsSkuList[].isStockEmpty` | string | 是否库存为空 |
| `goodsSkuList[].goodsBrandId` | string | 商品品牌ID |
| `goodsSkuList[].units` | string | 商品单位 |
| `goodsSkuList[].goodsGroupName` | string | 分组名称 |
| `goodsSkuList[].goodsGroupBreadcrumb` | string | 分组路径 |
| `goodsSkuList[].supplierList` | array<object> | 供应商列表 |
| `goodsSkuList[].supplierList[].goodsSupplierId` | string | 供应商id |
| … | | 共 109 个字段，详见 openapi.json |

### 仓储 > 商品包材

#### 获取列表

`POST /open/v1/ewm/packaging/fetch/search_packaging_page`  (文档: api-479592181)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `packagingList` | array<object> | 包材列表 |
| `packagingList[].packagingId` | string | ID |
| `packagingList[].packagingCode` | string | code |
| `packagingList[].name` | string | 包材名称 |
| `packagingList[].price` | string | 价格 |
| `packagingList[].length` | string | 长度 |
| `packagingList[].width` | string | 宽度 |
| `packagingList[].height` | string | 高度 |
| `packagingList[].weight` | string | 重量 |
| `packagingList[].remark` | string | 备注 |
| `packagingList[].gmtCreate` | string | 创建时间 |
| `packagingList[].gmtModified` | string | 更新时间 |
| `total` | integer | 总数 |

### 仓储 > 数据统计 > 销售数据

#### 获取商品销售数据列表

`POST /open/v1/ewm/stat/goods_sale_data/fetch/search_goods_sale_data_page`  (文档: api-479602617)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `shopIds` | array<integer> | 是 | 店铺ID数组 |
| `gmtStart` | string | 是 | 开始日期如2022-07-01 |
| `gmtEnd` | string | 是 | 结束日期如2022-07-01 |
| `warehouseIds` | array<integer> |  | 仓库ID数组 |
| `logisticsAgentWarehouseIds` | array<integer> |  | 第三方仓库id |
| `goodsSkuOuterIds` | string |  | 商品SKU |
| `goodsSkuOuterIdsRp` | string |  | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsName` | string |  | 商品名称 |
| `goodsNameRp` | string |  | 商品名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsSkuCustomCodes` | string |  | 商品代码 |
| `goodsSkuCustomCodesRp` | string |  | 商品代码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `foreignGoodsName` | string |  | 商品外文名称 |
| `foreignGoodsNameRp` | string |  | 商品外文名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsGroupIds` | array<integer> |  | 商品分组ID列表 |
| `shopFilterType` | string |  | 店铺类型shopId-按店铺Id,group-按店铺分组拣货单 |
| `shopGroupIds` | array<integer> |  | 店铺分组id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSaleList` | array<object> |  |
| `goodsSaleList[].goodsSkuId` | string | 商品sku Id |
| `goodsSaleList[].orderSaleCount` | string | 自营仓销售订单量 |
| `goodsSaleList[].goodsSaleCount` | string | 自营仓销量 |
| `goodsSaleList[].goodsRefundCount` | string | 退货数量 |
| `goodsSaleList[].goodsSaleAmount` | number | 销售金额 |
| `goodsSaleList[].goodsCostAmount` | number | 自营仓商品成本 |
| `goodsSaleList[].goodsRefundAmount` | number | 退款成本 |
| `goodsSaleList[].orderRefundAmount` | number | 退款金额 |
| `goodsSaleList[].goodsSkuInfo` | object | 商品信息 |
| `goodsSaleList[].goodsSkuInfo.goodsName` | string | 商品名称 |
| `goodsSaleList[].goodsSkuInfo.goodsMode` | string | 商品类型 |
| `goodsSaleList[].goodsSkuInfo.goodsId` | string | 商品id |
| `goodsSaleList[].goodsSkuInfo.goodsSkuId` | string | 商品SKUid |
| `goodsSaleList[].goodsSkuInfo.goodsSkuOuterId` | string | sku |
| `goodsSaleList[].goodsSkuInfo.logoOssPath` | string | 图片地址 |
| `goodsSaleList[].goodsSkuInfo.goodsSkuSubName` | string | 规格 |
| `goodsSaleList[].goodsSkuInfo.goodsSkuCustomCode` | string | 商品代码 |
| `goodsSaleList[].goodsSkuInfo.logoUrl` | string | 图片url |
| `goodsSaleList[].rank` | string | 排名 |
| `goodsSaleList[].logisticsAgentGoodsSkuAllSales` | object | 三方仓销售数据 |
| `goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuOrderSaleAmount` | number | 三方仓销售金额 |
| `goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuOrderSaleCount` | integer | 三方仓销售订单量 |
| `goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuGoodsSaleCount` | integer | 三方仓销量 |
| `goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuGoodsCostAmount` | number | 三方仓商品成本 |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList` | array<object> | 三方仓销售数据列表 |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentWarehouseId` | string | 仓库id |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentGoodsSkuId` | string | 第三方sku ID |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsSkuId` | string | 商品sku ID |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].orderSaleAmount` | string | 订单销售金额 |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].orderSaleCount` | string | 商品成本金额 |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsSaleCount` | string | 商品销售数量 |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsCostAmount` | string | 商品成本金额 |
| `goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentWarehouseName` | string | 仓库名称 |
| `total` | integer | 总数 |

### 仓储 > 数据统计 > 商品周转分析

#### 获取商品周转数据列表

`POST /open/v1/ewm/stat/goods_turnover_data/fetch/search_goods_turnover_data_page`  (文档: api-479602618)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `gmtStart` | string | 是 | 开始日期如2022-07-01 |
| `gmtEnd` | string | 是 | 结束日期如2022-07-01 |
| `warehouseIds` | array<integer> |  | 仓库ID数组 |
| `goodsSkuOuterIds` | string |  | 商品SKU |
| `goodsSkuOuterIdsRp` | string |  | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsName` | string |  | 商品名称 |
| `goodsNameRp` | string |  | 商品名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsGroupIds` | array<integer> |  | 商品分组ID列表 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsList` | array<object> |  |
| `goodsList[].rank` | string | 排名 |
| `goodsList[].turnoverRate` | string | 周转率（%） |
| `goodsList[].turnoverDay` | string | 周转天数（天） |
| `goodsList[].saleRate` | string | 动销率（%） |
| `goodsList[].endDtStockNum` | string | 期末库存总量 |
| `goodsList[].endDtStockCostAmount` | string | 期末库存成本 |
| `goodsList[].startDtStockNum` | string | 期初库存总量 |
| `goodsList[].startDtStockCostAmount` | string | 期初库存成本 |
| `goodsList[].confirmUseGoodsSkuWarehouseCount` | string | 销售出库数量 |
| `goodsList[].confirmUseGoodsSkuWarehouseCostAmount` | string | 销售出库成本 |
| `goodsList[].otherOutStorageCount` | string | 其他出库数量 |
| `goodsList[].otherOutStorageCostAmount` | string | 其他出库成本 |
| `goodsList[].allInStorageCount` | string | 入库数量 |
| `goodsList[].allInStorageCostAmount` | string | 入库成本 |
| `goodsList[].goodsSkuInfo` | object | 商品信息 |
| `goodsList[].goodsSkuInfo.goodsName` | string | 商品名称 |
| `goodsList[].goodsSkuInfo.goodsMode` | string | 商品类型 |
| `goodsList[].goodsSkuInfo.goodsId` | string | 商品id |
| `goodsList[].goodsSkuInfo.goodsSkuId` | string | 商品SKUid |
| `goodsList[].goodsSkuInfo.goodsSkuOuterId` | string | sku |
| `goodsList[].goodsSkuInfo.logoOssPath` | string | 图片地址 |
| `goodsList[].goodsSkuInfo.goodsSkuSubName` | string | 规格 |
| `goodsList[].goodsSkuInfo.goodsSkuCustomCode` | string | 商品代码 |
| `goodsList[].goodsSkuInfo.logoUrl` | string | 图片url |
| `total` | integer | 总数 |

### 仓储 > 库存 > 三方仓sku库存

#### 获取三方仓商品库存列表

`POST /open/v1/ewm/storage/third_warehouse/fetch/search_third_goods_sku_warehouse_page`  (文档: api-479599784)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `type` | string | 是 | 类型 1:第三方仓库服务商LogisticsAgent 2:第三方货代仓库服务商Forwarder 3:FBA仓库 4:FBT |
| `thirdWarehouseProviderAgentAuthIds` | array<integer> |  | 第三方仓库服务商授权主键ID （选一个） |
| `thirdWarehouseForwarderProviderAuthIds` | array<integer> |  | 第三方货代仓库服务商授权主键ID（选一个） |
| `thirdWarehouseProviderAuthId` | array<integer> |  | FBA\FBA授权id |
| `warehouseIds` | array<integer> | 是 | 仓库Ids |
| `keyword` | string |  | 第三方sku 多个用逗号分隔 |
| `matchSku` | string |  | 商品sku（映射关系） 多个用逗号分隔 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuWarehouseList` | object | 商品SKU库存数据 |
| `goodsSkuWarehouseList.goodsSkuOuterId` | string | 第三方sku |
| `goodsSkuWarehouseList.warehouseName` | string | 仓库名称 |
| `goodsSkuWarehouseList.logisticsAgentWarehouseId` | string | 第三方仓库id |
| `goodsSkuWarehouseList.stockNum` | string | 库存 |
| `goodsSkuWarehouseList.availableStockNum` | string | 可用库存 |
| `goodsSkuWarehouseList.lockedStockNum` | string | 预占库存 |
| `goodsSkuWarehouseList.frozenStockNum` | string | 待上架库存 |
| `goodsSkuWarehouseList.onWayStockNum` | string | 在途库存 |
| `goodsSkuWarehouseList.waitSubmitStockNum` | string | 待提交量 |
| `goodsSkuWarehouseList.onPlanNum` | string | 计划库存 |
| `goodsSkuWarehouseList.faultyStockNum` | integer | 次品库存数量 |
| `goodsSkuWarehouseList.notForSaleNum` | integer | 不可售数量（平台仓） |
| `goodsSkuWarehouseList.inboundNum` | integer | 入库数量（平台仓） |
| `goodsSkuWarehouseList.reservedNum` | integer | 活动预留数量 |
| `total` | integer |  |

### 仓储 > 库存 > 自营仓库存

#### 获取自营仓商品库存列表

`POST /open/v1/ewm/storage/warehouse/fetch/search_goods_sku_warehouse_page`  (文档: api-479599786)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `warehouseIds` | array<integer> |  | 仓库ids |
| `goodsSkuOuterIds` | array<string> |  | 商品sku |
| `warehouseShelfCellCode` | string |  | 仓位 |
| `warehouseShelfCellCodeRp` | string |  | 仓位搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuWarehouseList` | array<object> | 商品SKU库存数据 |
| `goodsSkuWarehouseList[].goodsSkuWarehouseId` | string | 仓库id |
| `goodsSkuWarehouseList[].warehouseId` | string | 仓库ID |
| `goodsSkuWarehouseList[].warehouseName` | string | 仓库名称 |
| `goodsSkuWarehouseList[].goodsSkuId` | string | 商品skuid |
| `goodsSkuWarehouseList[].goodsId` | string | 商品id |
| `goodsSkuWarehouseList[].stockNum` | string | 总库存 |
| `goodsSkuWarehouseList[].availableStockNum` | string | 可用库存 |
| `goodsSkuWarehouseList[].lockedStockNum` | string | 预占库存 |
| `goodsSkuWarehouseList[].onWayNum` | string | 在途库存 |
| `goodsSkuWarehouseList[].onPlanNum` | string | 计划库存 |
| `goodsSkuWarehouseList[].warehouseShelfId` | array<integer> | 货架ID |
| `goodsSkuWarehouseList[].warehouseGoodsShelfId` | array<integer> | 货架ID列表 |
| `goodsSkuWarehouseList[].warehouseShelfCellId` | array<integer> | 仓位ID |
| `goodsSkuWarehouseList[].warehouseShelfCellCode` | array<string> | 仓位编码 |
| `goodsSkuWarehouseList[].warehouseShelfCellCodes` | array<string> | 仓位编码列表 |
| `goodsSkuWarehouseList[].shelfName` | array<string> | 货架名称 |
| `total` | integer |  |

#### 获取商品SKU安全库存列表

`POST /open/v1/ewm/storage/warehouse/fetch/get_goods_sku_safe_stock_num_list`  (文档: api-479599785)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSkuOuterIds` | array<string> | 是 | 商品sku |
| `warehouseId` | integer | 是 | 仓库id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuOuterIdAndSafeStockNumMap` | array<object> |  |
| `goodsSkuOuterIdAndSafeStockNumMap[].goodsSkuOuterId` | string | 商品SKU |
| `goodsSkuOuterIdAndSafeStockNumMap[].safeStockNum` | integer | 库存安全数 |

### 仓储 > 仓库 > 自营仓仓库

#### 获取供应商仓库列表

`POST /open/v1/ewm/warehouse/fetch/supplier_warehouse_list`  (文档: api-476990600)

请求参数：无（body 传 `{}`）

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `supplierWarehouseList` | array<object> | 供应商仓库列表 |
| `supplierWarehouseList[].warehouseId` | integer | 仓库ID |
| `supplierWarehouseList[].warehouseName` | string | 仓库名称 |

#### 获取自营仓仓库列表

`POST /open/v1/ewm/warehouse/fetch/search_warehouse_page`  (文档: api-476435300)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `warehouseList` | array<object> |  |
| `warehouseList[].warehouseId` | integer | 仓库ID |
| `warehouseList[].warehouseName` | string | 仓库名称 |
| `warehouseList[].address` | string | 地址 |
| `warehouseList[].fullAddress` | string | 详细地址 |
| `warehouseList[].isDefault` | integer | 是否默认仓库 |
| `total` | integer |  |

### 仓储 > 仓库 > 三方仓仓库

#### 获取三方仓授权列表

`POST /open/v1/ewm/third_warehouse/fetch/search_third_provider_auth_page`  (文档: api-479592192)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `providerAuthList` | object | 第三方授权列表 |
| `providerAuthList.thirdWarehouseProviderAuthId` | string | 授权ID |
| `providerAuthList.providerId` | string | 服务商ID |
| `providerAuthList.type` | string | 三方仓类型 forwarder:货代；logisticsAgent 三方服务商 |
| `providerAuthList.appCustomerId` | string | 授权id |
| `providerAuthList.nickname` | string | 昵称 |
| `providerAuthList.status` | string | 状态 |
| `providerAuthList.isPlatformWarehouse` | string | 是否平台仓库 |
| `providerAuthList.providerName` | string | 服务商名称 |
| `providerAuthList.providerCode` | string | 服务商Code |
| `providerAuthList.authAgentWarehouseList` | array<object> | 授权三方服务商仓库列表 |
| `providerAuthList.authAgentWarehouseList[].logisticsAgentWarehouseAuthId` | string | 仓库授权id |
| `providerAuthList.authAgentWarehouseList[].logisticsAgentCustomerId` | string | 服务商授权Id |
| `providerAuthList.authAgentWarehouseList[].logisticsAgentWarehouseId` | string | 仓库id |
| `providerAuthList.authAgentWarehouseList[].isDisabled` | string | 是否禁用 1禁用 |
| `providerAuthList.authAgentWarehouseList[].nickname` | string | 昵称 |
| `providerAuthList.authAgentWarehouseList[].logisticsAgentId` | string | 服务商id |
| `providerAuthList.authAgentWarehouseList[].warehouseName` | string | 仓库名称 |
| `providerAuthList.authAgentWarehouseList[].platformWarehouseCode` | string | 平台仓库编码 |
| `providerAuthList.authAgentWarehouseList[].address` | string | 地址 |
| `providerAuthList.authAgentWarehouseList[].contactPhone` | string | 联系电话 |
| `providerAuthList.authAgentWarehouseList[].contactName` | string | 联系人名称 |
| `providerAuthList.authForwarderWarehouseList` | array<object> | 授权货代仓库列表 |
| `providerAuthList.authForwarderWarehouseList[].forwarderProviderWarehouseAuthId` | string | 货代服务商仓库授权id |
| `providerAuthList.authForwarderWarehouseList[].forwarderProviderCustomerId` | string | 货代服务商授权id |
| `providerAuthList.authForwarderWarehouseList[].forwarderProviderWarehouseId` | string | 货代服务商仓库id |
| `providerAuthList.authForwarderWarehouseList[].isDisabled` | string | 是否禁用 |
| `providerAuthList.authForwarderWarehouseList[].nickname` | string | 昵称 |
| `providerAuthList.authForwarderWarehouseList[].warehouseName` | string | 仓库名称 |
| `providerAuthList.authForwarderWarehouseList[].forwarderProviderId` | string | 货代服务商id |
| `providerAuthList.authForwarderWarehouseList[].address` | string | 地址 |
| `providerAuthList.authForwarderWarehouseList[].contactPhone` | string | 联系电话 |
| `providerAuthList.authForwarderWarehouseList[].contactName` | string | 联系人 |
| `total` | integer | 总数 |

#### 获取平台仓库列表

`POST /open/v1/ewm/third_warehouse/fetch/search_platform_warehouse_page`  (文档: api-479592193)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |
| `platformWarehouseType` | string | 是 | 平台类型 FBT / FBA |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `warehouseList` | array<object> |  |
| `warehouseList[].logisticsAgentWarehouseId` | string | ID |
| `warehouseList[].logisticsAgentId` | string | 服务商ID |
| `warehouseList[].warehouseName` | string | 仓库名称 |
| `warehouseList[].platformWarehouseId` | string | 平台仓库ID |
| `warehouseList[].platformWarehouseCode` | string | 平台仓库编码 |
| `warehouseList[].address` | string | 地址 |
| `warehouseList[].platformWarehouseType` | string | 平台仓库类型 |
| `warehouseList[].shopName` | string | 店铺名称 |
| `warehouseList[].thirdWarehouseProviderAuthId` | integer | 三方仓服务商授权ID |
| `total` | integer |  |

### 仓储 > 出入库

#### 查询出入库记录列表

`POST /open/v1/ewm/goods_out_in/fetch/search_goods_sku_warehouse_log_page`  (文档: api-532434240)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 | 页数,默认1 |
| `pageSize` | integer | 是 | 每页数量,默认20 max:100 |
| `warehouseId` | integer |  | 仓库ID |
| `outInType` | string |  | 出入库类型;(in:入库,out:出库) |
| `bizCode` | string |  | 业务类型;(purchase_in_storage:采购入库,manual_purchase_in_storage:手动采购入库,allocate_in_storage:调拨入库,inventory_profit_in_storage:盘盈入库,manual_return_in_storage:手动退货入库,sale_out_storage:销售出库,manual_sale_out_storage:手动销售出库,allocate_out_storage:调拨出库,inventory_loss_out_storage:盘亏出库,manual_return_out_storage:手动退货出库) |
| `goodsSkuOuterIds` | string |  | 商品SKU编码,多个以逗号分隔 |
| `goodsSkuOuterIdsRp` | string |  | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `bizNos` | string |  | 出入库单号,多个以逗号分隔 |
| `bizNosRp` | string |  | 出入库单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `platformOrderSns` | string |  | 订单号,多个以逗号分隔 |
| `platformOrderSnsRp` | string |  | 订单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsPurchaseOrderInternalSn` | string |  | 采购单号,多个以逗号分隔 |
| `goodsPurchaseOrderInternalSnRp` | string |  | 采购单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `warehouseShelfCellCode` | string |  | 仓位 |
| `warehouseShelfCellCodeRp` | string |  | 仓位搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `gmtCreateStart` | string |  | 出入库开始时间(Y-m-d H:i:s) 不填默认最近90天 |
| `gmtCreateEnd` | string |  | 出入库结束时间(Y-m-d H:i:s) 不填默认最近90天 |
| `operateSubAccountId` | integer |  | 操作员子账号ID |
| `shopName` | string |  | 店铺名称 |
| `note` | string |  | 备注 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuWarehouseLogList` | array<object> | 出入库记录列表 |
| `goodsSkuWarehouseLogList[].goodsSkuWarehouseId` | integer | 商品SKU库存id |
| `goodsSkuWarehouseLogList[].bizCode` | string | 业务类型编码;(purchase_in_storage:采购入库,manual_purchase_in_storage:手动采购入库,allocate_in_storage:调拨入库,inventory_profit_in_storage:盘盈入库,manual_return_in_storage:手动退货入库,sale_out_storage:销售出库,manual_sale_out_storage:手动销售出库,allocate_out_storage:调拨出库,inventory_loss_out_storage:盘亏出库,manual_return_out_storage:手动退货出库) |
| `goodsSkuWarehouseLogList[].bizName` | string | 业务类型名称 |
| `goodsSkuWarehouseLogList[].bizNo` | string | 出入库单号 |
| `goodsSkuWarehouseLogList[].bizRelatedId` | integer | 业务关联ID(采购单/订单/调拨单/盘点单等主键) |
| `goodsSkuWarehouseLogList[].warehouseName` | string | 仓库名称 |
| `goodsSkuWarehouseLogList[].warehouseShelfCellCodesStr` | string | 仓位编码(逗号分隔) |
| `goodsSkuWarehouseLogList[].warehouseZoneNames` | array<string> | 仓位区域名称列表 |
| `goodsSkuWarehouseLogList[].goodsName` | string | 商品名称 |
| `goodsSkuWarehouseLogList[].goodsSkuSubName` | string | 商品SKU名称 |
| `goodsSkuWarehouseLogList[].goodsSkuOuterId` | string | 商品SKU编码 |
| `goodsSkuWarehouseLogList[].logoUrl` | string | 商品主图URL |
| `goodsSkuWarehouseLogList[].isDelete` | integer | 商品是否已删除(0:未删除,1:已删除) |
| `goodsSkuWarehouseLogList[].beforeStockNum` | integer | 变更前库存 |
| `goodsSkuWarehouseLogList[].changeStockNum` | integer | 变更库存(正数入库/负数出库) |
| `goodsSkuWarehouseLogList[].afterStockNum` | integer | 变更后库存 |
| `goodsSkuWarehouseLogList[].prePurchasePrice` | string | 变更前采购价 |
| `goodsSkuWarehouseLogList[].purchasePrice` | string | 变更后采购价 |
| `goodsSkuWarehouseLogList[].outInPurchasePrice` | string | 本次出入库单价 |
| `goodsSkuWarehouseLogList[].changePrice` | string | 本次变更金额 |
| `goodsSkuWarehouseLogList[].goodsPurchaseOrderInternalSn` | string | 采购单内部编号 |
| `goodsSkuWarehouseLogList[].platformOrderSn` | string | 平台订单号 |
| `goodsSkuWarehouseLogList[].thirdWarehouseStockOrderSn` | string | 三方仓出库单号 |
| `goodsSkuWarehouseLogList[].warehouseTakeStockTaskSn` | string | 盘点任务单号 |
| `goodsSkuWarehouseLogList[].deliveryOrderSn` | string | 发货单号 |
| `goodsSkuWarehouseLogList[].returnSn` | string | 退货单号 |
| `goodsSkuWarehouseLogList[].shopNick` | string | 店铺昵称 |
| `goodsSkuWarehouseLogList[].operatorName` | string | 操作员名称 |
| `goodsSkuWarehouseLogList[].note` | string | 备注 |
| `goodsSkuWarehouseLogList[].gmtCreate` | string | 创建时间 |
| `total` | integer | 总记录数 |
| `page` | integer | 当前页数 |
| `pageSize` | integer | 每页数量 |

#### 新建入库申请单

`POST /open/v1/ewm/goods_out_in/operate/add_in_apply_order`  (文档: api-532434241)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `warehouseId` | integer | 是 | 仓库ID |
| `bizCode` | string | 是 | 入库业务类型;(inventory_profit_in_storage:盘盈入库,allocate_in_storage:调拨入库,manual_return_in_storage:手动退货入库,manual_purchase_in_storage:手动采购入库,other_in_storage:其他入库) |
| `goodsSkuList` | array<object> | 是 | 商品sku列表 |
| `goodsSkuList[].goodsSkuOuterId` | string | 是 | 商品SKU |
| `goodsSkuList[].purchasePrice` | string |  | 单价(入库时填写) |
| `goodsSkuList[].storageList` | array<object> | 是 | 库存信息列表 |
| `goodsSkuList[].storageList[].warehouseShelfCellId` | integer | 是 | 仓位ID |
| `goodsSkuList[].storageList[].quantity` | integer | 是 | 出入库数量 |
| `note` | string |  | 备注 |
| `saveType` | string | 是 | 保存类型 save(保存), saveAndSubmit (保存并入库) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuWarehouseOutInApplyOrderId` | integer | 出入库申请单ID |

#### 新建出库申请单

`POST /open/v1/ewm/goods_out_in/operate/add_out_apply_order`  (文档: api-532434242)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `warehouseId` | integer | 是 | 仓库ID |
| `bizCode` | string | 是 | 出库业务类型;(inventory_loss_out_storage:盘亏出库,allocate_out_storage:调拨出库,manual_sale_out_storage:手动销售出库,other_out_storage:其他出库) |
| `goodsSkuList` | array<object> | 是 | 商品sku列表 |
| `goodsSkuList[].goodsSkuOuterId` | string | 是 | 商品SKU |
| `goodsSkuList[].purchasePrice` | string |  | 单价(入库时填写) |
| `goodsSkuList[].storageList` | array<object> | 是 | 库存信息列表 |
| `goodsSkuList[].storageList[].warehouseShelfCellId` | integer | 是 | 仓位ID |
| `goodsSkuList[].storageList[].quantity` | integer | 是 | 出入库数量 |
| `note` | string |  | 备注 |
| `saveType` | string | 是 | 保存类型 save(保存), saveAndSubmit (保存并出库) |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `goodsSkuWarehouseOutInApplyOrderId` | integer | 出入库申请单ID |

### 货源账号

#### 获取货源账号列表

`POST /open/v1/resell_account/fetch/search_reseller_account_page`  (文档: api-479848083)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 | max:100 |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `resellerAccountList` | array<object> |  |
| `resellerAccountList[].resellerAccountId` | string | ID |
| `resellerAccountList[].resellerId` | string | 账号ID |
| `resellerAccountList[].resellerAccount` | string | 1688账号名称 |
| `resellerAccountList[].resellerNick` | string | 1688昵称 |
| `resellerAccountList[].platform` | string | 平台 |
| `resellerAccountList[].authStatus` | string | 授权状态 |
| `resellerAccountList[].status` | string | 状态 |
| `resellerAccountList[].gmtLastAuth` | string | 最后认证时间 |
| `resellerAccountList[].gmtCreate` | string | 创建时间 |
| `resellerAccountList[].gmtModified` | string | 修改时间 |
| `resellerAccountList[].gmtExpire` | string | 过期时间 |
| `total` | integer | 总计 |

#### 获取账号地址列表

`POST /open/v1/resell_account/fetch/get_reseller_account_address_list`  (文档: api-479848084)

请求参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `resellerAccountId` | integer | 是 | 采购账号id |

返回 data 字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `resellerAccountAddressList` | array<object> |  |
| `resellerAccountAddressList[].provinceId` | string | 省ID |
| `resellerAccountAddressList[].cityId` | string | 市ID |
| `resellerAccountAddressList[].countyId` | string | 区县ID |
| `resellerAccountAddressList[].townId` | string | 镇街ID |
| `resellerAccountAddressList[].province` | string | 省 |
| `resellerAccountAddressList[].city` | string | 市 |
| `resellerAccountAddressList[].county` | string | 区县 |
| `resellerAccountAddressList[].town` | string | 镇街 |
| `resellerAccountAddressList[].fullname` | string | 姓名 |
| `resellerAccountAddressList[].mobile` | string | 手机 |
| `resellerAccountAddressList[].telephone` | string | 电话 |
| `resellerAccountAddressList[].address` | string | 地址 |
