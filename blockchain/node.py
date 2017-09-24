import os
import json
import time
from flask import Flask
from twitter import Api
from blockchain.chain import Chain


app = Flask(__name__)

USER_ID = 25073877 # This is Donald Trump
CONSUMER_KEY = os.getenv("CONSUMER_KEY", None)
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", None)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", None)
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", None)

trump_chain = Chain()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/check")
def check():
    return json.dumps(get_latest_tweets_sorted())

@app.route("/last")
def get_last_block_data():
    return trump_chain.get_latest_block().data

@app.route("/update")
def update_block_chain_data():
    latest_tweets = get_latest_tweets_sorted()
    if len(trump_chain.chain) is 1:
        add_tweets(latest_tweets)
    else:
        last_data = trump_chain.get_latest_block().data
        latest_created_at = json.loads(last_data)['created']
        tweets_to_be_added = []
        for tweet in latest_tweets:
            if tweet['created'] > latest_created_at:
                tweets_to_be_added.append(tweet)
        if len(tweets_to_be_added) == 0:
            return "No new tweets since last update"
        else:
            add_tweets(tweets_to_be_added)
            return "Added {} new Tweets".format(len(tweets_to_be_added))
    return "Done"

@app.route("/validate")
def check_if_block_chain_is_valid():
    is_valid = str(trump_chain.all_blocks_valid())
    number_of_blocks = len(trump_chain.chain)
    return "The whole blockchain is valid: {}\n\nCurrent total length of the blockchain: {}".format(is_valid, number_of_blocks)

def get_latest_tweets_sorted():
    api = Api(CONSUMER_KEY,
              CONSUMER_SECRET,
              ACCESS_TOKEN,
              ACCESS_TOKEN_SECRET)
    statuses = api.GetUserTimeline(user_id=USER_ID)
    status_list = list()
    for status in statuses:
        created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y'))
        status_list.append(dict(user=status.user.screen_name, text=status.text, id=status.id, created=created_at))
        status_list = sorted(status_list, key=lambda k: k['created'])
    return status_list

def add_tweets(latest_tweets):
    for tweet in latest_tweets:
        trump_chain.add_new_block(json.dumps(tweet))
