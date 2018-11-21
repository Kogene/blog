from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^detail/(?P<id>\d+)', views.detail, name = 'detail'),
    url(r'^create/$', views.create, name = 'create'),
    url(r'^edit/(?P<id>\d+)', views.edit, name = 'edit'),
    url(r'^delete/(?P<id>\d+)', views.delete, name = 'delete'),
    url(r'$', views.home, name = 'home')

]
