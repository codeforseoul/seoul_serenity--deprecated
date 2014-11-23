# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required, current_user
# from flask.ext.login import login_user, login_required, logout_user, current_user

from seoul_serenity.client_committee.models import Client
from seoul_serenity.project.models import Project
from seoul_serenity.user.models import User_project, User

blueprint = Blueprint("client_committee", __name__, url_prefix='/client/committee',
                        static_folder="../static")


# TODO : client_committee, client_mayor 두개를 client로 통합
# 아래코드는 client로 통합 후 추후 삭제


# 우선은 페이지 하나 하나로 routing 시킴

@blueprint.route("/")
def home():
	projects = []
# TODO : replace u_id=1 to current_user 
	# if current_user and current_user.is_authenticated():
	user_projects = User_project.query.filter_by(u_id=1)
	for user_project in user_projects:
		project = Project.get_by_id(user_project.p_id)
		projects.append(project)
	return render_template("client/committee/index.html", projects=projects)

# @blueprint.route("/view")
@blueprint.route("/view/<int:project_id>")
def view(project_id):
	project = Project.query.filter_by(id=project_id).first_or_404()	
	return render_template("client/committee/view.html", project=project)

# @blueprint.route("/write")
@blueprint.route("/write/<int:project_id>")
def write(project_id):
	project = Project.query.filter_by(id=project_id).first_or_404()
	return render_template("client/committee/write.html", project=project)

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