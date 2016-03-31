# -*- coding: utf-8 -*-
# pip install tweepy 
# pip install elasticsearch

import json
import tweepy
from datetime import datetime
from elasticsearch import Elasticsearch

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def get_es():
  d = datetime.now()
  dt = d.strftime("%Y-%m-%dT%H:00:00Z")
  qry = {
    "query": {
      "range": {
        "dt": {
          "gte": dt
        }
      }
    },
    "sort": {
      "dt": {
        "order": "desc"
      }
    },
    "from": 0,
    "size": 1
  }
  es = Elasticsearch()
  res = es.search(index="ieth", body=qry)
  hit = res['hits']['hits']
  return hit
  


def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "KEY",
    "consumer_secret"     : "KEY",
    "access_token"        : "KEY",
    "access_token_secret" : "KEY" 
    }
  tmp = get_es()
  it = tmp[0]['_source']['it']
  et = tmp[0]['_source']['et']
  ih = tmp[0]['_source']['ih']
  eh = tmp[0]['_source']['eh']
  dt = tmp[0]['_source']['dt']
  print("%s => it: %s, et: %s, ih: %s, eh: %s" % (dt, it, et, ih, eh))

  t = datetime.now()
  tm = t.strftime("%I:%M %p")

  tweet = "Weather Today at {}: temperature(room={}°C, outside={}°C), humidity(room={}%, outside={}%) #raspberrypi".format(tm,it,et,ih,eh)
  print tweet
  # print tmp['et']
  api = get_api(cfg)
  # tweet = "Hello, world! from tweepy"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
