from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.job_controller import create , apply , list_by_job_applications

jobs_bp = Blueprint('jobs_bp', __name__)

@jobs_bp.post('/jobs/create')
@jwt_required()
def create_job_wrapper():
    return create()

@jobs_bp.post('/jobs/apply')
@jwt_required()
def apply_job_wrapper():
    return apply()

@jobs_bp.get('/jobs/applications/job/<int:job_id>')
@jwt_required()
def list_by_job_applications_wrapper(job_id):
    return list_by_job_applications(job_id)


