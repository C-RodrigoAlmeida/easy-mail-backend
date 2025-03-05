from django.db import models
from django.contrib.auth import get_user_model

from src.core.base_model import BaseModel

User = get_user_model()

class TemplateModel(BaseModel):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.TextField(max_length=255, null=False, blank=False)
  content = models.TextField(max_length=5000)