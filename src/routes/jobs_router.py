from flask import Blueprint
from controllers.job_controller import create , apply

jobs_bp = Blueprint('jobs_bp', __name__)

@jobs_bp.post('/jobs/create')
def create_job_wrapper():
    return create()

@jobs_bp.post('/jobs/apply')
def apply_job_wrapper():
    return apply()

# /jobs/list_by_job - job_id
# /jobs/mine - user_id