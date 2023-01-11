import json
# import newAPIdata
import traceback
import sys
import requests
import apiKeys






def getTweet():
    tweet=[]
    try:
# get new data from api
        newData=None
        res = requests.get(apiKeys.apiURL)
        newData = json.loads(res.text)
        # print('newData',newData)
    
    # with open('newAPIdata.json') as f:
    #     newData = json.load(f)
    # print(d)
# print(newData)
    except Exception:
        print(traceback.format_exc())

    # get old data from file
    oldData=None
    try:
        with open('old.json') as f:
            oldData = json.load(f)
        # print(d)
    # print(oldData)
    except Exception:
        # print(traceback.format_exc())
        pass
    
    # compair two flights if diffrent in flightstatus add to tweet
    flightState=['departure','arrivals']


    newFlight=[]
    
    try:
        if(oldData==None or (oldData['data']['arrivals']!=[] or oldData['data']['departure'])!=[]):
            for a in flightState:
                # print(a)
                try:
                    lastOldFlight=oldData['data'][a][len(oldData['data'][a])-1]['FlightNumber']
                except:
                    lastOldFlight=''
                    # pass
                # print('lastOldFlight of ',a,lastOldFlight)
                # if(len(newData['data'][a])==):
                #     print(x)
                new=False
                
                for x in range(len(newData['data'][a])):
                    if(new):
                        # print(x,y)
                        newFlight.append(newData['data'][a][x])
                        # print('new')
                    if(newData['data'][a][x]['FlightNumber']==lastOldFlight):
                        new=True
                        # print(x,y)
                    try:
                        
                        for y in range(len(oldData['data'][a])):
                            # print('x',x,'y',y)
                            try:
                                if(newData['data'][a][x]['FlightNumber']==oldData['data'][a][y]['FlightNumber']):
                                    
                                    # print('x',x,'y',y)
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
                                    # tweet.append()
                                    if(save):
                                        tweet.append(tempTweet[0])
                                        # print(tempTweet)
                                        # print(tweet)
                                # else:
                                    # print('new data',newData['data'][a][x]['FlightNumber'])
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
        # print(traceback.format_exc())
        pass

    print('tweet',tweet)


    # list or dict of flights that should be tweeted

    try:
        res = requests.get(apiKeys.apiURL)
        newData = json.loads(res.text)
        with open('old.json', 'w') as f:
            json.dump(newData, f)
    except Exception:
            # print(traceback.format_exc())
            pass
    return tweet

# arrival=''
# =>landed


# departure=''
# => check_in => security check => Last Call => boarding => Boarding Completed => departed

# oldData=''




# # remove landed or departed
# data=json.loads(apiData)
# oldData=data




