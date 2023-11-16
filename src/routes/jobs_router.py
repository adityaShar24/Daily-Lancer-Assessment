from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.job_controller import create , apply ,  get_all_jobs , list_by_job_applications
from .user_router import cache

jobs_bp = Blueprint('jobs_bp', __name__)

@jobs_bp.post('/jobs/create')
@jwt_required()
def create_job_wrapper():
    return create()

@jobs_bp.post('/jobs/apply')
@jwt_required()
def apply_job_wrapper():
    return apply()

@jobs_bp.get('/jobs/get-all-jobs')
@jwt_required()
def get_all_jobs_wrapper():
    return get_all_jobs()


@jobs_bp.get('/jobs/applications/job/<int:job_id>')
@jwt_required()
@cache.cached(timeout=60)
def list_by_job_applications_wrapper(job_id):
    return list_by_job_applications(job_id)


