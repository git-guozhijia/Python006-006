from django.shortcuts import render
from django.http import HttpResponse
from django_redis import get_redis_connection

def testRedis(request, video_id):
	conn = get_redis_connection('default')
	conn.zincrby("count_number", 1, f"{video_id}")
	return HttpResponse(f'当前阅读的video已经阅读了{int(conn.zscore("count_number", f"{video_id}"))}次！')