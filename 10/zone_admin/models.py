from django.db import models


class zone_admin(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    salary = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# Create your models here.
