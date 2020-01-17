#!/usr/bin/env python

from flask import Flask
from .views import main_page

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(main_page)
