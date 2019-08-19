# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 16:00
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import DEPOT_RETURN
from service.webrestful_service import add_depo_return, get_depo_return


def test_depot_return_get():
    """获取商品退货单"""
    # 新增商品退货
    data_ = copy.deepcopy(DEPOT_RETURN)
    resp_add = add_depo_return(data_)
    retu_id = resp_add['data']['retu_id']
    # 获取商品退货单
    resp_get = get_depo_return(retu_id)
    assert resp_get['data']['retu_id'] == retu_id
