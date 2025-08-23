from django.db import models

# Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=100)

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)


class Student(models.Model):
    college= models.OneToOneField(College,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
