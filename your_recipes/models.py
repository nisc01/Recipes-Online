from django.db import models
from django.utils import timezone
from django.forms.widgets import HiddenInput

# Create your models here.
class Recipes(models.Model):
    title=models.CharField(max_length=200)
    author_name=models.CharField(max_length=200,blank = True)
    date_posted=models.DateField(default=timezone.localdate(),editable=False)
    image=models.ImageField(upload_to='static/')
    ingredients=models.TextField()
    description=models.TextField()

