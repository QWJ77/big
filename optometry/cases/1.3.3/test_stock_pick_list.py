# -*- coding=utf-8 -*-
import copy

from args_template.args_webrestful import STOCK_PICK_LIST
from requester.base_requester import check_fields
from service.webrestful_service import stock_pick_list


def verify_result(resp_data):
    ages = ('item_size', 'saleUserId', 'sale_id', 'sale_no', 'sale_user_name', 'tradTime', 'trad_payuser', 'trad_time',
            'user_phone')
    check_fields(ages, resp_data['list'][0].keys())


def test_pick_list():
    """库存商品销售提货单列表"""
    params = copy.deepcopy(STOCK_PICK_LIST)
    resp = stock_pick_list(params)
    verify_result(resp['data'])


