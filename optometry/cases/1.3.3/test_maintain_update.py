# -*- coding=utf-8 -*-
import copy

import pytest

from args_template.args_optometry import MAINTAIN_DATA, MAINTAIN_DATA_UPDATE, PARAMS_MAINTAIN_LIST
from common_method import unique_id
from requester.web_requester import WebRequester
from service.optometry_service import maintain_update, maintain_new, get_maintain_list

REQUESTER = WebRequester()


def verify_result(data_, goods_id, main_id):
    params = copy.deepcopy(PARAMS_MAINTAIN_LIST)
    params['goods_id'] = goods_id
    resp = get_maintain_list(params)
    latest_record = resp['data'][-1]
    assert latest_record['main_id'] == main_id
    assert latest_record['main_time'] == data_['main_time']
    assert latest_record['main_quality'] == data_['goods_quality']
    assert latest_record['is_sale'] == data_['is_sale']


@pytest.mark.smoke
def test_maintain_update():
    """养护记录修改"""
    # 新增养护记录
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    resp_new = maintain_new(maintain_data)
    maintain_data_update = copy.deepcopy(MAINTAIN_DATA_UPDATE)
    maintain_update(resp_new['data']['main_id'], maintain_data_update)
    # 校验
    verify_result(maintain_data_update, maintain_data['goods_id'], resp_new['data']['main_id'])


def test_maintain_update_sale_0():
    """养护记录修改(不继续销售)"""
    # 新增养护记录
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    resp_new = maintain_new(maintain_data)
    maintain_data_update = copy.deepcopy(MAINTAIN_DATA_UPDATE)
    maintain_data_update['is_sale'] = 0
    maintain_update(resp_new['data']['main_id'], maintain_data_update)
    # 校验
    verify_result(maintain_data_update, maintain_data['goods_id'], resp_new['data']['main_id'])
