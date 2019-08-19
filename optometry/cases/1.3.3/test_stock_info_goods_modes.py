# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import PARAMS_STOCK_INFO_GOODS_MODES
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import get_stock_info_goods_modes

"""
视光运营-病库管理-库存详情-进销存详情
"""

REQUESTER = WebRequester()


def test_goods_modes():
    # 进销存业务列表
    params = copy.deepcopy(PARAMS_STOCK_INFO_GOODS_MODES)
    resp = get_stock_info_goods_modes(params)
    ages = ('mode_id', 'mode_name')
    check_fields(ages, resp['data'][0].keys())
