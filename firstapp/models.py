from django.db import models

class Person(models.Model):
    user=models.CharField(max_length=20)
    age=models.ImageField()
    objects=models.Manager()
    DoesNotExist = models.Manager

class Company(models.Model):
    mame=models.CharField(max_length=30)

class Product(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.ImageField()