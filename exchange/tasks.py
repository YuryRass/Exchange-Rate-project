import asyncio

from exchange.utils import exchange_rate_task
from logger import get_logger

logger = get_logger("exchange")


def fetch_exchange_rate():
    """Crontab задача: добавление раз в минуту курса валюты в БД."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # no running event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(exchange_rate_task.fetch_exchange_rate())
        logger.info(f"Добавление курса валюты выполнено успешно")
    except Exception as ex:
        logger.error(f"Ошибка при добавлении курса валюты: {ex}")


def check_exchange_rates():
    """Выполняется перед запуском сервера: проверка записей в БД."""
    try:
        logger.info(f"Началась проверка/добавление данных в обменник")
        asyncio.create_task(exchange_rate_task.check_exchange_rates())
        logger.info(f"Проверка/добавление данных в обменник закончена")
    except RuntimeError as ex:
        logger.error(f"Ошибка при проверке обменника валют: {ex}")
