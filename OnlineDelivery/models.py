from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal
from django.db.models import F, Sum


class Hookah(models.Model):
    category = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    decsription = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Bowl(models.Model):
    category = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    decsription = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Tabacco(models.Model):
    category = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    decsription = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Coals(models.Model):
    category = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    decsription = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name


class Complect(models.Model):
    hookah = models.ForeignKey(Hookah,null=True,on_delete=models.SET_NULL)
    bowl = models.ForeignKey(Bowl, null=True, on_delete=models.SET_NULL)
    tabacco = models.ForeignKey(Tabacco, null=True, on_delete=models.SET_NULL)
    coals = models.ForeignKey(Coals, null=True, on_delete=models.SET_NULL)
    price = models.FloatField(editable=False,null=True,blank=True)
    sale = models.BooleanField(null=True)

class Adresses(models.Model):
    adress = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)


class Actions(models.Model):
    first = models.CharField(max_length=200, null=True)
    second = models.CharField(max_length=200, null=True)
    third = models.CharField(max_length=200, null=True)


class Comments(models.Model):
    pass




