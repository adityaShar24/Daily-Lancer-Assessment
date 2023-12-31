from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_caching import Cache
from controllers.user_controller import register , login , get_all_users , list_applications_by_user

auth_bp = Blueprint('auth_bp' , __name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})

@auth_bp.post('/auth/register')
def register_user_wrapper():
    return register()

    
@auth_bp.post('/auth/login')
def login_user_wrapper():
    return login()

@auth_bp.get('/auth/get-all-users')
@jwt_required()
@cache.cached(timeout=60)
def get_all_users_wrapper():
    return get_all_users()

@auth_bp.get('/auth/application/user')
@jwt_required()
@cache.cached(timeout=60)
def list_applications_by_user_wrapper(user_id):
    return list_applications_by_user(user_id)
