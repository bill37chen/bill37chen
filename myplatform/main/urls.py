from django.conf.urls import patterns, url
from main.views import *

__author__ = 'Bill'


urlpatterns = patterns('',
    url(r'^$', main),
)