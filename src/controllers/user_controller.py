from flask import request , json , make_response
from database.repositories.user_repository import User_Repository
from utils.constants import HTTP_201_CREATED , USER_REGISTERED_SUCCESS_MESSAGE
import bson.json_util as json_util


def register():
    body = json.loads(request.data)
    
    username = body['username']    
    password = body['password']
    
    saved_user = User_Repository().create({ "username":username , "password":password })
    
    json_version = json_util.dumps(saved_user)
    
    return make_response({"message": USER_REGISTERED_SUCCESS_MESSAGE, "user":json_version}, HTTP_201_CREATED)
    