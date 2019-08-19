# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/3 10:31
@Author  : xiaoyichao
@Contact : xiaoyc@gratone.cn
@Software: PyCharm
@Desc    : 请求基础类
"""
import json
import requests
from logzero import logger
from env_constants.constants_public import REQUEST_METHOD


class Requester(object):
    @staticmethod
    def clean_path(path):
        if path.startswith('/'):
            # Remove slash from the beginning of path
            path = path[1:]
        return path

    def __init__(self):
        self.cached_headers = dict()

    def send_request(self, url, request_type=REQUEST_METHOD['GET'], **kwargs):
        headers = kwargs.get('headers')
        if request_type == REQUEST_METHOD['GET']:
            resp = requests.get(url, headers=headers, params=kwargs.get('params', None))
            logger.debug(resp.url)
        elif request_type == REQUEST_METHOD['POST']:
            arg_data = kwargs['data']
            if isinstance(arg_data, dict) or isinstance(arg_data, list):
                data = arg_data
            else:
                try:
                    data = json.loads(arg_data)
                    # headers.update({'content-type': 'application/json'})
                    # import ipdb; ipdb.set_trace()
                    # data = json.dumps(data)
                except:
                    data = dict()
                    for mapping in arg_data.split('&'):
                        k, v = mapping.split('=')
                        data[k] = v
            logger.debug(url)
            data = json.dumps(data)
            resp = requests.post(url, headers=headers, data=data)
        elif request_type == REQUEST_METHOD['DELETE']:
            logger.debug(url)
            resp = requests.delete(url, headers=headers)
        elif request_type == REQUEST_METHOD['PUT']:
            logger.debug(url)
            data = json.dumps(kwargs['data'])
            resp = requests.put(url, headers=headers, data=data)
        else:
            raise Exception('Request type must be one of [GET, POST]')

        try:
            logger.debug(resp.content.decode('utf8'))
        except UnicodeDecodeError, e:
            logger.debug(str(e))
        return resp

    def send_get(self, url, **kwargs):
        """
        发送 GET 请求
        :param url: 请求URL
        :param kwargs: 请求参数，包括请求头，参数等
        :return: 返回 requests.response 对象
        """
        return self.send_request(url, REQUEST_METHOD['GET'], **kwargs)

    def send_post(self, url, **kwargs):
        """
        发送 POST 请求
        :param url: 请求URL
        :param kwargs: 请求参数，包括请求头、参数和Body等
        :return: 返回 requests.response 对象
        """
        return self.send_request(url, REQUEST_METHOD['POST'], **kwargs)

    def send_delete(self, url, **kwargs):
        """
        发送 DELETE 请求
        :param url: 请求URL
        :param kwargs: 请求参数，包括请求头、参数等
        :return: 返回 requests.response 对象
        """
        return self.send_request(url, REQUEST_METHOD['DELETE'], **kwargs)

    def send_put(self, url, **kwargs):
        """
        发送 PUT 请求
        :param url: 请求URL
        :param kwargs: 请求参数，包括请求头、参数等
        :return: 返回 requests.response 对象
        """
        return self.send_request(url, REQUEST_METHOD['PUT'], **kwargs)


def common_check(resp):
    """
    公共Check方法，检查 200 响应码和 status字段值(000为正常)
    :param resp: request.response 对象
    :return:
    """

    assert resp.status_code == 200, error_request_detail(resp, '响应码非200').decode("utf-8")
    assert resp.json()['status'] == '000', error_request_detail(resp, '响应内容中 Status 不为 "000"').decode("utf-8")


def abnormal_check(resp, message=''):
    """
    异常Check方法，验证返回的错误信息
    :param resp: request.response 对象
    :param message: 信息内容
    :return:
    """
    # pdb.set_trace()
    assert resp['message'] == message


def check_fields(expect, actual, ignore_additional=True):
    """
    比较两个 Set 并找出差异。主要用来判断 HTTP响应里是否缺少字段或多返回了字段
    :param expect: 期望字段列表
    :param actual: 实际返回字段列表
    :param ignore_additional: 是否忽略返回结果中的多余字段
    :return:
    """
    # pdb.set_trace()
    assert not set(expect) - set(actual), u'返回值里少了字段：( {} )'.format(', '.join(set(expect) - set(actual)))
    if not ignore_additional:
        assert not set(actual) - set(expect), u'返回值里多了字段：( {} )'.format(', '.join(set(actual) - set(expect)))


def error_request_detail(resp, error_msg=''):
    """
    打印完整请求信息，用于报错时调试
    :param resp: request.response 对象
    :param error_msg: 错误信息
    :return: 请求信息（字符串）
    """
    content = '{}\n{}'.format(_get_request_info(resp), error_msg)
    return content


def _get_request_info(resp):
    """
    从 request.response 对象中提取请求和返回的详细信息
    :param resp: request.response 对象
    :return: 请求信息（字符串）
    """
    content = """
    [ 请求信息 ]
    URL: {}
    Headers: {}
    Body: {}
    ------------------------
    [ 响应信息 ]
    Status: {}
    Content: {}
    """.format(resp.request.url, resp.request.headers, resp.request.body, resp.status_code,
                resp.text.encode('utf-8'))
    return content
