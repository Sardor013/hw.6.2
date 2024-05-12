from django.db import models

class ads(models.Model):
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=225)
    job = models.CharField(max_length=225)
    description = models.CharField(max_length=225)  

    def __str__(self):
        return self.description
# Create your models here.
