""" This is a module docstring """
from flask import Flask, request, redirect, url_for
from login import Login
from logging import FileHandler,WARNING

app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    """Handles login routing"""
    user_login = Login()
    if request.method == "POST":
        user = request.json["user"]
        password = request.json["password"]
        if user_login.login(user, password):
            return redirect(url_for("login_success", name=user))
        return redirect(url_for("login_failure", name = user))

@app.route("/register", methods=["POST", "GET"])
def register():
    """Handles register routing"""
    user_login = Login()
    if request.method == "POST":
        username = request.json["username"]
        email = request.json["email"]
        password = request.json["password"]
        phone = request.json["phone"]
        result = user_login.register(username, email, password, phone) 
        if (
            (not username)
            or (not email)
            or (not password)
            or (not phone)
            or (not result)
        ):
            return redirect(url_for("register_failure", name =username))
        return redirect(url_for("register_success", name=username))

# Login and register successful/unsuccessful
@app.route("/login_success/<name>")
def login_success(name: str):
    """Login succesful"""
    return f"welcome {name}"


@app.route("/login_failure/<name>")
def login_failure():
    """Login failure"""
    return "User not found, please try again"


@app.route("/register_success/<name>")
def register_success(name: str):
    """Resgiter successful"""
    return f"Register successful, welcome {name}"


@app.route("/register_failure/<name>")
def register_failure():
    """Register failure"""
    return "Register failed due to incomplete information, please try again"


if __name__ == "__main__":
    app.run(debug=True)
