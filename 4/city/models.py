from django.db import models

class city(models.Model):
    name = models.CharField(max_length=100)
    villages = models.IntegerField()
    aholi = models.IntegerField()

# Create your models here.
