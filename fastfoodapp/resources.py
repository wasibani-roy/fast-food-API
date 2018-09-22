from flask_restful import Resource
import flask
from fastfoodapp import models

class make_order(Resource):
    def post(self):
        orders=models.order()
        product = flask.request.form["product"]
        quantity = flask.request.form["quantity"]
        price = flask.request.form["price"]
        if product=="" or quantity=="" or price=="":
            return {"Error":"Sorry your order is incomplete please try again"}
        else:
            new_order={"product":product, "quantity":quantity, "price":price}
            return orders.make_order(new_order)


class Orders(Resource):
    def get(self):
        orders = models.order()

        return orders.list_orders()


class specific_order(Resource):
    def get(self, id):
        orders=models.order()
        orderid = int(id)
        return orders.specific_order(orderid)


class update_order(Resource):
    def put(self, id):
        id = int(id)
        orders=models.order()
        print('order_status')
        order_status = flask.request.form["status"]
        # print(order_status)
        return orders.update_order(id,order_status)

