# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 16:21
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-库存管理-库存报警-库存报警设置-修改
"""
import copy
from args_template.args_webrestful import DEPOT_WARN_NEW, DEPOT_WARN_VIEW_LIST
from service.webrestful_service import depot_warn_new, depot_warn_view_list


def verify_result(data_):
    """
    :param data_: 新增商品库存报警参数
    :return:
    """
    data_view_list = copy.deepcopy(DEPOT_WARN_VIEW_LIST)
    resp_view_list = depot_warn_view_list(data_view_list)
    flag = False
    for view in resp_view_list['data']['list']:
        if view['warn_goods_id'] == data_['warn_goods_id']:
            assert view['warn_upper'] == data_['warn_upper']
            assert view['warn_lower'] == data_['warn_lower']
            flag = True
    assert flag


def test_depot_warn_new():
    """新增商品库存报警"""
    data_ = copy.deepcopy(DEPOT_WARN_NEW)
    depot_warn_new(data_)
    verify_result(data_)
