# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 17:14
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from requester.base_requester import check_fields
from service.webrestful_service import special_check_goods_list


def verify_result(resp_data):
    args = ('clas_id', 'clas_code', 'clas_name', 'list')
    check_fields(args, resp_data[0].keys())
    args_good = ('goods_id', 'goods_name', 'goods_unit')
    check_fields(args_good, resp_data[0]['list'][0].keys())


def test_special_check_goods_list():
    """商品列表"""
    resp = special_check_goods_list()
    verify_result(resp['data'])
