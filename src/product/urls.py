from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    url(r'^(?P<num>[0-9]+)/$', views.product_view, name='view'),
]