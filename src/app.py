from flask import Flask
from flask_jwt_extended import JWTManager
from routes.user_router import auth_bp , cache
from routes.jobs_router import jobs_bp
from middlewares.user_middleware import register_user_middleware , login_user_middleware 
from middlewares.job_middleware import create_job_middleware
from middlewares.job_application_middleware import create_job_application_middleware


app = Flask(__name__)
app.config['SECRET_KEY'] = "my_secret_key"

JWTManager(app)

cache.init_app(app)


app.before_request(register_user_middleware)
app.before_request(login_user_middleware)
app.before_request(create_job_middleware)
app.before_request(create_job_application_middleware)

app.register_blueprint(auth_bp)
app.register_blueprint(jobs_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)