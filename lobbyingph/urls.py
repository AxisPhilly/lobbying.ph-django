from django.conf.urls import patterns, include, url
from lobbyingph.views import LobbyistList, LobbyistDetail
from lobbyingph.views import FirmList, FirmDetail
from lobbyingph.views import PrincipalList, PrincipalDetail

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LobbyistList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lobbyists/$', LobbyistList.as_view()),
    url(r'^lobbyist/(?P<pk>\d+)/$', LobbyistDetail.as_view()),
    url(r'^firms/$', FirmList.as_view()),
    url(r'^firm/(?P<pk>\d+)/$', FirmDetail.as_view()),
    url(r'^principals/$', PrincipalList.as_view()),
    url(r'^principal/(?P<pk>\d+)/$', PrincipalDetail.as_view()),
)
