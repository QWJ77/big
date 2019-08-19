# -*- coding=utf-8 -*-
import copy
from args_template.args_optometry import PARAMS_STOCK_INFO_GOODS_ADJU_LIST, STOCK_INFO_GOODS_ADJUSTMENT, \
    STOCK_INFO_GOODS_ADJU_GOODS
from requester.web_requester import WebRequester
from service.optometry_service import stock_info_goods_adju_new, get_stock_info_goods_adju_list

REQUESTER = WebRequester()


def verify_result(resp, adju_id):
    assert resp['page_num']
    assert resp['page_size']
    assert resp['total']
    assert resp['pages']

    found = False
    for reco in resp['list']:
        if reco['adju_id'] == adju_id:
            found = True
            assert reco['adju_time']
            assert reco['adju_no']
            assert reco['adju_user_name']
    assert found


def test_goods_list():
    """成本调整记录列表"""
    # 新增成本调整记录
    data_ = copy.deepcopy(STOCK_INFO_GOODS_ADJUSTMENT)
    # 添加商品
    goods = copy.deepcopy(STOCK_INFO_GOODS_ADJU_GOODS)
    data_['adju_goods'].append(goods)
    resp_new = stock_info_goods_adju_new(data_)
    # 成本调整记录列表
    params = copy.deepcopy(PARAMS_STOCK_INFO_GOODS_ADJU_LIST)
    resp = get_stock_info_goods_adju_list(params)
    verify_result(resp['data'], resp_new['data']['adju_id'])
