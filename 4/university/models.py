from django.db import models
class university(models.Model):
    name = models.CharField(max_length=100)
    students = models.IntegerField()
    teachers = models.IntegerField
    groups = models.IntegerField
# Create your models here.
