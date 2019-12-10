from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    fans = models.ManyToManyField('accounts.User', related_name='star')
    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})
    
    def __str__(self):
        return self.username