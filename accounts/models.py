from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	userid = models.ForeignKey(User,unique='true')
	age = models.SmallIntegerField(null='true',blank='true')
	location = models.CharField(max_length=30,null='true',blank='true') # maybe save a google map location ?
	avatar = models.FileField(upload_to='avatars',null='true',blank='true')
	notes = models.TextField(null='true',blank='true')
	favorite_fantasy_game = models.CharField(max_length=20,null='true',blank='true')
	favorite_race = models.CharField(max_length=20,null='true',blank='true')
	favorite_class = models.CharField(max_length=20,null='true',blank='true')
	STATUS_CHOICES = (
		( 'O' , 'OK' ),
		( 'B' , 'BANNED'),
	)
	status = models.CharField(max_length=1,default='O',choices=STATUS_CHOICES)
	ban_reason = models.CharField(max_length=60,null='true',blank='true')
	
	def __unicode__(self):
		return self.userid.username

