from django.db import models

# Create your models here.
class Form(models.Model):
    first_name=models.CharField(max_length=300)
    dateofbirth=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=500)
    district=models.CharField(max_length=300)
    branch=models.CharField(max_length=300)
    accounttype=models.CharField(max_length=300)
    materials=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name




