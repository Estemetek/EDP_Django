from django.db import models

# Create your models here.
class Student(models.Model):
    whole_name=models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=5)
    gender = models.CharField(max_length=1)

class Add(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=4)
    gender = models.CharField(max_length=2)