# -*- coding=utf-8 -*-
from env_constants.constants_yot_test import SALE_ID
from service.webrestful_service import sale_order_list
from requester.base_requester import check_fields


def verify_result(resp):
    ages = ('stat_id', 'stat_sale_itemid', 'stat_goods_id', 'goods_name', 'stat_depo_id', 'depo_name',
            'stat_pickup', 'is_return')
    check_fields(ages, resp[0].keys())


def test_sale_list():
    # 返回数据新增字段
    resp = sale_order_list(SALE_ID)
    verify_result(resp['data'])
