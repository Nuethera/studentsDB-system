import random
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, abort, jsonify
import os
import datetime as dt
import pytz
import pymongo
from mydb.db import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


# decorators
def loggedin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged_in']:
            return f(*args, *kwargs)
        else:
            print('Log in please')
            return redirect('/')

    return wrap


def admin_only(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged_in']:
            if session['user']['admin']:
                return f(*args, *kwargs)
            else:
                return abort(403)
        else:
            print('Log in please')
            return redirect('/')

    return wrap


@app.route('/')
def hello_world():
    students = list(class1.find())
    return render_template('index.html', students=students[:50])


if __name__ == '__main__':
    app.run()
