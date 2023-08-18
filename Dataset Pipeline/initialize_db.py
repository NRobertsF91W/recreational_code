import csv
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

# Load and insert data from CSV file
with open("data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    csv_data = list(csv_reader)

    # Insert data into MongoDB collection
    collection.insert_many(csv_data)

print("CSV data loaded into MongoDB successfully!")
