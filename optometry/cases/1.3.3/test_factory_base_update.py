# -*- coding=utf-8 -*-
import copy

import pytest

from args_template.args_optometry import MFR_DATA
from common_method import unique_id
from requester.web_requester import WebRequester
from service.optometry_service import get_factory_info, upload_picture, save_factory_base_info, update_factory_base_info

REQUESTER = WebRequester()


def verify_result(data_save, resp_save):
    """
    校验视光厂商——基本信息保存
    :param data_save: 视光厂商——基本信息保存 入参
    :param resp_save: 视光厂商——基本信息保存 调用成功后返回结果
    :return: None
    """
    # 获取视光厂商
    resp_search = get_factory_info(resp_save['mfr_id'])['data']
    # 比较
    assert resp_search['mfr_id'] == resp_save['mfr_id']
    assert resp_search['mfr_code'] == data_save['mfr_code']
    assert resp_search['mfr_name'] == data_save['mfr_name']
    assert resp_search['mfr_type'] == data_save['mfr_type']
    assert resp_search['mfr_enable'] == data_save['mfr_enable']
    assert str(resp_search['mfr_taxrate']) == str(data_save['mfr_taxrate'])
    assert resp_search['mfr_coun_code'] == data_save['mfr_area_code']
    assert resp_search['mfr_compaddress'] == data_save['mfr_compaddress']
    assert resp_search['mfr_remind_time'] == data_save['mfr_remind_time']
    assert resp_search['mfr_biz_licence_code'] == data_save['mfr_biz_licence_code']
    assert resp_search['mfr_biz_licence_validity_str'] == data_save['mfr_biz_licence_validity_str']
    if data_save.get('mfr_biz_licence_photo', None):
        assert resp_search['mfr_biz_licence_photo'] == data_save['mfr_biz_licence_photo']
        assert resp_search['mfr_biz_licence_photo_url']
    assert resp_search['mfr_licence_code'] == data_save['mfr_licence_code']
    assert resp_search['mfr_licence_validity_str'] == data_save['mfr_licence_validity_str']
    if data_save.get('mfr_licence_photo', None):
        assert resp_search['mfr_licence_photo'] == data_save['mfr_licence_photo']
        assert resp_search['mfr_licence_photo_url']
    assert resp_search['mfr_production'] == data_save['mfr_production']
    assert resp_search['mfr_produ_validity_str'] == data_save['mfr_produ_validity_str']
    if data_save.get('mfr_produ_photo', None):
        assert resp_search['mfr_produ_photo'] == data_save['mfr_produ_photo']
        assert resp_search['mfr_produ_photo_url']


@pytest.mark.smoke
def test_factory_base_update():
    """视光厂商——基本信息修改"""
    # 新增供应商（正常情况）
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 3
    # 上传工商营业执照
    file_id_biz = upload_picture(12, 'jpeg', 'picture/beauty.jpeg')
    data_['mfr_biz_licence_photo'] = file_id_biz
    # 医疗器械经营许可证
    file_id_run = upload_picture(7, 'jpg', 'picture/anti-mage.jpg')
    data_['mfr_licence_photo'] = file_id_run
    # 医疗器械生产许可证证照片
    file_id_prod = upload_picture(8, 'png', 'picture/dog.png')
    data_['mfr_produ_photo'] = file_id_prod
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 修改基本信息
    data_update = copy.deepcopy(data_)
    data_update['mfr_id'] = resp_save['data']['mfr_id']
    data_update['mfr_compaddress'] = u"物联网街451号"
    update_factory_base_info(data_update)
    # 校验
    verify_result(data_update, resp_save['data'])


@pytest.mark.parametrize('mfr_type', [1, 2, 3])
def test_factory_base_update_traveral_type(mfr_type):
    """视光厂商——基本信息修改(遍历类型)"""
    # 新增供应商（正常情况）
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 3
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 修改基本信息
    data_update = copy.deepcopy(data_)
    data_update['mfr_id'] = resp_save['data']['mfr_id']
    data_update['mfr_type'] = mfr_type
    update_factory_base_info(data_update)
    # 校验
    verify_result(data_update, resp_save['data'])


@pytest.mark.parametrize('mfr_enable', [0, 1])
def test_factory_base_update_traveral_enable(mfr_enable):
    """视光厂商——基本信息修改(遍历enable)"""
    # 新增供应商（正常情况）
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 3
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 修改基本信息
    data_update = copy.deepcopy(data_)
    data_update['mfr_id'] = resp_save['data']['mfr_id']
    data_update['mfr_enable'] = mfr_enable
    update_factory_base_info(data_update)
    # 校验
    verify_result(data_update, resp_save['data'])


def test_factory_base_update_no_code():
    """视光厂商——基本信息修改(编码不输入)"""
    # 新增供应商（正常情况）
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 3
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 修改基本信息
    data_update = copy.deepcopy(data_)
    data_update['mfr_id'] = resp_save['data']['mfr_id']
    data_update.pop('mfr_code')
    update_factory_base_info(data_update, exp_http_status=500, exp_status='0001', exp_message=u'编码不能为空')


def test_factory_base_update_no_name():
    """视光厂商——基本信息修改(名称不输入)"""
    # 新增供应商（正常情况）
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 3
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 修改基本信息
    data_update = copy.deepcopy(data_)
    data_update['mfr_id'] = resp_save['data']['mfr_id']
    data_update.pop('mfr_name')
    update_factory_base_info(data_update, exp_http_status=500, exp_status='0001', exp_message=u'名称不能为空')


def test_factory_base_update_no_type():
    """视光厂商——基本信息修改(单位性质不传)"""
    # 新增供应商（正常情况）
    data_ = copy.deepcopy(MFR_DATA)
    data_['mfr_code'] = unique_id(13)
    data_['mfr_name'] = unique_id(13)
    data_['mfr_type'] = 3
    # 基本信息保存
    resp_save = save_factory_base_info(data_)
    # 修改基本信息
    data_update = copy.deepcopy(data_)
    data_update['mfr_id'] = resp_save['data']['mfr_id']
    data_update.pop('mfr_type')
    update_factory_base_info(data_update, exp_http_status=500, exp_status='0001', exp_message=u'单位性质不能为空')
