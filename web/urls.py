from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^tramites$', views.tramites),
        url(r'^registro$', views.registro),
        url(r'^login$', views.login),
        url(r'^logout$', views.logout),
        url(r'^documentos/(?P<filename>.*)$', views.documentos),
    ]
