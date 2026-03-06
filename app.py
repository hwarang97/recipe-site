from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import make_response
from pymongo import MongoClient
from auth import is_login
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
    return render_template("index.html", is_login=is_login(request, secret))


@app.route("/recipe", methods=["GET"])
def recipe():
    food = db.recipe.find_one({"title": "백종원 스타일 김치볶음밥"})
    title = food["title"]
    content = food["content"]
    image_location = food["image"]
    return render_template(
        "recipe.html",
        is_login=is_login(request, secret),
        title=title,
        content=content,
        image_location=image_location,
    )


@app.route("/login", methods=["GET"])
def login():
    food = db.recipe.find_one({"title": "백종원 스타일 김치볶음밥"})
    return render_template("login.html", is_login=is_login(request, secret))


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
    food = db.recipe.find_one({"title": "백종원 스타일 김치볶음밥"})
    title = food["title"]
    content = food["content"]
    return render_template(
        "mypage.html",
        is_login=is_login(request, secret),
        name="",
        contents=content,
    )


@app.route("/find", methods=["GET"])
def find():
    return render_template("find.html", is_login=is_login(request, secret))


@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html", is_login=is_login(request, secret))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
