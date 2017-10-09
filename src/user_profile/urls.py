from django.conf.urls import url, include
from django.contrib import admin
from . import views
app_name = 'user_profile'

urlpatterns = [
    url(r'^change-password/success$', views.success),
    # url(r'^profile$', views.profile, name='profile'),
    url(r'^$', views.profile, name='profile'),
    url(r'^success$', views.success, name='success'),
    # url(r'^edit$', views.profile_edit, name='profile_edit'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    # url(r'^change-password/profile$', views.profile),
    url(r'^cancel$', views.cancel, name='cancel'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk')
]
