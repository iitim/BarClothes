from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^top_up/$', views.top_up, name='top_up'),
    url(r'^$', views.activate_store, name='activate_store'),
]
