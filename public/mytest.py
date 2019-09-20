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
        self.url = ConfigInit.login_url
        self.headers = {'Content-Type': 'application/json'}
        logger.info('############################### START ###############################')


    def tearDown(self):
        logger.info('###############################  End  ###############################')


class MyTokenTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """

    @classmethod
    def login_func(self, account='281878321@qq.com', pw='q5310543'):
        """封装登陆函数"""
        send_data = {
            "account":account,
            "password":pw,
            "platform_code":"PLATFORM",
            "app_id":"a1287a3837f640e0"
        }
        url = ConfigInit.login_url + '/login'
        logger.info(url)
        headers = {'Content-Type': 'application/json'}
        logger.info(send_data)
        logger.info(headers)
        r = SendRequest().send_json_post(url=url, dict=send_data, header=headers)
        logger.info(r)
        token = r['data']['accessToken']
        return token

    @classmethod
    def setUpClass(cls):
        cls.token = cls.login_func()

    def setUp(self):
        self.url = ConfigInit.url
        self.headers = {'Content-Type': 'application/json',
                        'Authorization':'Bearer ' + self.token
                        }
        logger.info('############################### START ###############################')


    def tearDown(self):
        logger.info('###############################  End  ###############################')