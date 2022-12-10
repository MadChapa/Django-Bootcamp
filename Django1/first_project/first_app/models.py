from django.db import models
from django.db.models import Model


# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    # topic=models.ForeignKey(Topic)
    topic= models.ForeignKey('Topic', on_delete=models.PROTECT)

    name=models.CharField(max_length=200, unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    # name=models.ForeignKey(Webpage)
    name= models.ForeignKey('Webpage', on_delete=models.PROTECT)

    date=models.DateTimeField()

    def __str__(self):
        return str(self.date)
