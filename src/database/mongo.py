from pymongo import MongoClient
from .models.user_model import user_schema
from utils.constants import CONNECTED_TO_MONGODB , CONNECTION_FAILED

CONNECTION_STRING  = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/'

client = MongoClient(CONNECTION_STRING)

database = client['Job-App']

def create_collection(database , collection_name , schema):  
    if collection_name in database.list_collection_names():
        return database[collection_name]
    else:
        return database.create_collection(collection_name ,**{"validator": {"$jsonSchema": schema}})
    


try:
    mongo_client = MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)
    mongo_client.server_info()  # Check if the server is reachable
    print(CONNECTED_TO_MONGODB)
    users_collection = create_collection(database , 'users' , user_schema)

except Exception as e:
    print(CONNECTION_FAILED , e)