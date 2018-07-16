from pymongo import MongoClient


# connect to mongodb server
client = MongoClient('localhost', 27017)
# select pymlb2-insta database
db = client['instagram']
