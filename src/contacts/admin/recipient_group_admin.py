from django.contrib import admin
from src.contacts.models.recipient_group_model import RecipientGroupModel

@admin.register(RecipientGroupModel)
class RecipientGroupAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title')
    search_fields = ('owner', 'title')