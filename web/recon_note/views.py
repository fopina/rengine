import json

from django.shortcuts import render
from django.http import JsonResponse

from recon_note.models import *
from startScan.models import *

def list_note(request):
    context = {}
    context['recon_note_active'] = 'true'
    return render(request, 'note/index.html', context)


def add_note(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        note = TodoNote()
        note.title = body['title']
        note.description = body['description']

        # check for existence of scan history
        if 'scan_history' in body:
            scan_history = ScanHistory.objects.get(id=body['scan_history'])
            note.scan_history = scan_history

        if 'subdomain' in body:
            subdomain = Subdomain.objects.get(id=body['subdomain'])
            note.subdomain = subdomain

        note.save()

    return JsonResponse({'status': True})
