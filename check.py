from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_SECRET")


# print("API_KEY:", API_KEY)
# print("API_SECRET:", API_SECRET_KEY)
# print("ACCESS_TOKEN:", ACCESS_TOKEN)
# print("ACCESS_SECRET:", ACCESS_TOKEN_SECRET)




import tweepy

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication successful")
except Exception as e:
    print("Error during authentication:", e)
