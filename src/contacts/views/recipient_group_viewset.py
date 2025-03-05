from django.db.models import QuerySet

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from drf_spectacular.utils import extend_schema

from src.contacts.models import RecipientGroupModel
from src.contacts.serializers import MutateRecipientsGroupSerializer, GetRecipientGroupSerializer

@extend_schema(tags=['Recipient Groups'])
class RecipientGroupViewSet(ModelViewSet):
    queryset = RecipientGroupModel.objects.all()

    def get_queryset(self) -> QuerySet[RecipientGroupModel]:
        return self.queryset.filter(owner=self.request.user)

    def get_serializer_class(self) -> type[ModelSerializer]:
        if self.action in ['list', 'retrieve']:
            return GetRecipientGroupSerializer
    
        return MutateRecipientsGroupSerializer
