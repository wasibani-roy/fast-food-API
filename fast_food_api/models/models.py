from fast_food_api import database_query
from passlib.hash import pbkdf2_sha256 as sha256
from flask import jsonify
from flask_jwt_extended import \
    (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class Users:
    def check_user(self,user_data):
        x=database_query.database_query()
        if x.check_table("users") :
            email = user_data["email"]
            username = user_data["username"]
            password = user_data['password']
            '''user_id = user["userid"]'''
            query = "insert into users(username, email, password) values (%s, %s, %s)"
            user_details = (username, email, password)
            database_query.cur.execute(query, user_details)
            database_query.con.commit()
            return ("table exists data added")
        else:
            database_query.cur.execute\
                ("create table users(user_id serial primary key,username varchar(25) not null, email varchar(25) not null, password varchar not null)")
            email = user_data["email"]
            username = user_data["username"]
            password = user_data['password']
            '''user_id = user["userid"]'''
            query = "insert into users(username, email, password) values (%s, %s, %s)"
            user_details = ( username, email, password)
            database_query.cur.execute(query, user_details)
            database_query.con.commit()
            return ("table now created and data added")
        '''try:
            cur.execute(query, data)
            new_user=cur.commit()
            cur.close()
            return new_user
        except:

            cur.execute(query, data)
            new_user=cur.commit()
            cur.close()
            return new_user'''

    '''def login_users(self, username):
        database_query.cur.execute("select * from users where username =%s", [username])
        result = database_query.cur.rowcount
        if result > 0:
            data = database_query.cur.fetchone()
            password = data[3]
            # print(password)
            return password
        else:
            return {"Error": "Sorry invalid username and password"}'''
    def authenticate_user(self, username, password_candidate):
        database_query.cur.execute("select * from users where username =%s", [username])
        result = database_query.cur.rowcount
        if result > 0:
            data = database_query.cur.fetchone()
            user_id = data[0]
            password = data[3]
            if sha256.verify(password_candidate, password):
                access_token = create_access_token(identity= user_id)
                refresh_token = create_refresh_token(identity= user_id)
                return jsonify({"Message": "Logged in as {}".format(username),
                                "Access token": access_token, "Refresh token": refresh_token}), 200
            else:
                return jsonify({"Error": "Invalid username and password "}), 404
        else:
            return jsonify({"Error": "No user Found"}), 500

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    '''@staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)'''

    def new_menu(self, menu_data):
        x = database_query.database_query()
        if x.check_table("menu"):
            product = menu_data["product"]
            description = menu_data["description"]
            price = menu_data["price"]
            '''user_id = user["userid"]'''
            query = "insert into menu(product, description, price) values (%s, %s, %s)"
            user_details = (product, description, price)
            database_query.cur.execute(query, user_details)
            database_query.con.commit()
            return ("Menu item added")
        else:
            database_query.cur.execute \
                (
                    "create table menu(menu_id serial primary key,product varchar(25) not null, description varchar(100) not null, price varchar not null)")
            product = menu_data["product"]
            description = menu_data["description"]
            price = menu_data["price"]
            query = "insert into menu(product, description, price) values (%s, %s, %s)"
            menu_details = (product, description, price)
            database_query.cur.execute(query, menu_details)
            database_query.con.commit()
            return ("Menu item now created")

    def get_menu_items(self):
        x = database_query.database_query()
        database_query.cur.execute("select * from menu")
        result = database_query.cur.rowcount
        if result > 0:
            data = database_query.cur.fetchall()
            return jsonify(data), 200
        else:
            return jsonify({"Error": "No such table exists"}), 500
