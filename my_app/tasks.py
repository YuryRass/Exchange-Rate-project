from .models import ExchangeRate


def update_db():
    # Retrieve notifications to be sent via email
    ExchangeRate.objects.create(
        currency_from="USDT",
        currency_to="RUB",
        rate=45.32,
    )
