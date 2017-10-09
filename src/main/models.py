from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

USER_TYPE_CHOICES = (
    ('C', 'Customer'),
    ('S', 'Seller'),
)

PRODUCT_TYPE_CHOICES = (
    ('Top', 'TOP'),
    ('Jac', 'Jacket'),
    ('Dre', 'Dress'),
    ('Ski', 'Skirt'),
    ('Pan', 'Pants'),
    ('Sht', 'Shorts'),
    ('T-s', 'T-shirt'),
    ('Sui', 'Suits'),
    ('Bag', 'Bag'),
    ('Sho', 'Shoes'),
    ('Acc', 'Accessory'),
)

class UserExtendData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type =  models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    id_num = models.CharField(max_length=13)
    address = models.CharField(max_length=1000)
    tel_no = models.CharField(max_length=45)
    bill_pic = models.ImageField(upload_to='bill_pic/', blank=True)

# currently hasn't data to be extended
class SellerExtendData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField()
    detail = models.CharField(max_length=500)
    amount = models.IntegerField()
    seller = models.ForeignKey(SellerExtendData, on_delete=models.CASCADE)
    picture_path = models.ImageField(upload_to='product_pic/', default = 'product_pic/catalog-minimize.jpg')

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
