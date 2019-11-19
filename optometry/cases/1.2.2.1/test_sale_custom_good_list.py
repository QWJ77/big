# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 14:31
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import SALE_CUSTOM_ORDER_LIST
from requester.base_requester import check_fields
from service.webrestful_service import sale_custom_good_list


def verify_result(resp):
    """
    :param resp: 返回结果
    :return:
    """
    resp_data = resp['data']
    args = ('page_num', 'page_size', 'total', 'pages', 'list')
    check_fields(args, resp_data.keys())
    args_goods = ('good_id', 'good_name', 'good_price', 'clas_process', 'good_give', 'depot_id', 'depot_name', 'has_char')
    check_fields(args_goods, resp_data['list'][0].keys())


def test_sale_custom_good_list():
    """销售定做商品列表"""
    params = copy.deepcopy(SALE_CUSTOM_ORDER_LIST)
    resp = sale_custom_good_list(params)
    # 校验
    verify_result(resp)
