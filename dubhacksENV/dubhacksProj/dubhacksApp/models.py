from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 45)
	major = models.CharField(max_length = 55)
	response1 = models.TextField()
	response2 = models.TextField()
	response3 = models.TextField()
	response4 = models.TextField()
	response5 = models.TextField()
