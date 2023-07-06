# https://dummyjson.com/users

import requests

response = requests.get('https://dummyjson.com/users')

response_dict = response.json()
print(type(response_dict))

#print(response_dict['users'])
print(type(response_dict['users']))

#convert python object to json object

