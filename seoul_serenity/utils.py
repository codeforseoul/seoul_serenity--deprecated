# -*- coding: utf-8 -*-
'''Helper utilities and decorators.'''
from flask import flash
from functools import wraps
# from flask.ext.login import login_user, login_required, logout_user, current_user
from flask.ext.login import login_required, current_user

# from flask import (_request_ctx_stack, abort, current_app, flash, redirect,
#                    request, session, url_for, has_request_context)

def flash_errors(form, category="warning"):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                    .format(getattr(form, field).label.text, error), category)


# @login_required
def admin_required(func):
	@wraps(func)
	def decorated_view(*args, **kwargs):
		if current_user.get_id() == 1 :
			return func(*args, **kwargs)
		# return current_app.login_manager.unauthorized()
		return 'testing'
	return decorated_view
