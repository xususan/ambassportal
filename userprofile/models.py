from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
	name = models.CharField(max_length=30)
	points = models.IntegerField()
	photo = models.CharField(max_length=30)
	university = models.CharField(max_length=30)
	ambassador_lead =models.CharField(max_length=30)

	