# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/26 15:16
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import PATIENT_QUERY_OPTO_LIST
from requester.base_requester import check_fields
from service.webrestful_service import patient_query_opto_list


def verify_result(resp_data):
    res = resp_data['list'][0]
    args = ('opto_time', 'opto_doctor', 'list')
    check_fields(args, res.keys())


def test_patient_query_opto_list():
    """根据患者查询处方列表"""
    params = copy.deepcopy(PATIENT_QUERY_OPTO_LIST)
    resp = patient_query_opto_list(params)
    verify_result(resp['data'])
