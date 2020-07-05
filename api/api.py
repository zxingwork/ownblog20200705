from flask import Flask, request
from api import tool
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/register', methods=['post'])
def register():
    """
    注册账户
    request format：{username:"",password:"",email:""}
    :param username:
    :param password:
    :param email:
    :return:
    """
    result = {}
    status = 0
    massage = ""
    username = request.get_json()["username"].strip()
    password = request.get_json()["password"].strip()
    email = request.get_json()["email"].strip()
    print(username, password, email)
    try:
        SQL = """INSERT INTO users (NAME,PASSWORD,EMAIL) VALUES ('%s','%s','%s') """ % (username, password, email)
        print(SQL)
        tool.execute(SQL)
        status = 1
        massage = ""
    except Exception as e:
        print(e)
        status = 0
        massage = e
    result["status"] = status
    result["massage"] = massage
    return result


@app.route('/login',methods=['post'])
def login():
    """
    登陆
    request format {username:"",password:""}
    :return:
    """
    username = request.get_json()["username"].strip()
    password = request.get_json()["password"].strip()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9527, debug=True)
