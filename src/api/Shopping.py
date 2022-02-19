import requests
import json

"""
written by Uddhav Swami

formats the directions to values that can be read by the google api
"""
def formatDirections(streetNum, streetType, city, state): 
    return streenNum + "+" + streetType + "+" + city + "+" + state

def jsonGen():
    api = "AIzaSyCbbl_tqvQZ2-qZhNnTD5i5ZW7XUy85lIg"
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=" + api

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.content

    """
    #    print(response.text)
    with open('directions.json', 'wb') as f:
        f.write(data)
    """
     holder = json.loads(data)

