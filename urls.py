from django.conf.urls import  url

from . import views



urlpatterns = [url(r'^$', views.Indexview.as_view(), name = 'index'),]

