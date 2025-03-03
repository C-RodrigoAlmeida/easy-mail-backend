from django.contrib import admin
from src.inbox.models import TemplateModel

@admin.register(TemplateModel)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'content')
    search_fields = ('owner', 'title')