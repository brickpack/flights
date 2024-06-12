import requests
import json

url = "https://sky-scanner3.p.rapidapi.com/flights/airports"

payload={}
headers = {
  'Content-Type': 'application/json',
  'X-RapidAPI-Key': '6cf30de894mshedc18ece267a5efp1facb0jsn5dec589fcf68',
  'X-RapidAPI-Host': 'sky-scanner3.p.rapidapi.com'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
with open('airports_new.json', 'w') as f:
    json.dump(data, f)

print(response.json())
print(response.text)