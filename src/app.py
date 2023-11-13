from flask import Flask
from flask_jwt_extended import JWTManager
from routes.user_router import auth_bp


app = Flask(__name__)

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)