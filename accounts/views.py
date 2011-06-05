from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from letsrpg.accounts.forms import *
from letsrpg.accounts.models import *
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings
from django.utils.http import urlquote, base36_to_int
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *

@csrf_protect
def signup(request, template_name='registration/signup.html', 
		   email_template_name='registration/signup_email.html',
		   signup_form=UserCreationForm,
		   token_generator=default_token_generator,
		   post_signup_redirect=None):
	if post_signup_redirect is None:
		post_signup_redirect = reverse('letsrpg.accounts.views.signup_done')
	if request.method == "POST":
		form = signup_form(request.POST)
		if form.is_valid():
			opts = {}
			opts['use_https'] = request.is_secure()
			opts['token_generator'] = token_generator
			opts['email_template_name'] = email_template_name
			if not Site._meta.installed:
				opts['domain_override'] = RequestSite(request).domain
			form.save(**opts)
			return HttpResponseRedirect(post_signup_redirect)
	else:
		form = signup_form()
	return render_to_response(template_name, {'form': form,}, 
							  context_instance=RequestContext(request))

def signup_done(request, template_name='registration/signup_done.html'):
	return render_to_response(template_name, 
							  context_instance=RequestContext(request))

def signup_confirm(request, uidb36=None, token=None,
				   token_generator=default_token_generator,
				   post_signup_redirect=None):
	assert uidb36 is not None and token is not None #checked par url
	if post_signup_redirect is None:
		post_signup_redirect = reverse('letsrpg.accounts.views.signup_complete')
	try:
		uid_int = base36_to_int(uidb36)
	except ValueError:
		raise Http404

	user = get_object_or_404(User, id=uid_int)
	context_instance = RequestContext(request)

	if token_generator.check_token(user, token):
		context_instance['validlink'] = True
		user.is_active = True
		user.save()
	else:
		context_instance['validlink'] = False
	return HttpResponseRedirect(post_signup_redirect)

def signup_complete(request, template_name='registration/signup_complete.html'):
	return render_to_response(template_name, 
							  context_instance=RequestContext(request, 
															  {'login_url': settings.LOGIN_URL}))

@login_required												  
def signed_in(request, template_name='accounts/profile.html'):
	return render_to_response(template_name, 
							  context_instance=RequestContext(request))

@login_required	
def go_to_settings(request, template_name='accounts/settings.html'):
	user = 	request.user
	passform = PasswordChangeForm(user)
	mailform = EmailForm()
	try:
		profile = UserProfile.objects.get(userid=user)
		form = UserProfileForm(
			initial={'last_name': user.last_name, 'first_name': user.first_name,
			'location': profile.location, 'age': profile.age, 'notes': profile.notes}
		)
	except:
		form = UserProfileForm()
	return render_to_response(template_name,
							  {'form': form ,'passform': passform,
								'mailform': mailform},
							  context_instance=RequestContext(request))

@login_required	
def save_profile(request, template_name='accounts/settings_change.html'):
	form = UserProfileForm(request.POST)
	user = request.user
	try:
		profile = UserProfile.objects.get(userid=user)
		try:
			int(request.POST['age'])
			profile.age = request.POST['age']
		except:
			return render_to_response(template_name, {'error_message': "Age has to be an integer!"},
							  context_instance=RequestContext(request))
		profile.location = request.POST['location']
		profile.notes = request.POST['notes']
		profile.save()
	except:
		profile = UserProfile()
		profile.userid = user
		try:
			int(request.POST['age'])
			profile.age = request.POST['age']
		except:
			True
		profile.location = request.POST['location']
		profile.notes = request.POST['notes']
		profile.save()
	user.last_name = request.POST['last_name']
	user.first_name = request.POST['first_name']
	user.save()
	return render_to_response(template_name,
							  context_instance=RequestContext(request))

@login_required
def change_email(request, template_name='accounts/settings_change.html'):	
	user = request.user	
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			user.email = request.POST['email1']
			user.save()
			return render_to_response(template_name,
							  context_instance=RequestContext(request))
	return render_to_response(template_name, {'error_message': "Email confirmation failed!"},
							  context_instance=RequestContext(request))
	
