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

    def get_context_data(self, **kwargs):
        context = super(FirmDetail, self).get_context_data()

        # the clients (principals)
        clients = self.object.filing_set.distinct('principal')
        client = []

        for c in clients:
            client.append(c.principal)

        topic = []

        # FIX: Distinct needs to be executed on the whole filing set,
        # not just row by row. Shouldn't have to do list membership test
        for row in self.object.filing_set.all():
            # the lobbying categories
            topics = row.exp_direct_comm_set.distinct('category')

            for t in topics: 
                if (t.category not in topic):
                    topic.append(t.category)

        context['clients'] = client
        context['topics'] = topic

        return context

class PrincipalList(ListView):
    model = Principal

class PrincipalDetail(DetailView):
    model = Principal