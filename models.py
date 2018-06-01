# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import PIL as pillow
import django_tables2 as tables


# Create your models here.
class TrueOdds(models.Model):
	country=models.CharField(max_length=200)
	flags=models.ImageField(upload_to='post_image', blank='')
	home_team=models.CharField(max_length=200)
	away_team=models.CharField(max_length=200)
	tips=models.CharField(max_length=200)
	#created_at = models.DateTimeField(auto_now_add=True)
	#updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.tips
		

class Categories(models.Model):
	pass