import os
import random
orders={}
class order:

    def __init__(self):
        self.orders=orders
    def make_order(self, new_order):
        x = random.randint(1, 20)
        self.orders[x]= new_order
        return new_order

    def list_orders(self):

        return {"order_details": self.orders, "status_code":200}

    def specific_order(self,orderId):
        y=int(orderId)
        if y in self.orders.keys():
            return self.orders[y]
        else:
            return ('Sorry orderid not found')

    def update_order(self,orderId,orderStatus):
        new_status=int(orderStatus)
        if new_status == 1:
            self.orders[orderId].update({"Status": "Approved"})
            return self.orders[orderId]
        elif new_status == 2:
            self.orders[orderId].update({"Status": "Denied"})
            return self.orders[orderId]
        else:
            return {"Error": "No status change has been made"}


