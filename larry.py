import sys
import pymongo
import json
from sets import Set

from pymongo import MongoClient
client = MongoClient()

from pymongo import ASCENDING, DESCENDING

db = client.cs4501
tweets = db.tweets

reldist = []
distset = Set()

for tweet in tweets.find( { "retweeted_status.id" : {"$ne":"null"} , "user.screen_name": "LarrySabato" }, { "text": 1 , "retweet_count":1, "created_at":1, "user.screen_name":1 }).sort("retweet_count",DESCENDING):
#    print tweet                                                                  
    if not tweet["text"] in distset:
        if u'RT' in tweet["text"]:
            reldist.append(tweet)
#            distset.add(tweet["text"])

for t in reldist:
    print t

#print "done"

