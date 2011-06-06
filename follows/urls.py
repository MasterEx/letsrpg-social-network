from django.conf.urls.defaults import *

urlpatterns = patterns('letsrpg.follows.views',
	(r'^follow/$', 
	 'follow', 
	 {'template_name': 'follows/follows.html'}),
	 
	 (r'^unfollow/$', 
	 'unfollow', 
	 {'template_name': 'follows/unfollows.html'}),
)
