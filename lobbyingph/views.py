from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal, Issue
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, render_to_response
from decimal import *
from django.db import connection

print connection.queries

def index(request):
    lobbyist_count = Lobbyist.objects.count()
    firm_count = Firm.objects.count()
    principal_count = Principal.objects.count()

    context = {
        'lobbyist_count': lobbyist_count,
        'firm_count': firm_count,
        'principal_count': principal_count,
    }

    return render(request, 'index.html', context)

class IssueDetail(DetailView):
    model = Issue
    template_name = 'issue_detail.html'

class LobbyistList(ListView):
    model = Lobbyist
    template_name = 'lobbyist_list.html'

class LobbyistDetail(DetailView):
    model = Lobbyist
    template_name = 'lobbyist_detail.html'

class FirmList(ListView):
    model = Firm
    template_name = 'firm_list.html'

class FirmDetail(DetailView):
    model = Firm
    template_name = 'firm_detail.html'

class PrincipalList(ListView):
    model = Principal
    template_name = 'principal_list.html'

class PrincipalDetail(DetailView):
    model = Principal
    template_name = 'principal_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetail, self).get_context_data(**kwargs)

        context['exp_totals'] = self.object.get_exp_totals()
        context['exp_percents'] = self.object.get_exp_percents()
        return context