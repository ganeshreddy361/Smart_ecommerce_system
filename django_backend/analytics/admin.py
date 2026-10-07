from django.contrib import admin
from .models import DailySales


@admin.register(DailySales)
class DailySalesAdmin(admin.ModelAdmin):

    list_display = (
        "date",
        "total_orders",
        "total_sales",
        "updated_at",
    )

    ordering = (
        "-date",
    )
