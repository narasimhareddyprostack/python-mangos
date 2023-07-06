# invoke API
import requests

import pymongo

client = pymongo.MongoClient()

db = client['dbone']
col = db['emp']

response=requests.get('https://dummyjson.com/users')

user_dict = response.json()
#print(type(user_dict))
#print(user_dict['users'])
col.insert_many(user_dict['users'])

