from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hellow Django!")


def year(request, year):
	return HttpResponse(year)


def name(request, **kwargs):
	# return HttpResponse(kwargs['name'])
	return HttpResponse([i for i in kwargs.values()])


def myyear(request, year):
	return render(request, 'yearview.html')


def home(request):
	return render(request, 'yearview.html')