#!/usr/bin/env python
# -*- coding=utf-8 -*-
import time
import datetime
from dba.db_tools import get_connection, commit_db


def update_visit_time(visi_id, visi_time):
    sqls = (
        'update tre_outp_treatment set trea_visi_time="%s" where visi_id="%s"' % (visi_time, visi_id),
        'update tre_outp_book set visi_create_time="%s" where visi_id="%s"' % (visi_time, visi_id),
        'update emr_treatment set emr_create_time="%s" where visi_id="%s"' % (visi_time, visi_id),
        'update emr_outp_preview set prev_time="%s" where visi_id="%s"' % (visi_time, visi_id)
    )
    conn = get_connection()
    for sql in sqls:
        print sql
        commit_db(conn, sql)


def unique_id(length, prefix='', suffix=''):
    """
    用时间戳生成指定长度的唯一值(数字类型)
    :param length: 唯一值的长度，包括前缀和后缀的长度
    :param prefix: 前缀
    :param suffix: 后缀
    :return: 唯一 ID
    """
    unique_length = length - len(prefix) - len(suffix)
    if unique_length <= 10:
        uid = str(int(time.time()))[10 - unique_length:]
    else:
        pattern = '{{:.{}f}}'.format(unique_length - 10)
        uid = pattern.format(time.time()).replace('.', '')
    uid = '{}{}{}'.format(prefix, uid, suffix)
    return uid


def date_to_string(date_obj, str_format='%Y-%m-%d'):
    """
    datetime.datetime对象转换成日期字符串
    :param date_obj: datetime.datetime类型
    :param str_format: 日期格式
    :return:
    """
    return date_obj.strftime(str_format)


def string_to_date(str_date, str_format='%Y-%m-%d'):
    return datetime.datetime.strptime(str_date, str_format)


def get_week_start_end(str_format='%Y-%m-%d'):
    today = datetime.date.today()
    weekday = today.weekday()
    monday_delta = datetime.timedelta(weekday)
    sunday_delta = datetime.timedelta(6 - weekday)
    monday = today - monday_delta
    sunday = today + sunday_delta
    if str_format:
        monday, sunday = date_to_string(monday), date_to_string(sunday)
    return monday, sunday


def datetime_to_string(datetime_, type_=1):
    if type_ == 1:
        return datetime_.strftime("%Y-%m-%d %H:%M:%S")
    elif type_ == 2:
        return datetime_.strftime("%Y-%m-%d")
    elif type_ == 3:
        return datetime_.strftime("%Y%m%d%H%M%S")


def init_goods_info(goods_info):
    """修改good_name和good_code"""
    uid_ = unique_id(13)
    goods_info['good_name'] = "GN" + uid_
    goods_info['good_code'] = "GC" + uid_


def init_drug_info(drug_info):
    """修改drug_code,gene_drug_name"""
    uid_ = unique_id(13)
    drug_info['drug_code'] = "DRUG" + uid_
    drug_info['gene_drug_name'] = "药品通用名" + uid_
    drug_info['goods_drug_name'] = "药品商品名" + uid_


if __name__ == "__main__":
    update_visit_time('26475943560352304', '2017-10-20 09:35:10')

