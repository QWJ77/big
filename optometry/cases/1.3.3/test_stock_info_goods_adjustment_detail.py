# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import STOCK_INFO_GOODS_ADJUSTMENT, STOCK_INFO_GOODS_ADJU_GOODS
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import stock_info_goods_adju_new, get_stock_info_goods_adju

REQUESTER = WebRequester()


def verify_result(data_, resp):
    ages = ('adju_goods', 'adju_time', 'adju_user_name', 'adjustment_name', 'total', 'total_bill_price',
            'total_num', 'total_price', 'total_src_bidprice', 'total_src_price')
    check_fields(ages, resp['data'].keys())
    data_goods = data_['adju_goods'][0]
    resp_goods = resp['data']['item_list'][0]
    assert resp_goods['item_id']
    assert resp_goods['item_goods_id'] == data_goods['goods_id']
    assert resp_goods['item_goods_name']
    assert str(resp_goods['item_src_bidprice']) == str(data_goods['goods_src_bidprice'])
    assert resp_goods['item_src_price']  # 原售价
    assert resp_goods['item_num'] == data_goods['goods_num']
    assert str(resp_goods['item_bill_bidprice']) == str(data_goods['goods_bill_price'])
    assert str(resp_goods['item_price']) == str(data_goods['goods_price'])
    if data_goods.get('goods_supplyno', None):
        assert resp_goods['item_supplyno'] == data_goods['goods_supplyno']
    if data_goods.get('goods_rem', None):
        assert resp_goods['item_rem'] == data_goods['goods_rem']
    assert str(resp_goods['item_total']) == str(data_goods['goods_total'])


def test_stock_info_goods_adju_detail():
    """成本调整记录详情"""
    # 新增成本调整记录
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    data_['adju_goods'].append(goods)
    resp_new = stock_info_goods_adju_new(data_)
    # 成本调整记录详情
    resp = get_stock_info_goods_adju(resp_new['data']['adju_id'])
    # 检验
    verify_result(data_, resp)
