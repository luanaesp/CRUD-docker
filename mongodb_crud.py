from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient('localhost', 27017)
db = client.mydatabase
collection = db.mycollection

# Create
document = {'name': 'John', 'age': 30}
collection.insert_one(document)

# Read
document = collection.find_one({'name': 'John'})
print(f'Read from MongoDB: {document}')

# Update
collection.update_one({'name': 'John'}, {'$set': {'age': 31}})

# Delete
collection.delete_one({'name': 'John'})
