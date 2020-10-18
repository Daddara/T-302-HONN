from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from frontend_logger.forms.frontend_event_form import FrontendEventForm
from frontend_logger.models import FrontendEvent, FRONTEND_EVENT_TYPES
# Create your views here.

@csrf_exempt
def log_frontend_event(request):
    if request.method != 'POST':
        return HttpResponse(status=200)
    
    form = FrontendEventForm(data=request.POST)
    if not form.is_valid():
        print(form.errors)
        return HttpResponse(status=400)
    if form.cleaned_data['event_type'] not in FRONTEND_EVENT_TYPES:
        return HttpResponse(status=400)

    session_meta = form.cleaned_data['session_meta']
    if len(session_meta) == 0:
        session_meta = None

    event = FrontendEvent(
        event_type=form.cleaned_data['event_type'],
        user_id=form.cleaned_data['user_id'],
        current_url=form.cleaned_data['current_url'],
        event_meta=form.cleaned_data['event_meta'],
        session_meta=session_meta
    )
    event.save()
    return HttpResponse(status=200)


