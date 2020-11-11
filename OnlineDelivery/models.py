from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    CATEGORY = (
        ('Кальян','Кальян'),
        ('Табак','Табак'),
        ('Чаша','Чаша'),
        ('Угли','Угли'),
    )
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    decsription = models.CharField(max_length=50,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name


class Adresses(models.Model):
    adress = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)


class Actions(models.Model):
    first = models.CharField(max_length=200, null=True)
    second = models.CharField(max_length=200, null=True)
    third = models.CharField(max_length=200, null=True)


class Comments(models.Model):
    pass



class Orders(models.Model):
    product = models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

