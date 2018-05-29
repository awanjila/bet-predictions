import django_tables2 as tables
from .models import TrueOdds

class TrueOddsTable(tables.Table):
	class Meta:
		model=TrueOdds
		template_name = 'django_tables2/bootstrap.html'
