from django.contrib.auth.models import User
from letsrpg.events.models import *
from letsrpg.events.forms import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def to_event(request, template_name='events/eventform.html'):
	form = EventForm()
	return render_to_response(template_name, {'form': form},
							  context_instance=RequestContext(request))

@login_required
def create_event(request, template_name='events/eventdone.html'):
	gm = request.POST['game_master']
	slots = request.POST['slots']
	location = request.POST['location']
	event = Event(game_master=gm,slots=slots,slots_taken=1,location=location)
	event.save()
	return render_to_response(template_name,
							  context_instance=RequestContext(request))

@login_required
def done(request, template_name='events/eventdone.html'):
	form = EventForm()
	return render_to_response(template_name, {'form': form},
							  context_instance=RequestContext(request))
