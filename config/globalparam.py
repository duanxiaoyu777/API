# coding=utf-8
import os
import time
from loguru import logger


# 项目路径
project_path = os.path.abspath('.')

# 日志路径
log_path = os.path.join(project_path,'report', 'log','test_{}.log'.format(time.strftime('%Y-%m-%d')))
logger.info(project_path)

# 测试报告路径
report_path = os.path.join(project_path, 'report', 'html_report')

# 测试数据路径
data_path = os.path.join(project_path, 'data', 'testdata')