from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(Product)
#admin.site.register(User)
admin.site.register(UserExtendData)
admin.site.register(SellerExtendData)