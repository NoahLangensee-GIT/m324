import pymongo
from src.user import User

class Db:
    def __init__(self, connection_string: str):
            self.client = pymongo.MongoClient(connection_string)
            self.db = self.client["integration_test_db"]
            self.collection = self.db["users"]

    def set_user(self, user: User):
        if user:
            self.collection.insert_one(user.to_dict())

    def get_user(self) -> User | None:
        user_data = self.collection.find_one()
        return User.from_dict(user_data)
