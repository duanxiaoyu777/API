# coding=utf-8

import unittest
import HTMLTestRunner
import time
import os
from loguru import logger
from config import globalparam
from public import sendmail
from public.mysql_utils import MysqlDatabase
# import BeautifulReport
from testcase import test_login


path = os.path.join(os.path.abspath('.'),'report', 'log','test_{}.log'.format(time.strftime('%Y-%m-%d')))
logger.add(path)  # 日志初始化
def run(method, test=None):
    if method == 'all':
        test_dir = './testcase'
        suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        reportname = os.path.join(globalparam.report_path, 'TestResult' + now + '.html')
        with open(reportname, 'wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(
                stream = f,
                verbosity = 2,
                title = '接口自动化测试报告',
                description = '输出如下报告'
            )
            runner.run(suite)
        time.sleep(2)
        # 发送邮件
        # mail = sendmail.SendMail()
        # mail.send()
        # 初始化测试数据，执行sql语句
        MysqlDatabase().delete_individual_user()
        MysqlDatabase().delete_enterprise_user()
        MysqlDatabase().delete_order_partner()
        MysqlDatabase().Update_invoice_status()
        MysqlDatabase().Update_confirm_money()

    # 此逻辑暂时作废
    # if method == 'one':
    #     suit = unittest.TestSuite()
    #     suit.addTest(test)  # 把这个类中需要执行的测试用例加进去，有多条再加即可
    #     runner = unittest.TextTestRunner()
    #     runner.run(suit)

if __name__ == '__main__':
    # run('one', test_login.Login('test_login'))
    # while True:
        run('all')