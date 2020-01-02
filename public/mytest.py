# coding=utf-8
import time
import unittest
from loguru import logger
from public.send_request import SendRequest
from config.basic_config import ConfigInit
# from testcase.test_login import Login


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.url = ConfigInit.url
        self.headers = {'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        logger.info('############################### START ###############################')


    def tearDown(self):
        logger.info('###############################  End  ###############################')


class MyTokenTest(unittest.TestCase):
    """
    The base class is for all testcase.=
    """

    @classmethod
    def login_func(cls, account='13800138907', password='5bc791b2da1b1efa077dd20b2211f6c1'):
        """封装登录函数"""

        send_data = {
            'mobile': account,
            'password': password
        }
        url = ConfigInit.url + 'member/login'
        logger.info(url)
        headers = {'Content-Type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        logger.info(send_data)
        logger.info(headers)
        r = SendRequest().send_json_post(url=url, dict=send_data, header=headers)
        logger.info(r)
        # print(r)
        token = r['data']['token']
        return token

    @classmethod
    def setUpClass(cls):
        cls.token = cls.login_func()

    def setUp(self):
        self.url = ConfigInit.url
        self.headers = {'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
                        'token': self.token
                        }
        logger.info('############################### START ###############################')


    def tearDown(self):
        logger.info('###############################  End  ###############################')