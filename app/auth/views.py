# -*-coding:utf-8 -*-
from . import auth
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from flask import redirect, render_template,request


@auth.route(r'/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('auth.login')
    return render_template('register.html', title='注册', form=form)


@auth.route(r'/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('index.html', title='首页')
