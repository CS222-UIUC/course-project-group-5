""" This is a module docstring """
import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    """
    This is a function docstring
    """
    return {'time': time.time()}
