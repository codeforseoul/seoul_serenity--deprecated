# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

from seoul_serenity.user.models import User, User_project
from seoul_serenity.project.models import Project

blueprint = Blueprint("user", __name__, url_prefix='/users',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
	users = User.query.all()
	return render_template("users/members.html", users=users)

@blueprint.route("/<int:user_id>")
@login_required
def member(user_id):
	user = User.query.filter_by(id=user_id).first_or_404()
	return render_template("users/member.html", user=user, username=user.username, email=user.email)

@blueprint.route("/assign/<int:user_id>")
def assign(user_id):
	projects = Project.query.all()
	return render_template("users/assign.html", projects=projects, user_id=user_id)

@blueprint.route("/<int:user_id>/assign/<int:project_id>", methods=['GET', 'POST'])
def assigned(user_id, project_id):
	find_assign = User_project.query.filter_by(u_id=user_id, p_id=project_id).first()
	if find_assign is None:
		new_assign = User_project.create(u_id=user_id, p_id=project_id)
		
		users = User.query.all()
		return render_template("users/members.html", users=users)
	else:
		users = User.query.all()
		return render_template("users/members.html", users=users)
