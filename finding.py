import pymongo #import library

client = pymongo.MongoClient("mongodb://localhost:27017") #connect to server

db = client["lib"] #connect to database
books = db["books"] #create books database
query = {
    "name": "Life 3.0"
}
#print([*books.find({
#    "name": "Life 3.0" #gets the book from this title
#},{
    #"_id": 0 #doesnt print book id just name author and published
#    "author": 1, #when you use only "author" it will just print the book of the author but if you do "author" and "name" it will get both
#    "name": 1
#})])# used to get all books from the db in a list format

# sort items from the db
print ([
    *books.find().sort("published", 1).limit(1)# display the books. if you want 1 then it will go assending -1 decending
    # *books.find().sort("published") will display all the books in the database
])