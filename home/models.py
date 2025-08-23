from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True)
    # null is for DB,blank is for Django
    gender = models.CharField(max_length=10, default="Male")
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
