
import json
import re
from langdetect import detect
import emoji
import pandas as pd


class Preprocessing:
    # Function to split tweet components
    def split_tweet(self,tweet):

        if isinstance(tweet['text'], list):
            text = ' '.join(tweet['text'])
        else:
            text = tweet['text']
        # Remove \n and \r
        text = text.replace('\n', ' ').replace('\r', ' ')
        #remove nuremeric

        text = re.sub(r'\d+', '', text)
        # Remove URLs
        urls = re.findall(r'http\S+', text)
        text = re.sub(r'http\S+', '', text)

        hashtags = re.findall(r'#\w+', text)
        text = re.sub(r'#\w+', '', text)
        emojis = ''.join(c for c in text if c in emoji.EMOJI_DATA)
        text = re.sub(r'[^\w\s]', '', text)
        return {
            'text': text.strip(),
            'urls': urls if urls else None,
            'hashtags': hashtags if hashtags else None,
            'emojis': emojis if emojis else None
        }
        
    def split_languages(self,text):
        words = text.split()
        print(words)
        print()
        tamil = ' '.join(w for w in words if  detect(w) == 'ta')
        english = ' '.join(w for w in words if detect(w) != 'ta')
        return pd.Series([tamil if tamil else None, english if english else None], index=['tamil', 'english'])
    
    def preprocessing(self,tweets):
        tweet_data = [self.split_tweet(tweet) for tweet in tweets]
        
        df = pd.DataFrame(tweet_data,columns=['text', 'urls', 'hashtags', 'emojis'])
        df[['tamil', 'english']] = df['text'].apply(self.split_languages)
        print("Updated DataFrame !")
        
        return df