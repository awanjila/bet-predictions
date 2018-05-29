# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,  ListView
from django.http import HttpResponse
from .models import TrueOdds
from .tables import TrueOddsTable
from django_tables2 import RequestConfig

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
	table=TrueOddsTable(TrueOdds.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'true_odds/index.html', {'table':table})