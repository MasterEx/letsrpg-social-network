from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, this is letsrpg home page.")

def user(request, username, template_name='user.html'):
	user = get_object_or_404(User, username=username)
	return render_to_response(template_name, {'homeuser': user},
							  context_instance=RequestContext(request))
	
