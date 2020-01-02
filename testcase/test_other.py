# coding=utf-8
import unittest
from public import mytest
from ddt import ddt,data,unpack
from loguru import logger
from public.send_request import SendRequest
from public.data_info import get_test_case_data, data_info,write_res
import json

@ddt
class Other(mytest.MyTokenTest):
    """其他模块相关"""

    # @unittest.skipIf(True, '调试不执行')
    @data(*get_test_case_data(data_info, 'other'))
    def test_api(self, data):
        logger.info(data)
        method = data['method']
        url = self.url + data['url']
        send_data = data['send_data']
        assert_info = data['assert_info']
        rownum = data['rownum']
        logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url,header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 接口返回值写入表格
        self.assertEqual(r['status'], assert_info['status'])            # 断言status==status
        self.assertEqual(r['info'], assert_info['info'])                # 断言info==info