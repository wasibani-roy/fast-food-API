# fast-food-API
[![Build Status](https://travis-ci.org/wasibani-roy/fast-food-API.svg?branch=api)]
[![Coverage Status](https://coveralls.io/repos/github/wasibani-roy/fast-food-API/badge.svg?branch=api)](https://coveralls.io/github/wasibani-roy/fast-food-API?branch=api)

# Fast-Food-Fast-app
Fast-Food-Fast-app is a food ordering app. The app is currnetly built using data structures for non persistent data

### Getting started
git clone https://github.com/wasibani-roy/fast-food-API.git into a directory of your choice

#### Prerquisites
Ensure you have python installed globally on your system.

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
| /orders/order_id'| PUT | `edit a single order` |

#### Running tests
Within you're enviroment run command pytest

### Built With
 - Python
 - Flask
 - FlaskRestFul
 - pytest

##### Author 
 - Wasibani Roy

##### Acknowledgement 
 - Andela 
 - David
###### Project Demo
 Here is the link to the App Demo: https://new-fast-food-fast-api-v1.herokuapp.com/order
