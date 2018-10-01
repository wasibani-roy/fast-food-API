from flask import Flask
import fast_food_api.config.config
from fast_food_api.views import Urls
from flask_jwt_extended import JWTManager


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        """
        Method create a flask object
        :param config: None
        :return: app
        """
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Urls.generate(app)
        return app


APP = Server().create_app(config=fast_food_api.config.config.DevelopmentConfig)
APP.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(APP)
