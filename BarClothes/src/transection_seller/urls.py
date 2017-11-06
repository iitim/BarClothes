from django.conf.urls import url
from . import views

app_name = 'transaction'

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^order/', views.orderpage, name='order]'),
    url(r'^transcus/', views.transcus, name='transcus'),
    # url(r'^transcus/(?P<num>[0-9]+)', views.upload_slip, name='upload_slip')
]
