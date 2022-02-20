# importing googlemaps module
import googlemaps
  
global distance
global duration

def distanceFunc(streetAddress1, streetAddress2):
    # Requires API key
    gmaps = googlemaps.Client(key='AIzaSyCbbl_tqvQZ2-qZhNnTD5i5ZW7XUy85lIg')
    my_dist = gmaps.distance_matrix(streetAddress1,streetAddress2)['rows'][0]['elements'][0]

    # Printing the result
    # print result
    distance = (my_dist['distance']["text"])
    duration = (my_dist['duration']["text"])

#def main():
#    distanceFunc("600 N Thomas St, Athens, GA 30601", "600 N Thomas St, Athens, GA 30601")

def getDistance():
    return distance

def getDuration():
    return duration 

#if __name__ == "__main__":
#    main()
