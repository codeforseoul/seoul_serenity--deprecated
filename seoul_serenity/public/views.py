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

# TODO 서영태 : 관리자 기능에 해당되는 부분들은 /admin 으로 routing 하도록 수정하는게 어떤지..

# Admin, Mayor, Committee
@blueprint.route("/index")
def index():
    return render_template("public/index.html")

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
                        firstname=form.firstname.data,
                        lastname=form.lastname.data,
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

# TODO 서영태 : 시뮬레이션을 위한 테스트 데이터 관련 부분은 별도 모듈로 이동
@blueprint.route("/test")
def testData():
    User.query.delete()
    Project.query.delete()
    User_project.query.delete()
    User.create(username="admin",email="admin@test.com",password="123456",firstname=u"리자",lastname=u"관",active=True)
    User.create(username="wonsoon",email="wonsoon@test.com",password="123456",firstname=u"원순",lastname=u"박",active=True)
    User.create(username="test1",email="comm1@test.com",password="123456",firstname=u"길동",lastname=u"홍",active=True)
    User.create(username="test2",email="comm2@test.com",password="123456",firstname=u"태현",lastname=u"차",active=True)
    User.create(username="test3",email="comm3@test.com",password="123456",firstname=u"순신",lastname=u"이",active=True)
    Project.create(name=u"어린이집늘리기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"어린이집을 늘려야 하거든요")
    Project.create(name=u"경로당늘리기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"경로당을 늘려야 하거든요")
    Project.create(name=u"카페늘리기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"카페를 늘려야 하거든요")
    Project.create(name=u"고양이 밥주기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"강아지 밥주기",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"주차장 오천개 확보 사업",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"박원순 생일 파티",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"서영태 생일 파티",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"홍대 길거리 청소 프로젝트",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"태양열 전지 확보 사업",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"청계천 정화 사업",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"2014년 크리스마스 비밀 파티",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    Project.create(name=u"2015년 신년회 프로젝트",start_date=datetime.now(),end_date=(datetime.now()+timedelta(days=7)),description=u"ㅇㅇㅇㅇ")
    User_project.create(u_id=1, p_id=1)
    User_project.create(u_id=2, p_id=1)
    User_project.create(u_id=3, p_id=1)
    User_project.create(u_id=1, p_id=2)
    User_project.create(u_id=2, p_id=2)
    User_project.create(u_id=3, p_id=2)
    User_project.create(u_id=1, p_id=3)
    User_project.create(u_id=2, p_id=3)
    User_project.create(u_id=3, p_id=3)
    flash("테스트 데이터가 생성되었습니다. ID : admin PW: 123456 ", 'success')
    return redirect(url_for('public.home'))
