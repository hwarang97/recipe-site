from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


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
