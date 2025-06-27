from datetime import date, datetime
import feedparser
import json
from random import choice
import sys
import time

def countdown(total_seconds):
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"\rCountdown till next X post: {timer}")
        sys.stdout.flush()
        time.sleep(1)
    print("\nTime's up!")


def get_random_messages(news_entry):
    day = date.today().strftime("%A")
    now_time = datetime.now().strftime("%I:%M%p")
    msgs = [
        # "Hello pilgrims, it's {}. I'm cookin' this Python for dinner.".format(day),
        "{}, it's about {}. Here's a news story from {}.\n\n{}".format(get_random_greeting(), now_time, news_entry.news_source, news_entry.link)
    ]
    
    return choice(msgs)

def get_random_greeting():
    greetings = [
        "Pilgrims",
        "Howdy Everyone",
        "Hi Friends",
        "Folks",
        "Alright Folks",
        "Ladies and Gents",
        "Alright you rustlers",
        "People",
        "Friends",
        "To all you cowboys (and cowgirls)"
    ]

    return choice(greetings)

def get_random_feed():
    with open('src/enums/feed_urls.json', 'r') as f:
        feed_urls = json.load(f)
    news_source, feed_url = choice(list(feed_urls.items()))
    print("* {}'s feed is {}".format(news_source, feed_url))
    NewsFeed = feedparser.parse(feed_url)

    if NewsFeed.entries:
        random_feed = choice(NewsFeed.entries)
        random_feed.news_source = news_source
        return random_feed
    return get_random_feed()