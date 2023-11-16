from flask import request , json , make_response
from database.repositories.user_repository import User_Repository
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE , INVALID_PASSWORD_MESSAGE , USER_LOGGEDIN_MESSAGE , ALL_USERS
from flask_jwt_extended import create_access_token
import bson.json_util as json_util
import datetime

def register():
    body = json.loads(request.data)
    
    username = body['username']    
    password = body['password']
    email = body['email']
    
    saved_user = User_Repository().create({ "username":username , "password":password , "email":email })
    
    json_version = json_util.dumps(saved_user)
    
    return make_response({'message': USER_REGISTERED_MESSAGE.format(username = username), 'user': json_version} , HTTP_201_CREATED)

def login():
    body = json.loads(request.data)
    
    username = body['username']
    password = body['password']
    
    user = User_Repository().find_one({ "username":username })
    
    if password != user['password']:
        return make_response({"message": INVALID_PASSWORD_MESSAGE} , HTTP_400_BAD_REQUEST)
    
    access_token = create_access_token(identity=username , fresh=datetime.timedelta(hours=6))
    
    return make_response({"message": USER_LOGGEDIN_MESSAGE.format(username = username) , "access_token":access_token} , HTTP_201_CREATED)

def get_all_users():
    users = User_Repository().find_many()
    list_all_users =  list(users)
    
    json_version = json_util.dumps(list_all_users)
    
    return make_response({"message": ALL_USERS, "users":json_version} , HTTP_201_CREATED)


def list_applications_by_user():
    user_id = request.args.get('user_id')
    
    applications = User_Repository().list_applications_by_user(user_id)
    
    json_version = json_util.dumps(applications)
    return make_response({'applications': json_version} , HTTP_201_CREATED)