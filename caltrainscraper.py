import requests
from google.transit import gtfs_realtime_pb2

my_key = '7f7684c2-dc19-4627-a6b8-78c4b69d1c25'
ct_position_url = "http://api.511.org/transit/vehiclepositions?api_key=[7f7684c2-dc19-4627-a6b8-78c4b69d1c25]&agency=[CT]"
traffic_url = "http://api.511.org/traffic/events?api_key=[7f7684c2-dc19-4627-a6b8-78c4b69d1c25]"
test_url = 'http://ethans_fake_twitter_site.surge.sh/'

response = requests.get(ct_position_url, timeout=5)
print(response.text)
