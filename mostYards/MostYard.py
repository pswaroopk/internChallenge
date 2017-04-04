'''
Programming Assignment - Variation of Most Appropriate Yard (Complex) (100 points)

a) Given the geo cordinates of different yard locations,
develop a model that determines the closest yard to the given pickup location. (20 points)

b)Optimize your solution to O(n-k) through unsupervised learning algorithm (80 points).
And also provide 2 more nearer locations to the chosen location.

The yard locations can be obtained from zip_codes_states.csv

'''
import time
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint
from geopy.distance import great_circle
from sklearn import metrics
import numpy as np
import pandas as pd
from math import sin, cos, sqrt, atan2, radians
import sys
Radian = 6373
#read from raw data
def readCSV(file):
    #"zip_code","latitude","longitude","city","state","county"
    df = pd.read_csv(file, names=['zip_code', 'latitude','longitude','city','state','county'])
    zipcode = df.zip_code.tolist()[1:]
    latitude = df.latitude.tolist()[1:]
    longitude = df.longitude.tolist()[1:]
    cities=df.city.tolist()[1:]
    states=df.state.tolist()[1:]
    counties=df.county.tolist()[1:]
    return zipcode,latitude,longitude,cities,states,counties

'''
compute the distance between two coordinate
'''
def distanceCompute(latitude1,longitude1,latitude2,longitude2):
    # approximate radius of earth in km
    global Radian
    lat1 = radians(float(latitude1))
    lon1 = radians(float(longitude1))
    lat2 = radians(float(latitude2))
    lon2 = radians(float(longitude2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = Radian * c
    if(distance==0):
        print lat1,lon1,lat2,lon2
    #print("Result:", distance)
    return distance

'''
#input: longtitude, latitude
#output: zipcode
#navie approach
'''
def findClosetYard(latitude,longitude,latitudes,longitudes,zipcode,cities,states,counties):
    start_time = time.time()
    mindistance=sys.maxint
    curr_latitude=latitude
    curr_longitude=longitude
    curr_index=0
    for i in range(0,len(latitudes)):
        newdistance=distanceCompute(curr_latitude,curr_longitude,latitudes[i],longitudes[i])
        if(newdistance<mindistance):
            mindistance = newdistance
            curr_index=i
    print "Given Geo Info:"
    print "latitude: ", curr_latitude, "longitude: ", curr_longitude
    print ""
    print "Closet Yard Info:"
    print "latitude: ",latitudes[curr_index],"longitude: ",longitudes[curr_index]
    print "zipcode: ",zipcode[curr_index]
    print "city: ",cities[curr_index]
    print "State:", states[curr_index]
    print "County:", counties[curr_index]
    print "Distance: ",mindistance, " km"
    print "Time consume:", time.time()-start_time


'''
#input: file
#output: zipcode
#Clustering approach - density-based spatial clustering
'''
def findClosetYardCluster(file):
    df = pd.read_csv(file, encoding='utf-8')
    #df.head()
    coords=df.as_matrix(columns=['latitude','longitude'])
    global Radian
    epsilon=1.5/Radian
    start_time=time.time()
    #use DBSCAN
    db= DBSCAN(eps=epsilon, min_samples=10, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
    # get the number of clusters
    num_clusters = len(set(cluster_labels))
    # all done, print the outcome
    message = 'Clustered {:,} yards down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'
    print(message.format(len(df), num_clusters, 100 * (1 - float(num_clusters) / len(df)), time.time() - start_time))
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])

#get centeriod
def get_centeriod_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    #return close point
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)



#main function
def main():
    #read from csv file
    zipcode, latitude, longitude, cities, states, counties=readCSV('zip_codes_states.csv')
    #test case for problem a
    given_latitude=33.024321
    given_longitude=-96.674504
    #findClosetYard(given_latitude,given_longitude,latitude, longitude, zipcode, cities, states, counties)
    #test case for problem b
    given_latitude = 33.024321
    given_longitude = -96.674504
    findClosetYardCluster('zip_codes_states.csv')



if __name__=='__main__':
    main()

