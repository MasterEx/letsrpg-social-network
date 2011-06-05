from django.conf.urls.defaults import *

urlpatterns = patterns('letsrpg.messages.views',
	(r'^inbox/$', 
	 'show_messages', 
	 {'template_name': 'messages/messages.html'}),
)
