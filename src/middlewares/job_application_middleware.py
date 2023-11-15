from flask import json , request , make_response
from database.repositories.user_repository import User_Repository
from utils.constants import HTTP_400_BAD_REQUEST  , USER_DOES_NOT_EXIST_MESSAGE , APPLICANT_ID_REQUIRED_MESSAGE , JOB_ID_REQUIRED_MESSAGE , RESUME_REQUIRED_MESSAGE , CONTACT_NO_REQUIRED_MESSAGE , EMAIL_REQUIRED_MESSAGE , COVER_LETTER_REQUIRED_MESSAGE

def create_job_application_middleware():
    body = json.loads(request.data)
    applicant_id = body['applicant_id']
    job_id = body['job_id']
    resume = body['resume']
    cover_letter = body['cover_letter']
    
    if not applicant_id:
        return make_response(HTTP_400_BAD_REQUEST , APPLICANT_ID_REQUIRED_MESSAGE)
    
    exisiting_user = User_Repository().find_one({"applicant_id": applicant_id})
    
    if not exisiting_user:
        return make_response(HTTP_400_BAD_REQUEST , USER_DOES_NOT_EXIST_MESSAGE )
    
    if not job_id:
        return make_response(HTTP_400_BAD_REQUEST , JOB_ID_REQUIRED_MESSAGE)
    
    if not resume:
        return make_response(HTTP_400_BAD_REQUEST , RESUME_REQUIRED_MESSAGE)
        
    if not cover_letter:
        return make_response(HTTP_400_BAD_REQUEST , COVER_LETTER_REQUIRED_MESSAGE) 
    