# -*- coding: utf-8 -*-

# set default encoding from ascii to utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

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
@blueprint.route("/projects")
# @login_required
def projects():
	projects = Project.query.all()
	return render_template("admin/projects.html", projects=projects)


@blueprint.route("/view_test")
def view_test():
	return render_template("admin/test.html")
