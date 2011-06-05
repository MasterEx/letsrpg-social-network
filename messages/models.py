from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	# id is auto generated
	userid_sender = models.ForeignKey(User,related_name='sender')
	userid_receiver = models.ForeignKey(User,related_name='receiver')
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add='true')
	STATUS_CHOICES = (
		( 'A' , 'public message'),
		( 'P' , 'private message'),
	)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES)
	READ_CHOICES = (
		( 'Y' , 'yes' ),
		( 'N' , 'no' ),
	)
	read = models.CharField(max_length=1,default='Y',choices=READ_CHOICES)

	def __unicode__(self):
		return "%s - %s" % (self.userid_sender.username,self.userid_receiver.username)

