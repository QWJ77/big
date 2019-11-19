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
from service.webrestful_service import stock_manage_good_new, get_good_detail


def verify_result(resp_data, data_):
    """
    :param resp_data: 获取的商品信息
    :param data_: 保存的商品信息
    :return:
    """
    assert resp_data['good_code'] == data_['good_code']
    assert resp_data['good_name'] == data_['good_name']
    assert resp_data['good_class_id'] == data_['good_class_id']
    assert resp_data['good_brand_id'] == data_['good_brand_id']
    assert resp_data['good_factory_id'] == data_['good_factory_id']
    assert resp_data['good_supplier_id'] == data_['good_supplier_id']
    assert resp_data['good_bidprice'] == data_['good_bidprice']
    assert resp_data['good_price'] == data_['good_price']
    assert resp_data['good_char_id'] == data_['good_char_id']
    assert resp_data['good_unitid'] == data_['good_unitid']
    assert resp_data['good_give'] == data_['good_give']
    assert resp_data['status'] == data_['status']


def test_stock_manage_good_detail():
    """获取商品明细"""
    # 新增商品
    data_new = copy.deepcopy(STOCK_MANAGE_GOOD_NEW)
    init_goods_info(data_new)
    resp_new = stock_manage_good_new(data_new)
    # 获取商品明细
    resp_get = get_good_detail(resp_new['data']['good_id'])
    # 校验
    verify_result(resp_get['data'], data_new)
