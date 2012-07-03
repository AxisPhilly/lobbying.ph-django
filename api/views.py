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
            'size': 15,
            'content': exp.filing.principal.name
        }

        response['nodes'].append(p)

        links = []

        for o in exp.officials.all():
            item = {
                'type': 'official',
                'name': o.last_name,
                'size': 7,
                'agency': 'agency_' + str(o.agency.pk),
                'content': o.first_name + ' ' + o.last_name + ' ' + o.title
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