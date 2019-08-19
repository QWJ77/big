# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 16:40
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import GLASS_LIST
from requester.base_requester import check_fields
from service.webrestful_service import glass_list


def verify_result(resp_data):
    args = ('proc_id', 'proc_no', 'sale_no', 'pay_time', 'proc_state', 'pati_id', 'pati_name')
    check_fields(args, resp_data.keys())


def test_glass_list():
    """制镜加工单列表"""
    params = copy.deepcopy(GLASS_LIST)
    resp = glass_list(params)
    # verify_result(resp['data'])
