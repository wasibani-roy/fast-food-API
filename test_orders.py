import unittest
from flask import json
from fastfoodapp import app
from fastfoodapp import resources
from fastfoodapp import models

class test_orders(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.test_data = {"product": "chicken", "quantity": "1", "price": "12000"}
        self.test_data_error_no_id = "Sorry orderid not found"
        self.test_data_update_approve = {"product": "chicken", "quantity": "1", "price": "12000", "Status":"Approved"}
        self.test_data_update_deny = {"product": "chicken", "quantity": "1", "price": "12000", "Status": "Denied"}
        self.test_data_update_no_status = {"Error": "No status change has been made"}
        self.testModal = models.order()
        self.testModal.orders[1] = {"product": "chicken", "quantity": "1", "price": "12000"}

    def test_API_Make_Order(self):
        self.assertEqual(self.testModal.make_order(self.test_data), self.test_data)

    def test_API_Get_All_Orders(self):
        orderValue = self.testModal.list_orders()
        self.assertEqual(orderValue["status_code"], 200)
        self.assertEqual(orderValue["order_details"], self.testModal.orders)

    def test_API_get_specific_order(self):
        orderValue = self.testModal.specific_order(1)
        self.assertEqual(orderValue["order_details"], self.test_data)

    def test_API_get_specific_order_wrong_id(self):
        self.assertEqual(self.testModal.specific_order(0), self.test_data_error_no_id)

    def test_API_update_specific_order_approve(self):
        orderValue = self.testModal.update_order(1,1)
        self.assertEqual(orderValue["order_details"], self.test_data_update_approve)

    def test_API_update_specific_order_deny(self):
        orderValue = self.testModal.update_order(1, 2)
        self.assertEqual(orderValue["order_details"], self.test_data_update_deny)

    def test_API_update_specific_order_no_status(self):
        self.assertEqual(self.testModal.update_order(1,0), self.test_data_update_no_status)

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
        response = self.app.get('/order')
        result = json.loads(response.data)
        self.assertEqual(result['status_code'], 200)

    def test_get_id(self):
        response = self.app.get('/order/1')
        result = json.loads(response.data)
        self.assertEqual(result['status_code'], 200)

    def test_put(self):
        data = {"status": 1}
        response = self.app.put('/order/1', data= data)
        result = json.loads(response.data)
        self.assertEqual(result['status_code'], 200)

if __name__ == '__main__':
        unittest.main()


