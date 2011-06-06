from django.conf.urls.defaults import *

urlpatterns = patterns('letsrpg.events.views',
	(r'^create/$', 
	 'to_event', 
	 {'template_name': 'events/eventform.html'}),
	 
	 (r'^done/$', 
	 'create_event', 
	 {'template_name': 'events/eventdone.html'}),
)
