from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Student(models.Model):
    # Choose ONE of these relationship types:
    
    # ForeignKey (many-to-one)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    # OR OneToOneField (one-to-one) 
    # department = models.OneToOneField(Department, on_delete=models.CASCADE)
    
    # OR ManyToManyField (many-to-many)
    # department = models.ManyToManyField(Department)

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default="Male")
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  