# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import login_required

# from seoul_serenity.user.models import User, User_project
# from seoul_serenity.project.models import Project

blueprint = Blueprint("storyboard", __name__, url_prefix='/storyboard',
                        static_folder="../static")


@blueprint.route("/")
def home():
	# users = User.query.all()
	return render_template("storyboard/home.html")

# @blueprint.route("/<int:user_id>")
# def member(user_id):
# 	user = User.query.filter_by(id=user_id).first_or_404()
# 	projects = []
# 	user_projects = User_project.query.filter_by(u_id=user.id)
# 	for user_project in user_projects:
# 		project = Project.get_by_id(user_project.p_id)
# 		projects.append(project)
# 	return render_template("users/member.html", user=user, projects=projects)

