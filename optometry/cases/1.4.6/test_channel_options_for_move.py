# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/26 18:03
@Author  : longyy
@Contact : longyy@gratone.cn
@Software: PyCharm
@Desc    : 
"""
from service.optometry_service import channel_options_for_move


def test_options_for_move():
    resp = channel_options_for_move("177379170773500011", "177379174221218005")
