from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'creator', ]
    list_filter = ['status', 'creator', ]
    list_display_links = ['title', ]


