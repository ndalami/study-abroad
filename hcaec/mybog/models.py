from django.db import models
from django.utils import timezone

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length = 250)
    email= models.EmailField()
    subject = models.CharField(max_length = 250)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length = 250)
    author = models.CharField(max_length = 50)
    about = models.CharField(max_length = 50)
    bdy = models.TextField(max_length = 10000)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class University(models.Model):
    universityName = models.CharField(max_length = 50)
    universityCountry = models.CharField(max_length = 50)
    universityContinent = models.CharField(max_length = 50)
    

    def __str__(self):
       return self.universityName
    
class Student(models.Model):
    studentFirstName = models.CharField(max_length = 50)
    studentMiddleName = models.CharField(max_length = 50)
    studentLastName = models.CharField(max_length = 50)
    studentGender = models.CharField(max_length = 50)
    studentEmail = models.EmailField()
    studentPhone = models.IntegerField()
    studentLevel = models.CharField(max_length = 50)
    studentCourse = models.CharField(max_length = 50)
    studentCountry = models.CharField(max_length = 50, blank=True)
    parentPhone = models.IntegerField()

    def __str__(self):
       return self.studentFirstName + ' ' + self.studentMiddleName + ' ' + self.studentLastName