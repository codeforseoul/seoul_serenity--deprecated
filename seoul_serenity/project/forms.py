from flask_wtf import Form

from wtforms import TextField, PasswordField
from wtforms.ext.dateutil.fields import DateTimeField

from wtforms.validators import DataRequired, Email, EqualTo, Length

# from .models import User
from .models import Project

class RegisterProjectForm(Form):
	name = TextField('Project', validators=[DataRequired(), Length(min=3)])

	start_date = DateTimeField('Start Date', validators=[DataRequired()])
	end_date = DateTimeField('End Date', validators=[DataRequired()])
	description = TextField('Description', validators=[Length(min=0)])

	## TODO : session id ( users.id )  
	#created_user_id = 

	def __init__(self, *args, **kwargs):
		super(RegisterProjectForm, self).__init__(*args, **kwargs)
        # self.user = None

	def validate(self):
		return True

# class RegisterForm(Form):
#     username = TextField('Username',
#                     validators=[DataRequired(), Length(min=3, max=25)])
#     email = TextField('Email',
#                     validators=[DataRequired(), Email(), Length(min=6, max=40)])
#     password = PasswordField('Password',
#                                 validators=[DataRequired(), Length(min=6, max=40)])
#     confirm = PasswordField('Verify password',
#                 [DataRequired(), EqualTo('password', message='Passwords must match')])

#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.user = None

#     def validate(self):
#         initial_validation = super(RegisterForm, self).validate()
#         if not initial_validation:
#             return False
#         user = User.query.filter_by(username=self.username.data).first()
#         if user:
#             self.username.errors.append("Username already registered")
#             return False
#         user = User.query.filter_by(email=self.email.data).first()
#         if user:
#             self.email.errors.append("Email already registered")
#             return False
#         return True