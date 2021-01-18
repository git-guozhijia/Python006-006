from django.shortcuts import render, redirect
from index.models import *


# Create your views here.
from django.http import HttpResponse


def orm_insert(request):
	'''
	try:
		n = Name()
		n.name = "红楼梦"
		n.author = "曹雪芹"
		n.stars = 9.6
		n.save()
		return HttpResponse("执行结束！")
	except Exception as e:
		return HttpResponse(e)
	'''

	try:
		Name.objects.create(name="红楼梦", author="曹雪芹", stars=9.99)
		Name.objects.create(name="活着", author="余华", stars=9.94)
		return HttpResponse("执行结束！")
	except Exception as e:
		return HttpResponse(f"orm_insert error: {e}")

def orm_get(request):
	"""
	try:
		result = Name.objects.get(id=2).name
		return HttpResponse(f"orm_get result: {result}")
	except Exception as e:
		return HttpResponse(f"orm_get error: {e}")
	"""
	'''
	try:
		return HttpResponse(f"orm_get 执行结果: {Name.objects.all()[0].name}")
	except Exception as e:
		return HttpResponse(f"orm_get error: {e}")
	'''
	'''
	try:
		return HttpResponse(f"orm_get 执行结果: {[i for i in Name.objects.values_list('name')]}")
	except Exception as e:
		return HttpResponse(f"orm_get error: {e}")
	'''

	try:
		return HttpResponse(f"orm_get 执行结果: {Name.objects.filter(name='红楼梦', stars=9.98).get()}")
	except Exception as e:
		return HttpResponse(f"orm_get error: {e}")

def books(request):
	try:
		# return HttpResponse(f"orm_get 执行结果: {[i for i in Name.objects.values_list('name','author')]}")
		n = Name.objects.all()
		# locals()代表吧books这个方法内的所有的本地变量传递给"booke.html"
		return render(request, "books.html", locals())
	except Exception as e:
		return HttpResponse(f"books func error: {e}")



def orm_update(request, **kwargs):
	try:
		Name.objects.filter(id=12).update(name=f"{kwargs['name']}")
		result = Name.objects.get(id=12).name
		return HttpResponse(f"orm_update result: {result}")
	except Exception as e:
		return HttpResponse(f"orm_update error: {e}")


def orm_delete(request, **kwargs):
	try:
		Name.objects.filter(id=kwargs['id']).delete()
		return HttpResponse(f"orm_delete 执行完成！")
	except Exception as e:
		return HttpResponse(f"orm_delete error: {e}")


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