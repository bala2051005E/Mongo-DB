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

db = client["todo_app"]
todos_collection = db["todos"]


data = [
    {"title": "Read a Book", "description": "Finish the novel you started last week."},
    {"title": "Go for a Run", "description": "Jog in the park for 30 minutes."},
    {
        "title": "Grocery Shopping",
        "description": "Buy fruits, vegetables, and milk from the store.",
    },
]

# create operations

# todos_collection.insert_one(
#     {"title": "Read a Book", "description": "Finish the novel you started last week."}
# )

# todos_collection.insert_many(data)


# Update operation

# query = {"_id": ObjectId("65d31847991bc40b86c3c43e")}
# update = {"$set": {"description": "be any combination of quotes from the work"}}
# todos_collection.update_one(query, update)


# Delete Operation

query = {"_id": ObjectId("65d31847991bc40b86c3c440")}

todos_collection.delete_one(query)
