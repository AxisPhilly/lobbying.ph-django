from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal, Issue
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, render_to_response

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

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetail, self).get_context_data()
        
        # the money
        exp_direct_comm = self.object.filing_set.aggregate(val=Sum('total_exp_direct_comm'))
        exp_indirect_comm = self.object.filing_set.aggregate(val=Sum('total_exp_indirect_comm'))
        exp_other = self.object.filing_set.aggregate(val=Sum('total_exp_other'))

        exp = float(exp_direct_comm['val'] or 0) + float(exp_indirect_comm['val'] or 0) + float(exp_other['val'] or 0)
        
        context['totals'] = {
            'exp': exp if exp else 0,
            'exp_direct_comm' : exp_direct_comm['val'] if exp_direct_comm['val'] else 0,
            'exp_indirect_comm' : exp_indirect_comm['val'] if exp_indirect_comm['val'] else 0,
            'exp_other' : exp_other['val'] if exp_other['val'] else 0
        }
        
        topic = []
        issue = {}
        bill = {}
        firms = None

        for row in self.object.filing_set.all():

            # the lobbying categories
            topics = row.exp_direct_comm_set.distinct('category')

            for t in topics: 
                topic.append(t.category)

            # the lobbying firms
            firms = row.firms.distinct('name')

            # the issues
            issues = row.exp_direct_comm_set.distinct('issue')
            
            for i in issues:
                if i.issue != None:
                    issue[i.issue] = i.get_position_display()

            # the bills
            bills = row.exp_direct_comm_set.distinct('bill')
            
            for b in bills:
                if b.bill != None:
                    bill[b.bill] = b.get_position_display()

        context['topics'] = topic
        context['firms'] = firms
        context['issues'] = issue
        context['bills'] = bill
        
        return context