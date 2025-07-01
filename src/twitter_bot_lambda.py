
import os
from random import *
import tweepy
from helpers import countdown, get_random_feed
from openai_helper import get_generated_message

bearer_token = os.environ.get("BEARER_TOKEN")
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

def lambda_handler(event, context):
    print("Lambda was triggered!")

    news_entry = get_random_feed()
    print("news_entry.title")
    print(news_entry.title)
    random_msg = f"{get_generated_message(news_entry)} {news_entry.link}"

    print("----------------------------------")
    print(random_msg)
    print("----------------------------------")

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