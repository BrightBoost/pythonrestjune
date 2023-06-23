import requests

base_url = "https://example.com"
username = "username"
password = "secret"
response = requests.get(base_url + "/something", auth=(username, password))

data = response.json()

# do something with the data