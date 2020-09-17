from flask import Flask, render_template
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import os

app = Flask(__name__)
@app.route('/') #Python decorator

def index():
    return render_template(
        "index.html"
        )

app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)