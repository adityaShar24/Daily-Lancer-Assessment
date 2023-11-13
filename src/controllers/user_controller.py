from flask import request , json , make_response
from database.repositories.user_repository import User_Repository
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE , INVALID_PASSWORD_MESSAGE , USER_LOGGEDIN_MESSAGE
from flask_jwt_extended import create_access_token
import bson.json_util as json_util
import datetime

def register():
    body = json.loads(request.data)
    
    username = body['username']    
    password = body['password']
    
    saved_user = User_Repository().create({ "username":username , "password":password })
    
    json_version = json_util.dumps(saved_user)
    
    return make_response({'message': USER_REGISTERED_MESSAGE.format(username), 'user': json_version} , HTTP_201_CREATED)

def login():
    body = json.loads(request.data)
    
    username = body['username']
    password = body['password']
    
    user = User_Repository().find_one({ "username":username })
    
    if password != user['password']:
        return make_response({"message": INVALID_PASSWORD_MESSAGE} , HTTP_400_BAD_REQUEST)
    
    acess_token = create_access_token(identity=username , fresh=datetime.timedelta(hours=6))
    
    return make_response({"message": USER_LOGGEDIN_MESSAGE.format(username) , "access_token":acess_token} , HTTP_201_CREATED)