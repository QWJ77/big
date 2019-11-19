# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import PARAMS_MAINTAIN_GOODS_LIST
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import get_maintain_goods_list

REQUESTER = WebRequester()


def test_maintain_goods_list():
    """养护记录商品列表"""
    params = copy.deepcopy(PARAMS_MAINTAIN_GOODS_LIST)
    resp = get_maintain_goods_list(params)
    ages = ('goods_batch', 'goods_factory', 'goods_id', 'goods_intime', 'goods_main_count', 'goods_main_quality',
            'goods_main_time', 'goods_name', 'goods_registrno', 'goods_stoc_num', 'goods_supplier', 'goods_unit',
            'goods_validity', 'is_sale')
    check_fields(ages, resp['data']['list'][0].keys())
