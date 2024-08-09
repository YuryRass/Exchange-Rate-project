from django.db import models


class ExchangeRate(models.Model):
    CURRENCY_CHOICES = [
        ("USDT", "USDT"),
        ("RUB", "RUB"),
    ]

    currency_from = models.CharField(
        max_length=4,
        choices=CURRENCY_CHOICES,
        verbose_name="Валюта источник",
    )
    currency_to = models.CharField(
        max_length=4,
        choices=CURRENCY_CHOICES,
        verbose_name="Валюта назначение",
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Значение курса",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Дата и время получения курса",
    )

    class Meta:
        verbose_name = "Обмен курса"
        verbose_name_plural = "Обмены курса"
        unique_together = ("currency_from", "currency_to", "timestamp")

    def __str__(self):
        return f"{self.currency_from} -> {self.currency_to}: {self.rate} в {self.timestamp}"
