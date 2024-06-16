from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    AppConfig for the 'checkout' app.

    Configures 'checkout' app: sets default auto field and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
