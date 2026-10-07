from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, Payment


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "cart",
        "product",
        "quantity",
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "total",
        "payment_status",
        "order_status",
        "timestamp",
    )

    list_filter = (
        "payment_status",
        "order_status",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    list_editable = (
        "payment_status",
        "order_status",
    )

    inlines = [
        OrderItemInline,
    ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "amount",
        "payment_method",
        "transaction_id",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_method",
    )

    search_fields = (
        "transaction_id",
    )
