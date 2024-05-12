from django.db import models
class magazin(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    year = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner
# Create your models here.
