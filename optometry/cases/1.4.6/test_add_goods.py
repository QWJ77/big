# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/29 11:31
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from dba import db_tools
from env_switch import settings
import copy
from args_template.args_optometry import ADD_GOODS_INFO
from service.optometry_service import atm_add_goods


def test_add_goods():
    """货道商品加货"""
    data_ = copy.deepcopy(ADD_GOODS_INFO)
    resp = atm_add_goods(data_)