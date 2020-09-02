from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
	full_name = models.CharField(max_length=1050, default="")
	email = models.CharField(max_length=1050, default="")
	message = models.CharField(max_length=1050, default="")
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.full_name
