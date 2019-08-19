# -*- coding=utf-8 -*-
import copy
from requester.web_requester import WebRequester
from service.optometry_service import prop_para
from args_template.args_optometry import ADD_PARA_DATA
from requester.base_requester import check_fields
from common_method import unique_id

REQUESTER = WebRequester()

# 【系统管理-视光后台设置-视光商品-商品属性】


def verify_result(resp):
    ages = ('choi_id', )
    check_fields(ages, resp.keys())


def test_porp_para():
    # 商品属性-参数保存
    para = copy.deepcopy(ADD_PARA_DATA)
    para['choi_name'] = unique_id(3)
    para['choi_code'] = unique_id(3)
    # pdb.set_trace()
    resp = prop_para(para)
    verify_result(resp['data'])


def test_porp_para_code():
    # 编码和名称都存在
    data_ = copy.deepcopy(ADD_PARA_DATA)
    # pdb.set_trace()
    prop_para(data_, exp_http_status=200, exp_status='210001', exp_message=u'编码和名称组合已存在')


def test_porp_para_no_code():
    # 编码为空
    data_ = copy.deepcopy(ADD_PARA_DATA)
    data_['choi_code'] = ''
    prop_para(data_, exp_http_status=200, exp_status='210001', exp_message=u'编码不能为空')


def test_porp_para_no_name():
    # 名称为空
    data_ = copy.deepcopy(ADD_PARA_DATA)
    data_['choi_name'] = ''
    prop_para(data_, exp_http_status=200, exp_status='210001', exp_message=u'名称不能为空')


def test_porp_codes():
    # 编码存在的情况
    data_ = copy.deepcopy(ADD_PARA_DATA)
    data_['choi_name'] = unique_id(2)
    resp = prop_para(data_)
    verify_result(resp['data'])


def test_porp_names():
    # m名称存在的情况
    data_ = copy.deepcopy(ADD_PARA_DATA)
    data_['choi_code'] = unique_id(2)
    resp = prop_para(data_)
    verify_result(resp['data'])



