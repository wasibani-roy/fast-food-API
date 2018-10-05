from fast_food_api import database_query
from passlib.hash import pbkdf2_sha256 as sha256
from flask import jsonify
from flask_jwt_extended import \
    (create_access_token, create_refresh_token)

class Users:
    def __init__(self, username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def check_user(self):
        new_user=database_query.database_query()
        if new_user.check_table("users") :
            query = "insert into users(username, email, password) values (%s, %s, %s)"
            user_details = (self.username, self.email, sha256.hash(self.password))
            database_query.cur.execute(query, user_details)
            database_query.con.commit()
            return jsonify({"success": "User added"}),201
        else:
            database_query.cur.execute\
                ("create table users(user_id serial primary key,username varchar(25) not null, email varchar(25) not null, password varchar not null)")
            query = "insert into users(username, email, password) values (%s, %s, %s)"
            user_details = ( self.username, self.email, self.password)
            database_query.cur.execute(query, user_details)
            database_query.con.commit()
            return jsonify({"success": "User created"}),201
    def authenticate_user(self):
        database_query.cur.execute("select * from users where username =%s", [self.username])
        result = database_query.cur.rowcount
        print(result)
        if result > 0:
            data = database_query.cur.fetchone()
            user_id = data[0]
            password = data[3]
            if sha256.verify(self.password, password):
                access_token = create_access_token(identity= user_id)
                refresh_token = create_refresh_token(identity= user_id)
                return jsonify({"Message": "Logged in as {}".format(self.username),
                                "Access token": access_token}), 200
            else:
                return jsonify({"Error": "Invalid username and password"}), 404
        else:
            return jsonify({"Error": "No user Found"}), 500


class Order:
    def __init__(self,user_id,menu_id,status,order_id):
        self.user_id = user_id
        self.menu_item_id = menu_id
        self.status = "new"
        self.order_id = order_id

    def add_order(self):
        x = database_query.database_query()
        if x.check_table("orders"):

            query = "insert into orders(menu_item_id, user_id, status_code) values (%s, %s, %s)"
            order_details = (self.menu_item_id, self.user_id, self.status)
            database_query.cur.execute(query, order_details)
            database_query.con.commit()
            return jsonify({"success": "order placed"}), 200
        else:
            database_query.cur.execute \
                    (
                    "create table orders(order_id serial primary key,menu_item_id integer references menu(menu_id), user_id integer references users(user_id), status_code varchar not null)")

            query = "insert into orders(menu_item_id, user_id, status_code) values (%s, %s,%s)"
            order_details = (self.menu_item_id, self.user_id, self.status)
            database_query.cur.execute(query, order_details)
            database_query.con.commit()
            return jsonify({"success": "order placed"}), 200

    def get_order_items(self):
        database_query.cur.execute("select users.username, menu.product, menu.price\
         from orders join users on orders.user_id=users.user_id join menu on orders.menu_item_id=menu.menu_id")
        data = database_query.cur.fetchall()
        return jsonify({"orders":data}), 200

    def order_by_id(self):
        database_query.cur.execute\
            ("select users.username, menu.product, menu.price from orders join users on orders.user_id=users.user_id join menu on orders.menu_item_id=menu.menu_id where order_id= %s", [self.order_id])
        data = database_query.cur.fetchall()
        return jsonify({"user_order":data}), 200

    def update_order(self,status):
        self.status = status
        database_query.cur.execute("update orders set status_code=%s where order_id=%s",[self.status, self.order_id])
        update_row = database_query.cur.rowcount
        if update_row >0:
            database_query.cur.execute("select users.username, menu.product, menu.price, orders.status_code from\
             orders join users on orders.user_id=users.user_id join\
              menu on orders.menu_item_id=menu.menu_id\
              where order_id=%s", [self.order_id])
            data = database_query.cur.fetchall()
            database_query.con.commit()
            return jsonify({"updated_order":data})
        return ("No update made")

    def get_user_order(self):
        database_query.cur.execute("select menu.product, menu.price, orders.status_code\
         from orders join users on orders.user_id=users.user_id join menu on orders.menu_item_id=menu.menu_id\
          where users.user_id=%s", [self.user_id])
        found_row = database_query.cur.rowcount
        if found_row > 0:
            data = database_query.cur.fetchall()
            return jsonify(data)
        return ("No history found")


class Menu:
    def __init__(self, product, description, price):
        self.product = product
        self.description = description
        self.price = price
    def new_menu(self):
        x = database_query.database_query()
        if x.check_table("menu"):
            '''user_id = user["userid"]'''
            query = "insert into menu(product, description, price) values (%s, %s, %s)"
            user_details = (self.product, self.description, self.price)
            database_query.cur.execute(query, user_details)
            database_query.con.commit()
            return ("Menu item added")
        else:
            database_query.cur.execute \
                (
                    "create table menu(menu_id serial primary key,product varchar(25) not null, description varchar(100) not null, price varchar not null)")
            query = "insert into menu(product, description, price) values (%s, %s, %s)"
            menu_details = (self.product, self.description, self.price)
            database_query.cur.execute(query, menu_details)
            database_query.con.commit()
            return ("Menu item now created")

    def get_menu_items(self):
        database_query.cur.execute("select * from menu")
        result = database_query.cur.rowcount
        if result > 0:
            data = database_query.cur.fetchall()
            return jsonify(data), 200
        else:
            return jsonify({"Error": "No such table exists"}), 500
