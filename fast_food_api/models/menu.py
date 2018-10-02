from flask_restful import Resource, reqparse
from flask import redirect, url_for, logging, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
# from passlib.hash import pbkdf2_sha256 as sha256
from fast_food_api import models
from fast_food_api.models.models import menu

class menu(Resource):

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user == 5:
            parser = reqparse.RequestParser()
            parser.add_argument('product', help='This field cannot be blank', required=True)
            parser.add_argument('description', help='This field cannot be blank', required=True)
            parser.add_argument('price', help='This field cannot be blank', required=True)
            data = parser.parse_args()
            product = data['product'].strip()
            description = data['description'].strip()
            price = data['price'].strip()
            if product == "" or description == "" or price == "":
                return jsonify({"Error": "Sorry one or more fields are incomplete"}), 404
            else:
                data = {"product": product, "description": description, "price": price}
                menu_item = menu()
                return menu_item.new_menu(data)
        else:
            return jsonify({"Error": "Unauthorised"}), 400

    def get(self):
        all_menu_items = menu()
        return all_menu_items.get_menu_items()

