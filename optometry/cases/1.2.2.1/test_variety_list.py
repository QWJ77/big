# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 商品品种列表(视光运营-库存管理-商品目录-批量新增)
"""
import copy

from args_template.args_webrestful import PARAMS_VARIETY_LIST
from requester.base_requester import check_fields
from service.webrestful_service import get_variety_list


def test_variety_list():
    """商品品种列表"""
    params = copy.deepcopy(PARAMS_VARIETY_LIST)
    resp = get_variety_list(params)
    args = ('page_num', 'page_size', 'total', 'pages', 'list')
    check_fields(args, resp['data'].keys())
    args = ('vari_id', 'vari_code', 'vari_name')
    check_fields(args, resp['data']['list'][0].keys())
