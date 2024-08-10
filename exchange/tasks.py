import asyncio
from exchange.utils import exchange_rate_task


def fetch_exchange_rate():
    asyncio.run(exchange_rate_task.fetch_exchange_rate())


def check_exchange_rates():
    asyncio.run(exchange_rate_task.check_exchange_rates())