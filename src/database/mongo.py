from pymongo import MongoClient
from .models.user_model import user_schema
from utils.constants import CONNECTED_TO_MONGODB , CONNECTION_FAILED

CONNECTION_STRING  = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(CONNECTION_STRING)

database = client['Job-Ap']

users_collection = None

if 'Users' in database.list_collection_names():
    users_collection = database['Users']
else:
    users_collection = database.create_collection('Users' , **{ "validator": { "$jsonSchema": user_schema } })
    
try:
    client.server_info()
    print(CONNECTED_TO_MONGODB)
except Exception as e:
    print(CONNECTION_FAILED , e)