import MySQLdb
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


def execute(sql):
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
    cur = cnn.cursor()
    cur.execute(sql)
    cnn.commit()
    cur.close()
    cnn.close()
    print("close connection;")


if __name__ == '__main__':
    sql = """INSERT INTO users (NAME,PASSWORD) VALUES ('root','root')"""
    execute(sql)