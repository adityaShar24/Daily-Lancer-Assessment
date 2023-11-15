from pymongo import MongoClient
from .models.user_model import user_schema 
from .models.job_model import job_schema
from .models.job_application_model import job_application_schema
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
    mongo_client.server_info() 
    print(CONNECTED_TO_MONGODB)
    users_collection = create_collection(database , 'users' , user_schema)
    jobs_collection = create_collection(database , 'Jobs' , job_schema)
    job_application_collection = create_collection(database , 'Job-Applications' , job_application_schema)

except Exception as e:
    print(CONNECTION_FAILED , e)