import datetime
import tweepy
import json
from data import getTweet
import time
from collections import OrderedDict
import traceback
import os
import apiKeys
# def api():
#     auth = tweepy.OAuthHandler(apiKeys.api_key, apiKeys.api_key_secret)
#     auth.set_access_token(apiKeys.access_token, apiKeys.access_token_secret)

#     return tweepy.API(auth)


# def tweet(api: tweepy.API, message: str):
#     api.update_status(message)
#     print('Tweeted successfully!')


# if __name__ == '__main__':
#     api = api()
#     tweet(api, 'This was tweeted from Python')
# print('env','bearer_token')
    
client = tweepy.Client(apiKeys.bearer_token,apiKeys.api_key, apiKeys.api_key_secret,apiKeys.access_token,apiKeys.access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(apiKeys.api_key, apiKeys.api_key_secret, apiKeys.access_token, apiKeys.access_token_secret)
api = tweepy.API(auth)
api = tweepy.API(auth,wait_on_rate_limit=True)
# api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)





# bot code
departure="🛫"
arrival="🛬"

# print(data.tweet)
# print(type(data.tweet))
# print(list(set(data.tweet)))
# print(list(OrderedDict.fromkeys(data.tweet)))

# list(set(data.tweet))


# {dat['STASTD_DATE_change'] if(dat['STASTD_DATE_change']) else ''}
#             {dat['ETAETD_date_change'] if(dat['ETAETD_date_change']) else ""}
#             {dat['FlightStatus_change'] if(dat['FlightStatus_change']) else ''}



# Creating a tweet to test the bot
while True:
    data=getTweet()
    try:
        for dat in data:
            # print(dat)
            # print(dat['ETAETD_date'])
            time.sleep(1)
            print('tweeted')
            client.create_tweet(
                text=f""" {arrival+"Arrival From" if(dat['type']=='Arrival') else departure+"Departure To"}  { dat['OrigDest'] }{"🇳🇵" if(dat['IntDom']=='0') else "🌐"}\n{dat['Airline']}({ dat['FlightNumber']}).\n{("STA: "+dat['ETAETD_date_change'] if(dat['type']=='Arrival') else "STD: " +dat['STASTD_DATE_change']) if('STASTD_DATE_change' in dat) else 'STA: '+dat['STASTD_DATE'] if(dat['type']=='Arrival') else 'STD: '+dat['STASTD_DATE']}\n{("ETA: "+dat['ETAETD_date_change'] if(dat['type']=='Arrival') else "ETD: " +dat['ETAETD_date_change']) if('ETAETD_date_change' in dat) else 'ETA: '+dat['ETAETD_date'] if(dat['type']=='Arrival') else 'ETD: '+dat['ETAETD_date']}\n{"FlightStatus "+dat['FlightStatus_change'] if('FlightStatus_change' in dat) else "FlightStatus: "+ "-"if(dat['FlightStatus']==None) else dat['FlightStatus']}\n#{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")}""")
            
        #     print(f"""{"🇳🇵" if(dat['IntDom']=='0') else "🌐"} Flight {arrival+"Arrival" if(dat['type']=='Arrival') else departure+"Departure"} From { dat['OrigDest'] }
        # Airlines: {dat['Airline']}({ dat['FlightNumber']}).
        # {("STA "+dat['ETAETD_date_change'] if(dat['type']=='Arrival') else "STD " +dat['STASTD_DATE_change']) if('STASTD_DATE_change' in dat) else 'STA '+dat['STASTD_DATE'] if(dat['type']=='Arrival') else 'STD '+dat['STASTD_DATE']}
        # {("ETA "+dat['ETAETD_date_change'] if(dat['type']=='Arrival') else "ETD " +dat['ETAETD_date_change']) if('ETAETD_date_change' in dat) else 'ETA '+dat['ETAETD_date'] if(dat['type']=='Arrival') else 'ETD '+dat['ETAETD_date']}
        # {"Flight Status "+dat['FlightStatus_change'] if('FlightStatus_change' in dat) else "FlightStatus: "+ "-"if(dat['FlightStatus']==None) else dat['FlightStatus']}
        # \n#{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")}""")
            # print(dat['STASTD_DATE_change'])
            # print(dat['ETAETD_date_change'])
            # print(dat['FlightStatus_change'])
    except Exception:
        print(traceback.format_exc())
        # pass
    time.sleep(60)
    print(time.time())
    print(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))