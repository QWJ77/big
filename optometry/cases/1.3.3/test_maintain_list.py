# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import MAINTAIN_DATA, PARAMS_MAINTAIN_LIST
from requester.web_requester import WebRequester
from env_switch import constants
from service.optometry_service import maintain_new, get_maintain_list

REQUESTER = WebRequester()


def verify_result(data_, latest_record, main_id):
    assert latest_record['main_id'] == main_id
    assert latest_record['main_time'] == data_['main_time']
    assert latest_record['main_quality'] == data_['goods_quality']
    assert latest_record['is_sale'] == data_['is_sale']


def test_maintain_list():
    """养护记录列表"""
    # 新增养护记录
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    resp_new = maintain_new(maintain_data)
    # 养护记录列表
    params = copy.deepcopy(PARAMS_MAINTAIN_LIST)
    params['goods_id'] = maintain_data['goods_id']
    resp = get_maintain_list(params)
    # 校验
    verify_result(maintain_data, resp['data'][-1], resp_new['data']['main_id'])


def test_maintain_list_no_data():
    """养护记录列表(无养护)"""
    params = copy.deepcopy(PARAMS_MAINTAIN_LIST)
    params['goods_id'] = constants.YGOOD_NO_ID
    resp = get_maintain_list(params)
    # 校验
    assert len(resp['data']) == 0
