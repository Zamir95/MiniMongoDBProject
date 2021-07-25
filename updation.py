import pymongo #import library

client = pymongo.MongoClient("mongodb://localhost:27017") #connect to server

db = client["lib"] #connect to database
books = db["books"] #create books database
#update books
# print(
#     books.update_one({
#         "name": "Life 3.0"
#     }, {
#         "$set": {
#             "published": 2017
#         }
#     }).modified_count
# )
# function update_many is used to update all books of a Particular name, author or published
books.update_many({"published" : 2021},{
    "$set":{
        "name": "PUBLISHED IN 2021"
    }
})
print([*books.find()])