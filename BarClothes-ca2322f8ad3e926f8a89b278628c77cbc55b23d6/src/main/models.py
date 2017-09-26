from django.db import models
from datetime import datetime

class Customer(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    regisDate = models.DateTimeField(default=datetime.now, blank=True)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    telNo = models.CharField(max_length=45)


class Seller(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    regisDate = models.DateTimeField(default=datetime.now, blank=True)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    telNo = models.CharField(max_length=45)


class Product(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    createDate = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField()
    detail = models.CharField(max_length=500)
    amount = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=45)

class ProductToTag(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    tag =  models.ForeignKey(Tag, on_delete=models.CASCADE)
