from django.db import models
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
	comment = models.CharField(max_length=1050)

	def __str__(self):
		return self.comment


class Option(models.Model):
	option = models.CharField(max_length=1050)

	def __str__(self):
		return self.option


class Poll(models.Model):
	title = models.CharField(max_length=1050)
	description = models.TextField(default="none")
	comments = models.ManyToManyField(Comment, through="PollCommentConnector", through_fields=("poll", "comment"),)
	options = models.ManyToManyField(Option, through="PollOptionConnector", through_fields=("poll", "option"),)
	image_1 = models.ImageField(upload_to='poll_product/images/', blank=True)
	image_2 = models.ImageField(upload_to='poll_product/images/', blank=True)
	image_3 = models.ImageField(upload_to='poll_product/images/', blank=True)


	def __str__(self):
		return self.title



class PollCommentConnector(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default="")
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)




class PollOptionConnector(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default="")
	option = models.ForeignKey(Option, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

