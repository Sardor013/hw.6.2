from django.db import models
class phones(models.Model):
    model = models.CharField(max_length=225)
    make = models.CharField(max_length=225)
    color = models.CharField(max_length=15)
    price = models.IntegerField()

    def __str__(self):
        return self.model
# Create your models here.
