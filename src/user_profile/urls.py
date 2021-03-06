from django.conf.urls import url, include
from django.contrib import admin
from . import views
app_name = 'user_profile'

urlpatterns = [
    url(r'^change-password/success$', views.success),
    url(r'^$', views.profile, name='profile'),
    url(r'^success$', views.success, name='success'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^cancel$', views.cancel, name='cancel'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^shopstatus/$', views.view_myshop, name='view_myshop'),
    url(r'^shopstatus/order/$', views.orderpage, name='orderpage'),
    url(r'^mycart/', include('mycart.urls'), name='mycart'),
    url(r'^shopstatus/order/(?P<num>[0-9]+)/$', views.orderpage_selected, name='orderpage_selected'),
]
