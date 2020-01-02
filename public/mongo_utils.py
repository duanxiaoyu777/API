# coding=utf-8
import pymongo
from urllib import parse
from config.basic_config import ConfigInit
from loguru import logger


class MongoDatabase:
    def __init__(self):
        self.db = self.connect_sql()

    def connect_sql(self):
        user = parse.quote_plus(ConfigInit.mongo_user)
        pw = parse.quote_plus(ConfigInit.mongo_pw)
        try:
            client = pymongo.MongoClient('mongodb://{}:{}@{}/'.format(user, pw, ConfigInit.mongo_ip))
            mongo_db = client['jimi-platform']
            logger.info('连接 jimi-platform 成功')
        except Exception as e:
            logger.info('连接数据库失败')

        return mongo_db

# if __name__ == '__main__':