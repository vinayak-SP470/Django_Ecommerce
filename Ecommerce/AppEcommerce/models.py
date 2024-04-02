from django.db import models
from django.contrib.auth.models import AbstractUser


class Demo(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20, blank=False)

