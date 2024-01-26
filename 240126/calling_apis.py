import requests # pip install requests
import json

base_url = "https://jsonplaceholder.typicode.com/"

response = requests.get(base_url + "users")

print(response)

data = response.json()

if response.status_code == 200:
    for user in data:
        print(user["name"], user["address"]["city"])
else:
    print("The call failed: ", response.status_code)