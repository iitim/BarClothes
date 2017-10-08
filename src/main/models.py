from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

USER_STATUS_CHOICES = (
    ('n', 'can_not_sell'),
    ('c', 'can_sell'),
)

PRODUCT_TYPE_CHOICES = (
    ('Top', 'top'),
    ('Jac', 'jacket'),
    ('Dre', 'dress'),
    ('Ski', 'skirt'),
    ('Pan', 'pants'),
    ('Sht', 'shorts'),
    ('T-s', 't-shirt'),
    ('Sui', 'suits'),
    ('Bag', 'bag'),
    ('Sho', 'shoes'),
    ('Acc', 'accessory'),
)

TRANSACTION_STATUS_CHOICES = (
    ('wpy', 'wait_for_pay'),
    ('wac', 'wait_for_admin_confirm'),
    ('wss', 'wait_for_seller_sent'),
    ('wp1', 'wait_for_receive_product_1'),
    ('wp2', 'wait_for_receive_product_2'),
    ('suc', 'success'),
    ('cnp', 'customer_not_pay'),
    ('ccl', 'customer_cancel'),
    ('cnr', 'customer_not_receive_product'),
    ('sns', 'seller_not_sent_product'),
)


class UserExtendData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status =  models.CharField(max_length=1, choices=USER_STATUS_CHOICES, default='n')
    id_num = models.CharField(max_length=13)
    address = models.CharField(max_length=1000)
    tel_no = models.CharField(max_length=45)
    picture = models.ImageField(upload_to='user_pic/', default = 'product_pic/catalog-minimize.jpg')
    selling_expire_date = models.DateTimeField(default=datetime.now)
# currently hasn't data to be extended
# class SellerExtendData(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField(default=0)
    detail = models.CharField(max_length=500)
    amount = models.IntegerField(default=1)
    reserved = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    seller = models.ForeignKey(UserExtendData, on_delete=models.CASCADE)
    picture_path = models.ImageField(upload_to='product_pic/', default = 'product_pic/catalog-minimize.jpg')

    def __str__(self):
        return self.name + "  " + self.type

class Tag(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class ProductToTag(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    tag =  models.ForeignKey(Tag, on_delete=models.CASCADE)

class Transaction(models.Model):
    customer = models.ForeignKey(UserExtendData, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    total_price = models.FloatField()
    status = models.CharField(max_length=3, choices=TRANSACTION_STATUS_CHOICES, default='wpy')
    create_date = models.DateTimeField(default=datetime.now)
    expire_date = models.DateTimeField(default=datetime.now)
    payment_picture = models.ImageField(upload_to='payment_pic/', blank=True)
    transport_code = models.CharField(max_length=13, blank=True)
    title_string = models.CharField(max_length=100)

    def __str__(self):
        return self.title_string

class TopUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slip_pic = models.ImageField(upload_to='slip_pic/', blank=True)
    top_up_date = models.DateTimeField(default=datetime.now)
