#coding=utf-8
import ast
from public import mytest
from ddt import ddt,data,unpack
from loguru import logger
from public.send_request import SendRequest
from public.data_info import get_test_case_data, data_info

@ddt
class Login(mytest.MyTest):
    """登陆模块"""

    @data(*get_test_case_data(data_info, 'login'))
    def test_login(self, data):
        "登陆接口"
        method = data['method']
        url = self.url + data['url']
        send_data = data['send_data']
        assert_info = data['assert_info']
        logger.info(url)
        logger.info(send_data)
        logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url,header=self.headers)
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])







