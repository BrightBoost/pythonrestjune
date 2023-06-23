import requests # pip install requests

base_url = "https://jsonplaceholder.typicode.com/"

response = requests.get(base_url + "comments")

data = response.json()

if response.status_code == 200:
    for item in data:
        print(item["email"], "=", item["name"])
else:
    print("Call was not successful")