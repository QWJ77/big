# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 通过属性名称查询属性
"""
from env_switch import constants
from requester.base_requester import check_fields
from service.webrestful_service import get_good_prop_list_by_name


def test_good_prop_list():
    """通过属性名称查询属性"""
    prop_name = constants.PROP_NAME
    resp = get_good_prop_list_by_name(prop_name)
    args = ('prop_id', 'prop_name')
    check_fields(args, resp['data'][0].keys())
