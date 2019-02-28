from django.db import models
import csv

# Create your models here.
class WineInfo(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
    price = models.FloatField()
    cat = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class WineWord(models.Model):
    word = models.CharField(max_length=100)
    time = models.IntegerField()
    type = models.CharField(max_length=10)
