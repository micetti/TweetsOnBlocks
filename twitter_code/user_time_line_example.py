import os
import json

from twitter import Api

CONSUMER_KEY = os.getenv("CONSUMER_KEY", None)
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", None)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", None)
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", None)

# Users to watch
USER_ID = 25073877 # This is Donald Trump

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']

# Since we're going to be using a streaming endpoint, there is no need to worry
# about rate limits.
api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)


def main():
    with open('output.txt', 'a') as f:
        statuses = api.GetUserTimeline(user_id=USER_ID)
        for status in statuses:
            user = status.user.screen_name
            tweet_text = status.text
            status_id = status.id
            tweet_created = status.created_at
            print(user)
            print(tweet_text)
            print(status_id)
            print(tweet_created)
            f.write(status.text)

if __name__ == '__main__':
    main()
