#README

###What is letsrpg?

letsrpg is a social network for role playing gamers

It'll be implemented in Python - Django with SQLite3

###Why?

letsrpg is an implementation of a social network for our 
class "development and implementation of IT systems"

Previous design steps can be found in Greek here:

 * [Step 1](https://docs.google.com/document/pub?id=19oVeNSMEer0Vi1SrpXwtIwaFSB381k-fR4rb5g7CaS8)
 * [Step 2](https://docs.google.com/document/pub?id=1ZYNCbqMQXp1kzf2Il7msWlSiY6jq8_rYBEW0_DuSAvk)
 * [Step 3](https://docs.google.com/document/pub?id=1MIYySAnjli2_5XIazbda0aEzuMjaGtaQrRaPFD8ICWI)

###Applications Structure

Each entity described in step 2 will be a django model in it's own application.
Exception is User and Profile entities that will be placed in an app named "account"
and Event and Event-Player entities that will be placed in an app named "event".

	account
		|-UserProfile
	event
		|-Event
		|-Event-Player
	follows
	rate
	useractions
		|-Abuse-Report
		|-Messages
	ads

###ToDo

 * <del>Create admin pages</del>
 * Create views
 * Create templates
 * Create test data
 * Find bugs
 * Fix bugs
 * Find more bugs and fix them too!

###References

Man pages and documentation that we'll probably need more than once!

####Django

 * [Field Types](https://docs.djangoproject.com/en/dev/ref/models/fields/#field-types)
 * [File Upload Example](http://abing.gotdns.com/posts/2009/django-file-upload-handling-examples/)
 * [Extending the Django User model 1](http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance/) ,
 [Extending the Django User model 2](http://www.kolios.dk/2010/01/22/how-to-extend-django-user-class-and-change-authentication-middleware/)
 * [Django User Profiles](http://www.turnkeylinux.org/blog/django-profile) 
 * [Django User Authentication](https://docs.djangoproject.com/en/dev/topics/auth/)
 * Easy authentication, using django.contrib.auth: [part1](http://peyman-django.blogspot.com/2010/03/full-easy-authentication-using.html),
 [part2](http://peyman-django.blogspot.com/2010/03/full-easy-authentication-using_19.html)
 * [Django Forms](http://www.djangobook.com/en/2.0/chapter07/)
 * [Django Limitings Access to Logged In Users](https://docs.djangoproject.com/en/dev/topics/auth/#limiting-access-to-logged-in-users)
 * [DIsplaying Other Content to Logged In Users](http://groups.google.com/group/django-users/browse_thread/thread/63ffa208ee2d2175?fwc=1)

###Tips-Notes

 * Database superuser credentials: username=admin , password=pass
 * Recreate database by deleting it and synchronizing again (not the best way though)
 * In order to send emails uncomment lines 156-160 in settings.py
 * User signup and password reset require a working smtp
 * To change the domain name, log into the admin interface and change
 example.com in the sites table as mentioned [here](http://codespatter.com/2009/01/05/django-settings-site-domain-examplecom/)
