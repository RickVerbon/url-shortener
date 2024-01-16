from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.


class ActivateUser(models.Model):
    user = models.ForeignKey(User, default=uuid4, on_delete=models.CASCADE)
    token = models.UUIDField(max_length=50)

    def __str__(self):
        return self.user.username
