from datetime import datetime, timedelta
from enum import Enum
import httpx  # type: ignore
from django.utils import timezone
from asgiref.sync import sync_to_async

from exchange.models import ExchangeRate
from project.settings import GARANTEX_URL


class Rates(str, Enum):
    USDTRUB = "usdtrub"
    RUBUSDT = "rubusdt"


class ExchangeRateTask:

    async def check_exchange_rates(self) -> None:
        last_sync: ExchangeRate = await self.__get_last_rec()
        if last_sync:
            last_time_sync = last_sync.timestamp
            time_now = timezone.now()
            while time_now - last_time_sync > timedelta(minutes=1):
                # Если прошло больше 1 минуты с последнего обновления, обновляем курс
                timestamp = (last_time_sync + timedelta(minutes=1)).timestamp()
                await self.fetch_exchange_rate(timestamp)
                last_time_sync += timedelta(minutes=1)

    async def fetch_exchange_rate(self, timestamp: float | None = None) -> None:
        await self.__add_exchange_rate(timestamp=timestamp)
        # self.__add_exchange_rate(market=Rates.RUBUSDT, timestamp=timestamp)

    async def __add_exchange_rate(
        self, market: str = Rates.USDTRUB, timestamp: float | None = None
    ) -> None:
        usdtrub_params = {
            "market": market.value,
            "timestamp": int(timestamp) if timestamp else "",
            "limit": 1,
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url=GARANTEX_URL, params=usdtrub_params)
                response.raise_for_status()
                rate = response.json()[0].get("price")

            if timestamp:
                naive_datetime = datetime.fromtimestamp(timestamp)
                naive_datetime = timezone.make_aware(naive_datetime)
            else:
                naive_datetime = timezone.now()

            data = {
                "rate": float(rate),
                "currency_from": "USDT" if market == Rates.USDTRUB else "RUB",
                "currency_to": "RUB" if market == Rates.USDTRUB else "USDT",
                "timestamp": naive_datetime,
            }

            await self.__create_rec(**data)
        except httpx.HTTPStatusError as ex:
            print(f"Произошла ошибка HTTP: {ex}")
        except Exception as ex:
            print(f"Произошла ошибка: {ex}")

    async def __get_last_rec(self) -> ExchangeRate | None:
        return await sync_to_async(ExchangeRate.objects.last)()

    async def __create_rec(self, **data) -> None:
        await sync_to_async(ExchangeRate.objects.create)(**data)


exchange_rate_task = ExchangeRateTask()
