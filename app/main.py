#!/usr/bin/env python3

from flask import Flask, make_response
import badges
import data

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello and welcome to SparkBadge!' 

#app.run(debug=True)
