# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    :
"""
import copy

from args_template.args_webrestful import STOCK_MANAGE_GOOD_NEW
from common_method import init_goods_info
from service.webrestful_service import stock_manage_good_new, stock_manage_good_update, get_good_detail


def verify_result(good_id, data_):
    """
    :param good_id: 商品id
    :param data_: 修改的商品信息
    :return:
    """
    resp_get = get_good_detail(good_id)
    resp_data = resp_get['data']
    assert resp_data['good_factory_id'] == data_['good_factory_id']
    assert resp_data['good_supplier_id'] == data_['good_supplier_id']
    assert resp_data['good_bidprice'] == data_['good_bidprice']
    assert resp_data['good_char_id'] == data_['good_char_id']
    assert resp_data['good_unitid'] == data_['good_unitid']
    assert resp_data['good_give'] == data_['good_give']
    assert resp_data['status'] == data_['status']


def test_stock_manage_good_update():
    """修改商品"""
    # 新增商品
    data_new = copy.deepcopy(STOCK_MANAGE_GOOD_NEW)
    init_goods_info(data_new)
    resp_new = stock_manage_good_new(data_new)
    good_id = resp_new['data']['good_id']
    # 修改商品
    data_update = copy.deepcopy(data_new)
    data_update['good_id'] = good_id
    data_update['good_give'] = 0
    stock_manage_good_update(data_update)
    # 校验
    verify_result(good_id, data_update)
