from flask import json , request , make_response
from database.repositories.jobs_repository import Jobs_Repository
from utils.constants import  HTTP_201_CREATED , JOB_CREATED_MESSAGE
import bson.json_util as json_util
from bson.objectid import ObjectId


def create_job():
    body = json.loads(request.data)
    title = body['title']
    description = body['description']
    skills = body['skills']
    salary = body['salary']
    posted_by = body['posted_by']
    
    saved_job = Jobs_Repository().create({"title":title , "description":description , "skills":skills , "salary":salary , "posted_by": ObjectId(posted_by) })
    
    json_version = json_util.dumps(saved_job)
    
    return make_response({'message': JOB_CREATED_MESSAGE , 'job': json_version} , HTTP_201_CREATED)