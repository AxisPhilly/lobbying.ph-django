from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal, Issue
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, render_to_response
from decimal import *

def index(request):
    lobbyists = Lobbyist.objects.count()
    firms = Firm.objects.count()
    principals = Principal.objects.count()

    context = {
        'lobbyists': lobbyists,
        'firms': firms,
        'principals': principals
    }

    return render(request, 'lobbyingph/index.html', context)

class IssueDetail(DetailView):
    model = Issue

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