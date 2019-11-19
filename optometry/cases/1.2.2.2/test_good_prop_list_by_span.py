# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-库存管理-商品目录-批量新增？？
"""
import copy
from env_switch import constants
from args_template.args_webrestful import PARAMS_GOOD_PROP_LIST_BY_SPAN
from service.webrestful_service import get_good_prop_list_by_span


def test_good_prop_list_by_span():
    """通过跨度查询属性"""
    params = copy.deepcopy(PARAMS_GOOD_PROP_LIST_BY_SPAN)
    params['prop_prop_id'] = constants.PROP_ID
    params['begin_code'] = constants.PROP_ID
    params['end_code'] = constants.PROP_ID
    params['span_value'] = constants.PROP_ID
    get_good_prop_list_by_span(params)
