from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.index,name='web-inicio'),
        url(r'^tramites$', views.tramites),
        url(r'^registro$', views.registro),
        url(r'^login$', views.login),
        url(r'^logout$', views.logout),
        url(r'^noticias/$', views.noticias,name='web-noticias'),
        url(r'^documentos/(?P<filename>.*)$', views.documentos),
        url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]
