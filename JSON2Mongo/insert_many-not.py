import pymongo

client = pymongo.MongoClient()

db = client['dbone']
col = db['emp']

col.insert_many([{"id":101},{"id":102},{"id":103}])
