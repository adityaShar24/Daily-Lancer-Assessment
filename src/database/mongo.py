from pymongo import MongoClient
from .models.user_model import user_schema

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
    print("Connected to MongoDB")
except Exception as e:
    print("Could not connect to MongoDB" , e)