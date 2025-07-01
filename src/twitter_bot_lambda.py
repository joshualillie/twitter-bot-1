
import os
from random import *
import tweepy
from helpers import countdown, get_random_feed
from openai_helper import get_generated_message

# bearer_token = os.environ.get("BEARER_TOKEN")
# consumer_key = os.environ.get("CONSUMER_KEY")
# consumer_secret = os.environ.get("CONSUMER_SECRET")
# access_token = os.environ.get("ACCESS_TOKEN")
# access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
# Upload image
# media = api.media_upload("john-wayne-3.jpeg")

# min_sleep_time = 90 * 60
# max_sleep_time = 120 * 60

def lambda_handler(event, context):
    print("Lambda was triggered!")

    news_entry = get_random_feed()
    print("news_entry.title")
    print(news_entry.title)
    random_msg = f"{get_generated_message(news_entry)} {news_entry.link}"

    consumer_key = "WnuUKniDBEqWJCWZ54y0nWH7D"
    consumer_secret = "avK38CHOzbDHKnCy4WmvJYkwQ9t1UcoMA7IapQwnio5Vrlfa0t"
    access_token = "1688265889035206656-sHN4xaPZwbQh4dzX8Nrve5geh6AsVi"
    access_token_secret = "9eXHReAmpINjCMAkuY9JSx2x8hROh3dIcjBZAFeVcygQA"

    print(random_msg)
    print("----------------------------------")
    print(consumer_key)
    print(consumer_secret)
    print(access_token)
    print(access_token_secret)
    print("----------------------------------")

    # auth = tweepy.OAuth1UserHandler(
    #     consumer_key, consumer_secret,
    #     access_token, access_token_secret
    # )
    # api = tweepy.API(auth)

    # # Post the tweet using the older API interface
    # api.update_status("Hello world from Tweepy!")

    x_client = tweepy.Client(
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret,
        access_token=access_token, 
        access_token_secret=access_token_secret
    )

    response = x_client.create_tweet(
        text=random_msg,
        # media_ids=[media.media_id]
    )

    print(f"https://twitter.com/user/status/{response.data['id']}")

    return {
        'statusCode': 200,
        'body': 'Hello from Twitter Bot!'
    }

# lambda_handler(None, None)


# while(True):
#     news_entry = get_random_feed()
#     print("news_entry.title")
#     print(news_entry.title)
#     random_msg = f"{get_generated_message(news_entry)} {news_entry.link}"

#     print(random_msg)

#     x_client = tweepy.Client(
#         consumer_key=consumer_key, 
#         consumer_secret=consumer_secret,
#         access_token=access_token, 
#         access_token_secret=access_token_secret
#     )

#     response = x_client.create_tweet(
#         text=random_msg,
#         # media_ids=[media.media_id]
#     )

#     print(f"https://twitter.com/user/status/{response.data['id']}")

#     sleep_time = int(uniform(min_sleep_time, max_sleep_time))
#     countdown(sleep_time)