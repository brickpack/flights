import requests
import json

url = "https://sky-scanner3.p.rapidapi.com/flights/skyId-list"

headers = {
	"x-rapidapi-key": "6cf30de894mshedc18ece267a5efp1facb0jsn5dec589fcf68",
	"x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data = response.json()
with open('sky_ids.json', 'w') as f:
    json.dump(data, f)

print(response.json())