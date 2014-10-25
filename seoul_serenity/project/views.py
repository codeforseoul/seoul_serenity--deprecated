# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.ext.login import login_required

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



@blueprint.route("/")
@login_required
def projects():
    projects = Project.query.all()
    return render_template("projects/projects.html", projects=projects)

@blueprint.route("/add")
@login_required
def add():
	project = Project.create(name="Hello")
	# db.session.add(project)
	# db.session.commit()
	return render_template("projects/add.html")

@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterProjectForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_project = Project.create(name=form.name.data)
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
	project = Project.query.filter_by(id=project_id).first_or_404()
	return render_template("projects/project.html", project=project)

