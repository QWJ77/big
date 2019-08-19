# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy

import pytest

from env_switch import constants
from args_template.args_webrestful import SALES_ORDER_LIST
from service.webrestful_service import gen_sale_info, commit_sale_order, sales_order_list


def verify_result(sale_id, sale_order, resp):
    """
    :param sale_id: 销售单id
    :param sale_order: 销售单开单参数
    :param resp: 查询结果
    :return:
    """
    assert resp['data']['page_num']
    assert resp['data']['page_size']
    assert 'pages' in resp['data']
    if resp['data']['total'] > 0:
        flag = False
        for r_sale in resp['data']['list']:
            if r_sale['sale_id'] == sale_id:
                assert r_sale['sale_no']
                assert r_sale['sale_time']
                assert str(r_sale['sale_pati_id']) == str(sale_order['pati_id'])
                assert r_sale['pait_name']
                assert r_sale['pati_gender']
                assert r_sale['pait_age']
                assert r_sale['sale_user_id']
                assert r_sale['sale_user_name']
                assert r_sale['sale_state']
                flag = True
        assert flag


def test_sales_order_list():
    """销售单列表"""
    # 提交非定做销售单
    sale_order = gen_sale_info(constants.ONLINE_PATI_ID, True, [0])
    sale_id = commit_sale_order(sale_order, return_sale_id=True)['sale_id']
    # 销售单列表
    params = copy.deepcopy(SALES_ORDER_LIST)
    resp = sales_order_list(params)
    # 校验
    verify_result(sale_id, sale_order, resp)


# @pytest.mark.parametrize('state', [1, 2, 3, 4, 5, 7])
# def test_sales_order_list_traver_state(state):
#     """销售单列表(遍历状态) - 页面不传state"""
#     # 提交非定做销售单
#     sale_order = gen_sale_info(constants.ONLINE_PATI_ID, False, [0])
#     sale_id = commit_sale_order(sale_order, return_sale_id=True)['sale_id']
#     # 销售单列表
#     params = copy.deepcopy(SALES_ORDER_LIST)
#     params['state'] = state
#     resp = sales_order_list(params)
#     # 校验
#     verify_result(sale_id, sale_order, resp)
