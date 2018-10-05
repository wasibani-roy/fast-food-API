import unittest
import psycopg2
from flask import json,Flask
from fast_food_api.app import APP
from fast_food_api.models.models import Users


con = psycopg2.connect("dbname=fastfoodapp_test user=postgres host=localhost password=root")
cur = con.cursor()

# cur.execute("create table if not exists users(user_id serial primary key,username varchar(25) not null, email varchar(25) not null, password varchar not null)")
# cur.execute("create table if not exists menu(menu_id serial primary key,product varchar(25) not null, description varchar(100) not null, price varchar not null)")
# cur.execute("create table if not exists orders(order_id serial primary key,menu_item_id integer references menu(menu_id), user_id integer references users(user_id), status_code varchar not null)")



class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client()
        con = psycopg2.connect("dbname=fastfoodapp_test user=postgres host=localhost password=root")
        cur = con.cursor()
        data = {'username': 'Dag', 'email': 'dag@gmail.com', 'password': 'dag'}
        # cur.execute("create table if not exists users(user_id serial primary key,username varchar(25) not null, email varchar(25) not null, password varchar not null)")
        # cur.execute("create table if not exists menu(menu_id serial primary key,product varchar(25) not null, description varchar(100) not null, price varchar not null)")
        # cur.execute("create table if not exists orders(order_id serial primary key,menu_item_id integer references menu(menu_id), user_id integer references users(user_id), status_code varchar not null)")
        # self.client.post(self.client.post('/api/v2/signup', data=json.dumps(
        #     data), content_type='application/json'))


    def check_table(self, table_name):
        cur.execute("select * from information_schema.tables where table_name=%s", (table_name,))
        return bool(cur.rowcount)

    def tearDown(self):
        """teardown all intialised variables"""
        cur.execute("drop table users,orders,menu")
        con.commit()


