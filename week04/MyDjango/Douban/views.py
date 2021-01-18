from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from Douban.models import T1
from django.db.models import Avg

def books_short(request):
	shorts = T1.objects.all()
	# 获取评论数量
	counter = T1.objects.all().count()
	# 聚合函数aggregate()：T1.objects.aggregate(Avg("n_star"))的返回值是一个字典
	star_avg = f'{T1.objects.aggregate(Avg("n_star"))["n_star__avg"]:0.1f}'
	sent_avg = f'{T1.objects.aggregate(Avg("sentiment"))["sentiment__avg"]:0.1f}'


	queryset = T1.objects.values('sentiment')
	# condsions 代表的意思：sentiment(要判断的表字段)两个下划线之后是标识 gte 表示：>= 0.5
	# gt ：>
	# lt ：<
	# lte ：<=
	condsions = {"sentiment__gte": 0.5}
	# queryset.filter(**condsions):<QuerySet [{'sentiment': 0.999}, {'sentiment': 0.8}]>
	plus = queryset.filter(**condsions).count()

	queryset = T1.objects.values('sentiment')
	condsions = {"sentiment__lt": 0.5}
	minus = queryset.filter(**condsions).count()

	return render(request, "./result.html", locals())
