from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'collection',
        'collection_name',
        'created_at',
    )

    search_fields = (
        'collection_name',
    )


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'quantity',
        'price',
        'created_at',
    )
