import unittest
from flask import json
import resources
from models import *
from app import app
import coveralls
Coveralls.wear!
class test_orders(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.test_data = {"product": "chicken", "quantity": "1", "price": "12000"}
        self.test_data_update = {"product": "chicken", "quantity": "1", "price": "12000", "Status":"Approved"}
        self.testModal = order()
        self.testModal.orders = {1: {"product": "chicken", "quantity": "1", "price": "12000"}}

    def test_API_Make_Order(self):
        self.assertEqual(self.testModal.make_order(self.test_data), self.test_data)

    def test_API_Get_All_Orders(self):
        orderValue = self.testModal.list_orders()
        self.assertEqual(orderValue["status_code"], 200)
        self.assertEqual(orderValue["order_details"], self.testModal.orders)

    def test_API_get_specific_order(self):
        self.assertEqual(self.testModal.specific_order(1), self.test_data)

    def test_API_update_specific_order(self):
        self.assertEqual(self.testModal.update_order(1,1), self.test_data_update)

    def test_post(self):
        data = {
            'product': 'beans',
            'quantity': 4,
            'price': 2000
        }
        response = self.app.post('/order', data=data)
        result = json.loads(response.data)
        self.assertEqual(result, {'product': 'beans', 'quantity': '4', 'price': '2000'})

    def test_get(self):
        self.testModal.orders = {1: {"product": "chicken", "quantity": "1", "price": "12000"}}
        response = self.app.get('/order')
        result = json.loads(response.data)
        self.assertEqual(result['status_code'], 200)

if __name__ == '__main__':
        unittest.main()


