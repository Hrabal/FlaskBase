# -*- coding: utf-8 -*-
import locale
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging

locale.setlocale(locale.LC_TIME, locale.getlocale())

app = Flask(__name__)
app.config.from_object("config")

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

import models
import views
