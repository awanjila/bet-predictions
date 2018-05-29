# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,  ListView
from django.http import HttpResponse
from .models import TrueOdds

# Create your views here.
"""
class Indexview(ListView):
	template_name='true_odds/index.html'

	def get_queryset(self):
		return TrueOdds.objects.all()

class AboutView(TemplateView):
	template_name='true_odds/about.html'
"""
def true_odds(request):
	return render(request, 'true_odds/index.html', {'true_odds':TrueOdds.objects.all()})