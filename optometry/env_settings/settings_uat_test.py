#!/usr/bin/env python
# -*- coding=utf-8 -*-
GET, POST, DELETE = 'get', 'post', 'delete'

WORKSTATION = {
    'login': ('authent',),
    'doctorstation': ('diag_service',),
    'nursestation': ('patient_service', 'treat_service', 'address_service'),
}

# 预发布环境
LOGIN_INFO = {
    'login_url': '/api/authent/login',
    'account': 'sqm',
    'password': 'aaaaaaa1'
}

# 预发布环境
TENANT_ID = '53319797731233991'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 ' \
             'Safari/537.36'
CONTENT_TYPE = 'application/json'
BASE_URL = 'https://test.best-seeing.cn'
DEPAID = '55574160918844390'
DEVICE = 'win10.0'
OS = 'webkit537.36ver537.36'
