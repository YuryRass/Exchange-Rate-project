from django.apps import AppConfig


class ExchangeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "exchange"

    def ready(self):
        from exchange.tasks import check_exchange_rates
        check_exchange_rates()
