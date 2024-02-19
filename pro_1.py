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

db = client["contact_manager"]
contacts_collection = db["contacts"]


def add_contact(name, email, phone):
    contact = {"name": name, "email": email, "phone": phone}
    contacts_collection.insert_one(contact)


def get_all_contacts():
    return list(contacts_collection.find())


def get_contact(contact_id):
    return contacts_collection.find_one({"_id": ObjectId(contact_id)})


def update_contact(contact_id, name, email, phone):
    updated_contact = {"name": name, "email": email, "phone": phone}
    contacts_collection.update_one(
        {"_id": ObjectId(contact_id)}, {"$set": updated_contact}
    )


def delete_contact(contact_id):
    contacts_collection.delete_one({"_id": ObjectId(contact_id)})


def search_contacts(query):
    return list(
        contacts_collection.find(
            {
                "$or": [
                    {"name": {"$regex": query, "$options": "i"}},
                    {"email": {"$regex": query, "$options": "i"}},
                    {"phone": {"$regex": query, "$options": "i"}},
                ]
            }
        )
    )


def sort_contacts(field):
    return list(contacts_collection.find().sort(field))


if __name__ == "__main__":
    # Example usage:
    add_contact("John Doe", "john@example.com", "123-456-7890")
    add_contact("Jane Smith", "jane@example.com", "987-654-3210")

    print("All Contacts:")
    print(get_all_contacts())

    print("\nSearching for 'John':")
    print(search_contacts("John"))

    print("\nSorting by name:")
    print(sort_contacts("name"))

    # Update and delete example
    contact_id_to_update = str(get_all_contacts()[0]["_id"])
    update_contact(
        contact_id_to_update,
        "John Doe Updated",
        "john.updated@example.com",
        "555-555-5555",
    )

    contact_id_to_delete = str(get_all_contacts()[1]["_id"])
    delete_contact(contact_id_to_delete)

    print("\nAfter Update and Delete:")
    print(get_all_contacts())
