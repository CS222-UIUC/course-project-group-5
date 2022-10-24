""" This is a module docstring """
from flask import Flask, request
from flask_cors import CORS
from apt import ObjectSchema
from apt import Apt
from mainpage import MainPage
from login import Login

# from logging import FileHandler, WARNING

app = Flask(__name__)

CORS(app)

@app.route("/login", methods=["POST", "GET"])
def login():
    """Handles login routing"""
    user_login = Login()
    user = request.json["user"]
    password = request.json["password"]
    if user_login.login(user, password):
        return f"welcome {user}", 200
    return "User not found, please try again", 404


@app.route("/register", methods=["POST", "GET"])
def register():
    """Handles register routing"""
    user_login = Login()
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]
    phone = request.json["phone"]
    result = user_login.register(username, email, password, phone)
    if not result.status:
        return result.message, 400
    return result.message, 200

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    """Takes in query string returns json of apartments"""
    mainpage = MainPage()
    query = request.json["q"]
    selected = request.json["selected"]
    if not query:
        return "Empty query", 400
    apts = mainpage.search_apartments(query)
    apt_schema = ObjectSchema()
    example = [Apt(1, "smile", "street", 0, 3, 1)]
    print(type(example), example)
    json_string = apt_schema.dumps(example, many=True)
    print(json_string)
    #pics = mainpage.get_apartments_pictures(len(apts))
    if not selected:
        apts = mainpage.apartments_default(len(apts))
        return "success", 200
    if ("low-high" in selected and "most popular" in selected) or (
        "low-high" in selected and "high-low" in selected and
        "most popular" in selected): # if both prices pressed it will sort low-high
        apts = mainpage.apartments_sorted(len(apts), -1, -1)
    elif "high-low" in selected and "most popular" in selected:
        apts = mainpage.apartments_sorted(len(apts), 1, -1)
    elif "most popular" in selected:
        apts = mainpage.apartments_sorted(len(apts), 1, 0)
    elif "low-high" in selected: # if both prices pressed it will sort low-high
        apts = mainpage.apartments_sorted(len(apts), -1, 0)
    elif "high-low" in selected:
        apts = mainpage.apartments_sorted(len(apts), 1, 0)
    return "success", 200


# The routes below are not implemented yet
# They are there as placeholders

# @app.route("/login_success/<name>")
# def login_success(name: str):
#    """Login succesful"""
#    return f"welcome {name}"


# @app.route("/login_failure/<name>")
# def login_failure():
#    """Login failure"""
#    return "User not found, please try again"


# @app.route("/register_success/<name>")
# def register_success(name: str):
#    """Resgiter successful"""
#    return f"Register successful, welcome {name}"


# @app.route("/register_failure/<name>")
# def register_failure():
#    """Register failure"""
#    return "Register failed due to incomplete information, please try again"


if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
