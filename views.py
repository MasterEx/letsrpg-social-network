from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from letsrpg.events.models import *

def index(request,template_name='index.html'):
	return render_to_response(template_name,
						  context_instance=RequestContext(request))

def user(request, username, template_name='user.html'):
	user = get_object_or_404(User, username=username)
	messages = Message.objects.filter(status='A')
	try:
		Follow.objects.get(userid_follower=request.user,userid_followed=user)
		follow = False
	except:
		follow = True
	return render_to_response(template_name, {'homeuser': user,'follow': follow,
												'messages': messages},
							  context_instance=RequestContext(request))
	
def event(request, username, template_name='event.html'):
	user = get_object_or_404(User, username=username)
	eventpl = EventPlayer.objects.filter(userid=user)
	events = []
	for eventp in eventpl:
		events.append(eventp.eventid)
	return render_to_response(template_name, {'homeuser': user,'events': events},
							  context_instance=RequestContext(request))
