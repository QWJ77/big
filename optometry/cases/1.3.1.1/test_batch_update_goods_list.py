# -*- coding=utf-8 -*-
import copy

import pytest

from args_template.args_optometry import PARAMS_BATCH_UPDATE_GOODS_LIST
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from env_switch import constants
from service.optometry_service import get_batch_update_goods_list

REQUESTER = WebRequester()


@pytest.mark.smoke
def test_batch_update_goods_list():
    # 批量修改时查询商品列表
    params = copy.deepcopy(PARAMS_BATCH_UPDATE_GOODS_LIST)
    resp = get_batch_update_goods_list(params)
    ages = ('good_bidprice', 'good_code', 'good_id', 'good_name', 'good_price', 'good_sell', 'good_unit')
    check_fields(ages, resp['data']['list'][0].keys())
    assert resp['data']['page_num']
    assert resp['data']['page_size']
    assert resp['data']['pages']


# def test_batch_update_no_goods_list():
#     # 无数据
#     params = copy.deepcopy(PARAMS_BATCH_UPDATE_GOODS_LIST)
#     params['good_class'] = constants.GOOD_CLASS_NO
#     resp = get_batch_update_goods_list(params)
#     assert len(resp['data']['list']) == 0
