from django.shortcuts import render

# Create your views here.

def home(request):


	#verificar credenciasi...
	#redirecionar...

	return render(request, 'django_teste/index.html')

def sitezao(request):
	return render(request, 'django_teste/Site.html')

