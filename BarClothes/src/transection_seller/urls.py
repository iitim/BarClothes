from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^order/', views.orderpage, name='order]'),
    url(r'^transcus/', views.orderpage, name='transcus'),
]
