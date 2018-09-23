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
            return {"order_details": self.orders[y], "status_code":200}
        else:
            return {"Error": "Order id not found"}

    def update_order(self,order_id,order_status):
        new_status=int(order_status)
        if new_status == 1:
            self.orders[order_id].update({"Status": "Approved"})
            return {"order_details": self.orders[order_id], "status_code":200}
        elif new_status == 2:
            self.orders[order_id].update({"Status": "Denied"})
            return {"order_details": self.orders[order_id], "status_code":200}
        else:
            return {"Error": "No status change has been made"}


