# -*- coding: utf-8 -*-
import datetime as dt

from flask.ext.login import UserMixin

from seoul_serenity.extensions import bcrypt
from seoul_serenity.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

# TODO : should support python2/3
from seoul_serenity.compat import unicode

class Role(SurrogatePK, Model):
    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = ReferenceCol('users', nullable=True)
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        return '<Role({name})>'.format(name=self.name)

class User(UserMixin, SurrogatePK, Model):

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)
    user_type = Column(db.Integer, default=0)

    # TODO : next plan
    # user_projects = db.relationship('User_project', backref='users',lazy='dynamic')
    
    def __init__(self, username, email, password=None, **kwargs):
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    def get_id(self):
        return unicode(self.id)
            
    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __repr__(self):
        return '<User({username!r})>'.format(username=self.username)


### minwook ###
# user_project
class User_project(SurrogatePK,Model):
    __tablename__ = 'user_project'
    
    # TODO : next plan
    # u_id = Column(db.Integer, db.ForeignKey('users.id'))
    # p_id = Column(db.Integer, db.ForeignKey('projects.id'))
    
    u_id = Column(db.Integer, nullable=False);
    p_id = Column(db.Integer, nullable=False);

    created_at = Column(db.DateTime, nullable=True) 
    display_yn = Column(db.Boolean, default=True)

    # projects = db.relationship('Project',backref='user_project',lazy='dynamic')
    
    def __init__(self, **kwargs):
        db.Model.__init__(self, **kwargs)

    def __repr__(self):
        return 'todo'

### minwook ###
# project 
# class Project(SurrogatePK, Model):
#     __tablename__ = 'projects'
#     name = Column(db.String(80), unique=False, nullable=False)
#     start_date = Column(db.DateTime, nullable=True)
#     end_date = Column(db.DateTime, nullable=True)
#     # minwook
#     description = Column(db.Text, nullable=True)
#     created_u_id = Column(db.Integer, nullable=False)
#     modified_at = Column(db.DateTime, nullable=True)
#     modified_u_id = Column(db.Integer, nullable=True)
#     display_yn = Column(db.Boolean, default=True)

#     def __init__(self, name, **kwargs):
#         db.Model.__init__(self, name=name, **kwargs)
