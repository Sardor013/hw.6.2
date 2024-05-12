from django.db import models
class cars(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=225)
    year = models.IntegerField()

    def __str__(self):
        return self.model

# Create your models here.
