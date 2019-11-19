# -*- coding=utf-8 -*-
# from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from args_template.args_optometry import SALE_DATA, PAY_DATA, SALE_ALL_DATA
import copy


REQUESTER = WebRequester()


def test_sale_fetch():
    # 库存商品全部取件
    resp = REQUESTER.post('/sale_service/sales_order', data=SALE_DATA)
    data = copy.deepcopy(PAY_DATA)
    data['bill_id'] = resp['data']['sale_id']
    REQUESTER.post('/charge_service/business/pay', data=data)
    sale_data = copy.deepcopy(SALE_ALL_DATA)
    sale_data['bill_id'] = resp['data']['sale_id']
    REQUESTER.post('/depo_service/pick/stock_pick/sale_fetch_all', data=sale_data)


def test_sale_batch():
    # 库存商品批量取件
    REQUESTER.get('/sale_service/promote/pati_match?pati_id=003191485')
    resp = REQUESTER.post('/sale_service/sales_order', data=SALE_DATA)
    data = copy.deepcopy(PAY_DATA)
    data['bill_id'] = resp['data']['sale_id']
    REQUESTER.post('/charge_service/business/pay', data=data)
    sale_data = copy.deepcopy(SALE_ALL_DATA)
    sale_data['bill_id'] = resp['data']['sale_id']
    # pdb.set_trace()
    REQUESTER.post('/depo_service/pick/stock_pick/sale_batch_fetch', data=[sale_data, ])
