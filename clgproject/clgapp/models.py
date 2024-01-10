from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(max_length=250)
    department = models.CharField(max_length=200)
    courses = models.CharField(max_length=150)
    purpose = models.CharField(max_length=120)
    materials_provide = models.CharField(max_length=100)

    def __str__(self):
        return '{}'. format(self.name)

