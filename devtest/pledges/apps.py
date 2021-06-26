from django.apps import AppConfig
from django.db.models import signals


def call_on_class_prepared(sender, **kwargs):
    if hasattr(sender, "on_class_prepared"):
        sender.on_class_prepared()


class PledgesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pledges"

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        signals.class_prepared.connect(call_on_class_prepared)
