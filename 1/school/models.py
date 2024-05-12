from django.db import models

class products(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
