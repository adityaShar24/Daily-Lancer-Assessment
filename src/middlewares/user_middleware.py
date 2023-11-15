from flask import json , request , make_response
from database.repositories.user_repository import User_Repository
from utils.constants import  HTTP_400_BAD_REQUEST , USERNAME_REQUIRED_MESSAGE , PASSWORD_REQUIRED_MESSAGE , USERNAME_ALREADY_EXISTS_MESSAGE , REGISTER_USER_ENDPOINT , LOGIN_USER_ENDPOINT , USER_DOES_NOT_EXIST_MESSAGE , EMAIL_REQUIRED_MESSAGE

def register_user_middleware():
    if request.endpoint == REGISTER_USER_ENDPOINT:
        body = json.loads(request.data)
        print(request.endpoint)
        
        username = body('username')  
        password = body('password')   
        email = body('email')
        
        if not username:
            return make_response({"message": USERNAME_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({"message": PASSWORD_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        if not email:
            return make_response({"message": EMAIL_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        existing_user = User_Repository().find_one({"username": username})
        
        if existing_user:
            return make_response({"message": USERNAME_ALREADY_EXISTS_MESSAGE } , HTTP_400_BAD_REQUEST)


def login_user_middleware():
    if request.endpoint == LOGIN_USER_ENDPOINT:
        body = json.loads(request.data)
        
        username = body['username']
        password = body['password']
        
        
        if not username:
            return make_response({"message": USERNAME_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({"message": PASSWORD_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)

        existing_user = User_Repository().find_one({"username": username})
        
        if not existing_user:
            return make_response({"message": USER_DOES_NOT_EXIST_MESSAGE } , HTTP_400_BAD_REQUEST)
