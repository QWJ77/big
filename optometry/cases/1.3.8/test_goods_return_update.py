# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/11 17:26
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
from args_template.args_webrestful import DEPOT_RETURN, DEPOT_RETURN_CONFIRM
from service.webrestful_service import add_depo_return, get_depo_return, confirm_depo_return


def verify_result(retu_id):
    resp_get = get_depo_return(retu_id)['data']
    assert resp_get['retu_state'] == 2


def test_goods_return_update():
    """商品完成退货"""
    # 新增商品退货
    data_ = copy.deepcopy(DEPOT_RETURN)
    resp_add = add_depo_return(data_)
    retu_id = resp_add['data']['retu_id']
    retu_no = resp_add['data']['retu_no']
    # 获取商品退货单
    resp_get = get_depo_return(retu_id)['data']
    # 商品完成退货
    data_update = copy.deepcopy(DEPOT_RETURN_CONFIRM)
    data_update['retu_id'] = retu_id
    data_update['retu_mfr_no'] = retu_no
    data_update['list'][0]['item_id'] = resp_get['list'][0]['item_id']
    data_update['list'][0]['item_return'] = resp_get['list'][0]['item_price']
    confirm_depo_return(data_update)
    verify_result(retu_id)

