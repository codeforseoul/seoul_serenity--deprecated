# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask import jsonify
# from flask.ext.login import login_required

blueprint = Blueprint("api", __name__, url_prefix='/api',
                        static_folder="../static")

# TODO : api 부분만 따로 모듈로 분리할지, 모듈별로 views.py에 상응하는 apis.py 를 추가할지 등등
# 추후에 정리. 일단 모바일웹 파트가 정리된 이후에 API 개발 시작 (서영태)

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
