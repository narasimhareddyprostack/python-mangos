# https://dummyjson.com/users

import requests
import json

import pymongo

client = pymongo.MongoClient()

db = client['dbone']
col = db['emp']

response = requests.get('https://dummyjson.com/users')

response_dict = response.json()
print(type(response_dict))

#print(response_dict['users'])
print(type(response_dict['users']))

#convert python object to json object

user_List = response_dict['users']

user_json = json.dumps(user_List)

print(user_json)

col.insert_many(user_json)