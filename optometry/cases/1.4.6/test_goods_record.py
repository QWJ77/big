# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/29 11:53
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from service.optometry_service import atm_put_record_list


def test_goods_record():
    """自助机放货记录"""
    resp = atm_put_record_list('177379170773500011', 1, 10)
    arg = ('channel_code', 'goods_name', 'goods_batchno', 'validity', 'put_num', 'unit', 'operator_user', 'operator_time')

