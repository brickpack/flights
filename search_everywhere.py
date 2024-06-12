import requests
import json

url = "https://sky-scanner3.p.rapidapi.com/flights/search-everywhere"

querystring = {"fromEntityId":"SLC","type":"oneway","cabinClass":"economy"}

headers = {
	"x-rapidapi-key": "6cf30de894mshedc18ece267a5efp1facb0jsn5dec589fcf68",
	"x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
with open('everywhere.json', 'w') as f:
    json.dump(data, f)

print(response.json())
