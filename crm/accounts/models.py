import email
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.test import tag

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200 , null = True)
    phone = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)


    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (
              ('Indoor','Indoor'),
              ('Out Door','Out Door'),

                )
    name = models.CharField(max_length=200 , null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200 , null = True , choices=CATEGORY)
    description = models.CharField(max_length=200 , null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)
    # tag = models.ManyToManyField(tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivered'),

            )
    customer = models.ForeignKey(Employee, null=True,on_delete=models.SET_NULL )
    product = models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add= True, null = True)
    status = models.CharField(max_length=200 , null = True , choices=STATUS)

  