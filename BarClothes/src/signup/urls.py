from django.conf.urls import url, include
from django.contrib import admin
<<<<<<< HEAD
from signup import views
# from .views import signup
=======
from .views import signup
>>>>>>> 9e911d7ed4ade2456e6a4afceb9b006322230f57
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name='signup'

urlpatterns = [
<<<<<<< HEAD
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name='home'),
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    # url(r'^accounts/profile', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', views.signup, name='signup'),
=======
    # url(r'^$', views.home, name='home'),
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    # url(r'^accounts/profile', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', signup, name='signup'),
>>>>>>> 9e911d7ed4ade2456e6a4afceb9b006322230f57

]
