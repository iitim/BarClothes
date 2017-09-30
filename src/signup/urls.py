from django.conf.urls import url, include
from django.contrib import admin
from signup import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name='signup'

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
]
