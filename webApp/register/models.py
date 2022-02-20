from django.db import models


# Create your models here.
class RegisterModel(models.Model):
    new_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.new_name

