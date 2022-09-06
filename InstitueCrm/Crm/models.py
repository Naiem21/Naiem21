from tracemalloc import start
from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200)
    duration=models.IntegerField()
    fess=models.FloatField()
    class Meta:
        db_table='course'

class Subject(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    courses=models.ManyToManyField(Course) 
    class Meta:
        db_table='subject'

class Batch(models.Model):
    startDate=models.DateField()
    startTime=models.TimeField()
    endTime=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.RESTRICT)
    class Meta:
        db_table='batch'

class Student(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    marks=models.FloatField()
    batch=models.ManyToManyField(Batch)
    class Meta:
        db_table='student'
        
class Faculty (models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    salary=models.FloatField()
    qulifications=models.CharField(max_length=100)
    skills=models.ManyToManyField(Subject)
    batches=models.ManyToManyField(Batch)
    class Meta:
        db_table='faculty'

class FeesRecord(models.Model):
    student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    batch=models.ForeignKey(Batch,null=True,on_delete=models.SET_NULL)
    amount=models.FloatField()
    date=models.DateField()
    time=models.TimeField()
    mode=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    class Meta:
        db_table='fees_record'

       
class Admin(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    class Meta:
        db_table='admin'