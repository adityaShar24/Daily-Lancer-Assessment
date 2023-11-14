from .abstract_repository import Abstract_Repository
from database.mongo import jobs_collection

class Jobs_Repository(Abstract_Repository):
    def __init__(self):
        super().__init__(jobs_collection)