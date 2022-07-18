import pymongo
client = pymongo.MongoClient("mongodb+srv://Nrjineuron:Nrjmikki@cluster0.pyewsln.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name" :"neeraj",
    "email" :"suryawanshi.neeraj@gmail.com",
    "surname" :"suryawanshi",
    "age":30

}
db1=client['mongodbproject']
coll=db1['test']
coll.insert_one(d)