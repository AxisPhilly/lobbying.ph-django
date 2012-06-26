from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal

class LobbyistList(ListView):
    model = Lobbyist

class LobbyistDetail(DetailView):
    model = Lobbyist

class FirmList(ListView):
    model = Firm

class FirmDetail(DetailView):
    model = Firm

class PrincipalList(ListView):
    model = Principal

class PrincipalDetail(DetailView):
    model = Principal