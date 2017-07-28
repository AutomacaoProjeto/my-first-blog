from django.conf.urls import url
from django_teste.views import home

urlpatterns = [
	url(r'^$', home),
]