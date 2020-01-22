
#----------------------------------------------------------#
#Import required packages
import requests
import json
from trip import Trip
import codecs
from datetime import datetime
import time
import pandas as pd
from sys import argv

#511 API keys
my_key = '7f7684c2-dc19-4627-a6b8-78c4b69d1c25'
ct_position_url = "http://api.511.org/transit/vehiclepositions?api_key=7f7684c2-dc19-4627-a6b8-78c4b69d1c25&agency=CT&format=json"

#Number of minutes to run
min_count = 0
total_min= int(argv[1])

#Establish list of IDs and trips
id_list = []
trips = []

#Gather data until required time up
while (min_count < total_min):
    #Scrape data from website
    response = requests.get(ct_position_url, timeout=5)
    #Get current system timestamp
    now = datetime.now()

    #Parse scraped data into json
    decoded_json = response.text.encode().decode('utf-8-sig')
    json_parsed = json.loads(decoded_json)

    #Obtain train timestamp (not used currently)
    train_timestamp = json_parsed['Header']['Timestamp']

    #For each train on the tracks currently
    for train in json_parsed['Entities']:
        id = train['Id']
        type = train['Vehicle']['Trip']['RouteId']
        longitude = train['Vehicle']['Position']['Longitude']
        latitude = train['Vehicle']['Position']['Latitude']

        #If train already exists, add new timepoint
        if id in id_list:
            for t in trips:
                if t.id == id:
                    t.add_timepoint(now, longitude, latitude)
                    break

        #If train does not already exist, create new train
        else:
            id_list.append(id)
            trip = Trip(id, type, [[now, longitude, latitude]])
            trips.append(trip)

    print(100*min_count/total_min, "% done")
    min_count+=1
    #Pause for 1 minute
    time.sleep(60)

print("100% done")

#Read out the trips to CSV
for t in trips:
    filename = "scraped_data/"+ t.id + '_'+ t.train_type + '.csv'
    t.timepoints.to_csv(filename)
