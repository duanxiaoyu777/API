#coding=utf-8
import ast
from public import mytest
from ddt import ddt,data,unpack
from loguru import logger
from public.send_request import SendRequest
from public.data_info import get_test_case_data, data_info
# import json

@ddt
class Other(mytest.MyTokenTest):
    """其他需要验证token的接口"""

    @data(*get_test_case_data(data_info, 'other'))
    def test_api(self, data):
        method = data['method']
        url = self.url + '/api' + data['url']
        send_data = data['send_data']
        assert_info = data['assert_info']
        logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url,header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])