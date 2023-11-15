from .abstract_repository import Abstract_Repository
from database.mongo import job_application_collection


class Jobs_Application_Repository(Abstract_Repository):
    def __init__(self):
        super().__init__( job_application_collection )