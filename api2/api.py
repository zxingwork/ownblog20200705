from flask import Flask
from flask import request
from flask_cors import *
import pymysql
try: from api2.common import Status
except: from common import Status

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
        SQL = 'insert into %s (name,password,email) values (%s,%s,%s)' % (user_table, username, password, email)
        try:
            cursor.execute(SQL)
            con.commit()
            cursor.close()
            con.close()
            massage = '注册成功'
            status = Status.success
        except Exception as e:
            print(e)
            massage = '注册失败'
            status = Status.mysqlError
    else:
        massage = '注册失败'
        status = Status.emptyError

    # return
    result['massage'] = massage
    result['status'] = status
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9527, debug=True)
