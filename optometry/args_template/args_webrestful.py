# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:57
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import datetime

from env_switch import constants

PARAMS_VARIETY_LIST = {
    # 必填字段
    'page_num': 1,  # 当前页
    'page_size': 10,  # 每页的数量
    # 非必填字段
    # 'key': '',  # 品种代码、品种名称
    # 'goods_class': '',  # 商品类别ID
    # 'goods_brand': '',  # 商品品种ID
}
PARAMS_GOOD_PROP = {
    # 必填字段123
    'prop_id': constants.PROP_ID,  # 属性ID
    # 非必填字段
    # 'key': '',  # 搜索关键字 模糊匹配code或名称
}
PARAMS_GOOD_PROP_LIST_BY_SPAN = {
    # 必填字段
    'prop_prop_id': '',  # 属性码ID
    'begin_code': '',  # 开始编码
    'end_code': '',  # 结束编码
    'span_value': '',  # 跨度
}
STOCK_MANAGE_GOOD_NEW = {
    # 必填字段
    "good_code": '',  # 商品编码
    "good_name": '',  # 商品名称
    "good_class_id": constants.GOODS_CLASS_ID,  # 商品类别id
    "good_brand_id": constants.GOODS_BRAND_ID,  # 商品品牌id
    "good_factory_id": constants.GOODS_FACTORY_ID,  # 生产厂商id
    "good_supplier_id": constants.GOODS_SUPPLIER_ID,  # 供应商id
    "good_char_id": constants.SALE_CHARGE_CLASS_ID,  # 收费类别ID
    "good_give": 1,  # 允许赠送,默认:0;0-不允许;1-允许
    "status": 1,  # 0-不在售;1-在售;停用2
    # 非必填字段
    "good_variety_id": constants.GOODS_VERIETY_ID,  # 商品品种id
    # "good_registrno" ,  # 注册证号
    "good_bidprice": "15.00",  # 参考成本价
    "good_price": "15.00",  # 售价
    "good_unitid": constants.GOODS_UNIT_ID,  # 单位id
    # "good_unitname" ,  # 商品单位名称
    # "stock_list" ,  # 入库属性列表
    # "list" ,  # 非入库属性列表
}
STOCK_MANAGE_GOOD_STOCK_PROP = {
    'prop_prop_id': '',  # 属性码ID
    'prop_prop_name': '',  # 属性码名称
}
STOCK_MANAGE_GOOD_NOT_STOCK_PROP = {
    'prop_prop_id': '',  # 属性码ID
    'prop_prop_name': '',  # 属性码名称
    'choi_id': '',  # 属性值ID
    'choi_code': '',  # 属性值代码
    'choi_value': '',  # 属性值内容
}
STOCK_MANAGE_GOOD_BATCH = {
    # 必填字段
    "good_code": '',  # 商品编码
    "good_name": '',  # 商品名称
    "good_class_id": constants.GOODS_CLASS_ID,  # 商品类别id
    "good_brand_id": constants.GOODS_BRAND_ID,  # 商品品牌id
    "good_variety_id": constants.GOODS_VERIETY_ID,  # 商品品种id
    "good_factory_id": constants.GOODS_FACTORY_ID,  # 生产厂商id
    "good_supplier_id": constants.GOODS_SUPPLIER_ID,  # 供应商id
    "good_give": 1,  # 允许赠送,默认:0;0-不允许;1-允许
    "status": 1,  # 0-不在售;1-在售;停用2
    "good_char_id": constants.SALE_CHARGE_CLASS_ID,  # 收费类别ID
    # 非必填字段
    "good_bidprice": "15.00",  # 参考成本价
    "good_price": "15.00",  # 售价
    "good_unitid": constants.GOODS_UNIT_ID,  # 单位id
    # "good_registrno" ,  # 注册证号
    # "good_unitname" ,  # 商品单位名称
    # good_regis_validity 注册证有效期
    # good_registr_img 注册证号图片资源ID
    # "stock_list" ,  # 入库属性列表
    # "list" ,  # 非入库属性批量参数列表（第一层）
}
STOCK_MANAGE_GOOD_NOT_STOCK_PROP_l1 = {
    # 必填字段
    'prop_prop_id': '',  # 属性码ID
    'choi_id': '',  # 属性值ID
    # 非必填字段
    # 'props_list': 非入库属性批量参数列表（第二层）
}
STOCK_MANAGE_GOOD_NOT_STOCK_PROP_l2 = {
    # 必填字段
    'prop_prop_id': '',  # 属性码ID
    'choi_id': '',  # 候选码ID
    # 非必填字段
    # 'props_list': 非入库属性批量参数列表（第三层）
}
STOCK_MANAGE_GOOD_NOT_STOCK_PROP_l3 = {
    # 必填字段
    'prop_prop_id': '',  # 属性码ID
    'choi_id': '',  # 候选码ID
}
CUSTOM_STATISTICS_EXPORT = {
    # 必填字段
    'supplier_list': [
        {'supplier': constants.GOODS_SUPPLIER_ID},
    ],  # 供应商列表
    'start_time': '2018-09-24',  # 开始时间
    'end_time': '2018-09-24',  # 结束时间
    # 非必填字段
    # 'state': ''  # 到货状态 0未到货 1已到货 不传表示全部
}
DEPOT_RETURN = {
    "retu_mfr_id": constants.GOODS_SUPPLIER_ID,  # 供应商ID
    "retu_depot": constants.WDEPOT_ID,  # 退货仓库ID
    "list": [
        {
            "stoc_id": constants.GOODS_STOCK_ID,  # 库存ID
            "item_num": 1  # 退货数量
        }
    ]
}
DEPOT_RETURN_CONFIRM = {
    "retu_id": "",
    "retu_mfr_no": "",
    "list": [
        {
            "item_id": "",
            "item_return": ""
        }
    ]
}
DEPOT_WARN_NEW = {
    # 必填字段
    # 'depo_id': constants.WDEPOT_ID,  # 仓库id
    #'warn_goods_id': constants.GOODS_ID,  # 仓库id
    'warn_goods_id':'99749637090575734',
    # 非必填字段
    'warn_upper': 9999,  # 报警上限
    'warn_lower': 49,  # 报警下限
}
DEPOT_WARN_UPDATE = {
    # 必填字段
    'warn_id': '',  # 报警ID
    # 非必填字段
    'warn_upper': 9998,  # 报警上限
    'warn_lower': 48,  # 报警下限
}
DEPOT_WARN_VIEW_LIST = {
    # "depo_id": ,  # 仓库id
    # "clas_id": ,  # 类别ID
    # "bran_id": ,  # 品牌ID
    # "vari_id": ,  # 品种码ID
    # "key": ,  # 商品名称或代码
    # "state": ,  # 库存状态:1:低于 2：高于 3零库存 4低于上限且高于下限 空代表全部
    # "pagesize": ,  # 每页条数 空表示10条
    # "pagenum": ,  # 第几页 空表示第1页回复报文参数
}
DEPOT_WARN_LIST = {
    # "depo_id": ,  # 仓库id
    # "clas_id": ,  # 类别ID
    # "bran_id": ,  # 品牌ID
    # "vari_id": ,  # 品种码ID
    # "key": ,  # 商品名称或代码
    # "page_size": ,  # 每页条数 空表示10条
    # "page_num": ,  # 第几页 空表示第1页回复报文参数
}
DEPOT_WARN_BATCH_UPDATE = {
    # 非必填字段
    # 'depo_id': constants.WDEPOT_ID,  # 仓库id
    'clas_id': constants.GOODS_CLASS_ID,  # 类别ID
    'bran_id': constants.GOODS_BRAND_ID,  # 品牌ID
    'vari_id': constants.GOODS_VERIETY_ID,  # 品种码ID
    'warn_upper': 9997,  # 报警上限
    'warn_lower': 47,  # 报警下限
}
ARRIVAL_ADD = {
    # 必填字段
    "mfr_id": constants.GOODS_SUPPLIER_ID,  # 供应商id
    "depo_id": constants.WDEPOT_ID,  # 仓库id
    "arri_supplyno": 'ghdh004',  # 供货单号
    "arri_rem": u'新增采购入库',  # 备注
    "arri_price": '12.00',  # 进价合计(试用)
    "arri_cesse": 1.74358974,  # 税额合计(试用)
    "item": [],  # 出入库单子列表
    # 非必填字段
    "arri_amount": 1,  # 数量合计
}
ARRIVAL_ITEM = {
    # 必填字段
    "goods_id": constants.GOODS_ID,  # 商品id
    "item_num": 1,  # 入库数量
    "batch_price": '12.00',  # 进价单价
    "item_bidamount": '12.00',  # 进价合计
    # 非必填字段
    "item_taxrate": '17.0',  # 税率
    # "item_cesse":,  # 税额
    # "batch_batchno":,  # 商品批号
    # "batch_validity":,  # 有效期
    # "batch_goods_registrno":,  # 注册证号
    # "stat_id":,  # 物资id（定做入库用）
    "list": [],  # 属性列表
    # "produced_date":,  # 生产日期,yyyy-MM-dd
}
ARRIVAL_ITEM_PROP = {
    # 必填字段
    "prop_prop_id": constants.PROP_ID2,  # 属性码ID
    "prop_prop_name": constants.PROP_NAME2,  # 属性名
    "prop_putinprop": 1,  # 入库属性标志,默认0;  0:非入库;1:入库属性
    # 非必填字段
    # "choi_id": ,  # 属性值ID
    # "choi_code": ,  # 属性值代码
    # "choi_value": ,  # 属性值内容
}
ARRIVAL_LIST = {
    # 必填字段
    "depot_id": constants.WDEPOT_ID,  # 入库仓库
    "begin": str(datetime.date.today()),  # 开始时间
    "end": str(datetime.date.today()),  # 结束时间
    "page_num": 1,  # 当前页
    "page_size": 10,  # 每页的数量
    # 非必填字段
    # "arri_supplier":,  # 供应商id
    # "arri_state":,  # 状态,默认:1-已入库;2-已冲红 空位全部
    # "goods_classs":,  # 以商品类别进行查询
}
COMMIT_SALE_ORDER = {
    "pati_id": "",
    "sale_price": 0.0,
    "sale_favor": 0.00,
    "sale_real_price": 0.0,
    "list": [],
    "full_money": 0,
    "discount_money": 0,
    "sale_give": 0
}
SALE_ORDER_ITEM_NOT_CUSTOM = [
    {
        "item_goodsid": constants.GOODS_ID,
        "good_name": constants.GOODS_NAME,
        "item_batchid": constants.GOODS_BATCH_ID,
        "batch_batchno": constants.GOODS_BATCH_NO,
        "item_purchase": 0,
        "item_purc_prop": "",
        "item_size": 1,
        "is_give": 0,
        "discount": 100,
        "good_price": str(constants.GOODS_PRICE),
        "good_total_price": constants.GOODS_PRICE,
        "depot_id": constants.WDEPOT_ID,
        "depot_name": constants.WDEPOT_NAME,
        "batch_validity": "2020-02-26",
        "stoc_id": constants.GOODS_STOCK_ID,
        "discount_item_id": "",
        "good_favor": 0,
        # "good_class_id": "1000024",
        # "good_brand_id": "1001373",
        # "good_variety_id": "1004471",
        "item_process": "0",
        "clas_process": 0
    },
    # {
    #     "item_goodsid": constants.GOODS_ID[1],
    #     "good_name": constants.GOODS_NAME[1],
    #     "item_batchid": constants.BATCH_ID[1],
    #     "batch_batchno": constants.BATCH_NO[1],
    #     "item_purchase": 0,
    #     "item_purc_prop": "",
    #     "item_size": 1,
    #     "is_give": 0,
    #     "discount": 100,
    #     "good_price": str(constants.GOODS_PRICE[1]),
    #     "good_total_price": constants.GOODS_PRICE[1],
    #     "depot_id": constants.DEPOT_ID,
    #     "depot_name": constants.DEPOT_NAME,
    #     "batch_validity": "2024-03-15",
    #     "stoc_id": constants.GOODS_STOCK_ID[1],
    #     "discount_item_id": "",
    #     "good_favor": 0,
    #     # "good_class_id": "3000006",
    #     # "good_brand_id": "3001196",
    #     # "good_variety_id": "3004485",
    #     "item_process": "0",
    #     "clas_process": 0,
    #     "stoc_waste": 0
    # }
]

SALE_ORDER_ITEM_CUSTOM = [
    {
        "item_goodsid": constants.GOODS_ID,
        "good_name": constants.GOODS_NAME,
        "item_purchase": 1,
        "item_purc_prop": "[{\"prop_prop_id\":\"75849089895502032\",\"prop_prop_name\":\"测试71\",\"type\":3,\"prop_putinprop\":1,\"prop_prop_type\":1,\"prop_flag\":0,\"od_choi_value\":\"\",\"os_choi_value\":\"\"},{\"prop_prop_id\":\"0\",\"prop_prop_name\":\"备注\",\"type\":3,\"prop_putinprop\":1,\"prop_prop_type\":1,\"od_choi_value\":\"\",\"os_choi_value\":\"\"}]",
        "item_odos": 0,
        "item_size": 1,
        "is_give": 0,
        "discount": 100,
        "good_price": str(constants.GOODS_PRICE),
        "good_total_price": constants.GOODS_PRICE,
        "depot_id": constants.WDEPOT_ID,
        "depot_name": constants.WDEPOT_NAME,
        "good_favor": 0,
        "item_process": "0",
        "clas_process": 0
    },
    # {
    #     "item_goodsid": constants.GOODS_ID[1],
    #     "good_name": constants.GOODS_NAME[1],
    #     "item_purchase": 1,
    #     "item_purc_prop": "[{\"prop_prop_name\":\"备注\",\"choi_value\":\"1\",\"prop_prop_id\":0,\"type\":3,\"prop_putinprop\":1}]",
    #     "item_odos": 1,
    #     "item_size": 1,
    #     "is_give": 0,
    #     "discount": 100,
    #     "good_price": str(constants.GOODS_PRICE[1]),
    #     "good_total_price": constants.GOODS_PRICE[1],
    #     "depot_id": constants.DEPOT_ID,
    #     "depot_name": constants.DEPOT_NAME,
    #     "good_favor": 0,
    #     # "good_class_id": "3000006",
    #     # "good_brand_id": "3001196",
    #     # "good_variety_id": "3004485",
    #     "item_process": "0",
    #     "clas_process": 0
    # }
]
SALES_ORDER_LIST = {
    # 必填字段
    "start_time": str(datetime.date.today()),  # 开始时间
    "end_time": str(datetime.date.today()),  # 结束时间
    # 非必填字段
    # "key": ,  # 订单号、客户姓名、手机号码
    # "pati_id": ,  # 患者id 刷卡查询时用该字段
    # "state": ,  # 状态;1-待付款;2-已付款;3-已撤销;4-待退费;5-已退费 空为全部
    # "sale_user_id": ,  # 销售员id  新增
    # "page_size": ,  # 每页条数 空表示10条
    # "page_num": ,  # 第几页 空表示第1页
}
SALE_ORDER_LIST = {
    # 非必填字段
    # good_class   | String  | 否   | 商品类别            |
    # good_brand   | String  | 否   | 商品品牌            |
    # good_variety | String  | 否   | 商品品种id          |
    # key          | String  | 否   | 商品编码或名称      |
    # batch_no     | String  | 否   | 生产批号            |
    # "page_size": 10,  # 每页条数 空表示10条 |
    # "page_num": 1     | Integer | 否   | 第几页 空表示第1页  |
}
SALE_CUSTOM_ORDER_LIST = {
    # 非必填字段
    # good_class   | String  | 否   | 商品类别            |
    # good_brand   | String  | 否   | 商品品牌            |
    # good_variety | String  | 否   | 商品品种id          |
    # key          | String  | 否   | 商品编码或名称      |
    # "page_size": 10,  # 每页条数 空表示10条 |
    # "page_num": 1     | Integer | 否   | 第几页 空表示第1页  |
}
STOCK_MANAGE_GOOD_PROP = {
    # 必填字段
    'goods_id': constants.GOODS_ID,  # 商品id
    # 'opto_id': '',  # 处方id
    # 非必填字段
    'show_rem': 1,  # 0:不显示备注；1:显示备注
}
PATIENT_QUERY_OPTO_LIST = {
    # 非必填字段
    'pati_id': constants.ONLINE_PATI_ID,
    # 'opto_flag': 1,  # 处方时间 1：一月内 2：三月内 3：半年内 4：一年内  空为全部
}
PRICE_GOOD_LIST = {
    # 非必填字段
    # | good_class   | String  | 否   | 商品类别                            |
    # | good_brand   | String  | 否   | 商品品牌                            |
    # | good_variety | String  | 否   | 商品品种id                          |
    # | is_send      | Integer | 否   | 是否允许赠送 0-不允许;1-允许        |
    # | have_price   | Integer | 否   | 是否已有售价 0：否 1：是 全部则为空 |
    # | key          | String  | 否   | 商品编码或名称                      |
    # | page_size    | Integer | 否   | 每页条数 空表示10条                 |
    # | page_num     | Integer | 否   | 第几页 空表示第1页                  |
}
STOCK_MANAGE_CUSTOM_GOOD_LIST = {
    # 必填字段
    'depo_id': constants.WDEPOT_ID,  # 当前仓库
    # 非必填字段
    # | good_class   | String  | 否   | 商品类别            |
    # | good_brand   | String  | 否   | 商品品牌            |
    # | good_variety | String  | 否   | 商品品种id          |
    # | key          | String  | 否   | 商品编码或名称      |
    # | page_size    | Integer | 否   | 每页条数 空表示10条 |
    # | page_num     | Integer | 否   | 第几页 空表示第1页  |
}
ALLO_GOOD_LIST = {
    # 必填字段
    'depo_id': constants.WDEPOT_ID,  # 仓库id
    # 非必填字段
    # | good_class   | String  | 否   | 商品类别                 |
    # | good_brand   | String  | 否   | 商品品牌                 |
    # | good_variety | String  | 否   | 商品品种id               |
    # | batch_no     | String  | 否   | 生产批号/序列号          |
    # | key          | String  | 否   | 商品编码或名称或生产批号 |
    # | page_size    | Integer | 否   | 每页条数 空表示10条      |
    # | page_num     | Integer | 否   | 第几页 空表示第1页       |
}
STOCK_MANAGE_GOOD_LIST = {
    # 必填字段
    'page_num': 1,  # 当前页
    'page_size': 10,  # 每页的数量
    # 非必填字段
    # | clas_id   | String  | 否   | 商品类别id（全部为空）                     |
    # | bran_id   | String  | 否   | 内码及品牌                                 |
    # "vari_id": "",  # 商品品种id V1.3.8追加
    # | key       | String  | 否   | 商品名称、商品编码、商品拼音码、商品五笔码 |
    # | type      | Integer | 否   | 0-不在售;1-在售;停用2;全部为空             |
    'order': 1,  # 0或者不传按照名称排序，1:按照时间排序
}
OPTO_PROP_SAVE = {  # 数据来源于试用环境，测试租户
    "far_list": [
        {
            "optoprop_name": u"球镜",
            "goodsprop_id": "68523357410300877",
            "optoprop_type": 0,
            "goodsprop_name": u"颜色"
        },
        {
            "optoprop_name": u"柱镜",
            "goodsprop_id": "97665549663863312",
            "optoprop_type": 1,
            "goodsprop_name": u"球面"
        },
        {
            "optoprop_name": u"轴向",
            "goodsprop_id": "111338112155779340",
            "optoprop_type": 2,
            "goodsprop_name": u"柱面"
        },
        {
            "optoprop_name": u"棱镜",
            "optoprop_type": 3
        },
        {
            "optoprop_name": u"视力",
            "optoprop_type": 4
        }
    ],
    "near_list": [
        {
            "optoprop_name": u"球镜",
            "optoprop_type": 10
        },
        {
            "optoprop_name": u"柱镜",
            "optoprop_type": 11
        },
        {
            "optoprop_name": u"轴向",
            "optoprop_type": 12
        },
        {
            "optoprop_name": u"棱镜",
            "optoprop_type": 13
        },
        {
            "optoprop_name": u"视力",
            "optoprop_type": 14
        }
    ],
    "contact_list": [
        {
            "optoprop_name": u"球镜",
            "optoprop_type": 20
        },
        {
            "optoprop_name": u"柱镜",
            "optoprop_type": 21
        },
        {
            "optoprop_name": u"轴向",
            "optoprop_type": 22
        }
    ],
    "rgp_list": [
        {
            "optoprop_name": u"基弧1",
            "optoprop_type": 30
        },
        {
            "optoprop_name": u"基弧2",
            "optoprop_type": 33
        },
        {
            "optoprop_name": u"直径",
            "optoprop_type": 31
        },
        {
            "optoprop_name": u"度数1",
            "optoprop_type": 32
        },
        {
            "optoprop_name": u"度数2",
            "optoprop_type": 34
        }
    ]
}
GLASS_LIST = {
    # 必填字段
    'start_time': str(datetime.date.today()),  # 开始时间
    'end_time': str(datetime.date.today()),  # 结束时间
    # 非必填字段
    # | key        | String  | 否   | 订单号、客户姓名、手机号码                                   |
    # | pati_id    | String  | 否   | 患者id                                                       |
    # | proc_state 状态:0-待受理; 1-已受理;2-待磨镜;3-待检测;4-待签收;5-待取件;6-已取件（完成）; 空为全部 |
    # | page_size  | Integer | 否   | 每页条数 空表示10条                                          |
    # | page_num   | Integer | 否   | 第几页 空表示第1页                                           |
}
STOCK_PICK_LIST = {
    # 必填字段
    'stat_depo_id': constants.WDEPOT_ID,  # 仓库ID
    # 非必填字段
    'start_date': '2018-03-10',  # 开始日期
    'end_date': '2018-09-06',  # 结束日期
    # key          | String  | 否   | 订单号/商品名称/客户姓名/手机号码 |
    # stat_pickup  | Integer | 否   | 取件状态：0-未取件，1-已取件      |
    'page_size': 4,  # 每页条数 空表示10条
    'page_num': 1,  # 第几页 空表示第1页
}
STOCK_PICK_SALE_DETAIL = {
    # 必填字段
    # "sale_id": '134192085636088506',  # 销售订单ID
    "sale_id": '201950330190168713',  # 销售订单ID
    "stat_depo_id": constants.WDEPOT_ID,  # 仓库柜台id
    # 非必填字段
    "stat_pickup": 0,  # 取件状态：0-未取件，1-已取件
}
SALE_PICK = {
    "stat_purchase": 0,
    "stat_id": ""
}
OPTO_SETTINGS_ONOFF_SAVE = {
    # 非必填字段
    "auto_printer": False,  # 销售单是否自动打印
    # "check_goods_class": False,  # 出入库单据是否判断同一类别
    # "salesman_gift": True,  # 允许销售直接赠送
    # "goods_linkage_query": False,  # 商品联级查询
    # "goods_price_modify": True,  # 商品小级修改
   #"point_handle": 0,
   #  "custom_show": True,
   #  "text_remind": 0,
   # # "print_check": True,
   #  "peak_season": False,
   #  "qr_code": False
}
GOOD_PROPCHOICE_LIST = {
    # 必填字段
    "prop_id": constants.PROP_ID,  # 是   | 内码及属性码ID
    # 非必填段
    # "key": ,  # 否   | 关键字
    # "page_num": ,  # 否   | 当前页
    # "page_size": ,  # 否   | 每页的数量
    # "is_all": ,  # 否   | 是否返回所有值，0:否，1:是
}
VARIETY_LIST_HIS = {
    # 非必填字段
    # "key": ,  # 品种代码、品种名称
    # "goods_class": ,  # 商品类别id
    # "goods_brand": ,  # 商品品种id
}
BRAND_LIST_HIS = {
    # 非必填字段
    # "key": ,  # 品种代码、品种名称
    # "goods_class": ,  # 商品类别id
}
PARAMS_SALES_REFUND = {
    "refu_id": constants.SALE_REFU_ID,  # 退货单子表ID
    "depo_id": constants.WDEPOT_ID,  # 仓库id
}
ADD_RETURN_WITHREASONS = {
    # 必填字段
    "sales_id": "",  # 销售单id
    # 非必填字段
    "refund_reasons": [
        {  # 退货备注（退货原因）
            'statId': "",  # 物资状态id
            'reason': u"不想要了",  # 退货原因（备注）
        }
    ],
}
SALE_PAY = {
    "amount": constants.GOODS_PRICE,  # 金额
    "pay_channel": 1,
    "func_id": constants.SALE_PAY_FUNC_ID,
    "char_source": 1,
    "bill_id": ""  # 销售单 sale id
}
CLASS_INFO = {
	"clas_name": "树脂现片",
	"clas_code": "SH",
	"clas_process": 1,  # 是否可加工；0-不可加工;1-可加工
	"custom": 0,  # 是否定制商品；0-否;1-是 (该版本新增）
	"clas_enable": 1,
	"clas_parent_id": "68523357410300874",
	"clas_id": "174793365290877488"
}
