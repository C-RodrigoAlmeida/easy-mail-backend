from django.db.models import QuerySet

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from drf_spectacular.utils import extend_schema

from src.contacts.models import RecipientModel
from src.contacts.serializers import MutateRecipientSerializer, GetRecipientSerializer

@extend_schema(tags=['Recipient'])
class RecipientViewSet(ModelViewSet):
    queryset = RecipientModel.objects.all()

    def get_queryset(self) -> QuerySet[RecipientModel]:
        return self.queryset.filter(owner=self.request.user)

    def get_serializer_class(self) -> type[ModelSerializer]:
        if self.action in ['list', 'retrieve']:
            return GetRecipientSerializer
    
        return MutateRecipientSerializer
