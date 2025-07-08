import openai
from openai import OpenAI
import os

openai_client = OpenAI(api_key=os.environ.get("OPEN_AI_API_KEY"))  # Use your actual API key

def get_generated_message(news_entry):


    content = f"Create a short message for a Twitter post regarding this news story from a John Wayne like personality. This personality does not like warmongering politicians or US aid going to foreign countries. If the news story is not about war or foreign aid there is no reason to mention these issues. : {news_entry.link}"
    
    # content = "Create a short message for Twitter regardiing today's news that that the FBI claims there is no Epstein client list and that Epstein did commit suicide. Make this post seem to have a John Wayne like personality. Find a news story regarding this and use this to help generate the content of the message. Also include a link to the news story for the Twitter post."

    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user", 
                "content": content
            }
        ]
    )

    return response.choices[0].message.content