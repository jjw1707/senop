from flask import Flask

import tweepy

from flask_jsglue import JSGlue

app = Flask(__name__, instance_relative_config = True)
app.config.from_object('config.BaseConfiguration')
app.config.from_pyfile('config.py', silent=True)

twauth = tweepy.OAuthHandler(app.config['TWITTER_KEY'], app.config['TWITTER_SECRET'])
twapi = tweepy.API(twauth)

jsglue = JSGlue(app)

import senop.controller

