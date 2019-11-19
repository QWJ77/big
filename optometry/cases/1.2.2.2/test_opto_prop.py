# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from requester.base_requester import check_fields
from service.webrestful_service import opto_prop


def verify_result(resp_data):
    """
    :param resp_data: 查询结果
    :return:
    """
    args = ('far_list', 'near_list', 'contact_list', 'rgp_list')
    check_fields(args, resp_data.keys())


def test_opto_prop():
    """处方属性关联获取"""
    resp_get = opto_prop()
    # 校验
    verify_result(resp_get['data'])

