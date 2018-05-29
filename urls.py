from django.conf.urls import  url

from odds_app.views import true_odds



urlpatterns = [url(r'^true_odds/', true_odds),]

