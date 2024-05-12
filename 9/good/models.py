from django.db import models


class goods(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here.
