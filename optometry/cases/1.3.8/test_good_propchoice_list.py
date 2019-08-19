# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/10 10:43
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy

import pytest

from args_template.args_webrestful import GOOD_PROPCHOICE_LIST
from requester.base_requester import check_fields
from service.webrestful_service import good_propchoice_list


def verify_result(resp):
    args = ('page_num', 'page_size', 'total', 'pages', 'list')
    check_fields(args, resp.keys())
    args = ('choi_id', 'choi_value')
    check_fields(args, resp['list'][0].keys())


def test_good_propchoice_list():
    """商品属性候选值列表"""
    params = copy.deepcopy(GOOD_PROPCHOICE_LIST)
    resp = good_propchoice_list(params)
    verify_result(resp['data'])


def test_good_propchoice_list_all_params():
    """商品属性候选值列表(所有参数)"""
    params = copy.deepcopy(GOOD_PROPCHOICE_LIST)
    params['key'] = ""
    params['page_num'] = 1
    params['page_size'] = 10
    params['is_all'] = 0
    resp = good_propchoice_list(params)
    verify_result(resp['data'])


@pytest.mark.parametrize('is_all', [0, 1])
def test_good_propchoice_list_traver_is_all(is_all):
    """商品属性候选值列表(遍历is_all)"""
    params = copy.deepcopy(GOOD_PROPCHOICE_LIST)
    params['is_all'] = is_all
    resp = good_propchoice_list(params)
    verify_result(resp['data'])


def test_good_propchoice_list_invalid_is_all():
    """商品属性候选值列表(非法的is_all)"""
    params = copy.deepcopy(GOOD_PROPCHOICE_LIST)
    params['is_all'] = 2
    resp = good_propchoice_list(params)
    verify_result(resp['data'])
