#!/usr/bin/env python
# encoding: utf-8
# @author   : changhsing
# @time     : 2020/7/5 21:39
# @site     : 
# @file     : test.py
# @software : PyCharm
import pymysql


class MysqlConfig():
    def __init__(self):
        self.host = "120.24.148.131"
        self.port = 3306
        self.user = "root"
        self.passwd = "ZXSSJDY"
        self.db = "admin1"
        self.charset = "utf8"


class Config():
    def __init__(self):
        self.mysql_config = MysqlConfig()


def execute():
    """
    exxcute slq
    :param sql:
    :return:
    """
    config = Config().mysql_config
    print("connect database;")
    cnn = pymysql.connect(host=config.host,
                          port=config.port,
                          user=config.user,
                          passwd=config.passwd,
                          db=config.db,
                          charset=config.charset)
    cursor = cnn.cursor()
    s = cursor.execute("select * from users")
    print(cursor.fetchone())

if __name__ == '__main__':
    execute()