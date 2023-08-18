import pymongo


# MongoDB connection details
mongo_host = "mymongodb"  # Docker container name
mongo_port = 27017
username = "admin"
password = "adminpassword"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_host, mongo_port,
                             username=username, password=password)
db = client["wbank"]  # Use your desired database
collection = db["indicators"]  # Use your desired collection

# Retrieve and display all documents in the collection
print("Documents in the collection:")
for document in collection.find({"country":"Albania"}):
    print(document)
