from rest_framework import serializers

from src.contacts.models import RecipientGroupModel
from src.contacts.serializers import DisplayRecipientSerializer

class BaseRecipientGroupSerializer(serializers.ModelSerializer):
  recipients = DisplayRecipientSerializer(many=True)

  class Meta:
    model = RecipientGroupModel
    fields = ['title', 'recipients']

class GetRecipientGroupSerializer(BaseRecipientGroupSerializer):
  recipients_amount = serializers.SerializerMethodField()

  class Meta(BaseRecipientGroupSerializer.Meta):
    fields = [*BaseRecipientGroupSerializer.Meta.fields, 'recipients_amount']

  def get_recipients_amount(self, obj) -> int:
    return obj.get_recipients_amount()


class MutateRecipientsGroupSerializer(BaseRecipientGroupSerializer):
  class Meta(BaseRecipientGroupSerializer.Meta):
    pass