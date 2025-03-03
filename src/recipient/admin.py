from django.contrib import admin
from src.recipient.models import RecipientModel

@admin.register(RecipientModel)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'email')
    search_fields = ('owner', 'name', 'email')