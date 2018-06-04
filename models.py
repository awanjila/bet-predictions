# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import PIL as pillow
import django_tables2 as tables
from django.utils.timezone import get_current_timezone
from datetime import datetime


# Create your models here.
class TrueOdds(models.Model):
	country=models.CharField(max_length=200, default='DEFAULT VALUE')
	flags=models.ImageField(upload_to='post_image', default='DEFAULT VALUE')
	home_team=models.CharField(max_length=200, default='DEFAULT VALUE')
	away_team=models.CharField(max_length=200, default='DEFAULT VALUE')
	tips=models.CharField(max_length=200, default='DEFAULT VALUE')
	scores=models.CharField(max_length=200, default='DEFAULT VALUE')
	created_at = models.DateTimeField(default=datetime.now)
	updated_at = models.DateTimeField(auto_now=True)
	


	def __str__(self):
		return self.tips
		

#class Categories(models.Model):
	#pass