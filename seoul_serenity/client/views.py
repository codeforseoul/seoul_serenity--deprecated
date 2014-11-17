# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for

# from flask import (Blueprint, request, render_template, flash, url_for,
#                     redirect, session)

from flask.ext.login import login_required, current_user
from seoul_serenity.extensions import login_manager

# from flask.ext.login import login_user, login_required, logout_user, current_user
from seoul_serenity.client.forms import LoginForm

from seoul_serenity.client_committee.models import Client
from seoul_serenity.project.models import Project
from seoul_serenity.user.models import User_project, User

blueprint = Blueprint("client", __name__, url_prefix='/client',
                        static_folder="../static")


# 우선은 페이지 하나 하나로 routing 시킴

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))

@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            # flash("You are logged in.", 'success')
            # redirect_url = request.args.get("next") or url_for("client.view")
            redirect_url = url_for("client.dashboard")
            return redirect(redirect_url)
        else:
        	# return redirect_url(url_for("client.home"))
        	return render_template("client/login.html", form=form)
            # flash_errors(form)
    return render_template("client/login.html", form=form)


@blueprint.route("/")
def dashboard():
    projects = []
    if current_user and current_user.is_authenticated():
        user_projects = User_project.query.filter_by(u_id=current_user.id)
        for user_project in user_projects:
            project = Project.get_by_id(user_project.p_id)
            projects.append(project)
        return render_template("client/home.html", projects=projects)
    return redirect(url_for("client.login"))


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

# @blueprint.route("/login")
# def login():
# 	return render_template("client/committee/login.html")


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