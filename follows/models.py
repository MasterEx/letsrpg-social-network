from django.db import models
from accounts.models import User

class Follow(models.Model):
	userid_follower = models.ForeignKey(User,related_name='follower')
	userid_followed = models.ForeignKey(User,related_name='followed')
	
	class Meta:
		unique_together = ( 'userid_follower' , 'userid_followed' )
	
	def __unicode__(self):
		return self.name
