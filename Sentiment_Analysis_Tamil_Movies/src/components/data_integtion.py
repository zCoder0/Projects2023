import json
import sys
import asyncio
import os
from twikit import Client
from src.exception.exception_base import ProjectException

class DataCollection:
    def __init__(self):
        try:
            print("Welcome to data collection")
            self.__client = Client('en-US')
        except Exception as e:
            ProjectException(e, sys)

    async def login(self, auth_info_1, auth_info_2, password):
        try:
            await self.__client.login(auth_info_1=auth_info_1, auth_info_2=auth_info_2, password=password)
            print("Login Success")
        except Exception as e:
            ProjectException(e, sys)

    async def get_data(self, query, trending="Latest", top=20):
        try:
            # Await the coroutine to get the tweets.
            tweets = await self.__client.search_tweet(query, trending, top)
            tweet_list = [
                {
                    'text': tweet.text,
                    'twit_id': tweet.id,
                }
                for tweet in tweets
            ]

            # Use os.path.join for a cross-platform file path.
            self.save_path = os.path.join("components", "dataset", "tweets.json")
            with open(self.save_path, "w", encoding="utf-8") as f:
                json.dump(tweet_list, f, ensure_ascii=False, indent=4)
            print("Tweets saved successfully!")
        except Exception as e:
            ProjectException(e, sys)
            
    def get(self):
        with open(self.save_path, 'r') as f:
            tweets = json.load(f)
            
        return tweets

