# -*- coding=utf-8 -*-
from requester.web_requester import WebRequester
from env_switch import constants
from service.optometry_service import get_discount_by_class_id

REQUESTER = WebRequester()


def test_get_discount_by_class_id():
    """根据类别获取折扣权限"""
    get_discount_by_class_id(constants.GOODS_CLASS_ID)



