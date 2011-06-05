from django.db import models
from django.contrib.auth.models import User

class AbuseReport(models.Model):
	userid_rater = models.ForeignKey(User,related_name='arater')
	userid_rated = models.ForeignKey(User,related_name='arated')
	commend = models.TextField()
	STATUS_CHOICES = (
		( 'O' , 'OPEN' ),
		( 'C' , 'CLOSED' ),
	)
	status = models.CharField(max_length=1,default='O',choices=STATUS_CHOICES)
	timestamp = models.DateTimeField(auto_now_add='true')
	
	def __unicode__(self):
		return "%s - %s" % (self.userid_rater.username,self.userid_rated.username)

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
		return "%s - %s" % (self.userid_rater.username,self.userid_rated.username)
