from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
	userid_follower = models.ForeignKey(User,related_name='follower')
	userid_followed = models.ForeignKey(User,related_name='followed')
	
	class Meta:
		unique_together = ( 'userid_follower' , 'userid_followed' )
	
	def __unicode__(self):
		return "%s - %s" % (self.userid_follower.username,self.userid_followed.username)
