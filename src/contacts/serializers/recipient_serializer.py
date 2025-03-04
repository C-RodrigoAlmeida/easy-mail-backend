from rest_framework import serializers

from src.contacts.models import RecipientModel

class BaseRecipientSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecipientModel
    fields = ['name', 'email']


class MutateRecipientSerializer(BaseRecipientSerializer):
  class Meta(BaseRecipientSerializer.Meta):
    pass

class DisplayRecipientSerializer(BaseRecipientSerializer):
  class Meta(BaseRecipientSerializer.Meta):
    pass

class GetRecipientSerializer(BaseRecipientSerializer):
  groups = serializers.SerializerMethodField()
  
  class Meta(BaseRecipientSerializer.Meta):
    fields = [*BaseRecipientSerializer.Meta.fields, 'groups']

  def get_groups(self, obj) -> str:
    return obj.get_group()
