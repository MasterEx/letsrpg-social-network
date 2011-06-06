from django.conf.urls.defaults import *

urlpatterns = patterns('letsrpg.messages.views',
	(r'^inbox/$', 
	 'show_messages', 
	 {'template_name': 'messages/messages.html'}),
	 
	 (r'^inbox/send/(?P<pkid>\d+)/$', 
	 'show_message', 
	 {'template_name': 'messages/view.html'}),
	 
	 (r'^inbox/send/mailsent/$', 
	 'send_message', 
	 {'template_name': 'messages/mailsent.html'}),
	 
	 (r'^inbox/send/new/$', 
	 'new_message', 
	 {'template_name': 'messages/newmessage.html'}),
	 
	 (r'^user/send/mailsent/$', 
	 'send_message2', 
	 {'template_name': 'messages/mailsent.html'}),
)
