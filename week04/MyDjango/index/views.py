from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hellow Django!")


def year(request, year):
	# return HttpResponse(year)
	# 重定向url的功能，当请求到year()视图函数之后，redirect()函数就会去重新请求"2020.html"
	return redirect("2020.html")


def name(request, **kwargs):
	# return HttpResponse(kwargs['name'])
	return HttpResponse([i for i in kwargs.values()])


def myyear(request, year):
	return render(request, 'yearview.html')


def home(request):
	return render(request, 'yearview.html')