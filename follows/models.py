from django.db import models
from accounts.models import User

class Follow(models.Model):
	userid_follower = models.ForeignKey(User)
	userid_followed = models.ForeignKey(User)

	def __unicode__(self):
		return self.name

