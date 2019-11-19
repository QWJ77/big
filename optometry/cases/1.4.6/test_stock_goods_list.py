# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/29 13:40
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from service.optometry_service import stock_goods_list
from requester.base_requester import check_fields


def test_stock_goods_list():
    """库存详情商品列表"""
    resp = stock_goods_list('scph003')
    arg = ('page_num', 'page_size', 'total', 'pages', 'list')
    arg_list = ('depot_name', 'depot_id', 'goods_id', 'goods_name', 'goods_factory_id', 'goods_factory', 'goods_stoc_name', 'stoc_chan_num', 'goods_src_price')
    check_fields(resp['data'], arg)
    check_fields(resp['data']['list'][0], arg_list)

