#!/usr/bin/env python3

from flask import Flask, make_response
import badges
import data

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello and welcome to SparkBadge! <a href="/random">Try this.</a>'

@app.route('/random')
def random():
    return badges.sparkline(data.sample())


#app.run(debug=True)
