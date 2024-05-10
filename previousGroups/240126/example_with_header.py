import requests # pip install requests
import json

base_url = "https://jsonplaceholder.typicode.com/"

users = requests.get(base_url + "users").json()

# migration code because awful for application performance
for user in users:
    # post example - won't work not a user obj
    user_obj = {
        "name": "The header",
        "body": "blablabla",
        "email": "bla@bla.bla",
        "postId": 2
    }

    headers = {"Authorization": "Bearer sometokenhere"}

    response2 = requests.put(base_url + "users/" + str(user["id"]), json.dumps(user_obj), headers=json.dumps(headers))
    print(response2.status_code)
    print(response2.json())

