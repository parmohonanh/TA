from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class perangkat (models.Model):
	nama = 	models.CharField(max_length=100)
	vendor =  models.CharField(max_length=50)
	

	def __unicode__(self):
		return self.nama
		