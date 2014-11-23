# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

from seoul_serenity.client_mayor.models import Client

blueprint = Blueprint("client_mayor", __name__, url_prefix='/client/mayor',
                        static_folder="../static")


# TODO 서영태 : client_committee, client_mayor 두개를 client로 통합
# 아래코드는 client로 통합 후 추후 삭제


# 우선은 페이지 하나 하나로 routing 시킴

@blueprint.route("/")
def home():
	return render_template("client/mayor/index.html")

@blueprint.route("/view")
def view():
	return render_template("client/mayor/view.html")

@blueprint.route("/write")
def write():
	return render_template("client/mayor/write.html")

@blueprint.route("/list")
def list():
	return render_template("client/mayor/list.html")

@blueprint.route("/login")
def login():
	return render_template("client/mayor/login.html")


# @blueprint.route("/")
# @login_required
# def members():
# 	users = User.query.all()
# 	return render_template("app/members.html", users=users)

# @blueprint.route("/<int:user_id>")
# @login_required
# def member(user_id):
# 	user = User.query.filter_by(id=user_id).first_or_404()
# 	return render_template("users/member.html", username=user.username, email=user.email)