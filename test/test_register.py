import pytest
import pymysql


def mysql():
    con = pymysql.connect(host='120.24.148.131',
                          port=3306,
                          db='admin1',
                          user='root',
                          passwd='ZXSSJDY',
                          charset='utf8')
    return con


@pytest.fixture(scope='function')
def initDatabases():
    print('[before test case][clean table users]')
    clean_table_user_sql = 'truncate table users'
    con = mysql()
    cursor = con.cursor()
    cursor.execute(clean_table_user_sql)

    yield cursor

    print('[after test case][close mysql connect]')
    cursor.close()
    con.close()


class TestRegister:
    @pytest.mark.parametrize('username,password,email', [('zhangxing','zxssjdy', '179@163.com')])
    def test_register(self, username, password, email, initDatabases):
        sql = "insert into users(name,password,email) values ('%s','%s','%s')" % (username, password, email)
        cursor = initDatabases
        print(type(cursor))
        cursor.execute(sql)


if __name__ == '__main__':
    pytest.main()