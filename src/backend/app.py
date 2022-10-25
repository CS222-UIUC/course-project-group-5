""" This is a module docstring """
from flask import Flask, request
from flask_cors import CORS
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

if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
