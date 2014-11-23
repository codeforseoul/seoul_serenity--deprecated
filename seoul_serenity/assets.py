# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle, Environment

# TODO : sbadmin2 적용 (서영태)
# TODO : 기본 템플릿용 리소스와 권기택님이 추가한 리소스 구분해서 정리 (서영태)
# 중복된 파일도 있을 것으로 판단되고 권기택님 리소스도 아래와 같이 번들로 묶을 것

css = Bundle(
    "libs/bootstrap/dist/css/bootstrap.css",
    "css/style.css",
    filters="cssmin",
    output="public/css/common.css"
)

js = Bundle(
    "libs/jQuery/dist/jquery.js",
    "libs/bootstrap/dist/js/bootstrap.js",
    "js/plugins.js",
    filters='jsmin',
    output="public/js/common.js"
)

assets = Environment()

assets.register("js_all", js)
assets.register("css_all", css)