# -*- coding=utf-8 -*-
import requests
from logzero import logger
from requester.web_requester import WebRequester

WEB_REQUESTER = WebRequester()


#def authent_login_type():



def is_optometry_read(**kwargs):
    """判断视光是否只读"""
    url = "/erp_service/group/is_optometry_read"
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def stock_goods_list(goods_batch, **kwargs):
    """库存详情"""
    url = "/erp_service/stock_info/goods/list?goods_batch={}".format(goods_batch)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def atm_put_record_list(atm_id, page_num, page_size, **kwargs):
    """货道放货记录查询"""
    url = "/erp_service/atm/put_record_list?atm_id={}&page_num={}&page_size={}".format(atm_id, page_num, page_size)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def atm_add_goods(data_, **kwargs):
    """货道商品加货"""
    url = "/erp_service/atm/add_goods"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_goods_list(atm_id, src_channel_id, page_num, page_size, **kwargs):
    """加货选择商品"""
    url = "/erp_service/atm/goods_list?atm_id={}&src_channel_id={}&page_num={}&page_size={}".format(atm_id, src_channel_id, page_num, page_size)
    resp = WEB_REQUESTER.get(url,  **kwargs)
    return resp


def get_atm_move(data_, **kwargs):
    """货道商品移除"""
    url = "/erp_service/atm/move"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_atm_channel_list(atm_id, page_num, page_size, **kwargs):
    """货道列表"""
    url = "/erp_service/atm/channel_list?atm_id={}&page_num={}&page_size={}".format(atm_id, page_num, page_size)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def channel_options_for_move(atm_id, src_channel_id, **kwargs):
    """移动货时货道选项列表"""
    url = "/erp_service/atm/channel_options_for_move?atm_id={}&src_channel_id={}".format(atm_id, src_channel_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def atm_channel_options(atm_id, **kwargs):
    """货道选项列表"""
    url = "/erp_service/atm/channel_options?atm_id={}".format(atm_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def upload_picture(source_type, extension, file_path):
    """
    上传图片资源
    :parameter source_type:
        [视光厂商][工商营业执照]: 12
        [视光厂商][医疗器械经营许可证号]: 7
        [视光厂商][医疗器械生产许可证号]: 8
    :parameter extension: 文件后缀名
    :parameter file_path: 文件路径
    :return: file id
    """
    ext_dict = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg'
    }
    # 请求OSS资源地址
    url_upload = "/tenant_service/tenant/upload_picture"
    data_upload = {
        "file_extension": extension,
        "file_type": ext_dict[extension],
        "source_type": source_type
    }
    resp_upload = WEB_REQUESTER.post(url_upload, data=data_upload)
    resp_data = resp_upload['data']
    # 资源上传
    url_oss = resp_data['url']
    data_oss = {
        "OSSAccessKeyId": resp_data['ossaccessKeyId'],
        "Signature": resp_data['signature'],
        "key": resp_data['key'],
        "policy": resp_data['policy'],
    }
    files = {
        'file': (file_path, open(file_path, 'rb'))
    }
    resp = requests.post(url_oss, files=files, data=data_oss)

    logger.debug("resp: {}".format(resp))
    return resp_data['file_id']


def save_factory_base_info(data_, **kwargs):
    """视光厂商——基本信息保存
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/system/factory/base'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def update_factory_base_info(data_, **kwargs):
    """视光厂商——基本信息修改
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/system/factory/base/update'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_factory_info(mfr_id, **kwargs):
    """视光厂商获取
    :param mfr_id: 视光厂商id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/system/factory?mfr_id={}'
    resp = WEB_REQUESTER.get(url.format(mfr_id), **kwargs)
    return resp


def get_factory_list(params, **kwargs):
    """视光厂商获取
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/system/factory/list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def copy_goods(good_id, **kwargs):
    """复制新增商品
    :param good_id: 商品id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    # url = '/erp_service/goods/copy/{}'.format(good_id)
    url = '/erp_service/stock_manage/good?good_id={}'.format(good_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def get_same_nation_list(params, **kwargs):
    """批量入库时商品族列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/arrival/batch_add/same_nation_list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_nation_view(nation_id, **kwargs):
    """批量入库时某族商品详细
    :param nation_id: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/arrival/batch_add/nation_view?nation_id={}'.format(nation_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def batch_update_goods(data_, **kwargs):
    """视光厂商——批量修改商品
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/system/goods/batch_update'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_goods_info(goods_id, **kwargs):
    """获取商品目录信息
    :param goods_id: 商品id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/opto_service/stock_manage/good?good_id={}'.format(goods_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def get_batch_update_goods_list(params, **kwargs):
    """批量修改时查询商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/system/goods/batch_update/goods_list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def maintain_new(data_, **kwargs):
    """新增养护记录
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/maintain'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_maintain_list(params, **kwargs):
    """养护记录列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/maintain/list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def maintain_update(main_id, data_, **kwargs):
    """修改养护记录
    :param main_id: 养护记录id
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/maintain/{}'.format(main_id)
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def maintain_delete(main_id, **kwargs):
    """修改养护记录
    :param main_id: 养护记录id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/maintain/{}'.format(main_id)
    resp = WEB_REQUESTER.delete(url, **kwargs)
    return resp


def get_maintain_goods_list(params, **kwargs):
    """养护记录商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/maintain/goods/list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_stock_info_goods_list(params, **kwargs):
    """库存详情商品列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/list'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_stock_info_goods_changes(params, **kwargs):
    """商品进销存详情列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/changes'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def get_stock_info_goods_modes(params, **kwargs):
    """商品进销存详情列表
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/modes'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_info_goods_adju_new(data_, **kwargs):
    """新增成本调整记录
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/adjustment'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_stock_info_goods_adju(adju_id, **kwargs):
    """获取成本调整记录详情
    :param adju_id: 成本调整ID
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/adjustment/{}'.format(adju_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def get_stock_info_goods_adju_list(params, **kwargs):
    """获取成本调整记录详情
    :param params: 查询参数
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/adjustments'
    resp = WEB_REQUESTER.get(url, params=params, **kwargs)
    return resp


def stock_info_goods_adju_delete(adju_id, **kwargs):
    """删除成本调整记录
    :param adju_id: 调整记录id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/stock_info/goods/adjustment/{}'.format(adju_id)
    resp = WEB_REQUESTER.delete(url, **kwargs)
    return resp


def batch_stock_list(data_, **kwargs):
    """批次库存数量列表
    :param data_: 请求数据
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/batch_stock/list'
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def get_discount_by_class_id(class_id, **kwargs):
    """根据类别获取折扣权限
    :param class_id: 商品类别id
    **kwargs:
        exp_http_status: 期望的http status
        exp_status: 期望的status
        exp_message: 期望的报错信息
    """
    url = '/erp_service/discount/{}'.format(class_id)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp


def prop_para(data_, **kwargs):
    """"商品属性-参数
            **kwargs:
                exp_http_status: 期望的http status
                exp_status: 期望的status
                exp_message: 期望的报错信息
            """
    url = "/sys_service/opto/good_prop/para"
    resp = WEB_REQUESTER.post(url, data=data_, **kwargs)
    return resp


def charg_account_list(query_type, **kwargs):
    """"获取运营机构
        **kwargs:
            exp_http_status: 期望的http status
            exp_status: 期望的status
            exp_message: 期望的报错信息
        """
    url = "/sys_service/charg_account/list?query_type={}".format(query_type)
    resp = WEB_REQUESTER.get(url, **kwargs)
    return resp
