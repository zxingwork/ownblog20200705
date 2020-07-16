from flask import Flask
from flask import request
from flask_cors import *

import time

try:
    from api2.Logger import Logger
    from api2.common import *
except:
    from Logger import *
    from common import *

log = Logger('app.log', level='debug')

app = Flask(__name__)
CORS(app, supports_credentials=True)


# @seq
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

    # table massage
    user_table = 'users'

    # get password and password from http request;
    request_data = request.get_json()
    log.logger.debug(f'request:{request_data}')
    username = request.get_json()['username']
    password = request.get_json()['password']

    # email is not requisite
    try:
        email = request.get_json()['email']
    except:
        email = ""

    # insert register user to database
    if username is not None and password is not None:
        SQL = "insert into %s (name,password,email) values ('%s','%s','%s')" % (user_table, username, password, email)
        try:
            # connect the mysql
            start_time = time.time()
            con = Mysql().connect()
            cursor = con.cursor()
            cursor.execute(SQL)
            con.commit()
            massage = '注册成功'
            status = Status.success.value
        except Exception as e:
            log.logger.error(e)
            massage = '注册失败'
            status = Status.mysqlError.value
        finally:
            cursor.close()
            con.close()
            end_time = time.time()
            log.logger.debug(f'Mysql execute sql:"{SQL}", cost time:{end_time - start_time}s')

    else:
        massage = '注册失败'
        status = Status.emptyError.value

    # return
    result['massage'] = massage
    result['status'] = status
    log.logger.debug(f'return:{result}')
    return result


# @seq
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
    request_data = request.get_json()
    log.logger.debug(f'request:{request_data}')
    username = request.get_json()['username']
    password = request.get_json()['password']

    # search record in database
    if username is not None and password is not None:
        SQl = f"select * from {user_table} where name='{username}' and password='{password}'"
        log.logger.debug(SQl)
        try:
            start_time = time.time()
            con = Mysql().connect()
            cursor = con.cursor()
            cursor.execute(SQl)
            status = Status.success.value
            massage = '登陆成功'
            log.logger.debug(massage)
        except Exception as e:
            status = Status.mysqlError.value
            massage = '登陆失败'
            log.logger.error(massage + e)
        finally:
            cursor.close()
            con.close()
            end_time = time.time()
            log.logger.debug(f'Mysql execute sql:"{SQl}", cost time:{end_time - start_time}s')

    else:
        status = Status.emptyError.value
        massage = '登陆失败'

    result['status'] = status
    result['massage'] = massage
    log.logger.debug(f'return:{result}')
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9527, debug=True)
