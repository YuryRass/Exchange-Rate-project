from django.contrib import admin

from .models import ExchangeRate


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ("currency_from", "currency_to", "rate", "timestamp")
    search_fields = ("currency_from", "currency_to")
