import requests
import json

keyFile = open("toa.key", 'r')
json_file = open("output.json", 'w')

api_key = keyFile.read()
url_base = "https://theorangealliance.org/api"

headers = {'X-TOA-Key' : api_key,
           'X-Application-Origin' : 'AutoVortex',
           'Content-Type' : 'application/json'
           }



response = requests.get(url_base+'/team/14278/results/2122', headers=headers)

print(response.status_code)
json.dump(response.json(), json_file, indent=4, sort_keys=True)