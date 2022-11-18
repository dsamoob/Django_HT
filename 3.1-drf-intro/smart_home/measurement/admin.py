from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_sensor', 'temperature', 'created_at']
    list_filter = ['temperature', 'created_at']

