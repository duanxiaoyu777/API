#coding=utf-8
import ast
import json
from pprint import pprint
from public import mytest
from ddt import ddt,data,unpack
from loguru import logger
from public.send_request import SendRequest
from public.data_info import get_test_case_data, data_info, write_res

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
        rownum = data['rownum']
        # logger.info(url)
        # logger.info(send_data)
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url,header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])







