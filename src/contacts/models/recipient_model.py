from django.db import models
from django.contrib.auth import get_user_model


from src.core.base_model import BaseModel

User = get_user_model()

class RecipientModel(BaseModel):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.TextField(null=False, blank=False)
  email = models.EmailField(null=False, blank=False)

  class Meta:
    ordering = ['name']
  
  def get_groups(self) -> str:
    return ', '.join(group.title for group in self.groups.all())

  def __str__(self) -> str:
    return self.email 