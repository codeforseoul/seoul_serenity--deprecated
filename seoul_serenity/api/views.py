# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask import jsonify
# from flask.ext.login import login_required

blueprint = Blueprint("api", __name__, url_prefix='/api',
                        static_folder="../static")


@blueprint.route("/")
#@login_required
def api_introduce():
    return render_template("api/introduce.html")

@blueprint.route("/getPhoneInfoOfMayor", methods=["GET", "POST"]) #@app.route('/users/<userid>', methods = ['GET'])
def getPhoneModelOfMayor(): #def api_users(userid):
	userid = '1'
	users = {'Manufacture':'Apple', 'PhoneNumber':'010-XXXX-XXXX', 'Model':'iPhone5S'}
	#if userid in users:
	#return jsonify({userid:users[userid]})
	return jsonify(users)
	#else:
	#	return not_found()
