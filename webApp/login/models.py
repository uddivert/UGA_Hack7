from django.db import models
from webApp.register.models import RegisterModel


# Create your models here.
class LoginModel(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

