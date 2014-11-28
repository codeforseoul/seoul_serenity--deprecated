# -*- coding: utf-8 -*-

'''Admin section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)
from flask.ext.login import login_user, login_required, logout_user
from datetime import datetime, timedelta

from seoul_serenity.extensions import login_manager
from seoul_serenity.project.models import Project
from seoul_serenity.public.forms import LoginForm
from seoul_serenity.user.forms import RegisterForm
from seoul_serenity.utils import flash_errors
from seoul_serenity.database import db

from seoul_serenity.compat import unicode

blueprint = Blueprint('admin', __name__, url_prefix='/admin', static_folder="../static")


@blueprint.route("/")
def index():
  return render_template("admin/index.html")

# TODO 서영태 : Pagination 적용 (MUST)
@blueprint.route("/projects/")
@blueprint.route("/projects/index/")
@blueprint.route("/projects/index/<int:page_num>")
@blueprint.route("/projects/index/<query>")
@blueprint.route("/projects/index/<query>/<int:page_num>")
# @login_required
def projects(page_num=1, query=None):
  # PER_PAGE config 위치 재설정 필요
  PER_PAGE = 2

  if request.args.get('project'):
    param = request.args.get('project')
    return redirect(url_for('admin.projects', query=param))
  else:
    if query == None:
      pagination = Project.query.paginate(page_num, PER_PAGE, False)
    else:
      pagination = Project.query.filter(Project.name.like(unicode('%' + query + '%'))).paginate(page_num, PER_PAGE, False)
  return render_template("admin/projects.html", pagination=pagination, query=query)


@blueprint.route("/view_test")
def view_test():
  return render_template("admin/test.html")
