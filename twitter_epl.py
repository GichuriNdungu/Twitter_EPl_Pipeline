import tweepy
import pandas as pd
import json
from datetime import datetime

def get_access_level():
    access_key = '1270042597126438912-Rl3l9Zd7QACyJmJIjLqlYSjehsnWT3'
    access_secret = '8XAUtvZ9W9vdI1m6aWFjalEUcogd9S5Cqyr3yTD7RhhzB'
    consumer_key = 'VPAYIJBTyQ3zf4IGrWivkFIPb'
    consumer_secret = 'ugGp10WeVWEV07V1wWe4fyyDeuDxDac21J8edmU7WKA5hOtRPu'

    """ Authenticate to twitter using tweepy AUTH handler"""
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key, access_secret)

    access_level = tweepy.get_access_level(auth)
    return  access_level

if __name__ == '__main__':
    print(get_access_level())