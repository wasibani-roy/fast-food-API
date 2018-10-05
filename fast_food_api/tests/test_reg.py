import unittest
from fast_food_api.app import APP
from flask import json
class test_user(unittest.TestCase):
    """This Tests user registration """
    def setUp(self):
        self.APP = APP.test_client()
    def test_user_registration(self):
        """This Tests user registration with valid data"""
        reg_response = self.APP.post('/api/v2/signup', data=json.dumps(
            dict(username="Dag", email="Dag@me.com",
                 password="Dag1234")), content_type='application/json')
        result = json.loads(reg_response.data)
        self.assertEqual(result, {"success": "User added"})

    def test_user_registration_no_user_name(self):
        reg_response = self.APP.post('/api/v2/signup', data=json.dumps(
            dict(username="", email="Dag@me.com",
                 password="Dag1234")), content_type='application/json')
        result = json.loads(reg_response.data)
        self.assertEqual(result, {"Error": "Fields have not been filled"})

    def test_user_registration_no_password(self):
        reg_response = self.APP.post('/api/v2/signup', data=json.dumps(
            dict(username="Dag", email="Dag@me.com",
                 password="")), content_type='application/json')
        result = json.loads(reg_response.data)
        self.assertEqual(result, {"Error": "Fields have not been filled"})

    def test_user_registration_no_email(self):
        reg_response = self.APP.post('/api/v2/signup', data=json.dumps(
            dict(username="Dag", email="Dag@me.com",
                 password="")), content_type='application/json')
        result = json.loads(reg_response.data)
        self.assertEqual(result, {"Error": "Fields have not been filled"})



if __name__ == '__main__':
    unittest.main()
