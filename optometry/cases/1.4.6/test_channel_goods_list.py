# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/28 14:18
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""

from service.optometry_service import get_goods_list
from requester.base_requester import check_fields


def test_good_list():
    """加货选择商品"""
    resp = get_goods_list('177379170773500011', '177379174221218005', 1, 10)
    arg = ('page_num', 'page_size', 'total', 'pages', 'list')
    check_fields(resp['data'], arg)
    arg_list = ('goods_id', 'goods_name', 'goods_batchno', 'validity', 'stock_num')
    check_fields(resp['data']['list'][0], arg_list)


def test_good_list_by_data():
    """加货商品只出现一个的情况"""
