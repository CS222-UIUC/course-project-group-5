import time
from flask import Flask, request, redirect, url_for
from login import Login

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


# Login
@app.route('/login', methods = ['POST', 'GET'])
def login():
    login = Login()
    if request.method == 'POST':
        user_name = request.form['name']
        user_password = request.form['password']
        return redirect(url_for('success', name = user_name))
    else:
        user_name = request.args.get('name')
        return redirect(url_for('success', name = user_name))

# Login successful
@app.route('/success/<name>')
def login_success(name: str):
    return 'welcome %name' % name

if __name__ == '__main__':
   app.run()