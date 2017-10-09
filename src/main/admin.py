from django.contrib import admin
from .models import *

admin.site.register(UserExtendData)
# admin.site.register(SellerExtendData)
admin.site.register(Product)
admin.site.register(Tag)
# admin.site.register(ProductToTag)
# admin.site.register(WaitForBillingProduct)

