# -*- coding=utf-8 -*-
from args_template.args_webrestful import CLASS_INFO
from service.webrestful_service import good_clas, sale_good_clas, opto_good_clas
from requester.base_requester import check_fields
from env_constants.constants_yot_test import GOOD_CLASS1
import copy, pdb


def test_good_clas_():
    # 商品类别-不允许定做
    good_clas(CLASS_INFO)
    resp = opto_good_clas(GOOD_CLASS1)
    assert resp['data']['custom'] == 0
    resp = sale_good_clas(GOOD_CLASS1)
    # pdb.set_trace()
    assert len(resp['data']['list']) == 0  # 校验定做商品是否有该类别下的商品返回
    # assert resp['data']['list'][0]['good_id'] == '174801201936859506'


def test_good_clas():
    # 商品类别-允许定做
    parm = copy.deepcopy(CLASS_INFO)
    parm['custom'] = 1
    good_clas(parm)
    resp = opto_good_clas(GOOD_CLASS1)
    assert resp['data']['custom'] == 1
    resp = sale_good_clas(GOOD_CLASS1)
    assert resp['data']['list'][0]['good_id'] == '174801201936859506'  # 校验定做商品是否有该类别下的商品返回