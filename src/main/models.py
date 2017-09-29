from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class UserExtendData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=45) # Customer or Seller
    address = models.CharField(max_length=45)
    tel_no = models.CharField(max_length=45)

# currently hasn't data to be extended
class SellerExtendData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField()
    detail = models.CharField(max_length=500)
    amount = models.IntegerField()
    picture = models.ImageField(upload_to='product_pic/', default = 'static/img/catalog-minimize.jpg')
    #seller = models.ForeignKey(SellerExtendData, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=45)

class ProductToTag(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    tag =  models.ForeignKey(Tag, on_delete=models.CASCADE)

class WaitForBillingProduct(models.Model):
    customer =  models.ForeignKey(UserExtendData, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField()
    total_price = models.FloatField()
    status = models.CharField(max_length=45)
    selected_date = models.DateTimeField(default=datetime.now, blank=True)
    expire_date = models.DateTimeField(default=datetime.now, blank=True)
