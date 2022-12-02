from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Thing(models.Model):
    name = models.TextField()
    description = models.TextField(default='0000000')
    quantity = models.IntegerField()
