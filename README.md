# fast-food-API
[![Build Status](https://travis-ci.org/wasibani-roy/fast-food-API.svg?branch=ft-challenge-3-api)](https://travis-ci.org/wasibani-roy/fast-food-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/082f4322dff29552df76/maintainability)](https://codeclimate.com/github/wasibani-roy/fast-food-API/maintainability)

# Fast-Food-Fast-app
Fast-Food-Fast-app is a food ordering app. The app is currnetly built using data structures for non persistent data.It is designed to enable a user to place an order for a meal from the comfort of there office or home

### Getting started
git clone https://github.com/wasibani-roy/fast-food-API.git into a directory of your choice

#### Prerquisites
Ensure you have python installed globally on your system.
Ensure you have setup Postgres database

#### Installing
cd into that folder
Set up an virtual enviroment
run pip install requirements.txt

#### Running the application
in terminal run command python app.py

##### Routes
|  EndPoint   | Methods | Functionality |
| ------------ |------------| ------------ |
| /order | GET | `Fetches all orders made`  |
| /orders/order_id | GET | `Fetches a specific order by id` |
| /order | POST | `add a new order`  |
| /orders/order_id'| PUT | `update order details` |
| /api/v2/signup/'| POST | `Create an account` |
| /api/v2/login/'| GET | `Log into the app` |
| /api/v2/menu/'| POST | `Create a menu item` |
| /api/v2/menu/'| GET| `List all orders` |
| /api/v2/user/order/'| Get | `Retrive user order history` |

#### Running tests
Within you're enviroment run command pytest

### Built With
 - Python
 - Flask
 - FlaskRestFul
 - pytest
 - postgres

##### Author 
 - Wasibani Roy

##### Acknowledgement 
 - Andela 
 - Arnold
###### Project Demo
 Here is the link to the App Demo: https://wasibani-roy-fast-food-app-v2.herokuapp.com/
