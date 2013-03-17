from shortcuts import template_response, json_response, html_response, not_found, redirect, now, datetime_to_unix
from django.db.models import Q
from tonehack.models import Instrument
from datetime import datetime

def index(request):
    instruments = Instrument.objects.filter()
    response = {
        'instruments': instruments,
    }
    return template_response('index.html', response, request)

def article(request):
    response = {}
    return template_response('article.html', response, request)

def save(request):
    waves = request.POST['waves']

    instrument = Instrument(
        waves_json=waves,
        ip=request.META['REMOTE_ADDR'],
        date=datetime.utcnow(),
    )

    instrument.save()
    response = {
        'status': 'ok',
    }
    return json_response(response)