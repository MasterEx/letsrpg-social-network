from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	userid = models.ForeignKey(User,unique='true')
	age = models.SmallIntegerField(null='true')
	location = models.CharField(max_length=30) # maybe save a google map location ?
	name_last = models.CharField(max_length=20)
	name_first = models.CharField(max_length=20)
	avatar = models.FileField(upload_to='avatars')
	notes = models.TextField()
	favorite_fantasy_game = models.CharField(max_length=20)
	favorite_race = models.CharField(max_length=20)
	favorite_class = models.CharField(max_length=20)
	STATUS_CHOICES = (
		( 'O' , 'OK' ),
		( 'B' , 'BANNED'),
	)
	status = models.CharField(max_length=1,default='O',choices=STATUS_CHOICES)
	ban_reason = models.CharField(max_length=60,null='true',blank='true')
	
	def __unicode__(self):
		return self.name

