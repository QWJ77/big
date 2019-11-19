# -*- coding=utf-8 -*-
import copy

from args_template.args_webrestful import STOCK_PICK_SALE_DETAIL
from requester.base_requester import check_fields
from service.webrestful_service import stock_pick_sale_detail


def verify_result(resp_data):
    ages = ('batchProducedDateLong', 'batch_batchno', 'batch_id', 'can_fetch', 'is_pickup', 'item_goods_id',
            'item_goods_name', 'item_odos', 'item_size', 'pati_birthday', 'saleUserId', 'sale_no',
            'statDepoId', 'stat_id', 'stat_purchase', 'stoc_id', 'tradTime', 'trad_payuser')
    check_fields(ages, resp_data[0].keys())
    # ages = ('choi_value', 'prop_prop_id', 'prop_prop_name', 'prop_putinprop')
    # check_fields(ages, resp_data[0].keys())
    assert resp_data[0]['item_goods_name'] == u"欧普康士隐形眼镜+1.44001"
    # assert resp_data[0]['sale_user_name'] == u"施秋梅"


def test_sale_detail():
    """库存商品提货销售单详情"""
    params = copy.deepcopy(STOCK_PICK_SALE_DETAIL)
    resp = stock_pick_sale_detail(params)
    verify_result(resp['data'])






