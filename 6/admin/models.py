from django.db import models
class admink(models.Model):
    user = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    job = models.CharField(max_length=225)

    def __str__(self):
        return self.name
# Create your models here.
