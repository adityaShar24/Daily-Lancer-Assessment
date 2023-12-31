from flask import json , request , make_response
from utils.constants import  HTTP_400_BAD_REQUEST , TITLE_REQUIRED_MESSAGE , DESCRIPTION_REQUIRED_MESSAGE , SKILLS_REQUIRED_MESSAGE , SALARY_REQUIRED_MESSAGE , POSTED_BY_REQUIRED_MESSAGE , CREATE_JOB_ENDPOINT , COMPANY_NAME_REQUIRED_MESSAGE\


def create_job_middleware():
    if request.endpoint == CREATE_JOB_ENDPOINT:
        body = json.loads(request.data)
        title = body['title']
        description = body['description']
        skills = body['skills']
        salary = body['salary']
        posted_by = body['posted_by']
        company_name = body['company_name']
        
        if not title:
            return make_response({'message': TITLE_REQUIRED_MESSAGE } , HTTP_400_BAD_REQUEST)
        
        if not description:
            return make_response({'message': DESCRIPTION_REQUIRED_MESSAGE } , HTTP_400_BAD_REQUEST)
        
        if not company_name:
            return make_response({"message": COMPANY_NAME_REQUIRED_MESSAGE} , HTTP_400_BAD_REQUEST)
        
        if not skills:
            return make_response({'message': SKILLS_REQUIRED_MESSAGE } , HTTP_400_BAD_REQUEST)
        
        if not salary:
            return make_response({'message': SALARY_REQUIRED_MESSAGE } , HTTP_400_BAD_REQUEST)
        
        if not posted_by:   
            return make_response({'message': POSTED_BY_REQUIRED_MESSAGE } , HTTP_400_BAD_REQUEST)