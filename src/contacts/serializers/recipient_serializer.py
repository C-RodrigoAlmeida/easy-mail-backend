from rest_framework import serializers

from src.contacts.models import RecipientModel


class RecipientSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecipientModel
    fields = ['name', 'email']
