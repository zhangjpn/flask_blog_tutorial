# -*-coding:utf-8 -*-

from flask import Blueprint

auth = Blueprint(name='auth', import_name=__name__)

from app.auth import views
