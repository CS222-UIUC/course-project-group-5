""" This is a module docstring """
from flask import Flask, request, redirect, url_for
from login import Login

app = Flask(__name__)

# Login
@app.route('/login', methods = ['POST', 'GET'])
def login():
    '''Handles login routing'''
    user_login = Login()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if user_login.login(username, password) or user_login.login(email, password):
            return redirect(url_for('login_success', name = username))
        return redirect(url_for('login_failure'))

    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    if user_login.login(username, password) or user_login.login(email, password):
        return redirect(url_for('login_success', name = username))
    return redirect(url_for('login_failure'))

# Register
@app.route('/register', methods = ['POST', 'GET'])
def register():
    '''Handles register routing'''
    user_login = Login()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        result = user_login.register(username, email, password, phone)
        if (not username) or (not email) or (not password) or (not phone) or (not result):
            return redirect(url_for('register_failure'))
        return redirect(url_for('register_success', name = username))

    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    phone = request.args.get('phone')
    result = user_login.register(username, email, password, phone)
    if (not username) or (not email) or (not password) or (not phone) or (not result):
        return redirect(url_for('register_failure'))
    return redirect(url_for('register_success', name = username))
# Login and register successful/unsuccessful
@app.route('/login_success/<name>')
def login_success(name: str):
    '''Login succesful'''
    return f"welcome {name}"

@app.route('/login_failure/<name>')
def login_failure():
    '''Login failure'''
    return 'User not found, please try again'

@app.route('/register_success/<name>')
def register_success(name: str):
    '''Resgiter successful'''
    return f"Register successful, welcome {name}"

@app.route('/register_failure/<name>')
def register_failure():
    '''Register failure'''
    return 'Register failed due to incomplete information, please try again'

if __name__ == '__main__':
    app.run()
