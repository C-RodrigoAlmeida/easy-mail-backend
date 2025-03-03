from django.db import models
from django.contrib.auth.models import User

from src.core.base_model import BaseModel


class RecipientGroupModel(BaseModel):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.TextField(null=False, blank=False)
  recipients = models.ManyToManyField("recipient.RecipientModel", related_name="groups")