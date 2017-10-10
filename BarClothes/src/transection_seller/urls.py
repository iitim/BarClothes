from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
]