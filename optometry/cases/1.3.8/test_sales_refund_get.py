# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/10 10:43
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import PARAMS_SALES_REFUND
from requester.base_requester import check_fields
from service.webrestful_service import sales_refund


def verify_result(resp):
    args = ('refu_id', 'refu_make_user_name', 'refu_make_time', 'refu_sale_no', 'sale_no', 'pay_time', 'sale_user_name',
            'list')
    check_fields(args, resp.keys())


def test_sales_refund_get():
    """获得一个销售退货单"""
    params = copy.deepcopy(PARAMS_SALES_REFUND)
    resp = sales_refund(params)
    verify_result(resp['data'])
