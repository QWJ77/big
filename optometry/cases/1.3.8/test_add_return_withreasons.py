# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/10 18:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from env_switch import constants
from args_template.args_webrestful import ADD_RETURN_WITHREASONS, SALE_PAY
from service.webrestful_service import add_return_withreasons, gen_sale_info, commit_sale_order, sale_pay, \
    sales_order_detail, get_return_list


def verify_result(sale_id):
    resp = sales_order_detail(sale_id)
    assert resp['data']['sale_state'] == 7  # 订单变成退费待申请


def test_add_return_withreasons():
    """退货（带备注）"""
    # 提交非定做销售单
    sale_order = gen_sale_info(constants.ONLINE_PATI_ID, True, [0])
    sale_id = commit_sale_order(sale_order, return_sale_id=True)['sale_id']
    # 付款
    data_pay = copy.deepcopy(SALE_PAY)
    data_pay['bill_id'] = sale_id
    data_pay['amount'] = sale_order['sale_real_price']
    sale_pay(data_pay)
    # 获取退货列表
    resp_return_list = get_return_list(sale_id)
    # 退货（带备注）
    data_ = copy.deepcopy(ADD_RETURN_WITHREASONS)
    data_['sales_id'] = sale_id
    data_['refund_reasons'][0]['statId'] = resp_return_list['data'][0]['stat_id']
    add_return_withreasons(data_)
    # 校验
    verify_result(sale_id)
