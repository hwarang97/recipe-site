from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/recipe", methods=["GET"])
def recipe():
    return render_template("recipe.html")


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/mypage", methods=["GET"])
def mypage():
    return render_template("mypage.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
