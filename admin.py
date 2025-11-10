from django.contrib import admin
from .models import Car, RentalRequest

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'price_per_day', 'available', 'created_at']
    list_filter = ['available', 'make', 'year']
    search_fields = ['make', 'model', 'description']
    list_editable = ['available']
    fields = ['make', 'model', 'year', 'color', 'price_per_day', 'description', 'image', 'interior_image', 'available']

@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'car', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer_name', 'customer_email', 'customer_phone']
    readonly_fields = ['created_at']
    list_editable = ['status']
