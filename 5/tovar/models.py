from django.db import models
class tovars(models.Model):
    typ = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.typ
# Create your models here.
