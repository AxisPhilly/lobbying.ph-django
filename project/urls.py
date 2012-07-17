from django.conf.urls import patterns, include, url
from django.contrib.flatpages import urls
from search.views import CustomSearchView
from haystack.views import search_view_factory
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('', include('lobbyingph.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^search/', search_view_factory(
        view_class=CustomSearchView,
        ), name='haystack_search'),
    url(r'^about/', include(urls.urlpatterns)),
    url(r'^admin/', include(admin.site.urls)),
)