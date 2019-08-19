# -*- coding:utf-8 -*-
GET, POST, DELETE = 'get', 'post', 'delete'


WORKSTATION = {
    'login': ('authent'),
    'doctorstation': ('diag_service'),
    'nursestation': ('patient_service', 'treat_service', 'address_service'),
    'system':('tenant_service','sys_service')
}

LOGIN_INFO = {
    'login_url': '/api/platform/authent/login',
    'account': '13757124497',
    'password': 'Guantong12'
}

TENANT_ID = '0'
USER_AGENT ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
CONTENT_TYPE = 'application/json'
BASE_URL = 'https://test.best-seeing.cn'
DEPAID = '1'
USERID = '551060640651'
DEVICE = 'win10.0'
OS = 'webkit537.36ver537.36'
ACCOID = '4306251157504'

# 预发布环境
# BASE_URL = 'http://106.15.81.71'

