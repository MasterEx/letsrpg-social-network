from django.db import models
from accounts.models import User

class Event(models.Model):
	# id is auto created
	game_master = models.CharField(max_length=10)
	user_role = models.CharField(max_length=10)
	date = models.DateTimeField(auto_now_add='true')
	slots = models.PositiveSmallIntegerField()
	slots_taken = models.IntegerField()
	location = models.CharField(max_length=20)

	def __unicode__(self):
			return self.name

class EventPlayer(models.Model):
	userid = models.ForeignKey(User)
	eventid = models.ForeignKey(Event)
	type = (
		( 'P' , 'Player'),
		( 'M' , 'Game Master - Story Tailer'),
	)

	def __unicode__(self):
			return self.name
