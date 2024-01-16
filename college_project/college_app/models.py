from django.db import models
from django.db import models


class StudentApplication(models.Model):
    name = models.CharField(max_length=100,null=True)
    dob = models.DateField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    mail_id = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    course = models.CharField(max_length=50,null=True,blank=True)
    purpose = models.CharField(max_length=50,null=True,blank=True)
    materials_provide = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return '{}'. format(self.name)