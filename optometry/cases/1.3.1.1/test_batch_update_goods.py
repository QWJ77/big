# -*- coding=utf-8 -*-
import copy
from env_switch import constants
from args_template.args_optometry import GOODS_UPDATE_DATA
from requester.web_requester import WebRequester
from service.optometry_service import batch_update_goods, get_goods_info

REQUESTER = WebRequester()


def test_batch_update_goods():
    # 批量修改商品
    data_ = copy.deepcopy(GOODS_UPDATE_DATA)
    batch_update_goods(data_)
    resp = get_goods_info(constants.GOOD_UPDATE_ID)
    assert resp['data']['good_factory'] == constants.GOODS_FACTORY_NAME
    assert resp['data']['good_supplier'] == constants.GOODS_FACTORY_NAME
    assert int(float(resp['data']['good_bidprice'])) == data_['good_bidprice']
    assert resp['data']['good_name'] == constants.GOOD_UPDATE_NAME
    assert resp['data']['good_char_id'] == data_['char_id']

