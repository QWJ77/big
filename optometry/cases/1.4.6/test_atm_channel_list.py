# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/27 10:31
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from service.optometry_service import get_atm_channel_list
from requester.base_requester import check_fields, abnormal_check


def test_get_atm_channel_list():
    """货道列表"""
    resp = get_atm_channel_list("177379170773500011", 1, 3)
    arg = ('page_num', 'page_size', 'total', 'pages', 'list')
    check_fields(resp['data'], arg)
    arg_list = ('channel_id', 'channel_code', 'max_num', 'channel_num', 'goods_name', 'goods_batchno', 'validity',
                'operator_id', 'oper_date', 'goods_id')
    check_fields(arg_list, resp['data']['list'][0])


def test_get_atm_channel_list_null():
    """货道列表---不存在的自助机ID"""
    resp = get_atm_channel_list("1000000000000", 1, 3)
    assert len(resp['data']['list']) == 0





