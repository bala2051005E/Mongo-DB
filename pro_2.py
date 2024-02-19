from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://bala2059:Jck0u6hUCvCQ3y8s@cluster0.gv6yaqj.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["db"]

users = db["users"]

data = [
    {"fullName": "Balaganapathy", "age": 20, "location": "pondy"},
    {"fullName": "Vijay", "age": 22, "location": "cuddalore"},
    {"fullName": "Ashwin", "age": 18, "location": "chennai"},
    {"fullName": "Ravi", "age": 16, "location": "bangalore"},
]

# creating operation

users.insert_one({"fullName": "Balaganapathy", "age": 20, "location": "pondy"})

users.insert_many(data)


# read operation

# query = {"_id  : ObjectId(65d30bbfd93f35f6393d5064)"}

# doc = users.find_one(query, {"_id": 0, "fullName": 1})
# print(doc)

# query = {"age": 30}

# data = []
# doc = users.find(query)
# print(list(doc))


# update operations

# query = {"_id": ObjectId("65d30c86cda01c63be0d55e8")}
# update = {"$set": {"age": 30}}

# users.update_one(query, update)


# query = {"age": 20}
# update = {"$set": {"age": 30}}

# users.update_many(query, update)
