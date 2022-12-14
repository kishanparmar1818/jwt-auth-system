from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
