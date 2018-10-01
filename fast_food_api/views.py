"""
Routes module to handle request urls
"""
# from fast_food_api.models import resources
from fast_food_api.models.menu import menu
from fast_food_api.models.users import user_login, user_registration


class Urls:
    """
        Class to generate urls
    """

    @staticmethod
    def generate(app):
        """
        Generate urls
        :param app:
        :return:
        """
        app.add_url_rule('/api/v2/register/', view_func=user_registration.as_view('register'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/login/', view_func=user_login.as_view('login'),
                         methods=['post'], strict_slashes=False)
        app.add_url_rule('/api/v2/menu/', view_func=menu.as_view('add_menu'),
                         methods=['post'], strict_slashes=False)
        app.add_url_rule('/api/v2/menu/', view_func=menu.as_view('list_menu_items'),
                         methods=['get'], strict_slashes=False)
