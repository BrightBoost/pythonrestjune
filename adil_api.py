import requests # pip install requests
import json
 
#base_url = "https://jsonplaceholder.typicode.com/"
 
base_url = "https://restcountries.com/v3.1/all"
  
response = requests.get(base_url)
 
data = response.json()
 
if response.status_code == 200:
    for item in data:
        print(item["name"]["common"] , "\n",  item["status"])
else:
    print("Call was not successful")