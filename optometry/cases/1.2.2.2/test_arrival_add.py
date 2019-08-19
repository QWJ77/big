# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import ARRIVAL_ADD, ARRIVAL_ITEM, ARRIVAL_ITEM_PROP
from service.webrestful_service import arrival_add, arrival_get


def verify_result(arri_id, data_add):
    """
    :param arri_id: 入库单id
    :param data_add: 新增入库单参数
    :return:
    """
    resp_get = arrival_get(arri_id)
    resp_get_data = resp_get['data']
    assert resp_get_data['arri_id'] == arri_id
    assert resp_get_data['arri_no']
    assert resp_get_data['mfr_id'] == data_add['mfr_id']
    assert resp_get_data['depo_name']
    assert resp_get_data['arri_supplyno'] == data_add['arri_supplyno']
    assert resp_get_data['arri_rem'] == data_add['arri_rem']
    assert str(resp_get_data['arri_price']) == str(data_add['arri_price'])
    assert str(resp_get_data['arri_cesse']) == str(data_add['arri_cesse'])
    for i, r_item in enumerate(resp_get_data['item']):
        a_item = data_add['item'][i]
        assert r_item['item_id']
        assert r_item['item_num'] == a_item['item_num']
        assert str(r_item['batch_price']) == str(a_item['batch_price'])
        assert str(r_item['item_bidamount']) == str(a_item['item_bidamount'])
        assert str(r_item['item_taxrate']) == str(a_item['item_taxrate'])
        assert r_item['batch_factory_name']
        assert r_item['goods_class']
        assert r_item['goods_class_name']
        assert r_item['good_unitname']
        for j, r_prop in enumerate(r_item['list']):
            a_prop = a_item['list']['j']
            assert r_prop['prop_id'] == a_prop['prop_prop_id']
            assert r_prop['prop_prop_name'] == a_prop['prop_prop_name']


def test_arrival_add():
    """新增采购入库单"""
    data_add = copy.deepcopy(ARRIVAL_ADD)
    data_add['item'].append(copy.deepcopy(ARRIVAL_ITEM))
    data_add['item'][0]['list'].append(copy.deepcopy(ARRIVAL_ITEM_PROP))
    resp_add = arrival_add(data_add)
    # 校验
    verify_result(resp_add['data']['arri_id'], data_add)

