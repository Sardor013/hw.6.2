from django.db import models

class worker(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    salary = models.IntegerField()
# Create your models here.
