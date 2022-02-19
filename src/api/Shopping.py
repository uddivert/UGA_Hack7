import requests
import json

def formatDirections(streetNum, streetType, city, state): 
    return streenNum + "+" + streetType + "+" + city + "+" + state

def jsonGen():
    api = "AIzaSyCbbl_tqvQZ2-qZhNnTD5i5ZW7XUy85lIg"
    url = "https://maps.googleapis.com/maps/api/directions/json?origin="+formatDirections()+"&destination="+formatDirections()+"&key="+ api

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.content

    #    print(response.text)
    with open('directions.json', 'wb') as f:
        f.write(data)
        
