import pymongo


client = pymongo.MongoClient()

db= client['dbone']
col=db['user']

data = col.find({"name":"Rahul"})

for d in data:
    print(d)

#print(data)
