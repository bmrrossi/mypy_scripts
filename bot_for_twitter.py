import tweepy
import tkinter

consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'
access_token = 'ACCESS TOKEN'
access_secret = 'ACCESS SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

user = api.me()

# Bot will follow all the contacts from twitter user
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print('Followed everyone that is following ' + user.name)
