from django.db import models
class noutbook(models.Model):
    model = models.Charfield(max_length=225)
    color = models.CharField(max_length=225)
    price = models.IntegerField()
    year = models.IntegerField()
    
    def __str__(self):
        return self.model