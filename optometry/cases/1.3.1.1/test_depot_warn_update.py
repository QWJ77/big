# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 16:21
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-库存管理-库存报警-库存报警设置-修改
"""
import copy
from args_template.args_webrestful import DEPOT_WARN_NEW, DEPOT_WARN_VIEW_LIST, DEPOT_WARN_UPDATE
from service.webrestful_service import depot_warn_new, depot_warn_view_list, depot_warn_update


def verify_result(data_new, data_update):
    """
    :param data_new: 新增商品库存报警参数
    :param data_update: 修改商品库存报警参数
    :return:
    """
    data_view_list = copy.deepcopy(DEPOT_WARN_VIEW_LIST)
    resp_view_list = depot_warn_view_list(data_view_list)
    flag = False
    for view in resp_view_list['data']['list']:
        if view['warn_goods_id'] == data_new['warn_goods_id']:
            assert view['warn_upper'] == data_update['warn_upper']
            assert view['warn_lower'] == data_update['warn_lower']
            flag = True
    assert flag


def test_depot_warn_update():
    """修改商品库存报警"""
    # 新增商品库存报警
    data_new = copy.deepcopy(DEPOT_WARN_NEW)
    resp_new = depot_warn_new(data_new)
    warn_id = resp_new['data']['warn_id']
    # 修改商品库存报警
    data_update = copy.deepcopy(DEPOT_WARN_UPDATE)
    data_update['warn_id'] = warn_id
    depot_warn_update(data_update)
    verify_result(data_new, data_update)
