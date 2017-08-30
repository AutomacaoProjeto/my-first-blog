from django.conf.urls import url
#from django_teste.views import sitezao  >> ESSE JEITO NÃO É O MAIS PRÁTICO
from . import views

urlpatterns = [
	url(r'^$', views.sitezao),
]