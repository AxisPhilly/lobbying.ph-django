from django.shortcuts import get_object_or_404, HttpResponse
from django.core import serializers
from lobbyingph.models import Issue, Bill
import json

def index(request, pk):
    issue = get_object_or_404(Issue, pk=pk)

    response = {
        #'name': issue.description,
        'nodes': [
            { 
                'id': 0,
                'type': 'issue',
                'name': issue.description, 
            },
        ],
        'links': []
    }

    for i, x in enumerate(issue.exp_direct_comm_set.all()): 
        response['nodes'].append({
                'type': 'principal',
                'name': x.filing.principal.name,
                'position': x.position,
                'id': x.filing.principal.pk,
                'group': x.filing.principal.pk
            })

        response['links'].append({
                'source': i + 1,
                'target': 0,
                'value': 10
            })

    return HttpResponse(json.dumps(response), mimetype="application/json")