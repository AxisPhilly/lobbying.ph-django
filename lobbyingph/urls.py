from django.conf.urls import patterns, include, url
from lobbyingph.views import index
from lobbyingph.views import LobbyistList, LobbyistDetail
from lobbyingph.views import FirmList, FirmDetail
from lobbyingph.views import PrincipalList, PrincipalDetail
from lobbyingph.views import IssueDetail
import settings

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^lobbyists/$', LobbyistList.as_view()),
    url(r'^lobbyists/(?P<pk>\d+)/$', LobbyistDetail.as_view()),
    url(r'^firms/$', FirmList.as_view()),
    url(r'^firms/(?P<pk>\d+)/$', FirmDetail.as_view()),
    url(r'^principals/$', PrincipalList.as_view()),
    url(r'^principals/(?P<pk>\d+)/$', PrincipalDetail.as_view()),
    #url(r'^issues/(?P<pk>\d+)/$', IssueDetail.as_view())
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )