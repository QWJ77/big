# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/25 9:55
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 视光运营-采购管理-定做查询
"""
import copy

from logzero import logger

from args_template.args_webrestful import CUSTOM_STATISTICS_EXPORT
from common_method import unique_id
from service.webrestful_service import custom_statistics_export


def verify_result(resp_data, data_):
    """
    :param resp_data: 获取的商品信息
    :param data_: 保存的商品信息
    :return:
    """
    assert resp_data['good_code'] == data_['good_code']
    assert resp_data['good_name'] == data_['good_name']
    assert resp_data['good_class_id'] == data_['good_class_id']
    assert resp_data['good_brand_id'] == data_['good_brand_id']
    assert resp_data['good_factory_id'] == data_['good_factory_id']
    assert resp_data['good_supplier_id'] == data_['good_supplier_id']
    assert resp_data['good_bidprice'] == data_['good_bidprice']
    assert resp_data['good_price'] == data_['good_price']
    assert resp_data['good_char_id'] == data_['good_char_id']
    assert resp_data['good_unitid'] == data_['good_unitid']
    assert resp_data['good_give'] == data_['good_give']
    assert resp_data['status'] == data_['status']


def test_custom_statistics_export():
    """所有供应商-定做统计导出压缩文件"""
    data_ = copy.deepcopy(CUSTOM_STATISTICS_EXPORT)
    resp = custom_statistics_export(data_)
    assert resp.content
    # file_name = '{}.xls'.format(str(unique_id(13)))
    # logger.debug(file_name)
    # f = open(file_name, 'wb')
    # f.write(resp.content)
    # f.close()
