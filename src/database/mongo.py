from pymongo import MongoClient

CONNECTION_STRING  = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(CONNECTION_STRING)

try:
    client.server_info()
    print("Connected to MongoDB")
except Exception as e:
    print("Could not connect to MongoDB" , e)