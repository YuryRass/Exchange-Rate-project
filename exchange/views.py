from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from exchange.models import ExchangeRate

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>Обмены курса</h1>")

def rates(request: HttpRequest):
    exchange_rates = ExchangeRate.objects.all()
    return render(request, 'exchange/rates.html', {'rates': exchange_rates})