from enum import Enum
from enum import unique
import pymysql


@unique
class Status(Enum):
    success = '0000'
    emptyError = '0001'
    mysqlError = '0003'


class Mysql:
    ALiyun_host = '120.24.148.131'
    TencentYun_host = '106.55.33.244'
    ALiyun_passwd = "ZXSSJDY"
    TencentYun_passwd = "zxssjdy111899"

    def __init__(self,
                 host=TencentYun_host,
                 port=3306,
                 db='admin1',
                 user='root',
                 passwd= TencentYun_passwd,
                 charset='utf8'):
        self.__host = host
        self.__port = port
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        self.charset = charset
        pass

    def connect(self):
        con = pymysql.connect(host=self.__host,
                              port=self.__port,
                              db=self.__db,
                              user=self.__user,
                              passwd=self.__passwd,
                              charset=self.charset)
        return con
