from django.contrib import admin
from .models import *
from datetime import datetime

class CanSellFilter(admin.SimpleListFilter):
    title = 'Can sell?'

    parameter_name = 'can_sell'

    def lookups(self, request, model_admin):
        return (
            ('n', 'can_not_sell'),
            ('c', 'can_sell'),
        )

    def queryset(self, request, queryset):
        from django.utils import timezone
        now = timezone.now()
        if self.value() == 'c':
            return queryset.filter(selling_expire_date__gte=now)
        if self.value() == 'n':
            return queryset.filter(selling_expire_date__lte=now)

class UserExtendDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'image','can_sell', 'tel_no', 'selling_expire_date',)
    list_filter = ( CanSellFilter,)
    search_fields = ['user__username']

admin.site.register(UserExtendData, UserExtendDataAdmin)

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('name','image', 'type', 'create_date', 'price','amount','sold','remain','seller',)
    search_fields = ['name', 'seller__user__username', 'tags__name']
    list_filter = ('type', 'tags',)

admin.site.register(Product, ProductAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Tag, TagAdmin)

def generate_log(modeladmin, request, queryset):
    for t in queryset:
        log = TransactionLog.from_transaction(t)
        log.save()
generate_log.short_description = "generate transaction log"

class TransactionAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('customer', 'product', 'amount', 'total_price', 'status', 'create_date', 'expire_date',)
    search_fields = ['customer__user__username', 'product__name',]
    list_filter = ('status',)
    actions = [generate_log]

admin.site.register(Transaction, TransactionAdmin)

class TransactionLogAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('customer', 'seller', 'product', 'amount', 'total_price', 'status', 'create_date')
    search_fields = ['customer', 'seller', 'product']
    list_filter = ('status',)

admin.site.register(TransactionLog, TransactionLogAdmin)

class TopUpAdmin(admin.ModelAdmin):
    date_hierarchy = 'top_up_date'
    list_display = ('user', 'top_up_date', 'price',)
    search_fields = ['user__username']

admin.site.register(TopUp,TopUpAdmin )
