from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal
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

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetail, self).get_context_data()
        
        # the money
        exp_direct_comm = self.object.filing_set.aggregate(val=Sum('total_exp_direct_comm'))
        exp_indirect_comm = self.object.filing_set.aggregate(val=Sum('total_exp_indirect_comm'))
        exp_other = self.object.filing_set.aggregate(val=Sum('total_exp_other'))

        exp = exp_direct_comm['val'] + exp_indirect_comm['val'] + exp_other['val']
        
        context['totals'] = {
            'exp': exp,
            'exp_direct_comm' : exp_direct_comm,
            'exp_indirect_comm' : exp_indirect_comm,
            'exp_other' : exp_other
        }
        
        for row in self.object.filing_set.all():

            # the lobbying categories
            topics = row.exp_direct_comm_set.distinct('category')
            topic = []

            for t in topics: 
                topic.append(t.category)

            # the lobbying firms
            firms = row.firms.distinct('name')

            # the issues
            issues = row.exp_direct_comm_set.distinct('issue')
            issue = {}

            for i in issues:
                issue[i.issue] = i.get_position_display()

        context['topics'] = topic
        context['firms'] = firms
        context['issues'] = issue
        
        return context