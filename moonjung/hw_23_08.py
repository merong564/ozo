import requests
import json

url = 'https://randomuser.me/api/'
r = requests.get(url)
data = json.loads(r.text)
print(data['results'][0]['name'])