from django.db import models

class work(models.Model):
    name = models.CharField(max_length=100)
    salary  = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
