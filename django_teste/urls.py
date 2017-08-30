from django.conf.urls import url
from django_teste.views import sitezao

urlpatterns = [
	url(r'^bitch/$', sitezao),
]