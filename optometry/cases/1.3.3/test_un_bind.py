# -*- coding=utf-8 -*-
from requester.web_requester import WebRequester

REQUESTER = WebRequester()


def test_sale_fetch():
    # 解绑
    # resp = post('/sale_service/sales_order', data=SALE_D)
    # DATA = copy.deepcopy(PAY_DATA)
    # DATA['bill_id'] = resp['data']['sale_id']
    # post('/charge_service/business/pay', data=DATA)
    # resp_S = get('/sale_service/sales_order?sale_id={}'.format(resp['data']['sale_id']))
    #
    #
    #
    # ALL_SALE=copy.deepcopy(SALE_ALL_DATA)
    # ALL_SALE['bill_id'] = resp['data']['sale_id']
    # post('/depo_service/pick/stock_pick/sale_fetch_all', data=ALL_SALE)
    data = {
        "stat_id":"143242267166114453"
    }
    REQUESTER.post('/depo_service/pick/un_bind', data=data)
