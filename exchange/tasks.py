import asyncio
from exchange.utils import exchange_rate_task

def fetch_exchange_rate():
    """Crontab задача: добавление раз в минуту курса валюты в БД."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # no running event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(exchange_rate_task.fetch_exchange_rate())


def check_exchange_rates():
    """Выполняется перед запуском сервера: проверка записей в БД."""
    try:
        asyncio.create_task(exchange_rate_task.check_exchange_rates())
    except RuntimeError:
        ...