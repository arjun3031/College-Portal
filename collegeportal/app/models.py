from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    coursename=models.CharField(max_length=255,null=True)
    fees=models.IntegerField(null=True)

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    age=models.IntegerField(null=True)
    phone=models.CharField(max_length=255,null=True)
    image=models.ImageField(upload_to='images',null=True)
    courses=models.CharField(max_length=255,null=True)


class Student(models.Model):
    studentname=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)
    age=models.IntegerField(null=True)
    date=models.DateField(null=True)
    image=models.ImageField(upload_to='images',null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
