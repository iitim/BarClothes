from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^top_up/$', views.top_up, name='top_up'),
    url(r'^wait_page/$', views.wait_page, name='wait_page'),
    url(r'^$', views.activate_store, name='activate_store'),
    url(r'^free_trial/$', views.free_trial, name='free_trial'),
    url(r'^topup_transaction/$', views.topup_transaction, name='topup_transaction'),

]
