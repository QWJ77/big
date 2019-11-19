# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import ARRIVAL_ADD, ARRIVAL_ITEM, ARRIVAL_ITEM_PROP, ARRIVAL_LIST
from service.webrestful_service import arrival_add, arrival_list


def verify_result(arri_id, params, resp_get):
    """
    :param arri_id: 入库单id
    :param params: 查询时入参
    :param resp_get: 查询结果
    :return:
    """
    resp_get_data = resp_get['data']
    assert resp_get_data['page_num'] == params['page_num']
    assert resp_get_data['page_size'] == params['page_size']
    assert resp_get_data['total']
    assert resp_get_data['pages']
    flag = False
    for r_arri in resp_get_data['list']:
        if r_arri['arri_id'] == arri_id:
            assert r_arri['arri_no']
            assert r_arri['depo_name']
            assert r_arri['user_name']
            assert r_arri['arri_time']
            assert r_arri['goods_classs']
            flag = True
    assert flag


def test_arrival_list():
    """获取入库单列表"""
    # 新增采购入库单
    data_add = copy.deepcopy(ARRIVAL_ADD)
    data_add['item'].append(copy.deepcopy(ARRIVAL_ITEM))
    data_add['item'][0]['list'].append(copy.deepcopy(ARRIVAL_ITEM_PROP))
    resp_add = arrival_add(data_add)
    arri_id = resp_add['data']['arri_id']
    # 获取入库单列表
    params = copy.deepcopy(ARRIVAL_LIST)
    params['depot_id'] = data_add['depo_id']
    resp_get = arrival_list(params)
    # 校验
    verify_result(arri_id, params, resp_get)

