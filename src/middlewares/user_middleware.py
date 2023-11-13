from flask import json , request , make_response
from database.repositories.user_repository import User_Repository
from utils.constants import  HTTP_400_BAD_REQUEST , USERNAME_REQUIRED_MESSAGE , PASSWORD_REQUIRED_MESSAGE , USERNAME_ALREADY_EXISTS_MESSAGE , REGISTER_USER_ENDPOINT

def register_user_middleware():
    if request.endpoint == REGISTER_USER_ENDPOINT:
        body = json.loads(request.data)
        
        username = body['username']
        password = body['password']
        
        if not username:
            return make_response({"message": USERNAME_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({"message": PASSWORD_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        
        existing_user = User_Repository().find_one({"username": username})
        
        if existing_user:
            return make_response({"message": USERNAME_ALREADY_EXISTS_MESSAGE } , HTTP_400_BAD_REQUEST)
    
    