from flask import Blueprint
from controllers.user_controller import register , login

auth_bp = Blueprint('auth_bp' , __name__)

@auth_bp.post('/auth/register')
def register_user_wrapper():
    return register()

    
@auth_bp.post('/auth/login')
def login_user_wrapper():
    return login()

