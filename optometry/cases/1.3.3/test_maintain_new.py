# -*- coding=utf-8 -*-
from args_template.args_optometry import MAINTAIN_DATA, PARAMS_MAINTAIN_LIST
from requester.web_requester import WebRequester
import copy

from service.optometry_service import maintain_new, get_maintain_list

"""
视光运营-库存管理-养护记录
"""

REQUESTER = WebRequester()


def verify_result(data_, main_id):
    params = copy.deepcopy(PARAMS_MAINTAIN_LIST)
    params['goods_id'] = data_['goods_id']
    resp = get_maintain_list(params)
    latest_record = resp['data'][-1]
    assert latest_record['main_id'] == main_id
    assert latest_record['main_time'] == data_['main_time']
    assert latest_record['main_quality'] == data_['goods_quality']
    assert latest_record['is_sale'] == data_['is_sale']


def test_maintain():
    # 新增养护记录
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    resp = maintain_new(maintain_data)
    # 校验
    verify_result(maintain_data, resp['data']['main_id'])


def test_maintain_sale_0():
    # 新增养护记录(不继续销售)
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    maintain_data['is_sale'] = 0
    resp = maintain_new(maintain_data)
    # 校验
    verify_result(maintain_data, resp['data']['main_id'])


def test_maintain_no_quality():
    # 新增养护记录(外包装质量情况不传)
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    maintain_data.pop('goods_quality')
    maintain_new(maintain_data, exp_http_status=500, exp_status='0001', exp_message=u'外包装质量情况不能为空')


def test_maintain_no_sale():
    # 新增养护记录(是否继续销售标志不输入)
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    maintain_data.pop('is_sale')
    maintain_new(maintain_data, exp_http_status=500, exp_status='0001', exp_message=u'是否继续销售标志不能为空')


def test_maintain_no_time():
    # 新增养护记录(养护时间不输入)
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    maintain_data.pop('main_time')
    maintain_new(maintain_data, exp_http_status=500, exp_status='0001', exp_message=u'养护日期不能为空')
