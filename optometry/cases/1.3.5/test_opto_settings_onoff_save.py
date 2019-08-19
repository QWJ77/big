# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 15:16
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import OPTO_SETTINGS_ONOFF_SAVE
from service.webrestful_service import opto_settings_onoff_save, opto_settings_onoff_list
import pdb


def verify_result(data_, resp_get):
    # resp_get['data'].pop('print_check')
    # resp_get['data'].pop('point_handle')
    # pdb.set_trace()
    assert resp_get == data_


def test_opto_settings_onoff_save():
    """修改视光后台参数设置"""
    data_ = copy.deepcopy(OPTO_SETTINGS_ONOFF_SAVE)
    if data_['auto_printer']:
        data_['auto_printer'] = False
    else:
        data_['auto_printer'] = True
    opto_settings_onoff_save(data_)
    # 获得视光后台参数设置
    resp_get = opto_settings_onoff_list()
    # 校验
    verify_result(data_['auto_printer'], resp_get['data']['auto_printer'])
