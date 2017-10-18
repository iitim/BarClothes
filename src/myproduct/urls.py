from django.conf.urls import url
from . import views

app_name = 'myproduct'

urlpatterns = [
    url(r'^new/$', views.product_new, name='new'),
]