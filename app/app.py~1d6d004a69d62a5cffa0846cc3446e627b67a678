from flask import Flask
from flask_restful import Api
import resources
app = Flask(__name__)
app.debug=True
api = Api(app)
api.add_resource(resources.make_order, '/order')
api.add_resource(resources.Orders, '/order')
api.add_resource(resources.specific_order, '/order/<id>')
api.add_resource(resources.update_order, '/order/<id>')


if __name__ == '__main__':
	app.run()