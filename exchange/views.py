from asgiref.sync import sync_to_async
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from exchange.models import ExchangeRate


class ExchangeView(View):
    async def get(self, request: HttpRequest):
        exchange_rates = await sync_to_async(list)(ExchangeRate.objects.all())
        return render(request, "exchange/rates.html", {"rates": exchange_rates})
