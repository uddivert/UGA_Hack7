from django.db import models


# Create your models here.
class RegisterModel(models.Model):
    new_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.new_name

