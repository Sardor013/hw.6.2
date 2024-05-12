from django.db import models
class Home(models.Model):
    rooms = models.IntegerField()
    price = models.IntegerField()
    village = models.CharField(max_length=225)
    
    def __str__(self):
        return self.village
# Create your models here.
