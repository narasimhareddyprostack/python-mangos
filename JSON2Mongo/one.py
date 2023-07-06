import pymongo

#establish connect
client = pymongo.MongoClient()

#get db
db=client['dbone']

#create or get collection 
col=db['user']

#insert doc
user = ''' { "id":101, "name":"Rahul"} '''
col.insert_one({"id": 102, "name": "Sonia"})
