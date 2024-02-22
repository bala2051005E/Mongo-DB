from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://bala2059:tYqXH7lz0jMUDg9w@cluster0.gv6yaqj.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



DB = client["contact_manager"] 

contacts = DB["contacts"]  

data = [
    {"name": "Alice", "phone": "+1234567890", "email": "alice@example.com"},
    {"name": "Bob", "phone": "+9876543210", "email": "bob@example.com"},
    {"name": "Charlie", "phone": "+1112233445", "email": "charlie@example.com"},
    {"name": "David", "phone": "+5556667777", "email": "david@example.com"},
    {"name": "Eva", "phone": "+9998887777", "email": "eva@example.com"},
    {"name": "Frank", "phone": "+4443332222", "email": "frank@example.com"},
    {"name": "Grace", "phone": "+7778889999", "email": "grace@example.com"},
 ]

# # Create Operation
# contacts.insert_one({"name": "Alice", "phone": "+1234567890", "email": "alice@example.com"})

# contacts.insert_many(data)

"---------"
# update operations

# query = {"_id": ObjectId("65d7267cfa110df221903604")}
# update = {"$set": {"phone": +9111586942}}

# contacts.update_one(query, update)

"----------"

# Delete operations

query = {"_id": ObjectId("65d72867357d3c32c49588b0")}

contacts.delete_one(query)