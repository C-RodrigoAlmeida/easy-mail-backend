from rest_framework import serializers

from src.inbox.models import TemplateModel

class TemplateSerializer(serializers.ModelSerializer):
  class Meta:
    model = TemplateModel
    fields = ['title', 'content']