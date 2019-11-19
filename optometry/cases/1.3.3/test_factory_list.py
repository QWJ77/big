# -*- coding=utf-8 -*-
import copy
import pytest
from args_template.args_optometry import PARAMS_FACTORY_LIST, MFR_DATA
from common_method import unique_id
from requester.web_requester import WebRequester
from service.optometry_service import get_factory_list, save_factory_base_info

REQUESTER = WebRequester()


def verify_result(resp_get, total, mfr_id, data_):
    """
    校验结果
    :param resp_get: 请求结果
    :param total: 总记录数
    :param mfr_id: 厂商id
    :param data_: 保存厂商参数，如果data_=None，表示获取不到视光厂商
    :return: None
    """
    if data_ is None:
        assert total == total
        assert resp_get.get("list", []) == []
    else:
        assert resp_get['page_num']
        assert resp_get['page_size']
        assert resp_get['total'] == total
        assert resp_get['pages']
        r_factory = resp_get['list'][0]
        assert r_factory['mfr_id'] == mfr_id
        assert r_factory['mfr_code'] == data_['mfr_code']
        assert r_factory['mfr_name'] == data_['mfr_name']
        assert r_factory['mfr_type'] == data_['mfr_type']
        assert r_factory['mfr_enable'] == data_['mfr_enable']
        assert r_factory['expire_state']


@pytest.mark.smoke
def test_factory_list():
    # 视光厂商列表
    # 新增供应商; enable状态为1
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 1
    data_['mfr_enable'] = 1
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 查询厂商列表 key=mfr_code,状态全部,性质全部
    params = copy.deepcopy(PARAMS_FACTORY_LIST)
    params['key'] = data_['mfr_code']
    resp_get = get_factory_list(params)
    # 校验 期望能查询到数据
    verify_result(resp_get['data'], 1, resp_save['data']['mfr_id'],  data_)

    # 查询厂商列表 key=mfr_code,状态停用,性质全部
    params = copy.deepcopy(PARAMS_FACTORY_LIST)
    params['key'] = data_['mfr_code']
    params['mfr_enable'] = 0
    resp_get = get_factory_list(params)
    # 校验 期望不能查询到数据
    verify_result(resp_get['data'], 0, resp_save['data']['mfr_id'], None)

    # 查询厂商列表 key=mfr_code,状态全部,性质生产商
    params = copy.deepcopy(PARAMS_FACTORY_LIST)
    params['key'] = data_['mfr_code']
    params['mfr_type'] = 2
    resp_get = get_factory_list(params)
    # 校验 期望不能查询到数据
    verify_result(resp_get['data'], 0, resp_save['data']['mfr_id'], None)
