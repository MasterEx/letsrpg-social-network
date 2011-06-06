from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'letsrpg.views.index', name='home'),
    (r'^accounts/', include('letsrpg.accounts.urls')),
    (r'^messages/', include('letsrpg.messages.urls')),
    (r'^player/', include('letsrpg.follows.urls')),
    (r'^event/', include('letsrpg.events.urls')),
    (r'^user/(?P<username>\S+)/$', 'letsrpg.views.user'),
    (r'^events/(?P<username>\S+)/$', 'letsrpg.views.event'),
    # url(r'^$', 'letsrpg.views.home', name='home'),
    # url(r'^letsrpg/', include('letsrpg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
