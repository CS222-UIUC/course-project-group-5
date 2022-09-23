""" This is a module docstring """
from flask import Flask, request, redirect, url_for
from login import Login

app = Flask(__name__)

# Login
@app.route('/login', methods = ['POST', 'GET'])
def login():
    login = Login()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if login.login(username, email, password):
            return redirect(url_for('success', name = username))
        else:
            return redirect(url_for('failure', name = username))
    else:
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        if login.login(username, email, password):
            return redirect(url_for('login_success', name = username))
        else:
            return redirect(url_for('login_failure', name = username))

# Register
@app.route('/register', methods = ['POST', 'GET'])
def register():
    login = Login()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        result = login.register(username, email, password, phone)
        if (not username) or (not email) or (not password) or (not phone):
            return redirect(url_for('register_failure', name = username))
        else:
            return redirect(url_for('register_success', name = username))
    else:
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        phone = request.args.get('phone')
        result = login.register(username, email, password, phone)
        if (not username) or (not email) or (not password) or (not phone):
            return redirect(url_for('register_failure', name = username))
        else:
            return redirect(url_for('register_success', name = username))
# Login and register successful/unsuccessful
@app.route('/login_success/<name>')
def login_success(name: str):
    return 'welcome %name' % name

@app.route('/login_failure/<name>')
def login_failure(name: str):
    return 'User not found, please try again'

@app.route('/register_success/<name>')
def register_success(name: str):
    return 'Register successful, welcome %name' % name

@app.route('/register_failure/<name>')
def login_failure(name: str):
    return 'Register failed due to incomplete information, please try again'

if __name__ == '__main__':
   app.run()
