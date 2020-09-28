from flask import Flask, render_template
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import requests
import random
import sys
import os
from dotenv import load_dotenv
from os.path import join, dirname
import spoonacular as sp

#env
dotenv_path = join(dirname(__file__), 'development.env')
load_dotenv(dotenv_path)

#keys
key = os.getenv('CONSUMER_KEY')
secret = os.getenv('CONSUMER_SECRET')
token = os.getenv('ACCESS_KEY')
token_secret = os.getenv('ACCESS_SECRET')
key2 = os.getenv('SPOON_KEY')

#tweepy api auth
auth = OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = API(auth)

#https://rapidapi.com/spoonacular/api/recipe-food-nutrition/endpoints
headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': key2
    }

app = Flask(__name__)
@app.route('/')

def index():
 
    dessertList = ["cookies", "cake", "ice cream", "apple pie", "brownies", "cupcakes", "smores"]
    randomDessert = random.choice(dessertList)
    
    
    #Spoonacular info
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    querystring = {"query":"cookies"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data=response.json()
    
    
    #tweepy info
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