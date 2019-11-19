# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-销售管理-视光销售-检索选择患者-直接销售-新增商品-定做商品-选择
"""
import copy

from args_template.args_webrestful import STOCK_MANAGE_GOOD_PROP
from requester.base_requester import check_fields
from service.webrestful_service import stock_manage_good_prop


def verify_result(resp_data):
    """
    :param resp_data: 返回结果
    :return:
    """
    args = ('prop_prop_id', 'prop_prop_name', 'type', 'prop_prop_type', 'prop_putinprop')
    check_fields(args, resp_data[0].keys())


def test_stock_manage_good_prop():
    """根据商品获取属性列表"""
    params = copy.deepcopy(STOCK_MANAGE_GOOD_PROP)
    resp = stock_manage_good_prop(params)
    # 校验
    verify_result(resp['data'])
