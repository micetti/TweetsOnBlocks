import os
import json
from flask import Flask
from twitter import Api
from chain.chain import Chain


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
def check_for_updates():
    api = Api(CONSUMER_KEY,
              CONSUMER_SECRET,
              ACCESS_TOKEN,
              ACCESS_TOKEN_SECRET)
    statuses = api.GetUserTimeline(user_id=USER_ID)
    status_list = [dict(user=status.user.screen_name, text = status.text, id = status.id, created = status.created_at) for status in statuses]
    return  json.dumps(status_list)

@app.route("/last")
def get_last_block_data():
    return trump_chain.get_latest_block().data

@app.route("/update")
def update_block_chain_data():
    # now we just need to add all tweets that are not on blocks yet.
    pass

