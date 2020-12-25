from collections import namedtuple, Counter
import re

import matplotlib as plt
import numpy as np
from PIL import Image
import tweepy
from wordcloud import WordCloud, STOPWORDS

import credlib


Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_APP_NAME = 'HydroPlantVax'

TWITTER_ACCESS_TOKEN    = credlib.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_SECRET   = credlib.TWITTER_ACCESS_SECRET
TWITTER_KEY             = credlib.TWITTER_KEY
TWITTER_SECRET          = credlib.TWITTER_SECRET

# Create API Object
auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_APP_NAME,
                            exclude_replies=False).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)

# Wordcloud
pb_mask = np.array(Image.open('cp2077.png'))
stopwords = set(STOPWORDS)

stopwords.add('co')
stopwords.add('https')

wc = WordCloud(background_color="white", max_words=100, mask=pb_mask, stopwords=stopwords)


if __name__ == "__main__":
    tweets = list(get_tweets())
    wc_img = wc.generate(tweets)
