# -*- coding=utf-8 -*-
import copy
from args_template.args_optometry import STOCK_INFO_GOODS_ADJU_GOODS, STOCK_INFO_GOODS_ADJUSTMENT
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import stock_info_goods_adju_new, get_stock_info_goods_adju

"""
视光运营-库存管理-库存详情-勾选列表中的商品-点左下角成本调整
"""
REQUESTER = WebRequester()


def verify_result(data_, adju_id):
    resp = get_stock_info_goods_adju(adju_id)
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


def test_stock_info_goods_adju_new():
    """新增成本调整记录"""
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    data_['adju_goods'].append(goods)
    resp_new = stock_info_goods_adju_new(data_)
    # 检验
    verify_result(data_, resp_new['data']['adju_id'])


def test_stock_info_goods_adju_new_no_bill():
    """新增成本调整记录(进价不输入)"""
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    goods.pop('goods_bill_price')
    data_['adju_goods'].append(goods)
    stock_info_goods_adju_new(data_, exp_http_status=500, exp_status='0001', exp_message=u'开票进价不能为空')


def test_stock_info_goods_adju_new_no_price():
    """新增成本调整记录(现售价不输入)"""
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    goods.pop('goods_price')
    data_['adju_goods'].append(goods)
    stock_info_goods_adju_new(data_, exp_http_status=500, exp_status='0001', exp_message=u'现售价不能为空')


def test_stock_info_goods_adju_new_no_num():
    """新增成本调整记录(数量不输入)"""
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    goods.pop('goods_num')
    data_['adju_goods'].append(goods)
    stock_info_goods_adju_new(data_, exp_http_status=500, exp_status='0001', exp_message=u'数量不能为空')


def test_stock_info_goods_adju_new_no_total():
    """新增成本调整记录(进销存差额不输入)"""
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    goods.pop('goods_total')
    data_['adju_goods'].append(goods)
    stock_info_goods_adju_new(data_, exp_http_status=500, exp_status='0001', exp_message=u'进价差额总价不能为空')
