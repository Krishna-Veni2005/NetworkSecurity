
from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

uri = "mongodb+srv://srirangamkrishnaveni05_db_user:Krishna_mongodb@cluster0.ysaki8a.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)