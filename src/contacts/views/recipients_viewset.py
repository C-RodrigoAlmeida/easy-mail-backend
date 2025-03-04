from rest_framework import viewsets

from src.contacts.models import RecipientModel
from src.contacts.serializers import RecipientSerializer

class RecipientViewSet(viewsets.ModelViewSet):
  queryset = RecipientModel.objects.all()
  serializer_class = RecipientSerializer