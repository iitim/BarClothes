from django.conf.urls import url, include
from django.contrib import admin
from signup import views
# from .views import signup
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name='signup'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name='home'),
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    # url(r'^accounts/profile', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', views.signup, name='signup'),

]
