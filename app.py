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
    
    
    #Spoonacular search info
    search_url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    querystring = {"query":"cookies", "number":1}
    search_response = requests.request("GET", search_url, headers=headers, params=querystring)
    search_data=search_response.json()
    for rec in search_data["results"]:
        rec_id=rec["id"]
        rec_title=rec["title"]
        rec_servings=rec["servings"]
        rec_prep_time=rec["readyInMinutes"]
        rec_image=rec["image"]
        rec_url=rec["sourceUrl"]
        #print(ing_id, ing_title, ing_servings, ing_prep_time, ing_url, ing_image)
    
    #Spoonacular ingredients by id info
    ing_url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+str(rec_id)+"/ingredientWidget.json"
    ing_response = requests.request("GET", ing_url, headers=headers)
    ing_data=ing_response.json()
    for ing in ing_data["ingredients"]:
        ing_name = ing["name"]
        ing_amount_value = ing["amount"]["us"]["value"]
        ing_amount_unit = ing["amount"]["us"]["unit"]
        #print(ing_name, ing_amount_unit, ing_amount_value)
    
    
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