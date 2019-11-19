# -*- coding=utf-8 -*-
import copy
from args_template.args_optometry import PARAMS_STOCK_INFO_GOODS_LIST
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import get_stock_info_goods_list

"""
视光运营-病库管理-库存详情-点查询
"""

REQUESTER = WebRequester()


def test_stock_info_goods_list():
    """库存详情商品列表"""
    params = copy.deepcopy(PARAMS_STOCK_INFO_GOODS_LIST)
    resp = get_stock_info_goods_list(params)
    ages = ('depot_id', 'depot_name', 'goods_factory', 'goods_factory_id', 'goods_id', 'goods_name', 'goods_src_price', 'goods_stoc_name')
    check_fields(ages, resp['data']['list'][0].keys())
