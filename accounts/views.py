from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def login(request):
    return render_to_response('accounts/login.html',
                               context_instance=RequestContext(request))
def check(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)			
	if user is not None:
		if user.is_active:
			#login(request, user)
			return HttpResponse('Authenticated')
		else:
			return render_to_response('accounts/login.html', {
			'error_message': "The user account is disabled.",
		}, context_instance=RequestContext(request))
	else:
		return render_to_response('accounts/login.html', {
			'error_message': "The user doesn't exist.",
		}, context_instance=RequestContext(request))
