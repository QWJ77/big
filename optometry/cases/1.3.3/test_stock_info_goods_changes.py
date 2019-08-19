# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import PARAMS_STOCK_INFO_GOODS_CHANGES
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from env_constants import constants_yot_test
from service.optometry_service import get_stock_info_goods_changes
"""
视光运营-库存管理-库存详情-进销存详情
"""

REQUESTER = WebRequester()

def test_goods_changes():
    # 商品进销存详情列表
    params = copy.deepcopy(PARAMS_STOCK_INFO_GOODS_CHANGES)
    resp = get_stock_info_goods_changes(params)
    aegs = ('change_name', 'change_no', 'change_time')
    check_fields(aegs, resp['data']['list'][0].keys())
    ages = ('change_num', 'goods_bidprice', 'goods_price')
    check_fields(ages, resp['data']['list'][0]['batch_list'][0].keys())
    assert resp['data']['list'][0]['change_name']
