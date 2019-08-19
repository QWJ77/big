# -*- coding=utf-8 -*-
import copy

from args_template.args_optometry import MAINTAIN_DATA, PARAMS_MAINTAIN_LIST
from requester.web_requester import WebRequester
from service.optometry_service import maintain_delete, maintain_new, get_maintain_list

REQUESTER = WebRequester()


def verify_result(goods_id, main_id):
    params = copy.deepcopy(PARAMS_MAINTAIN_LIST)
    params['goods_id'] = goods_id
    resp = get_maintain_list(params)
    found = False
    for res in resp['data']:
        if res['main_id'] == main_id:
            found = True
    assert not found


def test_maintain_delete():
    """养护记录删除"""
    maintain_data = copy.deepcopy(MAINTAIN_DATA)
    resp_new = maintain_new(maintain_data)
    main_id = resp_new['data']['main_id']
    maintain_delete(main_id)
    verify_result(maintain_data['goods_id'], main_id)
