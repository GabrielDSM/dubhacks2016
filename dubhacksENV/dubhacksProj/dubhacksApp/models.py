from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Woman(models.Model):
	name = models.CharField(max_length = 45)
	major = models.CharField(max_length = 55)
	response1 = models.TextField()
	response2 = models.TextField()
	response3 = models.TextField()
	response4 = models.TextField()
	response5 = models.TextField()
	# Add field for image, look into BLOB


class Major(models.Model):
	title = models.CharField(max_length = 55)
	description = models.TextField()
	link = CharField(max_length = 34)


		
