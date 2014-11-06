from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'articulos.views.listar_articulos', name = 'listar_articulos'), 
    # Urls de Django-allauth
    url(r'^accounts/', include('allauth.urls')),
    # Admin de Django
    url(r'^admin/', include(admin.site.urls)),
)


