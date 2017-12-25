# -*- coding=utf-8 -*-
from . import main
from flask import render_template, flash, redirect, url_for, request, session, make_response
from flask_login import login_required, current_user, login_user, logout_user
from forms import LoginForm, Answer, RegistrationForm
from ..models import Marks_record, User, Question
from .. import db
from functools import wraps
import sys
import random
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')


def admin_required(func):
    @wraps(func)
    def admin(*args, **kwargs):
        per = User.query.filter_by(username=session.get('name')).first()

        if per.permission == 0:
            return func(*args, **kwargs)
        else:
            flash(u'你不是管理员')
            return redirect(url_for('main.index'))

    return admin


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'小e提示：仔细看看自己是否输入正确的学号与密码！')

    return render_template('main/login.html', form=form)


@main.route('/next1', methods=['GET', 'POST'])
def next1():
    return render_template('main/next1.html')


@main.route('/next2', methods=['GET', 'POST'])
def next2():
    return render_template('main/next2.html')



