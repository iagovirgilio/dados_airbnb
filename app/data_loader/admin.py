from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser, Stay

@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    pass