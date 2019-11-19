# -*- coding=utf-8 -*-
import pytest

from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import copy_goods
from env_constants import constants_yot_test

"""
页面操作：视光运营-商品目录-选择商品详情-复制新增商品
"""

REQUESTER = WebRequester()


@pytest.mark.smoke
def test_goods_copy():
    # resp = copy_goods(132398028257624820)
    resp = copy_goods(constants_yot_test.GOODS_ID)
    ages = ('good_unitid',  'good_unitname', 'status', 'good_bidprice', 'good_price', 'good_class_id',
            'good_class_name', 'good_brand_id', 'good_brand', 'good_variety_id', 'good_variety_code', 'good_variety',
            'good_factory_id', 'good_factory', 'good_supplier_id', 'good_supplier', 'good_give')
    check_fields(ages, resp['data'].keys())
    ages = ('prop_prop_id', 'prop_prop_name', 'choi_id', 'choi_code', 'choi_value')
    check_fields(ages, resp['data']['list'][0].keys())
    assert resp['data']['good_unitid'] == constants_yot_test.GOODS_UNIT_ID
    assert resp['data']['good_class_name'] == constants_yot_test.GOODS_CLASS_NAME
    assert resp['data']['list'][0]['prop_prop_name'] == u"颜色"
