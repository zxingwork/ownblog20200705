from flask import Flask,request,jsonify
from api import tool

server = Flask(__name__)

@server.route('/register',methods=['post'])
def register():
    """
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
        SQL = """INSERT INTO users (NAME,PASSWORD,EMAIL) VALUES ('%s','%s','%s') """ % (username,password,email)
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

if __name__ == '__main__':
    server.run(host='0.0.0.0',port=9527,debug=True)

