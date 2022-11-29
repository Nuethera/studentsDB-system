import random
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, abort, jsonify
import os
import datetime as dt
import pytz
import pymongo


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
from mydb.db import *
from user import routes

# decorators
def loggedin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged_in']:
            return f(*args, *kwargs)
        else:
            print('Log in please')
            return redirect(url_for('login_portal'))

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
    students = list(class2.find())
    return render_template('index1.html')


@app.route('/login/')
def login_portal():
    return render_template('login.html')


@app.route('/class/<sec>/')
def show_class(sec):
    students = list(class2.find({'branch':sec}))
    return render_template('class.html', students=students[:50], sec=sec, title=f"{sec} Class")


@app.route('/student/<roll>/')
def show_student(roll):
    student = (class2.find_one({'roll_no': int(roll)}))
    return render_template('student.html', student=student)


if __name__ == '__main__':
    app.run()
