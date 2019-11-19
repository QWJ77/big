# -*- coding=utf-8 -*-
from requester.base_requester import check_fields
from requester.web_requester import WebRequester

REQUESTER = WebRequester()


def test_allo():
    # 调拨单详情
    resp = REQUESTER.get('/depo_service/allo?allo_id=142887028382630863&type=0')
    ages = ('alloMakeTime', 'alloMakeUser', 'allo_id', 'allo_in_depot', 'allo_in_depot_name', 'allo_make_time',
            'allo_make_user', 'allo_no', 'allo_out_depot', 'allo_out_depot_name', 'allo_rem', 'allo_state')
    check_fields(ages, resp['data'].keys())
    ages = ('amount_price', 'batchValidity', 'batch_batchno', 'batch_goods_registrno', 'batch_id', 'batch_validity',
            'good_unitname', 'goods_class', 'goods_class_name', 'itemPrice', 'item_amount', 'item_depo_num',
            'item_goods_id', 'item_goods_name', 'item_id', 'item_num', 'item_num_unitname', 'item_price', 'mfr_name',
            'produced_date', 'stoc_depo_id', 'stoc_id', 'stoc_waste', 'unit_price', 'variName')
    check_fields(ages, resp['data']['list'][0].keys())
    ages = ('choi_value', 'prop_id', 'prop_prop_id', 'prop_prop_name', 'prop_putinprop')
    check_fields(ages, resp['data']['list'][0]['list'][0].keys())
    assert resp['data']['allo_id'] == "142887028382630863"
    assert resp['data']['allo_make_user'] == u"施秋梅"