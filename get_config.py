import requests

url = "https://sky-scanner3.p.rapidapi.com/get-config"

headers = {
	"x-rapidapi-key": "6cf30de894mshedc18ece267a5efp1facb0jsn5dec589fcf68",
	"x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())