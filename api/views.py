from django.shortcuts import get_object_or_404, HttpResponse
from django.core import serializers
from lobbyingph.models import Issue, Bill
import json

def index(request, pk):
    issue = get_object_or_404(Issue, pk=pk)

    response = {
        'name': issue.description,
        'support': {},
        'oppose': {}
    }

    for x in issue.exp_direct_comm_set.all(): 
        if x.position == 1:
            response['support'][x.filing.principal.pk] = x.filing.principal.name
        elif x.position == 2:
            response['oppose'][x.filing.principal.pk] = x.filing.principal.name

    return HttpResponse(json.dumps(response), mimetype="application/json")