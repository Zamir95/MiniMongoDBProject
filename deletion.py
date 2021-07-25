import pymongo #import library

client = pymongo.MongoClient("mongodb://localhost:27017") #connect to server

db = client["lib"] #connect to database
books = db["books"] #create books database
#deletes one record from the db
# books.delete_one({
#     "published": 2017,
#     "author": "Max Tegmark"
# })
#delete many books from the db
books.delete_many({
    "published": 2021,
})

print([*books.find()])