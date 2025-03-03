from django.db import models
from django.contrib.auth.models import User

from src.core.base_model import BaseModel

class TemplateModel(BaseModel):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.TextField(max_length=255, null=False, blank=False)
  content = models.TextField(max_length=5000)