from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=127)