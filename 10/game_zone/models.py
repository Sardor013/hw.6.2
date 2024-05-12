from django.db import models
class game(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name    

# Create your models here.
