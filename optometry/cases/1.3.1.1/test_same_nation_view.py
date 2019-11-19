# -*- coding=utf-8 -*-
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from env_switch import constants
from service.optometry_service import get_nation_view

REQUESTER = WebRequester()


def test_same_nation_view():
    # 批量入库时某族商品详细
    resp = get_nation_view(constants.NATION_ID)
    ages = ('good_id', 'good_bidprice', 'good_code', 'good_factory', 'good_factory_name', 'good_id',
            'good_name', 'good_now_price', 'good_supplier', 'good_supplier_name', 'good_unit')
    check_fields(ages, resp['data'][0]['goods'].keys())
    # ages = ('cylinder_value',)
    # check_fields(ages, resp['data'][0]['cylinder_list'][1].keys())
    # ages = ('sphere_value', )
    # check_fields(ages, resp['data'][0].keys())
    assert resp['data'][0]['goods']['good_id'] == u"132398028324733205"
    assert resp['data'][0]['goods']['good_code'] == u"opksYXTK+1.442.001.00"
