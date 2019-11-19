# -*- coding=utf-8 -*-
import copy
import json

import requests, pdb
from logzero import logger

from args_template.args_webrestful import COMMIT_SALE_ORDER, SALE_ORDER_ITEM_CUSTOM, SALE_ORDER_ITEM_NOT_CUSTOM
from requester.web_requester import WebRequester

WEB_REQUESTER = WebRequester()


def get_variety_list(params, **kwargs):
    """根据类别获取折扣权限
    :param params: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/common_service/variety_list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_goods_prop(params, **kwargs):
    """获取商品属性信息
    :param params: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/sys_service/opto/good_prop'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_good_prop_list_by_name(prop_name, **kwargs):
    """获取商品属性信息
    :param prop_name: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    if isinstance(prop_name, unicode):
        prop_name = prop_name.encode('utf8')
    url = '/sys_service/opto/good_prop/list?prop_name={}'.format(prop_name)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def get_good_prop_list_by_span(params, **kwargs):
    """通过跨度查询属性
    :param params: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/sys_service/opto/good_prop/list_by_span'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_manage_good_new(data_, **kwargs):
    """新增商品
    :param data_: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/opto_service/stock_manage/good'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def stock_manage_good_update(data_, **kwargs):
    """修改商品
    :param data_: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/opto_service/stock_manage/good/update'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_good_detail(good_id, **kwargs):
    """获取商品明细
    :param good_id: 商品id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/opto_service/stock_manage/good?good_id={}'.format(good_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def stock_manage_good_batch(data_, **kwargs):
    """批量新增商品
    :param data_: 输入参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/opto_service/stock_manage/good/batch'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def custom_statistics_export(data_, **kwargs):
    """指定供应商-定做统计导出压缩文件
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/sale_service/query/custom_statistics/export'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def add_depo_return(data_, **kwargs):
    """"新增商品退货
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "erp_service/retu"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def confirm_depo_return(data_, **kwargs):
    """"商品完成退货
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "erp_service/retu/update"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_depo_return(retu_id, **kwargs):
    """获取商品退货单
    :param retu_id: 商品退货单id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/depo_service/retu?retu_id={}'.format(retu_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def depot_warn_new(data_, **kwargs):
    """"新增商品库存报警
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    # url = "/depo_service/depot_warn"
    url = "/erp_service/depot_warn"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def depot_warn_view_list(params, **kwargs):
    """"新增商品库存报警
    :param params: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/depot_warn/view_list"
    # url = "/erp_service/depot_warn/view_list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def depot_warn_list(params, **kwargs):
    """"库存报警设置列表
    :param params: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    # url = "/depo_service/depot_warn/list"
    url = "/erp_service/depot_warn/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def depot_warn_update(data_, **kwargs):
    """"修改商品库存报警
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/depot_warn/update"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def depot_warn_batch_update(data_, **kwargs):
    """"批量设置库存报警
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/depot_warn/batch_update"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def arrival_add(data_, **kwargs):
    """"新增采购入库单
    :param data_: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/stock_manage/arrival"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def arrival_get(arri_id, **kwargs):
    """"获取采购入库单明细
    :param arri_id: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/stock_manage/arrival?arri_id={}".format(arri_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def arrival_list(params, **kwargs):
    """"获取入库单列表
    :param params: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/stock_manage/arrival_list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def gen_sale_info(pati_id, is_custom, l_goods, count_list=[], odos=None):
    """
    构造销售订单数
    :param pati_id: 患者id
    :param is_custom: 是否是定做True表示定做，False表示非定做
    :param l_goods: 商品标志列表，0表示第一个商品，1表示第二个商品；商品定义在constants.py
    :param count_list: 商品数量列表，与l_goods一一对应
    :param odos: '定做眼别,默认:0;0-无眼别;1-OD;2-OS'
    """
    sale_order = copy.deepcopy(COMMIT_SALE_ORDER)
    sale_order['pati_id'] = pati_id
    for i, goods_flag in enumerate(l_goods):
        if is_custom:
            sale_item = copy.deepcopy(SALE_ORDER_ITEM_CUSTOM[goods_flag])
            if odos is not None:
                sale_item['item_odos'] = odos
        else:
            sale_item = copy.deepcopy(SALE_ORDER_ITEM_NOT_CUSTOM[goods_flag])
        # 修改数量
        sale_item['item_size'] = 1 if len(count_list) < 1 else count_list[i]
        # 添加sale_item
        sale_order['list'].append(sale_item)
        # 修改价格
        sale_item['good_total_price'] = sale_item['good_total_price'] * sale_item['item_size']
        sale_order['sale_price'] += sale_item['good_total_price']
        sale_order['sale_real_price'] += sale_item['good_total_price']
    return sale_order


def commit_sale_order(sale_info, return_sale_id=False, **kwargs):
    """提交销售订单"""
    url = '/erp_service/sales_order'
    resp = WEB_REQUESTER.post(url, data=sale_info, **kwargs)
    logger.debug(resp)
    if return_sale_id and 'data' in resp:
        return resp['data']


def sales_order_list(params, **kwargs):
    """"销售单列表
    :param params: 请求参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/sales_order/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def sales_order_detail(sale_id, **kwargs):
    """"获得一个销售订单
    :param sale_id: 销售单id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/sales_order?sale_id={}".format(sale_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def sale_good_list(params, **kwargs):
    """"销售非定做商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/erp_service/sale/good/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def sale_custom_good_list(params, **kwargs):
    """"销售定做商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/sale/custom_good/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_manage_good_prop(params, **kwargs):
    """"根据商品获取属性列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/stock_manage/good_prop"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def patient_query_opto_list(params, **kwargs):
    """"根据患者查询处方列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/patient/query_opto_list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def price_good_list(params, **kwargs):
    """"采购入库-商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/price/good/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_manage_custom_good_list(params, **kwargs):
    """"采购入库定做商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/stock_manage/custom_good/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def allo_good_list(params, **kwargs):
    """"库存商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/allo/good/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_manage_good_list(params, **kwargs):
    """"系统管理商品目录
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/stock_manage/good_list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def opto_prop(**kwargs):
    """"处方属性关联获取
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sys_service/opto_prop"
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def opto_prop_save(data_, **kwargs):
    """"处方属性关联保存
    :param data_: 保存参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sys_service/opto_prop"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def glass_list(params, **kwargs):
    """"制镜加工单列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/process_service/glass/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_pick_list(params, **kwargs):
    """"库存商品销售提货单列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/pick/stock_pick/list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_pick_sale_detail(params, **kwargs):
    """"库存商品提货销售单详情
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    # url = "/depo_service/pick/stock_pick/sale_detail"
    url = "/erp_service/pick/stock_pick/sale_detail"

    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def sale_pick(data_, **kwargs):
    """"銷售提货
    :param data_: 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/pick"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def special_check_goods_list(**kwargs):
    """"商品列表
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/diag_service/special_check/goods_list"
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def opto_settings_onoff_save(data_, **kwargs):
    """"修改视光后台参数设置
    :param data_: 保存参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sys_service/optometry_settings/onoff"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def opto_settings_onoff_list(**kwargs):
    """"获得视光后台参数设置
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sys_service/optometry_settings/onoff/list"
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def good_propchoice_list(params, **kwargs):
    """"商品属性候选值列表
    :param params 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/good/good_propchoice_list"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def variety_list_his(params, **kwargs):
    """"商品品种列表
    :param params 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/common_service/variety_list_his"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def brand_list_his(params, **kwargs):
    """"商品品牌列表
    :param params 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/common_service/brand_list_his"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def bad_reasons_list(goods_id, **kwargs):
    """"商品报损记录
    :param goods_id 商品id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/opto_service/good/bad_reasons_list?goods_id={}".format(goods_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def sales_refund(params, **kwargs):
    """"获得一个销售退货单
    :param params 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/sales_refund"
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_return_list(sale_id, **kwargs):
    """"
    :param sale_id 销售单id
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/sale_service/sales_order/return_list?sale_id= {}".format(sale_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def add_return_withreasons(data_, **kwargs):
    """"退货（带备注）
    :param data_ 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/depo_service/sales_order/add_return_withreasons"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def cancel_return(data_, **kwargs):
    """"撤回退货
    :param data_ 参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/sales_order/cancel_return"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def sale_pay(salepay_info, **kwargs):
    """"视光收费
        :param salepay_info 参数
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/charge_service/business/pay"
    resp = WEB_REQUESTER.post(url, data=salepay_info, **kwargs)
    return resp


def return_recycle(data_, **kwargs):
    """"销售退货回收（带备注）
        :param data_ 参数
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/sale_service/sales_order/return"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def goods_template_download(**kwargs):
    """"商品导入模板文件下载
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/erp_service/goods/goods_template/download"
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def sale_order_list(sale_id, **kwargs):
    """"获得退货商品列表
    ""  【销售管理-销售订单-申请退货】
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/sale_service/sales_order/return_list?sale_id={}".format(sale_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def service_glass(proc_id, **kwargs):
    """"制镜单详情
    ""  【加工管理-制镜加工】
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/process_service/glass?proc_id={}".format(proc_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def good_clas(data, **kwargs):
    """"商品类别（142加了定做设置）
    ""
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/sys_service/opto/good_clas/update"
    resp = WEB_REQUESTER.post(url,data=data, **kwargs)
    return resp


def sale_good_clas(good_class, **kwargs):
    """"销售定做商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sale_service/sale/custom_good/list?good_class={}".format(good_class)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def opto_good_clas(clas_id, **kwargs):
    """"商品类别列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = "/sys_service/opto/good_clas?clas_id={}".format(clas_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp

# def get_sche_info(depart_id):
#     """获取排班信息"""
#     url = "/schedule_service/query_by_depa?depa_id={}&page_size=6&page_num=1".format(depart_id)
#     resp = get(url)
#     return resp['data']['list'][0]['list']
#
#
# def emr_book(sche_id, pati_id):
#     """门诊挂号"""
#     url = "/book_service/book"
#     package_id = get_package_id()
#     args = {
#         "sche_id": sche_id,
#         "pati_id": pati_id,
#         "package_type": 1,
#         "package_id": package_id
#     }
#     resp = post(url, data=args)
#     return resp['data']['visi_id']
#
#
# def get_treat_id_by_visit_id(visit_id):
#     """通过挂号ID查询就诊ID"""
#     treat_id = None
#     url = "/treat_service/preview/list"  # ?page_size=4&page_num=1"
#     resp = get(url)
#     for item in resp['data']['list']:
#         if str(item['visi_id']) == str(visit_id):
#             treat_id = item['trea_id']
#             break
#     return treat_id
#
#
# def emr_start(treat_id):
#     """医生接诊/开始就诊"""
#     url = "/diag_service/diagnosis/accept"
#     args = {
#         "trea_id": treat_id
#     }
#     post(url, data=args)
#
#
# def emr_save_diagnose(emr_diag_info):
#     """医生保存诊断"""
#     return post("/diag_service/diagnosis", data=emr_diag_info)['data']['reco_id']
#
#
# def emr_save_drug_order(drug_order_info):
#     """保存医品医嘱处方"""
#     return post("/diag_service/order", data=drug_order_info)
#
#
#
#
# def add_goods():
#     """新增商品"""
#     goods_info = copy.deepcopy(GOODS_INFO)
#     init_goods_info(goods_info)
#     resp = OptoServiceStockManageGoodPost.send_post(goods_info)
#     return resp['good_id']
#
#
# def add_drug(drug_info=None):
#     """新增药品信息"""
#     if drug_info is None:
#         drug_info = copy.deepcopy(DRUG_INFO)
#         init_drug_info(drug_info)
#     resp = post('/api/sys_service/drug', data=drug_info)
#     return resp['data']['drug_id']
#
#
# def add_depo_revision():
#     """新增商品在库调整单"""
#     url = "/depo_service/revision"
#     args = {
#         "depo_id": DEPOT_ID,
#         "list": [
#             {
#                 "item_num": 1,
#                 "stoc_id": GOODS_STOCK_ID,
#                 "list": [
#                 ],
#                 "item_goods_id": GOODS_ID
#             }
#         ]
#     }
#     resp = post(url, data=args)
#     return resp['data']
#
#
# def add_depot_revision():
#     """新增商品在库调整单"""
#     url = "/depo_service/revision"
#     resp = get('/api/depo_service/allo/good/list?page_size=7&depo_id=%s' % DEPO_ID)
#     stoc_id = resp['data']['list'][0]['batc_list'][0]['stoc_id']
#     item_num = resp['data']['list'][0]['batc_list'][0]['stoc_avail_num']
#     good_id = resp['data']['list'][0]['good_id']
#     args = {
#         "depo_id": "",
#         "list": [
#             {
#                 "batch_batchno": "20180509",
#                 "batch_validity": "2018-05-09",
#                 "produced_date": "2018-05-09",
#                 "item_num": 1216,
#                 "stoc_id": "",
#                 "list": [
#                     {
#                         "prop_prop_id": "75849089895502032",
#                         "prop_prop_name": "测试71",
#                          "prop_putinprop": 1,
#                         "choi_value": "12"
#                     }
#                 ],
#                "item_goods_id": ""
#             }
#         ]
# }
#     args['depo_id'] = DEPO_ID
#     args['list'][0]['stoc_id'] = stoc_id
#     args['list'][0]['item_num'] = item_num
#     args['list'][0]['item_goods_id'] = good_id
#     resp = post(url, data=args)
#     return resp['data']
#
#
# def add_inventory_and_item():
#     """新增盘点单及细目"""
#     #  新增盘点单
#     args = {
#         "depo_id": DEPOT_ID,  # 仓库id
#     }
#     inve_id = DepoServiceDepotInventoryPost.send_post(args)['inve_id']
#     # 新增盘点单细目
#     args = {
#         "inve_id": inve_id,  # 盘点单id
#         "goods_id": GOODS_ID,  # 商品id
#     }
#     item_id = DepoServiceDepotInventoryItemPost.send_get(args)['item_id']
#     return {'inve_id': inve_id, 'item_id': item_id}
#
#
# def get_inventory_detail(inve_id, item_id=-1):
#     """获得盘点单详情"""
#     args = {
#         "inve_id": inve_id,  # 盘点单id
#         "page_num": 1,  # 当前页
#         "page_size": 10  # 每页的数量
#     }
#     return_data = DepoServiceDepotInventoryGet.send_get(args)
#     if item_id <= 0:  # 返回盘点单详情
#         return return_data
#     if item_id > 0:  # 返回盘点单细目
#         l_item = [x for x in return_data['list'] if x['item_id'] == item_id]
#         if any(l_item):
#             return l_item[0]
#         else:
#             return None
#
#
# def cancel_promote_sales(prom_id):
#     """作废优惠"""
#     args = {"prom_id": prom_id}
#     SaleServicePromoteCancelPost.send_post(args)
#
#
# def add_promote_sales():
#     """"新增促销优惠"""
#     now = datetime.datetime.now()
#     args = {
#         "prom_name": "春节大促销{}".format(unique_id(10)),  # 活动名称
#         "prom_begin_time": date_to_string(now, str_format='%Y-%m-%d %H:%M:%S'),  # 优惠生效时间
#         "prom_end_time": date_to_string(now+datetime.timedelta(days=7), str_format='%Y-%m-%d %H:%M:%S'),  # 优惠结束时间
#         "list": [  # 促销细目列表
#             {
#                 "item_goodsid": GOODS_ID,  # 商品id
#                 "promote": 66.9  # 商品促销价
#             }
#         ]
#     }
#     return_data = SaleServicePromoteSalesPost.send_post(args)
#     return return_data['prom_id']
#
#
# def add_promote_buy(prom_obj):
#     """"新增买赠优惠"""
#     now = datetime.datetime.now()
#     args = {
#         "prom_name": "春节大买赠{}".format(unique_id(10)),  # 活动名称
#         "prom_obj": prom_obj,  # 优惠商品范围,1-商品;2-类别;3-整单;4-品牌
#         "prom_begin_time": date_to_string(now, str_format='%Y-%m-%d %H:%M:%S'),  # 优惠生效时间
#         "prom_end_time": date_to_string(now+datetime.timedelta(days=7), str_format='%Y-%m-%d %H:%M:%S'),  # 优惠结束时间
#         "list": [  # 买赠优惠细目列表
#             {
#                 "item_goodsid": GOODS_ID,
#                 "buy": 3,  # 数量满
#                 "give": 1,  # 赠品件数
#                 "give_goods": [  # 买赠商品细目列表
#                     {
#                         "goods_id": GOODS_ID,
#                         "goods_num": 1
#                     }
#                 ]
#             }
#         ]
#     }
#     return_data = SaleServicePromoteBuyPost.send_post(args)
#     return return_data['prom_id']
#
#
# def add_promote_full_cut(prom_obj):
#     """"新增满减优惠"""
#     now = datetime.datetime.now()
#     args = {
#         "prom_name": "春节大满减{}".format(unique_id(10)),  # 活动名称
#         "prom_obj": prom_obj,  # 优惠商品范围,1-商品;2-类别;3-整单;4-品牌
#         "prom_begin_time": date_to_string(now, str_format='%Y-%m-%d %H:%M:%S'),  # 优惠生效时间
#         "prom_end_time": date_to_string(now+datetime.timedelta(days=7), str_format='%Y-%m-%d %H:%M:%S'),  # 优惠结束时间
#         "list": [  # 满减优惠细目列表
#             {
#                 "item_goodsid": GOODS_ID,
#                 "full": 99.9,  # 售价满
#                 "dec": 19.9,  # 减免
#             }
#         ]
#     }
#     return_data = SaleServicePromoteFullCutPost.send_post(args)
#     return return_data['prom_id']
#
#
# def add_promote_discount(prom_obj):
#     """"新增折扣优惠"""
#     now = datetime.datetime.now()
#     args = {
#         "prom_name": "春节大折扣{}".format(unique_id(10)),  # 活动名称
#         "prom_obj": prom_obj,  # 优惠商品范围,1-商品;2-类别;3-整单;4-品牌
#         "prom_begin_time": date_to_string(now, str_format='%Y-%m-%d %H:%M:%S'),  # 优惠生效时间
#         "prom_end_time": date_to_string(now+datetime.timedelta(days=7), str_format='%Y-%m-%d %H:%M:%S'),  # 优惠结束时间
#         "list": [  # 折扣优惠列表
#             {
#                 "item_goodsid": GOODS_ID,
#                 "discount": 85  # 单价折扣%
#             }
#         ]
#     }
#     return_data = SaleServicePromoteDiscountPost.send_post(args)
#     return return_data['prom_id']
#
#
# def update_depot_inventory_state(depot_id, state):
#     """"锁盘状态修改"""
#     args = {
#         "depo_id": depot_id,  # 仓库id
#         "depo_lock": state,  # 锁库标志;0-不锁库;1-锁库
#     }
#     DepoServiceDepotInventoryStatePost.send_post(args)
#
#
# def add_inventory(depot_id):
#     """"新增盘点单"""
#     args = {
#         "depo_id": depot_id,  # 仓库id
#     }
#     inve_id = DepoServiceDepotInventoryPost.send_post(args)['inve_id']
#     return inve_id
#
#
# def end_inventory(inve_id):
#     """"盘点结束"""
#     # 盘点结束
#     args = {
#         "inve_id": inve_id,  # 盘点单细目id
#         "inve_rem": "结束备注"
#     }
#     DepoServiceDepotInventoryEndPost.send_post(args)
#
#
# def adjust_inventory(inve_id):
#     """"盘点单库存修正"""
#     args = {
#         "inve_id": inve_id,  # 盘点单细目id
#     }
#     DepoServiceDepotInventoryAdjustStockPost.send_post(args)
#
#
# def auto_inventory(inve_id):
#     """"盘点自动匹配"""
#     args = {
#         "inve_id": inve_id,  # 盘点单细目id
#     }
#     DepoServiceDepotInventoryAutoInventoryPost.send_post(args)
#
#
# def pay(sale_id):
#     """销售订单-付款"""
#     url = "/sale_service/sales_order/pay"
#     data_ = {
#         'sale_id': sale_id
#     }
#     post(url, data=data_)
#
#
# def add_depot_warn_batch(warn_upper=100, warn_lower=10):
#     """"批量设置库存报警"""
#     args = {
#         "depo_id": DEPOT_ID,  # 仓库id
#         "clas_id": GOODS_CLASS_ID,  # 类别ID
#         "bran_id": GOODS_BRAND_ID,  # 品牌ID
#         "vari_id": GOODS_VARIETY_ID,  # 品种码ID
#         "warn_upper": warn_upper,  # 报警上限
#         "warn_lower": warn_lower  # 报警下限
#     }
#     DepoServiceDepotWarnBatchUpdatePost.send_post(args)
#
#
# def add_allo():
#     """"新增调拨出库"""
#     args = {
#         "allo_out_depot":  DEPOT_ID,  # 调出仓库
#         "allo_in_depot": DEPOT_ID_2,  # 调入仓库
#         "list": [
#             {
#                 "stoc_id": GOODS_STOCK_ID,  # 库存ID
#                 "item_num": 1  # 调拨数量
#             }
#         ]
#     }
#     allo_id = DepoServiceAlloPost.send_post(args)['allo_id']
#     return allo_id
#
#
# def add_allo_other():
#     """"新增其他商品出库"""
#     url = "/depo_service/otherout"
#     args = {
#         "type_id": OUT_TYPE_ID,
#         "othe_reaason": "其他原因",
#         "depo_id": DEPOT_ID,
#         "list":
#             [
#                 {"stoc_id": GOODS_STOCK_ID,
#                  "item_num": 1}
#             ]
#     }
#     allo_other_info = post(url, data=args)
#     return allo_other_info['data']
#
#
# def add_good_price_adjustment():
#     """"新增商品调价单"""
#     url = "/opto_service/price/adju"
#     args = {
#         "adju_active": 0,
#         "list": [
#             {
#                 "item_goodsid": GOODS_ID,
#                 "item_goodsname": GOODS_NAME,
#                 "item_goodscode": GOODS_CODE,
#                 "item_bidprice": GOODS_PRICE,
#                 "good_unit": GOODS_UNIT_ID,
#                 "cost_price": GOODS_COST_PRICE,
#                 "key": 0,
#                 "item_price": GOODS_PRICE
#             }
#         ],
#         "adju_active_time": datetime_to_string(datetime.datetime.now())
#     }
#     allo_other_info = post(url, data=args)
#     return allo_other_info['data']
#
#
# def get_depot_pick_list_by_key(sale_no):
#     """获取销售提货单"""
#     args = {
#         "stat_depo_id": DEPOT_ID,
#         "start_date": date_to_string(datetime.datetime.now()),  # 开始日期
#         "end_date": date_to_string(datetime.datetime.now()),  # 结束日期
#         "key": sale_no
#     }
#     resp = DepoServicePickListGet.send_get(args)
#     return resp['list'][0]
#
#
# def sale_depo_pick(sale_no):
#     """"销售提货——取件"""
#     pick_order = get_depot_pick_list_by_key(sale_no)
#     args = {
#         "stat_id": pick_order['stat_id'],  # 销售单子表ID
#         "stat_purchase": 0,
#     }
#     DepoServicePickPost.send_post(args)
#     return pick_order['stat_id']
#
#
# def add_depo_return():
#     """"新增商品退货"""
#     args = {
#         "retu_mfr_id": AGEN_ID,  # 供应商ID
#         "retu_depot": DEPOT_ID,  # 退货仓库ID
#         "list": [
#             {
#                 "stoc_id": GOODS_STOCK_ID,  # 库存ID
#                 "item_num": 1  # 退货数量
#             }
#         ]
#     }
#     retu_id = DepoServiceRetuPost.send_post(args)['retu_id']
#     return retu_id
#
#
# def sale_return(stat_id):
#     """"销售退货"""
#     # 销售退货
#     args = [{"stat_id": stat_id}]
#     SaleServiceSalesOrderReturnPost.send_post(args)
#
#
# def get_sale_return_list():
#     """获取销售退货单列表"""
#     url = "/sale_service/sales_refund/list?depo_id={}&page_num=1&page_size=6".format(DEPOT_ID)
#     resp = get(url)
#     return resp['data']['list']
#
#
# def add_sale_return_order(sale_id):
#     """"生成退货单"""
#     args = {"sale_id": sale_id}
#     SaleServiceSalesOrderAddReturnPost.send_post(args)
#
#
# def sale_refund(sale_id):
#     """销售退费"""
#     args = {"sale_id": sale_id}
#     SaleServiceSalesOrderRefundPost.send_post(args)
#
#
# def add_arrival():
#     """新增采购入库单"""
#     resp = post('/opto_service/stock_manage/arrival', data=ARRIVAL_INFO)
#     return resp['data']['arri_id']
#
#
# def get_arrival_list():
#     """获取采购入库列表"""
#     url = "/opto_service/stock_manage/arrival_list?depot_id={}&page_num=1&page_size=9&goods_classs=%5B%5D"\
#         .format(DEPOT_ID)
#     resp = get(url)
#     return resp['data']['list']
#
#
# class DepotLocker(object):
#     def __init__(self, deport_id):
#         self.depot_id = deport_id
#         self.lock()
#
#     def update_status(self, status):
#         args = {
#             "depo_id": self.depot_id,
#             "depo_lock": status
#         }
#         DepoServiceDepotInventoryStatePost.send_post(args)
#
#     def lock(self):
#         """开启锁盘"""
#         self.update_status(1)
#
#     def close(self):
#         self.update_status(0)
#
#
# def sale_flow():
#     # 搜索患者test_sale_flow
#     resp_args = get('api/patient_service/patient/list/for_preview?key=sqm')
#     pati_id = resp_args['data'][2]['pati_id']
#     # 得到患者处方
#     resp_args = get('/api/sale_service/patient/query_opto_list?opto_flag=4&page_size=5&page_num=1&pati_id=%s'
#                     % pati_id)
#     opto_id = resp_args['data']['list'][0]['list'][0]['opto_id'] if any(resp_args['data']['list']) else ''
#     SALE_INFO['pati_id'] = pati_id
#     SALE_INFO['opto_id'] = opto_id
#     resp = post('api/sale_service/sales_order', data=SALE_INFO)
#     # 获取sale_id,付款
#     sale_id = resp['data']['sale_id']
#     resp_ = get('/api/charge_service/to_pay_trade?pati_id=%s&account_id=53319797731233991' % pati_id)
#     amount_ = resp_['data']['list'][0]['item_total_price']
#     resp_ = get('/sale_service/sales_order?sale_id=%s&r=1530868165265' % sale_id)
#     amount = resp_['data']['sale_price']
#     sale_data = {
#         "amount": amount,
#         "pay_channel": 1,
#         "func_id": "99356382616225418",
#         "char_source": 1,
#         "bill_id": sale_id
#     }
#     sale_pay(sale_data)
#     week = get_week_start_end()
#     resp_args = get('/api/sale_service/sales_order/list?page_size=5&page_num=1&start_time=%s&end_time=%s' %
#                     (week[0], week[1]))
#     sale_no = resp_args['data']['list'][0]['sale_no']
#     sale_id = resp_args['data']['list'][0]['sale_id']
#     return sale_no, sale_id
#
#
# def sale_pay(salepay_info):
#     """视光收费"""
#     post('/charge_service/business/pay', data=salepay_info)
#
#
# def check_http_status_message(resp, exp_code=SUCCESS_STATUS, exp_msg=SUCCESS_MESSAGE):
#
#     assert resp['status'] == exp_code
#     if exp_msg is None:
#         assert resp['message'] is None
#     else:
#         assert resp['message'].encode('utf8') == exp_msg
#
#
# def get_package_id():
#     """获取挂号类别id"""
#     resp = get('/api/schedule_service/sche?sche_id=%s&r=1532671659097' % globals()['SCHE_ID'])
#     return resp['data']['package_list'][0]['package_id']
