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


# POSTing a comment item
comment = {
    "email": "balbla@bla.com",
    "body": "some content",
    "postId": 8,
    "name": "blabla"
}

response2 = requests.post(base_url + "comments", data=json.dumps(comment))
print(response2.status_code)
print(response2.json())

# delete an item
toBeDeleted = 3
response3 = requests.delete(base_url + "posts/" + str(toBeDeleted))
print(response3.status_code)
print(response3.json())

# put 
response4 = requests.put(base_url + "comments/1", data=json.dumps(comment))
print(response4.status_code)
print(response4.json())
