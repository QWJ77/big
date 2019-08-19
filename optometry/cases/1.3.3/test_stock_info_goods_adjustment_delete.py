# -*- coding=utf-8 -*-
from args_template.args_optometry import STOCK_INFO_GOODS_ADJUSTMENT, STOCK_INFO_GOODS_ADJU_GOODS
from requester.web_requester import WebRequester
import copy
from service.optometry_service import stock_info_goods_adju_new, stock_info_goods_adju_delete, get_stock_info_goods_adju

REQUESTER = WebRequester()


def verify_result(adju_id):
    get_stock_info_goods_adju(adju_id, exp_http_status=500, exp_status='0099',
                              exp_message='class java.lang.NullPointerException')


def test_adjustment_delete():
    """删除成本调整记录"""
    # 新增成本调整记录
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    data_['adju_goods'].append(goods)
    resp_new = stock_info_goods_adju_new(data_)
    adju_id = resp_new['data']['adju_id']
    # 删除成本调整记录
    stock_info_goods_adju_delete(adju_id)
    # 校验
    verify_result(adju_id)
