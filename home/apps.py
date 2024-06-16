from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    AppConfig for the 'home' app.
    This class represents the configuration for the
    'home' app in the Django project.
    It sets the default auto field and specifies the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
