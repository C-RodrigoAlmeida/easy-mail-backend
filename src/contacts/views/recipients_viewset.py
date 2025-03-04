from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from src.contacts.models import RecipientModel
from src.contacts.serializers import MutateRecipientSerializer, GetRecipientSerializer

class RecipientViewSet(viewsets.ModelViewSet):
    queryset = RecipientModel.objects.all()

    def get_serializer_class(self) -> type[ModelSerializer]:
        if self.action in ['list', 'retrieve']:
            return GetRecipientSerializer
        return MutateRecipientSerializer
