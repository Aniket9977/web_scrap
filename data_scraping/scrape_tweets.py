import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials from .env file
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def scrape_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(count)
    data = []
    for tweet in tweets:
        data.append(tweet.full_text)
    return pd.DataFrame(data, columns=["Text"])

if __name__ == "__main__":
    keyword = "Tesla Stock"
    tweets_df = scrape_tweets(keyword, count=500)
    tweets_df.to_csv("tweets.csv", index=False)
    print("Tweets scraped and saved to tweets.csv")
