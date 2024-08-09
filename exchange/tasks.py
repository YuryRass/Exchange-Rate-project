from exchange.utils import exchange_rate_task


def fetch_exchange_rate():
    exchange_rate_task.fetch_exchange_rate()

def check_exchange_rates():
    exchange_rate_task.check_exchange_rates()