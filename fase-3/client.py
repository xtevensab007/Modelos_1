import requests

url = "http://localhost:5000/predict"
data = {
    "budget": 1000000,
    "popularity": 50
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:", response.json())
