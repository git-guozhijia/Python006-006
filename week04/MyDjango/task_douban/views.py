from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
import requests
from lxml import etree
import re
import time


def task(request):

    Comments.objects.filter().delete()
    time.sleep(1)
    try:
        get_url_name()
        time.sleep(1)
        queryset = Comments.objects.all()
        condsions = {"star_review__gte": 30.3}
        values = queryset.filter(**condsions)
        return render(request, 'index.html', locals())
    except Exception as e:
        return HttpResponse(f"task error: {e}")

    # try:
    #     queryset = Comments.objects.all()
    #     condsions = {"star_review__gte": 30.3}
    #     values = queryset.filter(**condsions)
    #     return render(request, 'index.html', locals())
    # except Exception as e:
    #     return HttpResponse(f"task error: {e}")

def get_url_name(tag=3):
    ERR = 0
    for i in range(tag):
        if ERR < 3:
            time.sleep(0.5)
            i = i * 20
            myurl = f"https://movie.douban.com/subject/24733428/comments?start={i}&limit=20&status=P&sort=new_score"
            print(f"myurl--------:{myurl}")
            ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
            headers = {'User-Agent': ua}
            response = requests.get(myurl, headers=headers)

            time.sleep(1)

            if response.status_code == 200:
                selector = etree.HTML(response.text)
                for i in range(1,21):
                    time.sleep(0.1)
                    try:
                        comments = selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()')[0]
                        comments_time = selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[3]/@title')[0]
                        star_review01 = selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@class')[0]
                        star_review = float(re.findall(r'\d+', star_review01)[0])

                        # print(comments_time)
                        # with open("log.log") as log:
                        #     log.write(selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()'))
                        #     log.write(selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[3]/@title'))
                        #     log.write(selector.xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@class'))

                        try:
                            Comments.objects.create(comments=comments, star_review=star_review, comments_time=comments_time)
                        except Exception as e:
                            print(f"Comments 写入报错 >>>  {e}")
                    except Exception as e:
                        print(f"error >>>  {e}")
                        ERR += 1
                        continue

