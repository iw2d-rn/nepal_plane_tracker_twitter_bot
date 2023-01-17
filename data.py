import json
import traceback
import sys
import requests
import apiKeys






def getTweet():
    tweet=[]
    try:
        newData=None
        res = requests.get(apiKeys.apiURL)
        newData = json.loads(res.text)
    except Exception:
        print(traceback.format_exc())
    oldData=None
    try:
        with open('old.json') as f:
            oldData = json.load(f)
    except Exception:
        pass
    
    flightState=['departure','arrivals']


    newFlight=[]
    
    try:
        if(oldData==None or (oldData['data']['arrivals']!=[] or oldData['data']['departure'])!=[]):
            for a in flightState:
                try:
                    lastOldFlight=oldData['data'][a][len(oldData['data'][a])-1]['FlightNumber']
                except:
                    lastOldFlight=''
                new=False
                
                for x in range(len(newData['data'][a])):
                    if(new):
                        newFlight.append(newData['data'][a][x])
                    if(newData['data'][a][x]['FlightNumber']==lastOldFlight):
                        new=True
                    try:
                        
                        for y in range(len(oldData['data'][a])):
                            try:
                                if(newData['data'][a][x]['FlightNumber']==oldData['data'][a][y]['FlightNumber']):
                                    tempTweet=[]
                                    tempTweet.append((newData['data'][a][x]))
                                    save=False
                                    if(newData['data'][a][x]['STASTD_DATE']!=oldData['data'][a][y]['STASTD_DATE']):
                                        save=True
                                        tempTweet[0]['STASTD_DATE_change']=f"""{oldData['data'][a][y]['STASTD_DATE']} -> {newData['data'][a][x]['STASTD_DATE']}"""
                                        print('STASTD_DATE changed',f"""{oldData['data'][a][y]['STASTD_DATE']} to {newData['data'][a][x]['STASTD_DATE']}""")
                                    if(newData['data'][a][x]['ETAETD_date']!=oldData['data'][a][y]['ETAETD_date']):
                                        save=True
                                        tempTweet[0]['ETAETD_date_change']=f"""{oldData['data'][a][y]['ETAETD_date']} -> {newData['data'][a][x]['ETAETD_date']}"""
                                        print('ETAETD_date changed',f"""{oldData['data'][a][y]['ETAETD_date']} to {newData['data'][a][x]['ETAETD_date']}""")
                                    if(newData['data'][a][x]['FlightStatus']!=oldData['data'][a][y]['FlightStatus']):
                                        save=True
                                        tempTweet[0]['FlightStatus_change']=f"""{oldData['data'][a][y]['FlightStatus']} -> {newData['data'][a][x]['FlightStatus']}"""
                                        print('FlightStatus changed',f"""from {oldData['data'][a][y]['FlightStatus']} to {newData['data'][a][x]['FlightStatus']}""")
                                    if(save):
                                        tweet.append(tempTweet[0])
                            except:
                                pass
                    except:
                        pass
            tweet=tweet+newFlight
        elif(newData==None or (newData['data']['arrivals']!=[] and newData['data']['departure'])!=[]):
            print('no tweets')
        else:
            print('POST ALL NEW DATA')
    except Exception:
        pass

    print('tweet',tweet)

    try:
        res = requests.get(apiKeys.apiURL)
        newData = json.loads(res.text)
        with open('old.json', 'w') as f:
            json.dump(newData, f)
    except Exception:
            pass
    return tweet



