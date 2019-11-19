# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/10 10:43
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from env_switch import constants
from args_template.args_webrestful import VARIETY_LIST_HIS
from requester.base_requester import check_fields
from service.webrestful_service import variety_list_his


def verify_result(resp):
    args = ('vari_id', 'vari_name')
    check_fields(args, resp['list'][0].keys())


def test_variety_list_his():
    """商品品种列表"""
    params = copy.deepcopy(VARIETY_LIST_HIS)
    resp = variety_list_his(params)
    verify_result(resp['data'])


# def test_variety_list_his_all_params():
#     """商品品种列表(所有参数)"""
#     params = copy.deepcopy(VARIETY_LIST_HIS)
#     params['key'] = constants.GOOD_VARIETY_NAME
#     params['goods_class'] = constants.GOOD_CLASS
#     params['goods_brand'] = constants.GOOD_BRAND
#     resp = variety_list_his(params)
#     verify_result(resp['data'])
