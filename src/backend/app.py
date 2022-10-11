""" This is a module docstring """
from flask import Flask, request
from login import Login, RegisterResult

# from logging import FileHandler, WARNING

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    """Handles login routing"""
    user_login = Login()
    user = request.json["user"]
    password = request.json["password"]
    if user_login.login(user, password):
        return f"welcome {user}", 200
    return "User not found, please try again", 404


@app.route("/register", methods=["POST"])
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
    app.run(debug=True)
