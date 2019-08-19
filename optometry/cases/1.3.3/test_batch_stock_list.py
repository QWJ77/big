# -*- coding=utf-8 -*-
import copy
from args_template.args_optometry import  BATCH_STOCK_LIST
from requester.base_requester import check_fields
from requester.web_requester import WebRequester
from service.optometry_service import batch_stock_list

REQUESTER = WebRequester()


def verify_result(resp):
    if len(resp) > 0:
        args = ('stoc_id', 'batch_id', 'depo_id', 'stoc_num', 'stoc_lock_num', 'stoc_avail_num')
        check_fields(args, resp[0].keys())


def test_batch_stock_list():
    """批次库存数量列表"""
    data_ = [copy.deepcopy(BATCH_STOCK_LIST), ]
    resp = batch_stock_list(data_)
    # 检验
    verify_result(resp['data'])


