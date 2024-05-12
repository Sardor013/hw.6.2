from django.db import models

class User(models.Model):
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    year = models.IntegerField()
    

# Create your models here.
