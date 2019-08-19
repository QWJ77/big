# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import ALLO_GOOD_LIST
from requester.base_requester import check_fields
from service.webrestful_service import allo_good_list


def verify_result(resp_data):
    """
    :param resp_data: 查询结果
    :return:
    """
    args = ('page_num', 'page_size', 'total', 'pages', 'is_hidden', 'list')
    check_fields(args, resp_data.keys())
    res = resp_data['list'][0]
    args_good = ('good_id', 'good_name', 'good_price', 'good_class')
    check_fields(args_good, res.keys())


def test_allo_good_list():
    """库存商品列表"""
    params = copy.deepcopy(ALLO_GOOD_LIST)
    resp_get = allo_good_list(params)
    # 校验
    verify_result(resp_get['data'])

