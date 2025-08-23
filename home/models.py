from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default="Male")
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

student=Student.objects.create(name="Abhijeet", age=23, gender="Male", phone_number="3453453454", email="sdf@gamil.com", date_of_birth="2212-03-03")

student.save()

student=Student.objects.get(id=1)

print(student.name)

student=Student.objects.all()
print(student)

student=Student.objects.filter(name="Abhijeet")
print(student)

# update
student.age=24
student.save()

# retrieve
student=Student.objects.get(id=1)
student.delete()

student=Student.objects.all().delete()