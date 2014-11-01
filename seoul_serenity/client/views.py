# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

from seoul_serenity.client.models import Client

blueprint = Blueprint("client", __name__, url_prefix='/client',
                        static_folder="../static")


@blueprint.route("/")
def home():
	return render_template("client/login.html")

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