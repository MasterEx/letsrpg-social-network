from django.db import models
from accounts.models import User

class Ad(models.Model):
	# id is auto generated
	userid = models.ForeignKey(User)
	notes = models.TextField()
	value = models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add='true')
	expiration_date = models.DateTimeField(null='true',blank='true')
