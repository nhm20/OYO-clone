from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default="Male")
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    student_registration = models.DateField()
    percentage = models.FloatField()

