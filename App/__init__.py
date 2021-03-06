#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-08-27 15:43
# @Author : Curry
# @Site : https://github.com/coolbreeze2
# @File : __init__.py.py
# @Software: PyCharm
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


def create_app(env):
    app=Flask(__name__)

    app.config.from_object(envs.get(env))

    init_ext(app)

    init_blue(app)
    return app