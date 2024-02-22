from pymongo.mongo_client import MongoClient

class ContactManager:
    def __init__(self, db_url, db_name, collection_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_contact(self, contact):
        result = self.collection.insert_one(contact)
        return result.inserted_id

    def read_contacts(self):
        contacts = list(self.collection.find())
        return contacts

    def read_contact(self, contact_id):
        contact = self.collection.find_one({"_id": contact_id})
        return contact

    def update_contact(self, contact_id, updated_data):
        result = self.collection.update_one({"_id": contact_id}, {"$set": updated_data})
        return result.modified_count

    def delete_contact(self, contact_id):
        result = self.collection.delete_one({"_id": contact_id})
        return result.deleted_count

# Example usage:
if __name__ == "__main__":
    # Replace 'your_mongodb_url', 'your_db_name', and 'your_collection_name' with your MongoDB details
    contact_manager = ContactManager('mongodb+srv://bala2059:tYqXH7lz0jMUDg9w@cluster0.gv6yaqj.mongodb.net/?retryWrites=true&w=majority', 'bala2059', 'new_contact')

    # Create a new contact
    new_contact = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    contact_id = contact_manager.create_contact(new_contact)
    print(f"Contact created with ID: {contact_id}")

    # Read all contacts
    all_contacts = contact_manager.read_contacts()
    print("All Contacts:")
    print(all_contacts)

    # Read a specific contact
    contact = contact_manager.read_contact(contact_id)
    print("Read Contact:")
    print(contact)

    # Update a contact
    updated_data = {"phone": "987-654-3210"}
    updated_count = contact_manager.update_contact(contact_id, updated_data)
    print(f"Updated {updated_count} contact(s)")

    # Delete a contact
    deleted_count = contact_manager.delete_contact(contact_id)
    print(f"Deleted {deleted_count} contact(s)")
33