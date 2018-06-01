from django.conf.urls import  url

from odds_app.views import true_odds

from odds_app.views import sort_by_tips



urlpatterns = [url(r'^true_odds/', true_odds),
                url(r'^sort_by_tips/', sort_by_tips),
                ]


