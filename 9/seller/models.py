from django.db import models



class seller(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    seller_salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.
