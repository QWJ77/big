# -*- coding=utf-8 -*-
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from env_switch import constants

REQUESTER = WebRequester()


def test_list():
    # 定做商品销售提货列表
    resp = REQUESTER.get('/depo_service/pick/list?stat_depo_id={}&start_date=2018-03-10&end_date=2018-09-06&page_size=4&page_num=1'
               '&stat_purchase=1&stat_pickup=0'.format(constants.WDEPOT_ID))
    ages = ('can_fetch', 'is_bind', 'item_goods_id', 'item_goods_name', 'item_odos', 'item_size', 'pati_age', 'pati_birthday',
            'purc_prop_text', 'saleUserId', 'sale_no', 'sale_user_name', 'stat_id', 'stat_purchase', 'tradTime', 'trad_payuser',
            'trad_time')
    check_fields(ages, resp['data']['list'][0].keys())
    ages = ('choi_value', 'prop_prop_id', 'prop_prop_name', 'prop_putinprop')
    check_fields(ages, resp['data']['list'][0]['purc_prop_list'][0].keys())