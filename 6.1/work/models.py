from django.db import models


class works(models.Model):
    name = models.CharField(max_length=225)
    typ = models.CharField(max_length=225)
    salary = models.IntegerField()

    def __str__(self):
        return self.typ
# Create your models here.
