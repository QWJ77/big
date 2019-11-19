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
from args_template.args_webrestful import SALE_PAY, STOCK_PICK_SALE_DETAIL, SALE_PICK
from service.webrestful_service import gen_sale_info, commit_sale_order, sale_pay, \
    sales_order_detail, stock_pick_sale_detail, sale_pick, return_recycle


def verify_result(sale_id):
    resp = sales_order_detail(sale_id)
    assert resp['data']['sale_state'] == 7  # 订单变成退费待申请


def test_return_recycle():
    """销售退货回收（带备注）"""
    # 提交非定做销售单
    sale_order = gen_sale_info(constants.ONLINE_PATI_ID, False, [0])
    sale_id = commit_sale_order(sale_order, return_sale_id=True)['sale_id']
    # 付款
    data_pay = copy.deepcopy(SALE_PAY)
    data_pay['bill_id'] = sale_id
    data_pay['amount'] = sale_order['sale_real_price']
    sale_pay(data_pay)
    # 库存商品提货销售单详情
    params_pick_sale_detial = copy.deepcopy(STOCK_PICK_SALE_DETAIL)
    params_pick_sale_detial['sale_id'] = sale_id
    params_pick_sale_detial['stat_depo_id'] = sale_order['list'][0]['depot_id']
    resp_pick_sale_detail = stock_pick_sale_detail(params_pick_sale_detial)
    if resp_pick_sale_detail['data']:
        stat_id = resp_pick_sale_detail['data'][0]['stat_id']
        # 取件
        data_sale_pick = copy.deepcopy(SALE_PICK)
        data_sale_pick['stat_id'] = stat_id
        sale_pick(data_sale_pick)
        # 退货回收
        data_recycle = list()
        data_recycle.append({'stat_id': stat_id})
        return_recycle(data_recycle)

