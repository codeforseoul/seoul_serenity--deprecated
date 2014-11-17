# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)
from flask.ext.login import login_user, login_required, logout_user
from datetime import datetime, timedelta

from seoul_serenity.extensions import login_manager
from seoul_serenity.user.models import User, User_project
from seoul_serenity.public.forms import LoginForm
from seoul_serenity.user.forms import RegisterForm
from seoul_serenity.utils import flash_errors
from seoul_serenity.database import db

from seoul_serenity.project.models import Project


blueprint = Blueprint('public', __name__, static_folder="../static")

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


# Admin, Mayor, Committee
@blueprint.route("/index")
def index():
    return render_template("public/index.html")

@blueprint.route("/put-dummy-data")
def putTestData():
    User.query.delete()
    Project.query.delete()
    User_project.query.delete()
    User.create(username="admin",email="admin@test.com",password="123456",name="관리자",active=True)
    User.create(username="wonsoon",email="wonsoon@test.com",password="123456",name="박원순",active=True)
    User.create(username="test1",email="comm1@test.com",password="123456",name="홍길동",active=True)
    User.create(username="test2",email="comm2@test.com",password="123456",name="차태현",active=True)
    User.create(username="test3",email="comm3@test.com",password="123456",name="이순신",active=True)
    Project.create(name=u"어린이집늘리기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"어린이집을 늘려야 하거든요")
    Project.create(name=u"경로당늘리기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"경로당을 늘려야 하거든요")
    Project.create(name=u"카페늘리기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"카페를 늘려야 하거든요")
    User_project.create(u_id=1, p_id=1)
    User_project.create(u_id=2, p_id=1)
    User_project.create(u_id=3, p_id=1)
    User_project.create(u_id=1, p_id=2)
    User_project.create(u_id=2, p_id=2)
    User_project.create(u_id=3, p_id=2)
    User_project.create(u_id=1, p_id=3)
    User_project.create(u_id=2, p_id=3)
    User_project.create(u_id=3, p_id=3)
    return "SUCCESS"

@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)

@blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))

@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User.create(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        first_name=form.name.data,
                        last_name=form.familyname.data,
                        active=True)
        # new_user.update(commit=True, first_name=form.name.data, last_name=form.familyname.data)
        flash("Thank you for registering. You can now log in.", 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)

@blueprint.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)