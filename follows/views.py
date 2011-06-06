from django.contrib.auth.models import User
from letsrpg.follows.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def follow(request, template_name='follows/follows.html'):
	homeuser = request.POST['followed']
	followed = User.objects.get(username=homeuser)
	follow = Follow(request.user,followed)
	#follow.save()
	return render_to_response(template_name,
							  context_instance=RequestContext(request))
