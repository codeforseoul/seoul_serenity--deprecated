# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask.ext.login import login_required
from flask.ext.login import login_user, login_required, logout_user, current_user
from seoul_serenity.utils import admin_required
from .models import Project
from .forms import RegisterProjectForm
from seoul_serenity.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

blueprint = Blueprint("project", __name__, url_prefix='/projects',
                        static_folder="../static")


# / (GET) : Project List Page
# / (POST) : Project ADD
# /<PID> (GET) : 특정 프로젝트 정보
# /<PID> (POST) : 특정 프로젝트 정보 입력

@blueprint.route("/test")
# @login_required
def ttt():
    if current_user == None:
        return current_user.username
    else:
        return "....."

@blueprint.route("/")
@login_required
def projects():
    projects = Project.query.all()
    return render_template("projects/projects.html", projects=projects)

# @blueprint.route("/add")
# @login_required
# def add():
# 	project = Project.create(name="Hello")
# 	# db.session.add(project)
# 	# db.session.commit()
# 	return render_template("projects/add.html")

@blueprint.route("/test")
@admin_required
def testing():
    return "testing"

@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterProjectForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_project = Project.create(name=form.name.data
            ,start_date=form.start_date.data
            ,end_date=form.end_date.data
            ,description=form.description.data)
                        # active=True)
        flash("새 프로젝트가 생성되었습니다.", 'success')
        return redirect(url_for('project.detail', project_id=new_project.id))
    # else:

    #     flash_errors(form)
    return render_template('projects/project_register.html', form=form)


@blueprint.route("/detail/<int:project_id>")
@login_required
def detail(project_id):
	# project =  Project("헬로우")
	project = Project.get_by_id(project_id)
	return render_template("projects/project.html", project=project)

@blueprint.route("/close/<int:project_id>")
@login_required
def close(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    if project != None :
        project.display_yn = False
        #project.update(self, True, project)

    return redirect('projects')

