# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

from seoul_serenity.client_committee.models import Client

blueprint = Blueprint("client_committee", __name__, url_prefix='/client/committee',
                        static_folder="../static")


# 우선은 페이지 하나 하나로 routing 시킴

@blueprint.route("/")
def home():
	return render_template("client/committee/index.html")

@blueprint.route("/view")
def view():
	return render_template("client/committee/view.html")

@blueprint.route("/write")
def write():
	return render_template("client/committee/write.html")

@blueprint.route("/list")
def list():
	return render_template("client/committee/list.html")

@blueprint.route("/login")
def login():
	return render_template("client/committee/login.html")


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