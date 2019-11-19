# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import PARAMS_SAME_NATION_LIST
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from env_switch import constants
from service.optometry_service import get_same_nation_list

REQUESTER = WebRequester()


def test_same_nation_list():
    # 批量入库时商品族列表
    params = copy.deepcopy(PARAMS_SAME_NATION_LIST)
    resp = get_same_nation_list(params)
    ages = ('bid_price', 'enable', 'nation_id', 'nation_name', 'unit')
    check_fields(ages, resp['data'][0].keys())
    assert resp['data'][0]['nation_name'] == u"欧普康士隐形眼镜"
    assert resp['data'][0]['bid_price'] == u"15.00"


# def test_same_nation_no_list():
#     # 无数据搜索
#     params = copy.deepcopy(PARAMS_SAME_NATION_LIST)
#     params['good_class'] = constants.GOOD_CLASS_NO
#     resp = get_same_nation_list(params)
#     assert len(resp['data']) == 0

