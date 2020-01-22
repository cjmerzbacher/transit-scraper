import requests
import json
from trip import Trip
import codecs

my_key = '7f7684c2-dc19-4627-a6b8-78c4b69d1c25'
ct_position_url = "http://api.511.org/transit/vehiclepositions?api_key=7f7684c2-dc19-4627-a6b8-78c4b69d1c25&agency=CT&format=json"

response = requests.get(ct_position_url, timeout=5)

decoded_json = response.text.encode().decode('utf-8-sig')
json_parsed = json.loads(decoded)

#Scrape data once per minute, using system clock to synchronize

#For each timestamp:
ts = json_parsed['Header']['Timestamp']
id_list = []
trips = []

for train in json_parsed['Entities']:
    id = train['Id']
    type = train['Vehicle']['Trip']['RouteId']
    longitude = train['Vehicle']['Position']['Longitude']
    latitude = train['Vehicle']['Position']['Latitude']

    if ~(id in id_list):
        id_list.append(id)
        trip = Trip(id, type, [[ts, longitude, latitude]])
        trips.append(trip)
    else:
        for t in trips:
            if t.id == id:
                t.add_timepoint(ts, longitude, latitude)
                break

for t in trips:
    print(t.id, t.timepoints)
