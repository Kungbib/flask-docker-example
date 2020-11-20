#!/usr/bin/env python3

from flask import Flask,request,render_template
from json import loads,dumps,load

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello():
    if 'use_template' in request.args:
        return render_template('hello.html')
    else:
        return 'Hello World!'

