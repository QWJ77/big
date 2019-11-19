# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from env_switch import constants
from args_template.args_webrestful import SALES_ORDER_LIST
from service.webrestful_service import gen_sale_info, commit_sale_order, sales_order_list, sales_order_detail


def verify_result(sale_id, sale_order, resp_data):
    """
    :param sale_id: 销售单id
    :param sale_order: 销售单开单参数
    :param resp_data: 查询结果
    :return:
    """
    assert resp_data['sale_id'] == sale_id
    assert resp_data['sale_no']
    assert resp_data['sale_time']
    assert resp_data['sale_user_id']
    assert resp_data['sale_user_name']
    assert resp_data['sale_state']
    assert 'return_state' in resp_data
    assert str(resp_data['sale_price']).rstrip('0') == str(sale_order['sale_price']).rstrip('0')
    assert str(resp_data['sale_favor']).rstrip('0') == str(sale_order['sale_favor']).rstrip('0')
    assert str(resp_data['sale_real_price']).rstrip('0') == str(sale_order['sale_real_price']).rstrip('0')
    assert 'sale_rem' in resp_data
    assert resp_data['sale_state_time']
    assert len(resp_data['list']) == len(sale_order['list'])

    for i, r_item in enumerate(resp_data['list']):
        a_item = sale_order['list'][i]
        assert r_item['item_id']
        assert r_item['item_goodsid'] == a_item['item_goodsid']
        assert r_item['item_goods_name'] == a_item['good_name']
       # assert r_item['item_batchid'] == a_item['item_batchid']
        # assert 'stoc_waste' in r_item
        assert r_item['is_give'] == a_item['is_give']
        assert r_item['item_purchase'] == a_item['item_purchase']
        assert r_item['item_size'] == a_item['item_size']
        assert str(r_item['good_price']).rstrip('0') == str(a_item['good_price']).rstrip('0')
        assert str(r_item['good_total_price']).rstrip('0') == str(a_item['good_total_price']).rstrip('0')
        assert r_item['depot_id'] == a_item['depot_id']
        assert r_item['depo_name'] == a_item['depot_name']


def test_sales_order_detail():
    """获得一个销售订单"""
    # 提交非定做销售单
    sale_order = gen_sale_info(constants.ONLINE_PATI_ID, True, [0])
    sale_id = commit_sale_order(sale_order, return_sale_id=True)['sale_id']
    # 获得一个销售订单
    resp = sales_order_detail(sale_id)
    # 校验
    verify_result(sale_id, sale_order, resp['data'])
