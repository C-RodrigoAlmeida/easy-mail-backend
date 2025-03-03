from django.contrib import admin
from src.contacts.models import RecipientModel

@admin.register(RecipientModel)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'email')
    search_fields = ('owner', 'name', 'email')