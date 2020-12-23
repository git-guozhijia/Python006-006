#（此作业需提交至 GitHub）编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log

import week01.logging_t,time,os

CurrentTime = time.strftime("%Y-%m-%d", time.localtime())
PATH = f'./var/log/python-{CurrentTime}/log.log'

def task():
    path_t = '.'
    for i in os.path.dirname(PATH).split('/')[1:]:
        path_t = path_t + f'/{i}'
        if os.path.exists(path_t):
            continue
        else:
            print(path_t)
            os.makedirs(path_t)
    logger = week01.logging_t.log(PATH)
    logger.info(CurrentTime)

if __name__ == "__main__":
    task()