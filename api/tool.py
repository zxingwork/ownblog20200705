import pymysql


class MysqlConfig():
    def __init__(self):
        self.host = "120.24.148.131"
        self.port = 3306
        self.user = "root"
        self.passwd = "ZXSSJDY"
        self.db = "admin1"
        self.charset = "utf8"


class Config:
    def __init__(self):
        self.mysql_config = MysqlConfig()


class Tool:
    def __init__(self):
        self.fetchall = self.fetchone = self.fetchmany = None

    @staticmethod
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
        if 'insert'.upper() in sql.upper():
            cur.execute(sql)
            cnn.commit()
        if 'select'.upper() in sql.upper():
            cur.execute(sql)
            Tool.fetchone = cur.fetchone()
            Tool.fetchall = cur.fetchall()
            Tool.fetchmany = cur.fetchmany()
        cur.close()
        cnn.close()

        print("close connection;")


if __name__ == '__main__':
    pass
