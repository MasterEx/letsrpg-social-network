from django.contrib.auth.models import User
from letsrpg.messages.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from letsrpg.messages.forms import *

@login_required
def show_messages(request, template_name='messages/messages.html'):
	messages = Message.objects.filter(userid_receiver=request.user,status="P")
	return render_to_response(template_name, {'messages': messages},
							  context_instance=RequestContext(request))
	
@login_required
def show_message(request, pkid, template_name='messages/view.html'):
	message = Message.objects.filter(pk=pkid)
	mailform = MessageForm(
	initial={'subject': 'RE: %s' % message[0].subject}
	)
	return render_to_response(template_name, {'message': message, 'mailform': mailform},
							  context_instance=RequestContext(request))

@login_required
def send_message(request, template_name='messages/mailsent.html'):
	user = request.user
	receiver = request.POST['sender']
	recuser = User.objects.get(pk=receiver)
	if (request.POST['subject'] != ""):
		subject = request.POST['subject']
	else:
		subject = "RE: %s" % request.POST['olfsubject']
	message = request.POST['message']
	msg = Message(userid_sender=user,userid_receiver=recuser,subject=subject,
					message=message,status="P")
	msg.save()
	return render_to_response(template_name,
							  context_instance=RequestContext(request))

@login_required
def new_message(request, template_name='messages/newmessage.html'):
	homeuser = request.POST['receiver']
	mailform = MessageForm()
	return render_to_response(template_name,{'mailform': mailform, 'receiver': homeuser},
							  context_instance=RequestContext(request))

@login_required
def send_message2(request, template_name='messages/mailsent.html'):
	user = request.user
	receiver = request.POST['sender']
	recuser = User.objects.get(username=receiver)
	if (request.POST['subject'] != ""):
		subject = request.POST['subject']
	else:
		True
	message = request.POST['message']
	msg = Message(userid_sender=user,userid_receiver=recuser,subject=subject,
					message=message,status="P")
	msg.save()
	return render_to_response(template_name,
							  context_instance=RequestContext(request))

@login_required
def to_wallpost(request, template_name='messages/wallpost.html'):
	homeuser = request.POST['receiver']
	wallform = PublicMessageForm()
	return render_to_response(template_name,{'form': wallform, 'receiver': homeuser},
							  context_instance=RequestContext(request))

@login_required
def wallpost(request, template_name='messages/mailsent.html'):
	user = request.user
	receiver = request.POST['sender']
	recuser = User.objects.get(username=receiver)
	message = request.POST['message']
	msg = Message(userid_sender=user,userid_receiver=recuser,
					message=message,status="A")
	msg.save()
	return render_to_response(template_name,
							  context_instance=RequestContext(request))
