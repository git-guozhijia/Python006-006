import week01.logging_t,time,os

CurrentTime = time.strftime("%Y-%m-%d", time.localtime())
PATH = f'./var/log/python-{CurrentTime}/log.log'

def task():
    path_t = '.'
    for i in os.path.dirname(PATH).split('/')[1:]:
        path_t = path_t + f'/{i}'
        if not os.path.exists(path_t):
            try:
                os.makedirs(path_t)
            except OSError as err:
                print(err)
    logger = week01.logging_t.log(PATH)
    logger.info(CurrentTime)

if __name__ == "__main__":
    task()