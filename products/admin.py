from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'name',
        'price',
        'category',
    )

    search_fields = (
        'title',
    )