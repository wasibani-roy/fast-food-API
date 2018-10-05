from flask_restful import Resource, reqparse
from flask import redirect, url_for, logging, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from fast_food_api import models
from fast_food_api.models.models import Order

class order_modal(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('menuid', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        menu_item_id = int(data["menuid"].strip())

        if menu_item_id == "":
            return jsonify({"Error": "You have not selected you're order"}), 404
        else:
                new_order = Order(menu_item_id, current_user,status="none",order_id="none")


                return new_order.add_order()

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        if current_user == 5:
            orders = Order(order_id="none", status="none", menu_id="none", user_id="none")
            return orders.get_order_items()
        else:
            return jsonify({"Error": "Unauthorised access"}), 400

 


    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderid', help='This field cannot be blank', required=True)
        parser.add_argument('status', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        order_id = data["orderid"].strip()
        order_status = data["status"].strip()
        if order_id == "" or order_status == "":
            return jsonify({"Error": "Missing order id or order status"})
        else:
            orders = Order(order_id=order_id,status="null", user_id="null", menu_id="null")
            return orders.update_order(order_status)


class specific_order(Resource):
    @jwt_required
    def get(self,order_id= id):
        current_user = get_jwt_identity()
        if current_user == 5:
            new_order_id = int(order_id)
            orders = Order(user_id=current_user, order_id=new_order_id, menu_id="none", status="none")

            return orders.order_by_id()
        else:
            return jsonify({"Error": "Unauthorised access"}), 400

class get_user_history(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        orders = Order(user_id=current_user, order_id="none", status="none", menu_id="none")
        return orders.get_user_order()


