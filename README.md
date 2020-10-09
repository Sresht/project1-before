**The contents of this are unmodified and in the original state from the submission for Project 1 from one of my students (whose name has been redacted).
I am using this as starter code to explain changes that I would make to restructure the code.
Check out github.com/Sresht/project1-after for my version of this app (with the same functionality).**


CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Technical Issues
 * Additional Features
 * Improvements


INTRODUCTION
------------

Twittsplay is an app that searches for a Tweet based on a randomly generated dessert and a recipe of that dessert. Twittsplay will display the dessert, the quote, the user, the date, and time. Twittsplay will also display the recipe title, prep time, ingredients, and a link to the recipe page. Clicking "Get a new dessert!", Twittsplay will search for a new dessert and display a new Tweet and recipe!


INSTALLATION
------------

**In order to get started please clone the repository by using: `git clone https://github.com/Sresht/project1-before`**


1. This app requires Flask 
  * `pip install flask`
  * https://flask.palletsprojects.com/en/1.1.x/
  
2. This app requires Tweepy
 * `pip install tweepy`
 * https://www.tweepy.org/
 
3. This app requires dotenv
 * `pip install python-dotenv`
 * https://pypi.org/project/python-dotenv/ 
 
4. This app uses the Twitter API and requires API keys
 * https://developer.twitter.com/en
 * Environment Variables
   * CONSUMER_KEY
   * CONSUMER_SECRET
   * ACCESS_KEY
   * ACCESS_SECRET

5. This app uses the Spoonacacular API and requires an API key with Rapid API
 * https://rapidapi.com/spoonacular/api/recipe-food-nutrition
 * Environment Variables
   * SPOON_KEY
  
  
**Once steps 1-5 have been completed, start the app by running: `python app.py`**


6. If on Cloud9, preview templates/index.html. This should successfully render the HTML!

7. This app can be hosted on Heroku for FREE, in order to deploy on Heroku
 * Sign up for heroku at https://www.heroku.com/
 * Follow these steps for deployment:
   * `heroku login -i`
   * `heroku create`
   * `git push heroku master`
* Navigate to your newly created Heroku site.
  * Add secret keys from development.env by going to https://dashboard.heroku.com/apps
  * Click into your app > Settings > Config Vars > Reveal Config Vars > Add key value pairs for each variable.
  * Configure requirements.txt with all requirements needed to run your app.
  * Configure Procfile with the command needed to run your app.
    
   
TECHNICAL ISSUES
----------------

1. Starting the server. Fixed by mapping the correct API keys to the correct variables. 

2. Using the Twitter API. Read the documentation.

3. Using Tweepy. Read documentation


ADDITIONAL FEATURES
-------------------

1. [Backend] Static/Dynamic Search
 * User has the ability to enter a dish in a search field (for example, ”sweet potato casserole”). Once they
press enter, the site will use relevant results from Twitter and Spoonacular to display a recipe/photo/tweets about
that dish.
 * User has the ability to start typing letters into a search field (for example, ”sw”). As the user types,
autofill answers will populate suggestions of dishes (for example, ”sweet potato casserole”, ”swedish meatballs”)
that the user may click on.
 * User has the ability to enter the name of an ingredient in a search field (for example, ”chickpeas”).
Once they press enter, the site will search Spoonacular for dishes with that ingredient and display one randomly
(for example, ”chana masala”).

2. [Frontend] Content Carousel
 * Pictures and tweets will swap out every few seconds for the dish. There is no animation.
 * Pictures and tweets will swap out every few seconds for the dish using a fade in/fade out animation.
 * Multiple pictures are laid in a collage view, and multiple tweets are featured as a word cloud.


IMPROVEMENTS
------------

1. Add more HTML and CSS for design

2. Add a button to refresh the page

3. Add a link to the direct tweet
