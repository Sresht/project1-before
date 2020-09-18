from flask import Flask, render_template
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import random
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
    
    dessertList = ["cookies", "cake", "ice cream", "apple pie", "brownies", "cupcakes", "smores"]
    randomDessert = random.choice(dessertList)
    searchTweet = Cursor(api.search,
              q=randomDessert,
              lang="en"
              ).items(1)
    for tweet in searchTweet:
        text = tweet.text
        screen_name = tweet.author.screen_name
        created_at = tweet.created_at
    
    return render_template(
        "index.html",
        dessertList = dessertList,
        randomDessert = randomDessert,
        searchTweet = searchTweet,
        tweet = tweet,
        text = text,
        screen_name = screen_name,
        created_at = created_at
        )

app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)