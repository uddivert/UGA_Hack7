import requests
import json
import re
import linecache

global distance
global duration

#written by Uddhav Swami
#formats the directions to values that can be read by the google api

def formatDirections(streetNum, streetType, city, state): 
    return streenNum + "+" + streetType + "+" + city + "+" + state

def jsonGen():
    api = "AIzaSyCbbl_tqvQZ2-qZhNnTD5i5ZW7XUy85lIg"
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+formatDirections()+"destinations="+formatDirections()"+&units=imperial&key=" + api

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.content

    #    print(response.text)
    with open('directions.json', 'wb') as f:
        f.write(data)

    holder = json.loads(data)
    line = linecache.getline("directions.json", 9)
    distance = int(re.search(r'\d+',line ).group())
    line = linecache.getline("directions.json", 13)
    duration = (re.findall('\d+', line))

def getDistance():
    return distance

def getDuration():
    return duration

jsonGen()
