from flask import json , request , make_response
from database.repositories.jobs_repository import Jobs_Repository
from database.repositories.job_application_repository import Jobs_Application_Repository
from utils.constants import  HTTP_201_CREATED , JOB_CREATED_MESSAGE , APPLIED_SUCCESSFULLY_MESSAGE , ALL_JOBS , APPLICATIONS_FOR_JOB
import bson.json_util as json_util
from bson.objectid import ObjectId


def create_job():
    body = json.loads(request.data)
    title = body['title']
    description = body['description']
    skills = body['skills']
    salary = body['salary']
    posted_by = body['posted_by']
    company_name = body['company_name']
    
    job = Jobs_Repository().create({"title":title , "description":description , "skills":skills , "salary":salary , "posted_by": ObjectId(posted_by), "company_name":company_name })
    
    json_version = json_util.dumps(job)
    
    return make_response({'message': JOB_CREATED_MESSAGE , 'job': json_version} , HTTP_201_CREATED)

def apply_for_job():
    body = json.loads(request.data)
    job_id = body['job_id']
    applicant_id = body['applicant_id']
    resume = body['resume']
    cover_letter = body['cover_letter']
    
    applicantion = Jobs_Application_Repository().create({"job_id":ObjectId(job_id) , "applicant":ObjectId(applicant_id) , "resume":resume , "cover_letter":cover_letter })
    
    json_version = json_util.dumps(applicantion)
    
    return make_response({'message': APPLIED_SUCCESSFULLY_MESSAGE  , "application_id": json_version } , HTTP_201_CREATED)


def get_all_jobs():
    jobs = Jobs_Repository().find_many()
    list_all_jobs =  list(jobs)
    
    json_version = json_util.dumps(list_all_jobs)
    
    return make_response({"message": ALL_JOBS , "jobs":json_version} , HTTP_201_CREATED)


def list_by_job_applications():
    job_id = request.args.get('job_id')
    
    applications = Jobs_Application_Repository().find_many({"job_id":ObjectId(job_id)})
    
    json_version = json_util.dumps(applications)
    
    return make_response({'message': APPLICATIONS_FOR_JOB.format(job_id = job_id), 'applications': json_version}, HTTP_201_CREATED)    