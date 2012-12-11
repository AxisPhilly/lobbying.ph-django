"""
View for Lobbyist, Firm, Principal and site index page
"""
from __future__ import division
from django.views.generic import ListView
from django.views.generic import DetailView
from lobbyingph.models import Lobbyist, Firm, Principal, Issue, Filing, Official
from django.shortcuts import render
import simplejson as json


def index(request):
    """
    Site index view
    """
    firms = Firm.objects.all()
    principals = Principal.objects.all()
    officials = Official.objects.all()

    # Count up all the money
    filings = Filing.objects.all()
    total_spending = 0
    for filing in filings:
        total_spending += filing.get_total_exp()

    # Sort the base lists
    # stackoverflow.com/questions/930865/
    firms_sorted_clients = sorted(firms,
        key=lambda f: -f.get_client_count())
    p_sorted_spending = sorted(principals,
        key=lambda p: -p.get_total_exp())
    p_sorted_issue_bill = sorted(principals,
        key=lambda p: -p.get_issue_and_bill_count())

    # Then generate top lists
    # http://stackoverflow.com/questions/5306756/
    top_firms = []
    for firm in firms_sorted_clients[:5]:
        top_firms.append({
            'object': firm,
            'count': firm.get_client_count(),
            'percent': "{:.0%}".format(firm.get_client_count() /
                firms_sorted_clients[0].get_client_count())
        })

    top_p_spending = []
    for principal in p_sorted_spending[:5]:
        top_p_spending.append({
            'object': principal,
            'count': principal.get_total_exp(),
            'percent': "{:.0%}".format(principal.get_total_exp() /
                p_sorted_spending[0].get_total_exp())
        })

    top_p_issue_bill = []
    for principal in p_sorted_issue_bill[:5]:
        top_p_issue_bill.append({
            'object': principal,
            'count': principal.get_issue_and_bill_count(),
            'percent': "{:.0%}".format(principal.get_issue_and_bill_count() /
                p_sorted_issue_bill[0].get_issue_and_bill_count())
        })

    context = {
        'lobbyist_count': Lobbyist.objects.count(),
        'firm_count': firms.count(),
        'principal_count': principals.count(),
        'official_count': officials.count(),
        'total_spending': total_spending,
        'top_firms': top_firms,
        'top_principals_by_spending': top_p_spending,
        'top_principals_by_issues_bills': top_p_issue_bill
    }

    return render(request, 'index.html', context)


class IssueDetail(DetailView):
    """
    Issue/Bill detail view
    """
    model = Issue
    template_name = 'issue_detail.html'


class LobbyistList(ListView):
    """
    Table/list view of Lobbyists
    """
    model = Lobbyist
    template_name = 'lobbyist_list.html'


class LobbyistDetail(DetailView):
    """
    Detail view of Lobbyist
    """
    model = Lobbyist
    template_name = 'lobbyist_detail.html'


class FirmList(ListView):
    """
    Table/List view of Firm
    """
    model = Firm
    template_name = 'firm_list.html'


class FirmDetail(DetailView):
    """
    Detail view of Firm
    """
    model = Firm
    template_name = 'firm_detail.html'


class OfficialList(ListView):
    """
    List view for City officials
    """
    model = Official
    template_name = 'official_list.html'


class OfficialDetail(DetailView):
    """
    Detail view for City officials
    """
    model = Official
    template_name = 'official_detail.html'

class PrincipalList(ListView):
    """
    Table/List view of Principal
    """
    model = Principal
    template_name = 'principal_list.html'


class PrincipalDetail(DetailView):
    """
    Detail view of Principal
    """
    model = Principal
    template_name = 'principal_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetail, self).get_context_data(**kwargs)

        # Construct a list that won't need any modification for use
        # in the d3 expenditure donut chart

        # Add the total expenditures first
        exp_data = {}
        exp_data['total'] = []
        percents = self.object.get_exp_percents()
        for exp_type, dollars in self.object.get_exp_totals().items():
            exp_data['total'].append(
            {
                'class': exp_type,
                'dollars': dollars,
                'percent': percents[exp_type]
            })

        # Then add the expenditures for each quarter
        q_percents = self.object.get_exp_percents_by_quarter()
        for quarter, totals in self.object.get_exp_totals_by_quarter().items():
            exp_data[quarter] = []
            for exp_type, dollars in totals.items():
                exp_data[quarter].append({
                    'class': exp_type,
                    'dollars': dollars,
                    'percent': q_percents[quarter][exp_type]
                })

        context['d3_data'] = json.dumps(exp_data)

        context['exp_totals'] = self.object.get_exp_totals()
        context['exp_percents'] = self.object.get_exp_percents()
        context['quarters'] = self.object.filing_set.distinct(
            'quarter', 'year').values('quarter', 'year')

        return context
