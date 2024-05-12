from django.db import models
class courses(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    lengt_course = models.IntegerField()
# Create your models here.
