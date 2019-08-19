# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/3 11:10
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 
"""
import copy
import json
import sys
import urlparse
import requests
from logzero import logger
from env_constants.constants_public import OS, DEVICE
from env_switch import settings, constants
from env_constants import constants_public
from base_requester import Requester
import pdb


class WebRequester(Requester):
    def __init__(self):
        super(WebRequester, self).__init__()
        self.login_url = 'authent/login'
        self.workstations = {
            'login': ('authent', ),
            'doctorstation': ('diag_service', ),
            'nursestation': ('patient_service', 'treat_service', 'address_service')
        }
        self.header_tempalte = {
            'User-Agent': constants_public.USER_AGENT,
            'station': None,
            'tenantId': settings.TENANT_ID,
            'Content-Type': 'application/json',
            'depaid': constants.ONLINE_DEPARTMENT_ID,
            'userid': str(constants.ONLINE_DOCTOR_ID),
            'device': DEVICE,
            'os': OS
        }

    @staticmethod
    def _full_url(path, is_relative=False):
        """
        根据 path 返回完整 URL
        :param path: 路径
        :param is_relative: 是否为相对路径
        :return: 完整 URL
        """
        if is_relative and path.startswith('/'):
            path = path[1:]
        if not path.startswith('/api'):
            if path.startswith('api'):
                path = '/{}'.format(path)
            else:
                if path.startswith('/'):
                    path = '/api{}'.format(path)
                else:
                    path = '/api/{}'.format(path)
        return urlparse.urljoin(settings.WEB_BASE_URL, path)

    def _detect_workstation(self, path):
        """
        根据 URL 判断属于哪个工作站，因为登录的时候请求头里需要带工作站
        :param path: 网址路径
        :return: 工作站名称
        """
        start_path = path.split('/')[0]
        for workstation, l_start in self.workstations.items():
            if start_path in l_start:
                return workstation

    def get_token(self, workstation):
        """
        获取 Token
        :param workstation: 工作站
        :return: Token 字符串
        """
        logger.debug('获取 Token: {}'.format(workstation))
        account = settings.WEB_LOGIN_INFO['account']
        password = settings.WEB_LOGIN_INFO['password']
        url = self._full_url(self.login_url)
        headers = copy.deepcopy(self.header_tempalte)
        headers['station'] = workstation
        data = {
            'account': account,
            'password': password
        }
        resp = requests.post(url, headers=headers, data=json.dumps(data))
        try:
            token = resp.json()['data']['token']
            logger.debug('获取Token, 工作站: {}, 用户名：{}, 密码：{}'.format(settings.TENANT_ID, account, password).decode('utf8'))
            return token
        except (TypeError, KeyError):
            logger.debug(resp.content.decode('utf8'))
            logger.debug('获取Token失败, 工作站: {}, 用户名：{}, 密码：{}'.format(workstation, account, password).decode('utf8'))
            sys.exit()

    def _get_headers(self, path, **kwargs):
        """
        生成请求头，主要是更新Token值。如果已经缓存则直接返回
        :param path: 网址路径
        :param kwargs: 请求参数
        :return: HTTP 请求头字典
        """
        workstation = self._detect_workstation(path)
        if workstation not in self.cached_headers:
            headers = copy.deepcopy(self.header_tempalte)
            headers['station'] = workstation
            if 'headers' in kwargs:
                headers.update(kwargs['headers'])
            token = self.get_token('login')
            headers.update({'token': token})
            self.cached_headers[workstation] = headers
        return self.cached_headers[workstation]

    def get(self, url, **kwargs):
        """
        封装了 GET 请求，并在返回中做了基本检查
        :param url: 请求路径
        :param kwargs: 参数
        :return: requests.response.json() 对象，因为现在用例里基本都是用的 dict，所以直接返回了 dict
        """
        headers = self._get_headers(url, **kwargs)
        kwargs['headers'] = headers
        # 更新token为传入的token
        if kwargs.get('token', None) is not None:
            headers['token'] = kwargs.get('token')
        resp = super(WebRequester, self).send_get(url, **kwargs)
        try:
            return resp.json()
        except ValueError, e:
            logger.debug(str(e))
            return resp

    def post(self, url, **kwargs):
        """
        封装了 POST 请求，并在返回中做了基本检查
        :param url: 请求路径
        :param kwargs: 参数
        :return: requests.response.json() 对象，因为现在用例里基本都是用的 dict，所以直接返回了 dict
        """
        headers = self._get_headers(url, **kwargs)
        kwargs['headers'] = headers
        # 更新token为传入的token
        if kwargs.get('token', None) is not None:
            headers['token'] = kwargs.get('token')
        resp = super(WebRequester, self).send_post(url, **kwargs)
        try:
            return resp.json()
        except ValueError, e:
            logger.debug(str(e))
            return resp

    def delete(self, url, **kwargs):
        """
        封装了 DELETE 请求，并在返回中做了基本检查
        :param url: 请求路径
        :param kwargs: 参数
        :return: requests.response.json() 对象，因为现在用例里基本都是用的 dict，所以直接返回了 dict
        """
        headers = self._get_headers(url, **kwargs)
        kwargs['headers'] = headers
        # 更新token为传入的token
        if kwargs.get('token', None) is not None:
            headers['token'] = kwargs.get('token')
        resp = super(WebRequester, self).send_delete(url, **kwargs)
        return resp.json()

    def send_request(self, path, request_type='get', **kwargs):
        path = self.clean_path(path)
        url = self._full_url(path)
        resp = super(WebRequester, self).send_request(url, request_type, **kwargs)
        self.basic_check(resp, **kwargs)
        return resp

    @staticmethod
    def basic_check(resp, exp_http_status=200, exp_status='000', exp_message='', **kwargs):
        assert resp.status_code == exp_http_status
        try:
            resp_json = resp.json()
            assert resp_json['status'] == exp_status
            if resp_json['status'] != '000':
                assert resp_json['message'] == exp_message
        except ValueError, e:
            logger.debug(str(e))


if __name__ == "__main__":
    logger.debug(WebRequester().get_token('login'))
