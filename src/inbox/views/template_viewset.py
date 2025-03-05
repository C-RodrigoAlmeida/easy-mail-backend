from rest_framework.viewsets import ModelViewSet

from django.db.models import QuerySet

from drf_spectacular.utils import extend_schema

from src.inbox.models import TemplateModel
from src.inbox.serializers import TemplateSerializer

@extend_schema(tags=['Template'])
class TemplateViewSet(ModelViewSet):
  queryset = TemplateModel.objects.all()
  serializer_class = TemplateSerializer
  

  def get_queryset(self) -> QuerySet[TemplateModel]:
    return self.queryset.filter(owner=self.request.user)