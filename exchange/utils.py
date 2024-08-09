from datetime import datetime, timedelta
from enum import Enum
import requests
from django.utils import timezone

from exchange.models import ExchangeRate
from project.settings import GARANTEX_URL


class Rates(str, Enum):
    USDTRUB = "usdtrub"
    RUBUSDT = "rubusdt"


class ExchangeRateTask:

    def check_exchange_rates(self) -> None:
        last_sync = ExchangeRate.objects.last()
        if last_sync:
            last_time_sync = last_sync.timestamp
            time_now = timezone.now()
            while time_now - last_time_sync > timedelta(minutes=1):
                # Если прошло больше 1 минуты с последнего обновления, обновляем курс
                timestamp = (last_time_sync + timedelta(minutes=1)).timestamp()
                self.fetch_exchange_rate(timestamp)
                last_time_sync += timedelta(minutes=1)

    def fetch_exchange_rate(self, timestamp: float | None = None) -> None:
        self.__add_exchange_rate(timestamp=timestamp)
        # self.__add_exchange_rate(market=Rates.RUBUSDT, timestamp=timestamp)

    def __add_exchange_rate(
        self, market: str = Rates.USDTRUB, timestamp: float | None = None
    ) -> None:
        usdtrub_params = {
            "market": market,
            "timestamp": int(timestamp) if timestamp else "",
            "limit": 1,
        }
        response = requests.get(url=GARANTEX_URL, params=usdtrub_params)
        response.raise_for_status()
        rate = response.json()[0].get("price")

        data = {
            "rate": float(rate),
            "currency_from": "USDT" if market == Rates.USDTRUB else "RUB",
            "currency_to": "RUB" if market == Rates.USDTRUB else "USDT",
            "timestamp": datetime.fromtimestamp(timestamp) if timestamp else datetime.now()
        }

        ExchangeRate.objects.create(**data)


exchange_rate_task = ExchangeRateTask()
