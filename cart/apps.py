from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    AppConfig for the 'cart' app.

    This class represents the configuration for the 'cart' app
    in the Django project.
    It sets the default auto field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
