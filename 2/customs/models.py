from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField

    def __str__(self):
        return self.name

# Create your models here.
