from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal, Issue, Filing
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, render_to_response
from decimal import *
from django.db import connection

print connection.queries

def index(request):
    lobbyists = Lobbyist.objects.all()
    firms = Firm.objects.all()
    principals = Principal.objects.all()

    # Count up the top level models
    lobbyist_count = lobbyists.count()
    firm_count = firms.count()
    principal_count = principals.count()

    # Count up all the money
    filings = Filing.objects.all()
    total_spending = 0
    for filing in filings:
        total_spending += filing.get_total_exp()

    # Top 5 lists
    # http://stackoverflow.com/questions/930865/how-to-sort-by-a-computed-value-in-django
    top_firms = sorted(firms, key = lambda f: -f.get_client_count())
    top_principals_by_spending = sorted(principals, key = lambda p: -p.get_total_exp())
    top_principals_by_issues = sorted(principals, key = lambda p: -p.get_issue_bill_count())

    context = {
        'lobbyist_count': lobbyist_count,
        'firm_count': firm_count,
        'principal_count': principal_count,
        'total_spending': total_spending,
        'top_firms': top_firms[:5],
        'top_principals_by_spending': top_principals_by_spending[:5],
        'top_principals_by_issues': top_principals_by_issues[:5]
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