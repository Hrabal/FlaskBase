# -*- coding: utf-8 -*-
import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from models.dbtools import Dictable


class User(db.Model, Dictable):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(300))
    email = db.Column(db.String(300))

    def __init__(self, username, password, email):
        self.username = username
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.email = email

    def validate_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password_setter(self, password):
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return "<User %r>" % (self.username)
