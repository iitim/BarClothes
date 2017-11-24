from django.conf.urls import url
from . import views

app_name = 'myproduct'

urlpatterns = [
    url(r'^new/$', views.product_new, name='new'),
    # url(r'^delete/$', views.product_delete, name='delete'),
    url(r'^update/(?P<num>[0-9]+)/$', views.product_update, name='update'),
    url(r'^delete/(?P<num>[0-9]+)/$', views.product_delete, name='delete'),
]