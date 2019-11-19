# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/26 17:49
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from dba import db_tools
from env_switch import settings
from service.optometry_service import atm_channel_options


def verify_channel(atm_id):
        conn = db_tools.get_connection(settings.DB_ENV)
        sql = "SELECT * FROM device_atm_channel WHERE channel_tena_id='{}' AND channel_atm_id='{}'".format(settings.TENANT_ID, atm_id)
        results = db_tools.select_db_all(conn, sql)
        conn.close()
        return results


def test_atm_channel_options():
    """货道选项列表"""
    resp = atm_channel_options('177379170773500011')
    result = verify_channel('177379170773500011')
    assert len(result) == len(resp['data'])


def test_atm_channel_options_not_exist():
    """货道选项列表----不存在的atmid"""
    resp = atm_channel_options('00000000')
    assert len(resp['data']) == 0

