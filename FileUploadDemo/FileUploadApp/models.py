from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    file=models.FileField(upload_to="profile_pics/")
    class Meta:
        db_table='user'
        
    