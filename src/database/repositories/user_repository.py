from .abstract_repository import Abstract_Repository
from database.mongo import users_collection

class User_Repository(Abstract_Repository):
    def __init__(self):
        super().__init__(users_collection)
    