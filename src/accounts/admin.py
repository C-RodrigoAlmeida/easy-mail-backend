from django.contrib import admin
from src.accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email')