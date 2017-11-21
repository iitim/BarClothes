from django.conf.urls import url
from . import views

app_name = 'catalog'

urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^top/$', views.top, name='top'),
    url(r'^jacket/$', views.jacket, name='jacket'),
    url(r'^dress/$', views.dress, name='dress'),
    url(r'^skirt/$', views.skirt, name='skirt'),
    url(r'^pants/$', views.pants, name='pants'),
    url(r'^shorts/$', views.shorts, name='shorts'),
    url(r'^t-shirt/$', views.tshirt, name='tshirt'),
    url(r'^suits/$', views.suits, name='suits'),
    url(r'^bag/$', views.bag, name='bag'),
    url(r'^shoes/$', views.shoes, name='shoes'),
    url(r'^accessory/$', views.accessory, name='accessory'),
    url(r'^(?P<num>[0-9]+)/$', views.catalog),
    url(r'^top/(?P<num>[0-9]+)/$', views.top),
    url(r'^jacket/(?P<num>[0-9]+)/$', views.jacket),
    url(r'^dress/(?P<num>[0-9]+)/$', views.dress),
    url(r'^skirt/(?P<num>[0-9]+)/$', views.skirt),
    url(r'^pants/(?P<num>[0-9]+)/$', views.pants),
    url(r'^shorts/(?P<num>[0-9]+)/$', views.shorts),
    url(r'^t-shirt/(?P<num>[0-9]+)/$', views.tshirt),
    url(r'^suits/(?P<num>[0-9]+)/$', views.suits),
    url(r'^bag/(?P<num>[0-9]+)/$', views.bag),
    url(r'^shoes/(?P<num>[0-9]+)/$', views.shoes),
    url(r'^accessory/(?P<num>[0-9]+)/$', views.accessory),
]
