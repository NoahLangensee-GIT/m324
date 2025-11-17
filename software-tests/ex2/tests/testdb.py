import time
import unittest
import docker
from src.db import Db
from src.user import User
 
 
class TestDb(unittest.TestCase):
 
    def setUp(self):
        self.client = docker.from_env()
 
        self.container = self.client.containers.run(
            "mongo:7.0",
            name="mongo-test",
            ports={"27017/tcp": 27017},
            detach=True
        )
 
        time.sleep(3)
 
        self.db = Db("mongodb://localhost:27017")
 
    def tearDown(self):
        try:
            self.container.stop()
            self.container.remove()
        except:
            pass
 
    def test_set_and_get_user(self):
 
        user = User(name="user", mail="user@example.com")
 
        self.db.set_user(user)
 
        read_user = self.db.get_user()
 
        self.assertIsNotNone(read_user)
        self.assertEqual(read_user.name, "user")
        self.assertEqual(read_user.mail, "user@example.com")
 
 
if __name__ == "__main__":
    unittest.main()
