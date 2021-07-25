import pymongo #import library

client = pymongo.MongoClient("mongodb://localhost:27017") #connect to server

db = client["lib"] #connect to database
books = db["books"] #create books database
#insert records
#books.insert_one({
#    "name": "atmomic habits",
#    "author": "Zamir Lalji",
#    "published": 2019
#})
#insert many records
books.insert_many([ #insert records into db
    {
        "name": "Good to Great",
        "author": "Jim Collins",
        "published": 1993
    },
    {
        "name": "Life 3.0",
        "author": "Max Tegmark",
        "published": 2017
    },
    {
        "name": "How to Program",
        "author": "Zamir Lalji",
        "published": 2017
    }
])