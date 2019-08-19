# -*- coding=utf-8 -*-
import copy
from requester.web_requester import WebRequester
from service.optometry_service import charg_account_list
from requester.base_requester import check_fields
import pdb

REQUESTER = WebRequester()

# 【视光运营-库存管理-库存详情-成本调整】


def verify_result(resp):
    ages = ('account_id', 'account_name', 'enable')
    check_fields(ages, resp[0].keys())


def test_charg_account_list():
    # 运营机构获取
    # pdb.set_trace()
    resp = charg_account_list(1)
    verify_result(resp['data'])

