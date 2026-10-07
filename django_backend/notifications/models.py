from django.conf import settings
from django.db import models


class Notification(models.Model):

    TYPE_CHOICES = [
        ("order_confirmed", "Order Confirmed"),
        ("payment_success", "Payment Success"),
        ("payment_failed", "Payment Failed"),
        ("order_shipped", "Order Shipped"),
        ("order_delivered", "Order Delivered"),
        ("low_stock", "Low Stock"),
        ("general", "General"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default="general"
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.type}"
