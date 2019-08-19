# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/10 13:50
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from env_switch import constants
from requester.base_requester import check_fields
from service.webrestful_service import bad_reasons_list


def verify_result(resp):
    if len(resp) > 0:
        args = ('bad_reasons', )
        check_fields(args, resp[0].keys())


def test_bad_reasons_list():
    """商品报损记录"""
    resp = bad_reasons_list(constants.GOODS_ID)
    verify_result(resp['data'])
