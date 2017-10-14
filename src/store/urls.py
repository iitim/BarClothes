from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
    url(r'^$', views.store, name='store'),
    url(r'^seller/$', views.store_detail, name='detail'),
]