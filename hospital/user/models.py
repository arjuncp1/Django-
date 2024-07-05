from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()



class Medicine(models.Model):
    mname = models.CharField(max_length=100)
    price = models.IntegerField()
    expiry_date = models.DateField()
    pharma_company =models.CharField(max_length=100)

