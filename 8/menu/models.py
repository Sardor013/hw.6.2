from django.db import models
class dishes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    minutes = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
