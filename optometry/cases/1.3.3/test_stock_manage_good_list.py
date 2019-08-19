# -*- coding=utf-8 -*-
import copy

import pytest

from env_switch import constants
from args_template.args_webrestful import STOCK_MANAGE_GOOD_LIST
from requester.base_requester import check_fields
from service.webrestful_service import stock_manage_good_list


def verify_result(resp_data, exists=True):
    """
    :param resp_data: 返回结果
    :param exists: 返回列表是否有值
    :return:
    """
    if exists:
        ages = ('good_bidprice', 'good_code', 'good_id', 'good_name', 'good_price', 'good_price', 'status')
        check_fields(ages, resp_data['list'][0].keys())
    else:
        assert len(resp_data['list']) == 0


def test_stock_manage_good_list():
    """系统管理商品目录"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_LIST)
    resp = stock_manage_good_list(params)
    verify_result(resp['data'])


def test_stock_manage_good_list_all_params():
    """系统管理商品目录(所有参数)"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_LIST)
    params['clas_id'] = constants.GOODS_CLASS_ID
    params['bran_id'] = constants.GOODS_BRAND_ID
    params['vari_id'] = constants.GOODS_VERIETY_ID
    params['key'] = constants.GOODS_NAME[:4]
    params['type'] = 1
    resp = stock_manage_good_list(params)
    verify_result(resp['data'])


@pytest.mark.parametrize('type_, exists', [(0, False), (1, True), (2, False)])
def test_stock_manage_good_list_traver_type(type_, exists):
    """系统管理商品目录"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_LIST)
    params['type'] = type_
    resp = stock_manage_good_list(params)
    verify_result(resp['data'], exists)


def test_stock_manage_good_list_invalid_type():
    """系统管理商品目录(非法type)"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_LIST)
    params['type'] = 3
    resp = stock_manage_good_list(params)
    verify_result(resp['data'], False)


@pytest.mark.parametrize('order', [0, 1])
def test_stock_manage_good_list_traver_order(order):
    """系统管理商品目录(遍历order)"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_LIST)
    params['order'] = order
    resp = stock_manage_good_list(params)
    verify_result(resp['data'])


def test_stock_manage_good_list_invalid_order():
    """系统管理商品目录(非法order)"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_LIST)
    params['order'] = 2
    resp = stock_manage_good_list(params)
    verify_result(resp['data'])
