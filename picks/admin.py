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


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
      list_display = (
        'id',
        'name',
        'period',
        'collection_total',
      )

      search_fields = (
        'name',
      )