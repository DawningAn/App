import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        # 接收用户通过POST形式发送来的数据
        print(request.form)
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        more = request.form.get("more")
        # 将用户信息写入文件实现注册、写入到excel实现注册、写入数据库实现注册
        # 给用户返回结果
        return "注册成功"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        print(request.form)
        return "登陆成功"


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
