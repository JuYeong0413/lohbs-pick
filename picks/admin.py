from django.contrib import admin
from .models import *

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'collection_name',
    )

    search_fields = (
        'collection_name',
    )