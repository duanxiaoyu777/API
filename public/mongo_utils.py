#coding=utf-8
import pymongo
from urllib import parse
from config.basic_config import ConfigInit

def connect_sql():
    user = parse.quote_plus(ConfigInit.mongo_user)
    pw = parse.quote_plus(ConfigInit.mongo_pw)
    client = pymongo.MongoClient('mongodb://{}:{}@{}/'.format(user, pw, ConfigInit.mongo_ip_port))

    return client