from django.conf.urls import patterns, include, url
from django.contrib.flatpages import urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('', include('lobbyingph.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^about/', include(urls.urlpatterns)),
)