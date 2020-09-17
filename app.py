from flask import Flask, render_template
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import os

key = os.environ['CONSUMER_KEY']
secret = os.environ['CONSUMER_SECRET']
token = os.environ['ACCESS_KEY']
token_secret = os.environ['ACCESS_SECRET']

auth = OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = API(auth)

app = Flask(__name__)
@app.route('/')

def index():
    return render_template(
        "index.html"
        )

app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)