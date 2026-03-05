from pymongo import MongoClient
from flask import Flask
from flask import render_template

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.db_food

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/recipe", methods=["GET"])
def recipe():
    # return render_template("recipe.html")
    food = db.recipe.find_one({"title": "김치볶음밥"})
    title = food["title"]
    content = food["content"]
    logo_location = "static/logo.png"
    image_location  = food["image"]
    return render_template("recipe.html", title=title, content=content, logo_location=logo_location, image_location=image_location) # "static/logo.jpg"


@app.route("/login", methods=["GET"])
def login():
    # return render_template("login.html")
    # TODO
    food = db.recipe.find_one({"title": "김치볶음밥"})
    logo_location = "static/logo.png"
    return render_template("login.html", logo_location=logo_location)


@app.route("/mypage", methods=["GET"])
def mypage():
    #return render_template("mypage.html")
    # TODO
    food = db.recipe.find_one({"title": "김치볶음밥"})
    logo_location = "static/logo.png"
    content = food["content"]
    name = food["id"]
    return render_template("mypage.html", logo_location=logo_location, name=name, content=content)


@app.route("/find", methods=["GET"])
def find():
    #return render_template("find.html")
    # TODO
    food = db.recipe.find_one({"title": "김치볶음밥"})
    logo_location = "static/logo.png"
    return render_template("find.html", logo_location=logo_location)


@app.route("/signin", methods=["GET"])
def signin():
    #return render_template("signin.html")
    # TODO
    food = db.recipe.find_one({"title": "김치볶음밥"})
    logo_location = "static/logo.png"
    return render_template("signin.html", logo_location=logo_location)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
