# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/18 13:38
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from env_switch import constants
import datetime

ADD_GOODS_INFO = {
        "atm_id": "177379170773500011",
        "goods_list": [
            {
                "channel_id": "177379174221218005",
                "goods_id": "99035300378050896",
                "goods_batchno": "28102831435",
                "num": 1
            }
        ]
    }

MOVRE_INFO = {
    "atm_id":"188817999518629947",
    "src_channel_id":"188818002043601832",
    "move_num":"1"
}

PARAMS_FACTORY_LIST = {
    # 非必填字段
    # "key": "",  # 关键字
    # "mfr_enable": 1,  # 是否有效 0：停用1：有效  传空全部
    # "mfr_type": 1,  # 厂商类型    1:供应商;2:生产商; 传空全部
    # "page_size": 10,  # 每页条数 空表示10条
    # "page_num": 1,  # 第几页 空表示第1页
}
# 视光厂商data
MFR_DATA = {
    # 必填字段
    'mfr_code': '12311',  # 厂商编码
    'mfr_name': 'sdsdd',  # 厂商名称
    'mfr_type': 3,  # 厂商类型 1:供应商;2:生产商;3:供应商入生产商
    'mfr_enable': 1,  # 是否有效 0：停用1：有效
    # 非必填字段
    "mfr_remind_time": 30,  # 证件有效期到期时间 单位天
    'mfr_taxrate': '6',  # 税率
    'mfr_area_code': '120101',  # 地市区代码
    "mfr_compaddress": u"解放路100号",  # 公司详细地址
    "mfr_biz_licence_code": "123454321",  # 工商营业执照号
    "mfr_biz_licence_validity_str": str(datetime.date.today() + datetime.timedelta(days=30)),  # 工商营业执照有效期
    "mfr_biz_licence_photo": '',  # 工商营业执照照片，文件资源ID
    "mfr_licence_code": "234565432",  # 医疗器械经营许可证号
    "mfr_licence_validity_str": str(datetime.date.today() + datetime.timedelta(days=30)),  # 医疗器械经营许可证有效期
    "mfr_licence_photo": "",  # 医疗器械经营许可证照片，文件资源ID
    "mfr_production": "345676543",  # 医疗器械生产许可证号
    "mfr_produ_validity_str": str(datetime.date.today() + datetime.timedelta(days=30)),  # 医疗器械生产许可证有效期
    "mfr_produ_photo": "",  # 医疗器械生产许可证证照片，文件资源ID
}
PARAMS_SAME_NATION_LIST = {
    # 必填字段
    "good_class": constants.GOOD_CLASS,  # 商品类别
    "good_brand": constants.GOOD_BRAND,  # 商品品牌
    "good_variety": constants.GOOD_VARIETY,  # 商品品种id
    # 非必填字段
    # "good_factory": "",  # 商品厂商id
    # "good_supplier": "",  # 商品供应商id
}
PARAMS_BATCH_UPDATE_GOODS_LIST = {
    # 必填字段
    "good_class": constants.GOOD_CLASS,  # 商品类别
    "good_brand": constants.GOOD_BRAND,  # 商品品牌
    "good_variety": constants.GOOD_VARIETY,  # 商品品种id
    "good_give": 0,
    "good_sell": 1,
    # 非必填字段
    # "page_size": 50,
    # "page_num": 1,
}
# 养护记录
MAINTAIN_DATA = {
    # 必填字段
    "goods_id": constants.GOODS_ID,  # 商品ID
    "main_time": str(datetime.date.today()),  # 养护日期
    "goods_quality": u"接口测试的",  # 外包装质量情况
    "is_sale": 1
    # 非必填字段
    # "goods_batchno": "",  # 生产批号
    # "goods_validity": "",  # 有效期
}
MAINTAIN_DATA_UPDATE = {
    # 必填字段
    "main_time": str(datetime.date.today()),  # 养护日期
    "goods_quality": u"更新接口测试的",  # 外包装质量情况
    "is_sale": 1
}
PARAMS_MAINTAIN_LIST = {
    # 必填字段
    "goods_id": constants.GOODS_ID,  # 商品ID
    # 非必填字段
    # "goods_batchno": "",  # 生产批号
    # "goods_validity": "",  # 有效期
}
PARAMS_MAINTAIN_GOODS_LIST = {
    # 必填字段
    "depot_id": constants.WDEPOT_ID,  # 仓库ID
    # 非必填字段
    # "clas_id   ": ,  # 类别ID，不传为全部       |
    # "bran_id   ": ,  # 品牌ID，不传为全部       |
    # "vari_id   ": ,  # 品种ID，不传为全部       |
    # "start_time": ,  # 最后一次养护开始时间       |
    # "end_time  ": ,  # 最后一次养护结束时间       |
    # "page_size ": ,  # 每页条数 空表示10条      |
    # "page_num  ": ,  # 第几页 空表示第1页回复报文参数 |
}
PARAMS_STOCK_INFO_GOODS_LIST = {
    # 非必填字段
    # "clas_id":,  # 类别ID，不传为全部
    # "bran_id":,  # 品牌ID，不传为全部
    # "vari_id":,  # 品种ID，不传为全部
    # "depot_id":,  # 仓库ID，不传为全部
    # "goods_factory_id":,  # 生产厂家
    # "goods_supplier_id":,  # 供应商
    # "key":,  # 商品编码或者商品名称
    # "page_size":,  # 每页条数 空表示10条
    # "page_num":,  # 第几页 空表示第1页回复报文参数
}
PARAMS_STOCK_INFO_GOODS_CHANGES = {
    # 必填字段
    "goods_id": constants.GOODS_ID,  # 商品ID

    "depot_id": constants.DEPOT_ID,  # 仓库ID
    "goods_factory_id": constants.GOODS_FACTORY_ID,  # 生产厂家id
    # 非必填字段
    # "mode_id        ":,  # 业务ID
    # "start_time     ":,  # 开始时间
    # "end_time       ":,  # 结束时间
    # "key            ":,  # 入库属性或者产品批号
    # "change_no      ":,  # 单号
    # "page_size      ":,  # 每页条数 空表示10条
    # "page_num       ":,  # 第几页 空表示第1页回复报文参数
}
PARAMS_STOCK_INFO_GOODS_MODES = {
    # 非必填字段
    # "mode_id":,  # 业务ID
    # "mode_name":,  # 业务名称
}
STOCK_INFO_GOODS_ADJUSTMENT = {
    "goods_agen_id": constants.AGEN_ID,
    "goods_agen_name": constants.AGEN_NAME,
    "adju_goods": [

    ],
    "goods_agen_id": 49015907598734210,  # 运营机构id  138增加
    "goods_agen_name": '患者维斯特洛',  # 运营机构名称  138增加
}
STOCK_INFO_GOODS_ADJU_GOODS = {
    # 必填字段

    "goods_id": constants.GOODS_ID,  # 商品ID
    "goods_src_bidprice": 9.99,  # 原进价
    "goods_num": 1,  # 数量
    "goods_bill_price": 8.88,  # 开票进价
    "goods_price": 11.11,  # 现售价
    "goods_total": -1.11,  # 进价差额总价
    # 非必填字段
    # "goods_supplyno":,  # 供货单号
    # "goods_rem":,  # 备注
}
PARAMS_STOCK_INFO_GOODS_ADJU_LIST = {
    # 非必填字段
    "start_time": str(datetime.date.today()),  # 开始时间
    "end_time": str(datetime.date.today()),  # 结束时间
    # "adju_no": "",  # 单据编号
    # "page_size": "",  # 每页条数 空表示10条
    # "page_num": "",  # 第几页 空表示第1页回复报文参数
}
BATCH_STOCK_LIST = {
    "batch_id": constants.BATCH_ID,  # 批次ID
    "depo_id": constants.WDEPOT_ID,  # 仓库ID
}


# 定做
SALE_D = {
    "pati_id": "3191485",
    "sale_price": 123,
    "sale_favor": 0,
    "sale_real_price": 123,
    "list": [{
        "item_goodsid": "99035300378050896",
        "good_name": "欧普康士隐形眼镜+1.44001",
        "item_purchase": 1,
        "item_purc_prop": "[{\"prop_prop_id\":\"75849089895502032\",\"prop_prop_name\":\"测试71\",\"type\":3,\"prop_putinprop\":1,\"prop_prop_type\":1,\"prop_flag\":0,\"od_choi_value\":\"\",\"os_choi_value\":\"\",\"choi_value\":\"12\"},{\"prop_prop_id\":\"0\",\"prop_prop_name\":\"备注\",\"type\":3,\"prop_putinprop\":1,\"prop_prop_type\":1,\"od_choi_value\":\"\",\"os_choi_value\":\"\"}]",
        "item_odos": 3,
        "item_size": 1,
        "is_give": 0,
        "discount": 100,
        "good_price": "123.00",
        "good_total_price": 123,
        "depot_id": "75838402926351065",
        "depot_name": "测试80",
        "good_favor": 0,
        "odos": "other",
        "good_class_id": "68524425208796186",
        "good_brand_id": "68523357410300876",
        "good_variety_id": "68524425208796190",
        "item_process": "1",
        "clas_process": 1,
        "prop_rule": "${75849089895502032}",
        "is_custom": 1
    }],
    "full_money": 0,
    "discount_money": 0,
    "sale_give": 0
}

# 库存商品全部取件
SALE_ALL_DATA = {
    "sale_id": "143231675743207547",
    "depo_id": "75838402926351065"
}

P_SALE_DATA = [{
    "sale_id": "143234783261098965",
    "depo_id": "75838402926351065"
}]

# 收费
PAY_DATA = {
    "amount": 13,
    "pay_channel": 1,
    "func_id": "99356382616225418",
    "char_source": 1,
    "bill_id": "143231675743207547"
}


# 销售单DATA
SALE_DATA = {
    "pati_id": "3191485",
    "sale_price": 13,
    "sale_favor": 0,
    "sale_real_price": 13,
    "list": [{
        "item_goodsid": "132398028425396290",
        "good_name": "欧普康士隐形眼镜+1.442.001.50",
        "item_batchid": "143231002460946901",
        "batch_batchno": "",
        "item_purchase": 0,
        "item_purc_prop": "",
        "item_size": 1,
        "is_give": 0,
        "discount": 100,
        "good_price": "12.00",
        "good_total_price": 12,
        "depot_id": "75838402926351065",
        "depot_name": "测试80",
        "stoc_id": "143231002733576312",
        "discount_item_id": "",
        "good_favor": 0,
        "good_class_id": "68524425208796189",
        "good_brand_id": "68523357410300876",
        "good_variety_id": "68524425208796190",
        "item_process": "0",
        "clas_process": 0,
        "stoc_waste": 0
    }, {
        "item_goodsid": "108749259502912486",
        "good_name": "耐克隐形眼镜+1.44134",
        "item_batchid": "143231002582582239",
        "batch_batchno": "",
        "item_purchase": 0,
        "item_purc_prop": "",
        "item_size": 1,
        "is_give": 0,
        "discount": 100,
        "good_price": "1.00",
        "good_total_price": 1,
        "depot_id": "75838402926351065",
        "depot_name": "测试80",
        "stoc_id": "143231002813268368",
        "discount_item_id": "",
        "good_favor": 0,
        "good_class_id": "68524425208796186",
        "good_brand_id": "98712974218363226",
        "good_variety_id": "68524425208796190",
        "item_process": "1",
        "clas_process": 1,
        "stoc_waste": 0
    }],
    "full_money": 0,
    "discount_money": 0,
    "sale_give": 0
}


# 成本调整data
ADJUSTMENT_DATA = {
    "adju_goods": [{
        "depot_id": "75838402926351065",
        "depot_name": "测试80",
        "goods_id": "99749637090575733",
        "goods_name": "GN1526374020040",
        "goods_factory_id": "68523357410300881",
        "goods_factory": "杭州市供应商",
        "goods_stoc_name": "2粒",
        "goods_src_price": "15.00",
        "uid": "E3A2C063-C3D1-4ECD-A990-1D6D926D0ACF",
        "goods_src_bidprice": "1.00",
        "goods_num": "2",
        "goods_bill_price": "1.00",
        "goods_total": "0.00",
        "goods_price": "2.00",
        "goods_supplyno": "11",
        "goods_rem": "12"
    }]
}

GOODS_UPDATE_DATA = {
    "good_factory": constants.GOODS_FACTORY_ID,
    "good_supplier": constants.GOODS_FACTORY_ID,
    "char_id": constants.SALE_CHARGE_CLASS_ID,
    "unitid": constants.GOODS_UNIT_ID,
    "good_bidprice": 111,
    "good_list": [{"good_id": constants.GOOD_UPDATE_ID}]
}
ADD_PARA_DATA = {
	"choi_prop_id": "111338112155779340",  # 属性id
	"choi_name": "-1.0",  # 参数编码
	"choi_code": "-1.0",   # 参数名称
	"choi_enable": 1   # 是否停用；0-停用；1-有效
}

