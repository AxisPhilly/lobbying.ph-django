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

    for i, x in enumerate(issue.exp_direct_comm_set.all()): 
        
        p = {
            'type': 'principal',
            'name': x.filing.principal.name,
            'position': x.position,
            'size': 10
        }

        response['nodes'].append(p)

        links = []

        for c, o in enumerate(x.officials.all()):
            item = {
                'type': 'official',
                'last_name': o.last_name,
                'size': 5
            }

            if item not in response['nodes']:
                response['nodes'].append(item)

            links.append(response['nodes'].index(item))

        for link in links: 
            response['links'].append({
                'source': response['nodes'].index(p),
                'target': link,
                'value': 10
            })

    return HttpResponse(json.dumps(response), mimetype="application/json")