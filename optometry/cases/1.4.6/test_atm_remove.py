# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/27 11:03
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import pytest
import copy
from service.optometry_service import get_atm_move
from args_template.args_optometry import MOVRE_INFO


def test_atm_remove():
    """货道商品移除"""
    data_ = copy.deepcopy(MOVRE_INFO)
    data_['atm_id'] = '177379170773500011'
    data_['src_channel_id'] = '177379174221218005'
    data_['move_num'] = 1
    resp = get_atm_move(data_)

