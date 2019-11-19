# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 获取商品属性信息
"""
import copy

from args_template.args_webrestful import PARAMS_GOOD_PROP
from requester.base_requester import check_fields
from service.webrestful_service import get_goods_prop


def test_good_prop():
    """获取商品属性信息"""
    params = copy.deepcopy(PARAMS_GOOD_PROP)
    resp = get_goods_prop(params)
    args = ('prop_id', 'prop_name', 'prop_type', 'prop_readonly', 'prop_flag', 'list')
    check_fields(args, resp['data'].keys())
    args = ('choi_id', 'choi_prop_id', 'choi_code', 'choi_name', 'choi_enable', 'choi_readonly')
    check_fields(args, resp['data']['list'][0].keys())
