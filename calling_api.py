import requests # pip install requests
import json 

base_url = "https://jsonplaceholder.typicode.com/"

response = requests.get(base_url + "posts")

data = response.json()

if response.status_code == 200:
    for item in data:
        print(item["userId"], "=", item["id"])
else:
    print("Call was not successful")