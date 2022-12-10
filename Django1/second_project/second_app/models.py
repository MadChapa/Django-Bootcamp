from django.db import models
from django.db.models import Model

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200, unique=True)


    # def __str__(self):
    #     return self.top_name
