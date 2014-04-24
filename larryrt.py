import sys
import pymongo
import json
from sets import Set

from pymongo import MongoClient
client = MongoClient()

from pymongo import ASCENDING, DESCENDING

db = client.cs4501
tweets = db.tweets


for tweet in tweets.find( { "retweeted_status.id" : {"$ne":"null"}, "retweet_count": {"$lt":433 }, "retweeted_status.user.screen_name": "LarrySabato" }, { "text": 1 , "retweet_count":1, "created_at":1, "user.screen_name":1 }).sort("retweet_count",DESCENDING):
    print tweet                                                                                            
