from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    salary=models.FloatField()
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    class Meta:
        db_table='employee'