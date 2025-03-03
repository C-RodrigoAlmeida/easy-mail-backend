from django.contrib import admin
from src.recipient_group.models import RecipientGroupModel

@admin.register(RecipientGroupModel)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title')
    search_fields = ('owner', 'title')