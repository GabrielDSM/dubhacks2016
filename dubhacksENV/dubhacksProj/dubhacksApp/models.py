from __future__ import unicode_literals

from django.db import models


class Woman(models.Model):
	name = models.CharField(max_length=45)
	major = models.CharField(max_length=55)
	response1 = models.TextField()
	response2 = models.TextField()
	response3 = models.TextField()
	response4 = models.TextField()
	response5 = models.TextField()
	image = models.ImageField()


class Major(models.Model):
	title = models.CharField(max_length=55)
	description = models.TextField()
	link = models.CharField(max_length=35)

