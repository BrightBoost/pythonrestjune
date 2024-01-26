import requests

base_url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(base_url)

data = response.json()
answer = input(data["setup"])
if answer == data["punchline"]:
    print("Hahahah that's right!")
else:
    print("Ha, no:", data["punchline"])