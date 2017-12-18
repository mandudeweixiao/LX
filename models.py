from django.db import models

# Create your models here.
class Grade(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateField()
    ggirlnum=models.IntegerField()
    gboynum=models.IntegerField()
    isdelete=models.BooleanField()
class Student(models.Model):
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()
    sinfo=models.CharField(max_length=100)
    isdelete=models.BooleanField()
    sgrade=models.ForeignKey('Grade')
