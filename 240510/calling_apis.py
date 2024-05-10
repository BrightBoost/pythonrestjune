import requests
import json

base_url = "https://jsonplaceholder.typicode.com/"
response = requests.get(base_url + "users")

if response.status_code == 200:
    data = response.json()

    for user in data:
        print(user["company"]["name"])
else:
    print("I did not successfully call the api")