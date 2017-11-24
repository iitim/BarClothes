"""BarClothes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from main import views
from signup import views as signup_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^store/', include('store.urls')),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^shop/', include('catalog.urls'), name='shop'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', signup_views.signup, name='signup'),
    url(r'^profiles/', include('user_profile.urls'), name='profile'),
    url(r'^product/', include('product.urls'), name='product'),
    url(r'^myproduct/', include('myproduct.urls'), name='myproduct'),
    url(r'^activate_store/', include('activate_store.urls'),name='activate_store'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
