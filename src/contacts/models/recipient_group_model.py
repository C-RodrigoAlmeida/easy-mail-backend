from django.db import models
from django.contrib.auth.models import User

from src.core.base_model import BaseModel
from src.contacts.models import RecipientModel

class RecipientGroupModel(BaseModel):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.TextField(null=False, blank=False)
  recipients = models.ManyToManyField(RecipientModel, related_name="groups")

  class Meta:
    ordering = ['title']

  def get_recipients_amount(self) -> int:
    return self.recipients.count()

  def __str__(self) -> str:
    return self.title