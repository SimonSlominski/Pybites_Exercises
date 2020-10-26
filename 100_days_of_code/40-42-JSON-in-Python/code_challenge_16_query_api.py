import json
import requests
from pprint import pprint

URL = "http://www.omdbapi.com/?apikey=9a7808bd&t=hero"

r = requests.get(URL)

data = json.loads(r.text)

for item in data.items():
    print(item)
