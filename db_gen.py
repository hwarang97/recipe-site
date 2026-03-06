from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.jungle

db.users.insert_one({"id": "ksj", "password": "1q"})
