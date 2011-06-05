from django.contrib.auth.models import User
from letsrpg.messages.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def show_messages(request, template_name='messages/messages.html'):
	messages = Message.objects.filter(userid_receiver=request.user,status="P")
	return render_to_response(template_name, {'messages': messages},
							  context_instance=RequestContext(request))
	
