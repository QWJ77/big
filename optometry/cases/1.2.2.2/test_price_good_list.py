# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import PRICE_GOOD_LIST
from requester.base_requester import check_fields
from service.webrestful_service import price_good_list


def verify_result(resp_data):
    """
    :param resp_data: 查询结果
    :return:
    """
    args = ('page_num', 'page_size', 'total', 'pages', 'list')
    check_fields(args, resp_data.keys())
    res = resp_data['list'][0]
    args_good = ('good_id', 'good_name', 'good_code', 'good_bidprice', 'good_price', 'now_price', 'good_unit',
                 'good_supplier', 'good_supplier_name', 'good_factory', 'good_factory_name',
                 'good_class')
    check_fields(args_good, res.keys())


def test_price_good_list():
    """采购入库-商品列表"""
    params = copy.deepcopy(PRICE_GOOD_LIST)
    resp_get = price_good_list(params)
    # 校验
    verify_result(resp_get['data'])

