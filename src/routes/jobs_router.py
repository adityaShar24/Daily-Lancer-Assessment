from flask import Blueprint
from controllers.job_controller import create_job

jobs_bp = Blueprint('jobs_bp', __name__)

@jobs_bp.post('/jobs/create')
def create_job_wrapper():
    return create_job()