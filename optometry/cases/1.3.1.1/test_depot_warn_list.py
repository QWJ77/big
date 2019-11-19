# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 16:21
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-库存管理-库存报警-库存报警设置
"""
import copy
from args_template.args_webrestful import DEPOT_WARN_NEW, DEPOT_WARN_VIEW_LIST, DEPOT_WARN_LIST
from service.webrestful_service import depot_warn_new, depot_warn_view_list, depot_warn_list


def verify_result(data_new, resp_list):
    """
    :param data_new: 新增商品库存报警参数
    :param resp_list: 查询列表
    :return:
    """

    flag = False
    for view in resp_list['data']['list']:
        if view['warn_goods_id'] == data_new['warn_goods_id']:
            assert view['warn_upper'] == data_new['warn_upper']
            assert view['warn_lower'] == data_new['warn_lower']
            flag = True
    assert flag


def test_depot_warn_view_list():
    """库存报警设置列表"""
    # 新增商品库存报警
    data_new = copy.deepcopy(DEPOT_WARN_NEW)
    resp = depot_warn_new(data_new)
    # 库存报警设置列表
    data_list = copy.deepcopy(DEPOT_WARN_LIST)
    resp_list = depot_warn_list(data_list)
    verify_result(data_new, resp_list)
