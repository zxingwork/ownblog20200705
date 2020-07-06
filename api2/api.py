from flask import Flask
from flask import request
from flask_cors import *
import pymysql
try: from api2.common import *
except: from common import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/register', methods=['post'])
def register():
    """
    register a new user
    :param: json{username:"", password:""}
    :return: json{massage:"", status:""}
    """
    # return fields init
    result = {}
    massage = ''
    status = ''

    #table massage
    user_table = 'users'

    # get password and password from http request;
    username = request.get_json()['username']
    password = request.get_json()['password']

    # email is not requisite
    try:
        email = request.get_json()['email']
    except:
        email = ""

    # connect the mysql
    con = pymysql.connect(host='120.24.148.131',
                          port=3306,
                          db='admin1',
                          user='root',
                          passwd='ZXSSJDY',
                          charset='utf8')
    cursor = con.cursor()

    # insert register user to database
    if username is not None and password is not None:
        SQL = "insert into %s (name,password,email) values ('%s','%s','%s')" % (user_table, username, password, email)
        try:
            cursor.execute(SQL)
            con.commit()
            massage = '注册成功'
            status = Status.success.value
        except Exception as e:
            print(e)
            massage = '注册失败'
            status = Status.mysqlError.value
        finally:
            cursor.close()
            con.close()
    else:
        massage = '注册失败'
        status = Status.emptyError.value

    # return
    result['massage'] = massage
    result['status'] = status
    print(massage, status)
    return result


@app.route('/login', methods=['post'])
def login():
    """
    login by {username, password}
    :return:
    """
    # return massage
    result = {}
    status = ''
    massage = ''

    # table massage
    user_table = 'users'

    # receive login massage
    username = request.get_json()['username']
    password = request.get_json()['password']

    # search record in database
    if username is not None and password is not None:
        try:
            SQl = "select * from %s where name='%s' and password='%s'" % (user_table, username, password)
            con = Mysql.connect()
            cursor = con.cursor()
            cursor.execute(SQl)
            status = Status.success.value
            massage = '登陆成功'
            print('登陆成功')
        except Exception as e:
            status = Status.mysqlError.value
            massage = '登陆失败'
            print('登陆失败', e)
    else:
        status = Status.emptyError.value
        massage = '登陆失败'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9527, debug=True)
