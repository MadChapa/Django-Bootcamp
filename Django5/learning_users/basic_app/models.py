from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class UserprofileInfo(models.Model):

    user=models.OneToOneField(User, on_delete=models.PROTECT)

    #additional classes
    Portfolio_site=models.URLField(blank=True)

    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
