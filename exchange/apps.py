import os
from django.apps import AppConfig


class ExchangeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "exchange"

    def ready(self):
        if not os.getenv("RUNNING_CRONTAB"):
            from exchange.tasks import check_exchange_rates

            check_exchange_rates()
