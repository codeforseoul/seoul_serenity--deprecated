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
from seoul_serenity.user.models import User
from seoul_serenity.utils import flash_errors
from seoul_serenity.database import db

from seoul_serenity.compat import unicode

blueprint = Blueprint('admin', __name__, url_prefix='/admin', static_folder="../static")


@blueprint.route("/")
def index():
  return render_template("admin/index.html")

# TODO 서영태 : Pagination 적용 (MUST)
#  TODO : Crate button to remove search result
@blueprint.route("/projects/")
# @login_required
def projects():
  # TODO : add Try Catch
  # TODO : add button(or dropbox) for items_per_page
  page_num = request.args.get('page_num',default=1, type=int)
  query = request.args.get('search_text')
  items_per_page = request.args.get('per_page',default=10, type=int)

  # yoseo : temporary removed
  # if request.args.get('project'):
  #   param = request.args.get('project')
  #   return redirect(url_for('admin.projects', query=param))
  # else:
  if query == None:
    pagination = Project.query.paginate(page_num, items_per_page, False)
  else:
    pagination = Project.query.filter(Project.name.like(unicode('%' + query + '%'))).paginate(page_num, items_per_page, False)
  return render_template("admin/projects.html", pagination=pagination, query=query)


# TODO 서영태 : Pagination 적용 (MUST)
#  TODO : Crate button to remove search result
@blueprint.route("/users/")
# @login_required
def users():
  # TODO : add Try Catch
  # TODO : add button(or dropbox) for items_per_page
  page_num = request.args.get('page_num',default=1, type=int)
  query = request.args.get('search_text')
  items_per_page = request.args.get('per_page',default=10, type=int)

  # yoseo : temporary removed
  # if request.args.get('project'):
  #   param = request.args.get('project')
  #   return redirect(url_for('admin.projects', query=param))
  # else:
  if query == None:
    pagination = User.query.paginate(page_num, items_per_page, False)
  else:
    pagination = User.query.filter(User.name.like(unicode('%' + query + '%'))).paginate(page_num, items_per_page, False)
  return render_template("admin/users.html", pagination=pagination, query=query)



# Test page for layout
@blueprint.route("/view_test")
def view_test():
  return render_template("admin/test.html")
