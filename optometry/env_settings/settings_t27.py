#!/usr/bin/env python
# -*- coding=utf-8 -*-
GET, POST, DELETE = 'get', 'post', 'delete'

WORKSTATION = {
    'login': ('authent',),
    'doctorstation': ('diag_service',),
    'nursestation': ('patient_service', 'treat_service', 'address_service'),
}

# 测试环境
LOGIN_INFO = {
    'login_url': 'api/authent/login',
    'account': '18805813180',
    'password': '4j284y2s'
}

# 测试环境
TENANT_ID = '48739379220582541'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 ' \
             'Safari/537.36'
CONTENT_TYPE = 'application/json'
BASE_URL = 'http://192.68.75.26/'
DEPAID = '48741634074087722'
USERID = '42914065508864246'
DEVICE = 'win10.0'
OS = 'webkit537.36ver537.36'
