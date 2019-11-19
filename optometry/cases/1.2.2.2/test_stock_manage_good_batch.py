# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    :
"""
import copy

from args_template.args_webrestful import STOCK_MANAGE_GOOD_BATCH
from common_method import init_goods_info
from service.webrestful_service import stock_manage_good_batch


def verify_result(resp_data):
    """
    :param resp_data: 返回结果
    :return:
    """
    assert resp_data['matched_rule_total'] == '0'
    assert resp_data['success_num'] == '0'
    assert resp_data['batch_goods_total'] == '0'


def test_stock_manage_good_batch():
    """批量新增商品"""
    data_ = copy.deepcopy(STOCK_MANAGE_GOOD_BATCH)
    init_goods_info(data_)
    resp = stock_manage_good_batch(data_)
    # 校验
    verify_result(resp['data'])
