from django.db import models

class User(models.Model):
	# id is auto generated
	username = models.CharField(max_length=10) # username can be 10 chars long
	password = models.CharField(max_length=32) # password will be saved as md5 hash
	email = models.EmailField()
	verification = models.BooleanField(default=False)
	role = models.BooleanField(default=False) # False for regular user - True for admin
	
	def __unicode__(self):
		return self.name

class Profile(models.Model):
	userid = models.ForeignKey(User)
	age = models.SmallIntegerField()
	location = models.CharField(max_length=30) # maybe save a google map location ?
	name_last = models.CharField(max_length=20)
	name_first = models.CharField(max_length=20)
	avatar = models.FileField(upload_to='avatars')
	notes = models.TextField()
	favorite_fantasy_game = models.CharField(max_length=20)
	favorite_race = models.CharField(max_length=20)
	favorite_class = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name

