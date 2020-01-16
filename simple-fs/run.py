#!/usr/bin/env python

import os
from app import app

PORT = os.getenv('PORT', 8080)
HOST = os.getenv('HOST', '127.0.0.1')

if app.config['DEBUG']:
    for key, val in os.environ.items():
        print(f'{key} = {val}')

app.run(host = HOST, port = PORT)
