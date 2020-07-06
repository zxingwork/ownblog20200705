from flask import Flask
from flask import request
from flask_cors import *
import pymysql

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/register', ['post'])
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
    email = request.get_json()['email']

    # connect the mysql
    con = pymysql.connect(host='120.24.148.131',
                          port=3306,
                          db='admin1',
                          user='root',
                          passwd='ZXSSJDY',
                          charset='utf8')
    cursor = con.cursor()

    if username is not None and password is not None:
        SQL = 'insert into %s (name,password,email) values (%s,%s,%s)' % (user_table, username, password, email)
        try:
            cursor.execute(SQL)
            con.commit()
            cursor.close()
            con.close()
            massage = '注册成功'
            status = '0'
        except Exception as e:
            print(e)
            massage = '注册失败'
            status = '4'
    else:
        status = '5'

