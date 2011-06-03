from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def login(request):
    return render_to_response('accounts/login.html',
                               context_instance=RequestContext(request))
