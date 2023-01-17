import datetime
import tweepy
import json
from data import getTweet
import time
from collections import OrderedDict
import traceback
import os
import apiKeys
    
client = tweepy.Client(apiKeys.bearer_token,apiKeys.api_key, apiKeys.api_key_secret,apiKeys.access_token,apiKeys.access_token_secret)

auth = tweepy.OAuth1UserHandler(apiKeys.api_key, apiKeys.api_key_secret, apiKeys.access_token, apiKeys.access_token_secret)
api = tweepy.API(auth)
api = tweepy.API(auth,wait_on_rate_limit=True)



departure="🛫"
arrival="🛬"

while True:
    data=getTweet()
    try:
        for dat in data:
            time.sleep(1)
            print('tweeted')
            client.create_tweet(
                text=f""" {arrival+"Arrival From" if(dat['type']=='Arrival') else departure+"Departure To"}  { dat['OrigDest'] }{"🇳🇵" if(dat['IntDom']=='0') else "🌐"}\n{dat['Airline']}({ dat['FlightNumber']}).\n{("STA: "+dat['ETAETD_date_change'] if(dat['type']=='Arrival') else "STD: " +dat['STASTD_DATE_change']) if('STASTD_DATE_change' in dat) else 'STA: '+dat['STASTD_DATE'] if(dat['type']=='Arrival') else 'STD: '+dat['STASTD_DATE']}\n{("ETA: "+dat['ETAETD_date_change'] if(dat['type']=='Arrival') else "ETD: " +dat['ETAETD_date_change']) if('ETAETD_date_change' in dat) else 'ETA: '+dat['ETAETD_date'] if(dat['type']=='Arrival') else 'ETD: '+dat['ETAETD_date']}\n{"FlightStatus "+dat['FlightStatus_change'] if('FlightStatus_change' in dat) else "FlightStatus: "+ "-"if(dat['FlightStatus']==None) else dat['FlightStatus']}\n#{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")}""")
    except Exception:
        print(traceback.format_exc())
    time.sleep(60)
    print(time.time())
    print(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))