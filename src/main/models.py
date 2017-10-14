from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

from django.utils import timezone


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
    id_num = models.CharField(max_length=13)
    address = models.CharField(max_length=1000)
    tel_no = models.CharField(max_length=45)
    picture = models.ImageField(upload_to='user_pic/', default = 'product_pic/catalog-minimize.jpg')
    selling_expire_date = models.DateTimeField(default=datetime.now)

    def can_sell(self):
        now = timezone.now()
        return self.selling_expire_date > now

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField(default=0)
    detail = models.CharField(max_length=500)
    amount = models.IntegerField(default=1)
    reserved = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    view =  models.IntegerField(default=0)
    seller = models.ForeignKey(UserExtendData, on_delete=models.CASCADE)
    picture_path = models.ImageField(upload_to='product_pic/', default = 'product_pic/catalog-minimize.jpg')
    tags = models.ManyToManyField(Tag, blank=True)

    def remain(self):
        return self.amount - self.sold - self.reserved

    def __str__(self):
        return self.name + " (" + self.type +")"

class Transaction(models.Model):
    customer = models.ForeignKey(UserExtendData, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    total_price = models.FloatField()
    status = models.CharField(max_length=3, choices=TRANSACTION_STATUS_CHOICES, default='wpy')
    create_date = models.DateTimeField(default=datetime.now)
    expire_date = models.DateTimeField(default=datetime.now() + timedelta(days=3))
    payment_date = models.DateTimeField(null = True, blank= True)
    sent_date = models.DateTimeField(null=True, blank=True)
    receive_date = models.DateTimeField(null=True, blank=True)
    payment_picture = models.ImageField(upload_to='payment_pic/', blank=True)
    transport_code = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.customer.user.username + " buy " + self.product.name +" at " + self.create_date.__str__() + " from " + self.product.seller.user.username + " current state:" + self.status

class TransactionLog(models.Model):
    customer = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    amount = models.IntegerField(default=1)
    total_price = models.FloatField()
    status = models.CharField(max_length=3, choices=TRANSACTION_STATUS_CHOICES, default='suc')
    create_date = models.DateTimeField(default=datetime.now)
    payment_date = models.DateTimeField(null=True, blank=True)
    sent_date = models.DateTimeField(null=True, blank=True)
    receive_date = models.DateTimeField(null=True, blank=True)
    transport_code = models.CharField(max_length=13, blank=True)

    @staticmethod
    def from_transaction(transaction):
        return TransactionLog(customer=transaction.customer.user.username,
                              seller=transaction.product.seller.user.username,
                              product=transaction.product.__str__(),
                              amount=transaction.amount,
                              total_price=transaction.total_price,
                              status=transaction.status,
                              create_date=transaction.create_date,
                              payment_date=transaction.payment_date,
                              sent_date=transaction.sent_date,
                              receive_date=transaction.receive_date,
                              transport_code=transaction.transport_code)

    def __str__(self):
        return self.customer + " buy " + self.product +" at " + self.create_date.__str__() + " from " + self.seller + " state:" + self.status


class TopUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slip_pic = models.ImageField(upload_to='slip_pic/', blank=True)
    price = models.FloatField(default=0)
    top_up_date = models.DateTimeField(default=datetime.now)
