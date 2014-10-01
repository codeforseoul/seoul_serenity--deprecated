# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
# from flask.ext.login import login_required

blueprint = Blueprint("api", __name__, url_prefix='/api',
                        static_folder="../static")


@blueprint.route("/")
#@login_required
def api_introduce():
    return render_template("api/introduce.html")