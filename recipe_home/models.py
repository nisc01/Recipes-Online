from django.db import models


# Create your models here.
#model to create new user
class AddUser(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=20)



