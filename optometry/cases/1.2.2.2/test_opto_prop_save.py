# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 9:54
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import OPTO_PROP_SAVE
from service.webrestful_service import opto_prop, opto_prop_save


def verify_result(data_):
    resp_get_data = opto_prop()['data']
    assert resp_get_data['far_list'] == data_['far_list']
    assert resp_get_data['near_list'] == data_['near_list']
    assert resp_get_data['contact_list'] == data_['contact_list']
    assert resp_get_data['rgp_list'] == data_['rgp_list']


def test_opto_prop_save():
    """处方属性关联保存"""
    data_ = copy.deepcopy(OPTO_PROP_SAVE)
    opto_prop_save(data_)
    # 校验
    verify_result(data_)

