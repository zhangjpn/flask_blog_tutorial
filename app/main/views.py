# -*-coding:utf-8 -*-

from app.main import main


@main.route(r'/', )
def index():
    return 'index'
