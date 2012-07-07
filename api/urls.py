from django.conf.urls import patterns, include, url
from api.views import *

urlpatterns = patterns('',
    url(r'^issue/(?P<pk>\d+)/$', issue),
)
