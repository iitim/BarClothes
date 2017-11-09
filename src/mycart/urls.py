from django.conf.urls import url
from . import views

app_name = 'mycart'

urlpatterns = [
    url(r'^$', views.mycart, name='mycart'),
]