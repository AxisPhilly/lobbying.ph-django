from django.shortcuts import get_object_or_404, HttpResponse
from django.core import serializers
from lobbyingph.models import Issue, Bill
import json

def index(request, pk):
    issue = get_object_or_404(Issue, pk=pk)

    response = {
        'nodes': [],
        'links': []
    }

    for exp in issue.exp_direct_comm_set.all(): 
        
        p = {
            'type': 'principal',
            'name': exp.filing.principal.name,
            'position': exp.position,
            'size': 20
        }

        response['nodes'].append(p)

        links = []

        for o in exp.officials.all():
            item = {
                'type': 'official',
                'name': o.last_name,
                'size': 10
            }

            if item not in response['nodes']:
                response['nodes'].append(item)

            links.append(response['nodes'].index(item))

        for link in links: 
            response['links'].append({
                'source': response['nodes'].index(p),
                'target': link,
                'value': 30
            })

    return HttpResponse(json.dumps(response), mimetype="application/json")