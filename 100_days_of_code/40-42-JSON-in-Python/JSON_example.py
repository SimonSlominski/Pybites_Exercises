import json
import requests
from pprint import pprint

r = requests.get("URL")

data = json.loads(r.text)

for item in data.items():
    print(item)

for item in data.items():
    pprint(item)

for item in data['key1']['key2']:
    pprint(item['name'])
