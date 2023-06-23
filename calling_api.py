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


# POSTing a post item
post = {
    "title": "My new post",
    "body": "some content",
    "userId": 8
}

response2 = requests.post(base_url + "posts", data=json.dumps(post))
print(response2.status_code)
print(response2.json())

# delete an item
toBeDeleted = 3
response3 = requests.delete(base_url + "posts/" + str(toBeDeleted))
print(response3.status_code)
print(response3.json())

# put 
response4 = requests.put(base_url + "posts/1", data=json.dumps(post))
print(response4.status_code)
print(response4.json())
