from django.db import models
from accounts.models import User

class AbuseReport(models.Model):
	userid_rater = models.ForeignKey(User,related_name='arater')
	userid_rated = models.ForeignKey(User,related_name='arated')
	commend = models.TextField()
	
	def __unicode__(self):
		return self.name

#extend models if possible ?
class Rate(models.Model):
	userid_rater = models.ForeignKey(User,related_name='rater')
	userid_rated = models.ForeignKey(User,related_name='rated')
	commend = models.TextField()
	RATE_CHOICES = (
		( '1' , '1/5' ),
		( '2' , '2/5' ),
		( '3' , '3/5' ),
		( '4' , '4/5' ),
		( '5' , '5/5' ),
	)
	rate = models.CharField(max_length=1,choices=RATE_CHOICES)
	
	def __unicode__(self):
		return self.name
