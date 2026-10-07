from django.db import models


class DailySales(models.Model):

    date = models.DateField(
        unique=True
    )

    total_orders = models.PositiveIntegerField(
        default=0
    )

    total_sales = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return str(self.date)
