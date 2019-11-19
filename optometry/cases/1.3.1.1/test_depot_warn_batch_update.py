# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 16:21
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-库存管理-库存报警-库存报警设置-批量设置报警
"""
import copy
from args_template.args_webrestful import DEPOT_WARN_VIEW_LIST, DEPOT_WARN_BATCH_UPDATE
from service.webrestful_service import depot_warn_view_list, depot_warn_batch_update


def verify_result(data_):
    """
    :param data_: 批量设置库存报警参数
    :return:
    """
    data_view_list = copy.deepcopy(DEPOT_WARN_VIEW_LIST)
    data_view_list['clas_id'] = data_['clas_id']
    data_view_list['bran_id'] = data_['bran_id']
    data_view_list['vari_id'] = data_['vari_id']
    resp_view_list = depot_warn_view_list(data_view_list)
    flag = False
    for view in resp_view_list['data']['list']:
        assert view['warn_upper'] == data_['warn_upper']
        assert view['warn_lower'] == data_['warn_lower']
        flag = True
    assert flag


def test_depot_warn_batch_update():
    """批量设置库存报警"""
    data_ = copy.deepcopy(DEPOT_WARN_BATCH_UPDATE)
    depot_warn_batch_update(data_)
    # 校验
    verify_result(data_)
