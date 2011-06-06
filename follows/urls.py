from django.conf.urls.defaults import *

urlpatterns = patterns('letsrpg.follows.views',
	(r'^follow/$', 
	 'follow', 
	 {'template_name': 'follows/follows.html'}),
)
