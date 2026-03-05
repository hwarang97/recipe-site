from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import make_response
from pymongo import MongoClient
import jwt

import os
from dotenv import load_dotenv

app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client.jungle

load_dotenv()
secret = os.getenv("SECRET")


@app.route("/", methods=["GET"])
def home():
    jwt = request.cookies.get("token")
    if jwt:  # 추후 무결성 검사
        print("have token")
        is_login = True
    else:
        print("no token")
        is_login = False
    return render_template("index.html", is_login=is_login)


@app.route("/recipe", methods=["GET"])
def recipe():
    return render_template("recipe.html")
    # TODO: DB에서 데이터를 가져와, 파라미터로 넘겨주면 됩니다. DB 만들고 나서 주석부분 진행해보세요.
    # return render_template("recipe.html", title=title, content=content, logo_location=logo_location, image_location=image_location)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")
    # TODO
    # return return render_template("login.html", logo_location=logo_location)


@app.route("/login", methods=["POST"])
def authenticate():
    id = request.form.get("id")
    password = request.form.get("password")
    stored_user = db.users.find_one({"id": f"{id}"})
    if stored_user and stored_user["password"] == password:
        payload = {"user_id": id, "iss": "whatdoieattoday"}
        token = jwt.encode(payload, secret, algorithm="HS256")
        response = make_response(jsonify({"result": "success"}))
        response.set_cookie("token", token, httponly=True, max_age=60)
        return response
    else:
        return jsonify({"result": "fail"})


@app.route("/mypage", methods=["GET"])
def mypage():
    return render_template("mypage.html")
    # TODO
    # return render_template("mypage.html", logo_location=logo_location, name=name, contents=contents)


@app.route("/find", methods=["GET"])
def find():
    return render_template("find.html")
    # TODO
    # return render_template("find.html", logo_location=logo_location)


@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")
    # TODO
    # return render_template("signin.html", logo_location=logo_location)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
