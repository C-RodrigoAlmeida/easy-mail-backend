from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class BaseUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password']
    extra_kwargs = {'password': {'write_only': True}}

class UserMutationSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields = [*BaseUserSerializer.Meta.fields, 'first_name', 'last_name']

class UserAuthSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    pass