import requests
import json
from trip import Trip
import codecs
from datetime import datetime
import time

my_key = '7f7684c2-dc19-4627-a6b8-78c4b69d1c25'
ct_position_url = "http://api.511.org/transit/vehiclepositions?api_key=7f7684c2-dc19-4627-a6b8-78c4b69d1c25&agency=CT&format=json"

min_count = 0
total_min=3

id_list = []
trips = []

while (min_count < total_min):
    response = requests.get(ct_position_url, timeout=5)
    now = datetime.now()
    print(now)
    decoded_json = response.text.encode().decode('utf-8-sig')
    json_parsed = json.loads(decoded_json)

    train_timestamp = json_parsed['Header']['Timestamp']



    for train in json_parsed['Entities']:
        id = train['Id']
        type = train['Vehicle']['Trip']['RouteId']
        longitude = train['Vehicle']['Position']['Longitude']
        latitude = train['Vehicle']['Position']['Latitude']
        if id in id_list:
            for t in trips:
                if t.id == id:
                    t.add_timepoint(train_timestamp, longitude, latitude)
                    break
        else:
            id_list.append(id)
            trip = Trip(id, type, [[train_timestamp, longitude, latitude]])
            trips.append(trip)



    min_count+=1
    time.sleep(60)

for t in trips:
    print("Train: ", t.id)
    print(t.timepoints)
