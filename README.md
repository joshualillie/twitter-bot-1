# twitter-bot-2

This is a very simple example of an X (Twitter) Bot that I threw together while sitting in a meeting (listening attentively, of course). It makes use of a couple of APIs - the Twitter API and the OpenAI API, combined with some old fashion RSS feeds. It's a pretty simple concept.

### Overview

The bot performs a very simple task. 

1. First it grabs a random news source and its RSS feed from a list of news sources (hard coded as an enum). It pulls the RSS feed and then chooses a random news story from the random news source. 

1. It sends the news story link as part of a request to OpenAI asking it to generate a message that we can use for X (Twitter). For fun I asked it to take on a certain personality and have a certain political slant.

1. Finally, it posts the message to X using the API.

There's not a whole lot more to it. 

### Considerations

Both the X API and OpenAI API have some pretty stiff restricitons and both are very expensive to use. Both have "free" options that are quite limited. For example, the Free Tier of X API only allows you to make 500 posts/month, which is about 16 posts a day. This is fine for just messing around and practicing, but wouldn't be good for people who want to have thier bot posting and replying all day every day. (Yuck)

### Usage

#### Running Locally

Set up Python environment and install dependencies.
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

If everything installs correctly, kick off the script with:
```
python3 src/app.py
```

### More Details To Come