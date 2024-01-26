import requests # pip install requests
import json

base_url = "https://jsonplaceholder.typicode.com/"

# get example
response = requests.get(base_url + "users")

print(response)

data = response.json()

if response.status_code == 200:
    for user in data:
        print(user["name"], user["address"]["city"])
else:
    print("The call failed: ", response.status_code)

# post example
comment_obj = {
    "name": "The header",
    "body": "blablabla",
    "email": "bla@bla.bla",
    "postId": 2
}

response2 = requests.post(base_url + "comments", json.dumps(comment_obj))
print(response2.status_code)
print(response2.json())


# delete example
response3 = requests.delete(base_url + "comments/65")
print(response3.status_code)
print(response3.json())

comment_obj2 = {
    "name": "The new header",
    "body": "new blablabla",
    "email": "bla@bla.bla",
    "postId": 2
}

response4 = requests.put(base_url + "comments/2", json.dumps(comment_obj2))
print(response4.status_code)
print(response4.json())