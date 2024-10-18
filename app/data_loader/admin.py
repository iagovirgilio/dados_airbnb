from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser, Stay

@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'name', 'host_name', 'neighbourhood', 'price', 'price_category', 'availability_365', 'monthly_occupancy', 'temperature')
    list_filter = ('neighbourhood', 'room_type', 'availability_365')
    search_fields = ('name', 'host_name', 'neighbourhood')
    ordering = ('-price',)

    def monthly_occupancy(self, obj):
        occupied_days = 365 - obj.availability_365
        occupancy_rate = (occupied_days / 365) * 100
        return f"{occupancy_rate:.1f}%"

    def price_category(self, obj):
        if obj.price < 100:
            return 'Barato'
        elif obj.price < 300:
            return 'Moderado'
        else:
            return 'Caro'
    price_category.short_description = 'Categoria de Preço'
