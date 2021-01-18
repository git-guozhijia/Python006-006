from django.urls import path, re_path, register_converter
from . import views, converters

# from django.urls import register_converter
# 调用register_converter()方法，把自己编写的正则匹配器当做参数传入
register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')


"""
# Django 内支持对URL设置变量，支持的变量类型有：
	str
	int
	slug -- 备注
	uuid
	path

# 使用方式：
	path("<int:year>", views.myyear),
"""


urlpatterns = [
    path('', views.index),

    # http://127.0.0.1:8000/index/orm_get
    path('orm_get', views.orm_get),
    # http://127.0.0.1:8000/index/orm_update/<str:name>
    path('orm_update/<str:name>', views.orm_update),
    # http://127.0.0.1:8000/index/orm_delete/<int:id>
    path('orm_delete/<int:id>', views.orm_delete),
    # http://127.0.0.1:8000/index/orm_insert
    path('orm_insert', views.orm_insert),

    path("2020.html", views.orm_get),
	path("books", views.books),
    # path('home/', views.home),

    # # 使用自定义正则匹配器，匹配url
    # path("<yyyy:year>", views.year),
    # path("<myint:year>", views.year),


    # 直接使用正常的类型判断url
    # path("<int:year>", views.year),
    # path("<int:year>/<str:name>", views.name),

    # ###正则表达式匹配url：from django.urls import re_path
    # re_path() 使用正则表达式方法去匹配正则
	# (?P<year>[0-9]{4}).html   解析
	# (?P<year>[0-9]{4}) 表示进行正则匹配的部分
		# ?P  表示该部分需要进行正则匹配
			# <year>   变量名
				# [0-9]{4}   匹配的正则表达式
    # re_path('((?P<year>[0-9]{4})=urlyear).html', views.myyear, name="urlyear"),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name="urlyear"),
]