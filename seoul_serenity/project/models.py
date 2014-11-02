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

class Project(SurrogatePK, Model):
    __tablename__ = 'projects'
    name = Column(db.String(80), unique=False, nullable=False)
    start_date = Column(db.DateTime, nullable=True)
    end_date = Column(db.DateTime, nullable=True)
    description = Column(db.Text, nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    created_user_id = Column(db.Integer,nullable=True)
    modified_at = Column(db.DateTime, nullable=True)
    modified_user_id = Column(db.Integer,nullable=True)
    display_yn = Column(db.Boolean, default=True)

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        return '<Project({name})>'.format(name=self.name)

    def datetimeformat(value, format='%d-%m-%Y'):
        return value.strftime(format,vlaue.gmtime())    


class project_iteration(SurrogatePK, Model):
    __tablename__ = 'project_iteration'

    p_id = Column(db.Integer,nullable=False)
    v_id = Column(db.Integer,nullable=False)
    week = Column(db.Integer,nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self,  **kwargs):
        db.Model.__init__(self, **kwargs)

# project vote #
class project_vote(SurrogatePK, Model):
    __tablename__ = 'project_vote'
    
    u_id = Column(db.Integer,nullable=False)
    score = Column(db.Integer,nullable=False)
    comment = Column(db.String(128),nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self,  **kwargs):
        db.Model.__init__(self, **kwargs)

# project summary #
class project_summary(SurrogatePK, Model):

    __tablename__ = 'project_summary'
    
    p_id = Column(db.Integer,nullable=False)
    summary_type = Column(db.Integer,nullable=False)
    score = Column(db.Float,nullable=True,default='0.0')
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self,  **kwargs):
        db.Model.__init__(self, **kwargs)
        
