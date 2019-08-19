2# -*- coding=utf-8 -*-
from env_constants.constants_yot_test import PROC_ID
from service.webrestful_service import service_glass
from requester.base_requester import check_fields


def verify_result(resp):
    ages = ('has_bad', 'is_return', 'pati_id', 'pati_name', 'pay_time', 'proc_flag', 'proc_id', 'proc_no',
            'proc_state', 'sale_no')
    check_fields(ages, resp.keys())
    ages = ('batch_no', 'depot_id', 'depot_name', 'goods_state', 'item_batchid', 'item_goods_id', 'item_id',
            'item_goods_name', 'item_size', 'odos', 'proc_state', 'stoc_waste')
    check_fields(ages, resp['list'][0].keys())


def test_service_glass():
    resp = service_glass(PROC_ID)
    verify_result(resp['data'])